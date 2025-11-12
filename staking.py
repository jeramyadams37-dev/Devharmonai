import streamlit as st
from datetime import datetime

def show():
    try:
        from wallet_manager import wallet_manager
        from crypto_data import fetcher
        from database import is_database_available
        
        st.header("💎 Staking Rewards")
        st.caption("Earn passive income by staking your cryptocurrency holdings")
        
        if not is_database_available():
            st.warning("⚠️ Database not available. Staking features require database connection.")
            st.info("Database features are currently unavailable. Please contact support if this persists.")
            return
        
        tab1, tab2, tab3 = st.tabs(["Active Staking", "Stake New Position", "Staking History"])
        
        with tab1:
            show_active_staking()
        
        with tab2:
            show_stake_new()
        
        with tab3:
            show_staking_history()
    
    except Exception as e:
        st.error(f"Error loading staking page: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

def show_active_staking():
    from wallet_manager import wallet_manager
    from crypto_data import fetcher
    
    st.subheader("💰 Your Active Staking Positions")
    
    positions = wallet_manager.get_staking_positions(status="active")
    
    if not positions:
        st.info("👋 No active staking positions. Stake cryptocurrency in the 'Stake New Position' tab to start earning rewards!")
        return
    
    total_staked_value = 0
    total_rewards = 0
    
    for position in positions:
        try:
            crypto_data = fetcher.get_crypto_by_id(position.crypto_id)
            if crypto_data:
                current_price = crypto_data.get('market_data', {}).get('current_price', {}).get('usd', position.stake_price)
            else:
                current_price = position.stake_price
            
            current_value = position.amount_staked * current_price
            total_staked_value += current_value
            
            rewards = wallet_manager.calculate_staking_rewards(position)
            total_rewards += rewards
            
            time_staked = (datetime.utcnow() - position.start_date).days
            
            with st.container():
                col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
                
                with col1:
                    st.write(f"**{position.crypto_name}** ({position.crypto_symbol.upper()})")
                    st.caption(f"Staked: {time_staked} days ago")
                
                with col2:
                    st.write(f"**{position.amount_staked:,.4f}** {position.crypto_symbol.upper()}")
                    st.write(f"${current_value:,.2f}")
                
                with col3:
                    st.write(f"**APY:** {position.apy:.2f}%")
                    profit_pct = ((current_price - position.stake_price) / position.stake_price * 100) if position.stake_price > 0 else 0
                    profit_color = "green" if profit_pct >= 0 else "red"
                    st.markdown(f"<span style='color:{profit_color}'>Price: {profit_pct:+.2f}%</span>", unsafe_allow_html=True)
                
                with col4:
                    st.write(f"**Rewards Earned:**")
                    st.write(f"{rewards:,.6f} {position.crypto_symbol.upper()}")
                    st.caption(f"${rewards * current_price:,.2f}")
                
                with col5:
                    if st.button("Unstake", key=f"unstake_{position.id}", type="secondary"):
                        if wallet_manager.unstake_position(position.id):
                            st.success("✅ Unstaked!")
                            st.rerun()
                        else:
                            st.error("Failed to unstake")
                
                st.markdown("---")
        
        except Exception as e:
            st.error(f"Error loading {position.crypto_name}: {str(e)}")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Staked Value", f"${total_staked_value:,.2f}")
    
    with col2:
        st.metric("Total Rewards Earned", f"${total_rewards * (current_price if positions else 1):,.2f}")
    
    with col3:
        avg_apy = sum(p.apy for p in positions) / len(positions) if positions else 0
        st.metric("Average APY", f"{avg_apy:.2f}%")

def show_stake_new():
    from wallet_manager import wallet_manager
    from crypto_data import fetcher
    
    st.subheader("➕ Stake New Position")
    
    st.info("💡 **Info:** Staking allows you to earn passive rewards while holding your cryptocurrency. Choose your coin, amount, and APY below.")
    
    crypto_search = st.text_input("Search cryptocurrency to stake", placeholder="Bitcoin, Ethereum, Cardano...")
    
    if crypto_search:
        with st.spinner("Searching..."):
            results = fetcher.search_crypto(crypto_search)
        
        if results:
            crypto_options = {f"{r['name']} ({r['symbol'].upper()})": r for r in results[:10]}
            selected_display = st.selectbox("Select cryptocurrency", list(crypto_options.keys()))
            selected_crypto = crypto_options[selected_display]
            
            crypto_id = selected_crypto['id']
            crypto_name = selected_crypto['name']
            crypto_symbol = selected_crypto['symbol']
            
            with st.spinner("Fetching current data..."):
                crypto_data = fetcher.get_crypto_by_id(crypto_id)
            
            if crypto_data:
                market_data = crypto_data.get('market_data', {})
                current_price = market_data.get('current_price', {}).get('usd', 0)
                price_change_24h = market_data.get('price_change_percentage_24h', 0)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Current Price", f"${current_price:,.6f}" if current_price < 1 else f"${current_price:,.2f}")
                
                with col2:
                    st.metric("24h Change", f"{price_change_24h:+.2f}%", delta=f"{price_change_24h:+.2f}%")
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    amount_to_stake = st.number_input(
                        f"Amount to stake ({crypto_symbol.upper()})",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f"
                    )
                
                with col2:
                    apy = st.number_input(
                        "Annual Percentage Yield (APY %)",
                        min_value=0.0,
                        max_value=100.0,
                        value=5.0,
                        step=0.1,
                        help="Typical staking APYs range from 3-15% depending on the cryptocurrency"
                    )
                
                if amount_to_stake > 0:
                    st.markdown("---")
                    
                    st.subheader("📊 Projected Rewards")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    daily_reward = (amount_to_stake * (apy / 100)) / 365
                    monthly_reward = daily_reward * 30
                    yearly_reward = amount_to_stake * (apy / 100)
                    
                    with col1:
                        st.metric("Daily Rewards", f"{daily_reward:.6f} {crypto_symbol.upper()}")
                        st.caption(f"${daily_reward * current_price:.2f}")
                    
                    with col2:
                        st.metric("Monthly Rewards", f"{monthly_reward:.6f} {crypto_symbol.upper()}")
                        st.caption(f"${monthly_reward * current_price:.2f}")
                    
                    with col3:
                        st.metric("Yearly Rewards", f"{yearly_reward:.6f} {crypto_symbol.upper()}")
                        st.caption(f"${yearly_reward * current_price:.2f}")
                    
                    with col4:
                        total_value_1y = amount_to_stake + yearly_reward
                        st.metric("Total After 1 Year", f"{total_value_1y:.6f} {crypto_symbol.upper()}")
                        st.caption(f"${total_value_1y * current_price:.2f}")
                    
                    st.markdown("---")
                    
                    if st.button("🔒 Stake Now", type="primary", use_container_width=True):
                        success = wallet_manager.create_staking_position(
                            crypto_id=crypto_id,
                            crypto_name=crypto_name,
                            crypto_symbol=crypto_symbol,
                            amount_staked=amount_to_stake,
                            stake_price=current_price,
                            apy=apy
                        )
                        
                        if success:
                            st.success(f"✅ Successfully staked {amount_to_stake} {crypto_symbol.upper()}!")
                            st.balloons()
                            st.info("👈 Go to 'Active Staking' tab to view your position and track rewards")
                        else:
                            st.error("Failed to create staking position. Please try again.")
        
        else:
            st.warning("No results found. Try: bitcoin, ethereum, cardano, solana")
    
    else:
        st.info("👆 Search for a cryptocurrency to start staking")
        
        st.markdown("---")
        
        st.subheader("🌟 Popular Staking Coins")
        
        popular_coins = [
            {"name": "Ethereum", "symbol": "ETH", "typical_apy": "4-6%"},
            {"name": "Cardano", "symbol": "ADA", "typical_apy": "4-5%"},
            {"name": "Solana", "symbol": "SOL", "typical_apy": "6-8%"},
            {"name": "Polkadot", "symbol": "DOT", "typical_apy": "10-14%"},
            {"name": "Avalanche", "symbol": "AVAX", "typical_apy": "8-10%"},
        ]
        
        for coin in popular_coins:
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.write(f"**{coin['name']}** ({coin['symbol']})")
            with col2:
                st.write(f"APY: {coin['typical_apy']}")
            with col3:
                if st.button("Stake", key=f"stake_{coin['symbol']}"):
                    st.rerun()

def show_staking_history():
    from wallet_manager import wallet_manager
    from crypto_data import fetcher
    
    st.subheader("📚 Staking History")
    
    all_positions = wallet_manager.get_staking_positions(status="all")
    
    if not all_positions:
        st.info("No staking history available yet.")
        return
    
    unstaked_positions = [p for p in all_positions if p.status == "unstaked"]
    
    if not unstaked_positions:
        st.info("No unstaked positions yet. All your staking positions are still active!")
        return
    
    st.write(f"Showing {len(unstaked_positions)} completed staking positions")
    
    for position in unstaked_positions:
        try:
            crypto_data = fetcher.get_crypto_by_id(position.crypto_id)
            if crypto_data:
                current_price = crypto_data.get('market_data', {}).get('current_price', {}).get('usd', position.stake_price)
            else:
                current_price = position.stake_price
            
            rewards = wallet_manager.calculate_staking_rewards(position)
            
            start_date = position.start_date.strftime("%Y-%m-%d") if position.start_date else "Unknown"
            end_date = position.end_date.strftime("%Y-%m-%d") if position.end_date else "Unknown"
            
            days_staked = (position.end_date - position.start_date).days if position.end_date else 0
            
            with st.expander(f"{position.crypto_name} - Staked for {days_staked} days"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write(f"**Amount Staked:** {position.amount_staked:,.6f} {position.crypto_symbol.upper()}")
                    st.write(f"**Stake Price:** ${position.stake_price:,.2f}")
                
                with col2:
                    st.write(f"**APY:** {position.apy:.2f}%")
                    st.write(f"**Duration:** {days_staked} days")
                
                with col3:
                    st.write(f"**Rewards Earned:** {rewards:,.6f} {position.crypto_symbol.upper()}")
                    st.write(f"**Reward Value:** ${rewards * current_price:,.2f}")
                
                st.caption(f"Staked: {start_date} → Unstaked: {end_date}")
        
        except Exception as e:
            st.error(f"Error loading {position.crypto_name}: {str(e)}")

# Call the main function
show()
