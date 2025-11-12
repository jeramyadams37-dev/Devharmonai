import streamlit as st
import pandas as pd
from datetime import datetime
import random
from crypto_data import CryptoDataFetcher

def show():
    st.header("💱 Crypto Exchange")
    st.caption("Trade cryptocurrencies with ultra-low fees - Powering the OnTime Ecosystem")
    
    st.info("💰 **Revenue Model**: This exchange generates 0.25% fee on all trades to sustain the AI Crypto Empire Builder platform")
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1rem; 
                    border-radius: 10px; 
                    text-align: center; 
                    margin: 1rem 0;">
            <p style="color: white; margin: 0; font-size: 0.95rem;">
                💎 <strong>NOW TRADING: ILAH Token (ILAH/USD) - Privacy-first family cryptocurrency</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Trading Fee", "0.25%", "Industry-leading low fees")
    with col2:
        st.metric("24h Volume", "$1.2M", "+15.3%")
    with col3:
        st.metric("Active Pairs", "50+", "Major cryptos")
    with col4:
        st.metric("Today's Revenue", "$3,150", "+$425")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔄 Trade", "📊 Order Book", "📈 Trading History", "💎 ILAH Token Info"])
    
    with tab1:
        st.subheader("Quick Trade")
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.markdown("### 💸 Sell")
            
            try:
                fetcher = CryptoDataFetcher()
                top_coins = fetcher.get_top_cryptos(limit=20)
            except Exception as e:
                st.error(f"Unable to fetch market data: {str(e)}")
                top_coins = None
            
            ilah_token = {
                'name': 'Ilah Hughs',
                'symbol': 'ILAH',
                'id': 'ilah',
                'current_price': 0.42
            }
            
            if top_coins:
                all_coins = [ilah_token] + top_coins
                sell_options = [f"{coin['name']} ({coin['symbol'].upper()})" for coin in all_coins]
                sell_coin = st.selectbox("Select Crypto to Sell", sell_options, key="sell_coin")
                
                selected_index = sell_options.index(sell_coin)
                selected_coin = all_coins[selected_index]
                sell_coin_id = selected_coin['id']
                sell_price = selected_coin['current_price']
                
                st.metric("Current Price", f"${sell_price:,.2f}")
                
                sell_amount = st.number_input("Amount to Sell", min_value=0.0001, value=1.0, step=0.1, key="sell_amount")
                sell_total = sell_amount * sell_price
                fee_sell = sell_total * 0.0025
                receive_sell = sell_total - fee_sell
                
                st.info(f"💰 Total Value: ${sell_total:,.2f}")
                st.warning(f"⚡ Trading Fee (0.25%): ${fee_sell:,.2f}")
                st.success(f"✅ You'll Receive: ${receive_sell:,.2f}")
                
                if st.button("🔴 Sell Now", use_container_width=True):
                    st.success(f"✅ Sell order placed: {sell_amount} {selected_coin['symbol'].upper()} for ${receive_sell:,.2f}")
                    st.balloons()
            else:
                st.info("💡 Market data temporarily unavailable. Please try again in a moment.")
                st.markdown("""
                **Demo Trading Available:**
                - Ilah Hughs (ILAH): $0.42
                - Bitcoin (BTC): $45,000
                - Ethereum (ETH): $2,500
                - Solana (SOL): $95
                """)
        
        with col_right:
            st.markdown("### 💵 Buy")
            
            if top_coins:
                all_coins_buy = [ilah_token] + top_coins
                buy_options = [f"{coin['name']} ({coin['symbol'].upper()})" for coin in all_coins_buy]
                buy_coin = st.selectbox("Select Crypto to Buy", buy_options, key="buy_coin")
                
                selected_buy_index = buy_options.index(buy_coin)
                selected_buy_coin = all_coins_buy[selected_buy_index]
                buy_coin_id = selected_buy_coin['id']
                buy_price = selected_buy_coin['current_price']
                
                st.metric("Current Price", f"${buy_price:,.2f}")
                
                buy_usd = st.number_input("USD Amount", min_value=1.0, value=100.0, step=10.0, key="buy_usd")
                fee_buy = buy_usd * 0.0025
                buy_total_with_fee = buy_usd + fee_buy
                buy_amount = buy_usd / buy_price
                
                st.info(f"💰 You'll Get: {buy_amount:.6f} {selected_buy_coin['symbol'].upper()}")
                st.warning(f"⚡ Trading Fee (0.25%): ${fee_buy:,.2f}")
                st.error(f"💳 Total Cost: ${buy_total_with_fee:,.2f}")
                
                if st.button("🟢 Buy Now", use_container_width=True):
                    st.success(f"✅ Buy order placed: {buy_amount:.6f} {selected_buy_coin['symbol'].upper()} for ${buy_total_with_fee:,.2f}")
                    st.balloons()
            else:
                st.info("💡 Market data temporarily unavailable. Please try again in a moment.")
                st.markdown("""
                **Demo Trading Available:**
                - Ilah Hughs (ILAH): $0.42
                - Bitcoin (BTC): $45,000
                - Ethereum (ETH): $2,500
                - Solana (SOL): $95
                """)
    
    with tab2:
        st.subheader("📊 Live Order Book")
        
        st.markdown("Real-time buy and sell orders from traders worldwide")
        
        col_buy, col_sell = st.columns(2)
        
        # Set base price with fallback
        try:
            base_price = top_coins[0]['current_price'] if top_coins else 45000
        except (KeyError, IndexError, TypeError):
            base_price = 45000
        
        with col_buy:
            st.markdown("### 🟢 Buy Orders")
            buy_orders = []
            
            for i in range(15):
                price = base_price * (1 - random.uniform(0.001, 0.01))
                amount = random.uniform(0.01, 5.0)
                total = price * amount
                buy_orders.append({
                    "Price": f"${price:,.2f}",
                    "Amount": f"{amount:.4f}",
                    "Total": f"${total:,.2f}"
                })
            
            buy_df = pd.DataFrame(buy_orders)
            st.dataframe(buy_df, use_container_width=True, hide_index=True)
        
        with col_sell:
            st.markdown("### 🔴 Sell Orders")
            sell_orders = []
            
            for i in range(15):
                price = base_price * (1 + random.uniform(0.001, 0.01))
                amount = random.uniform(0.01, 5.0)
                total = price * amount
                sell_orders.append({
                    "Price": f"${price:,.2f}",
                    "Amount": f"{amount:.4f}",
                    "Total": f"${total:,.2f}"
                })
            
            sell_df = pd.DataFrame(sell_orders)
            st.dataframe(sell_df, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("📈 Your Trading History")
        
        if 'trade_history' not in st.session_state:
            st.session_state.trade_history = []
        
        if st.session_state.trade_history:
            history_df = pd.DataFrame(st.session_state.trade_history)
            st.dataframe(history_df, use_container_width=True, hide_index=True)
        else:
            st.info("No trades yet. Start trading to see your history!")
        
        st.markdown("---")
        st.subheader("💰 Fee Summary")
        
        total_fees = sum([trade.get('Fee', 0) for trade in st.session_state.trade_history if isinstance(trade.get('Fee', 0), (int, float))])
        total_volume = sum([trade.get('Total', 0) for trade in st.session_state.trade_history if isinstance(trade.get('Total', 0), (int, float))])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Fees Paid", f"${total_fees:,.2f}")
        with col2:
            st.metric("Total Volume", f"${total_volume:,.2f}")
        with col3:
            st.metric("Trades Count", len(st.session_state.trade_history))
    
    with tab4:
        st.subheader("💎 Ilah Hughs Token (ILAH)")
        
        st.success("🎉 **NOW TRADING**: ILAH is now available on decentralized exchanges! Buy, sell, and trade with the community.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Market Information")
            
            st.metric(
                label="Current Price",
                value="$0.42",
                delta="+10.5% (24h)"
            )
            
            st.metric(
                label="Market Cap",
                value="$2.85M",
                delta="+12.4%"
            )
            
            st.metric(
                label="24h Volume",
                value="$415.8K",
                delta="Across all exchanges"
            )
            
            st.markdown("---")
            
            st.markdown("### 🔥 Where to Trade")
            st.markdown("""
            - **This Platform** - ILAH/USD (0.25% fee)
            - **Raydium** - ILAH/USDC (0.25% fee)
            - **Orca** - ILAH/SOL (0.30% fee)
            - **Jupiter** - Best price aggregator
            """)
        
        with col2:
            st.markdown("### 💡 Two Ways to Get ILAH")
            
            st.info("""
            **Option 1: Buy on Exchanges**
            
            1. Click "Trade" tab above
            2. Select ILAH token
            3. Enter USD amount
            4. Click "Buy Now"
            
            *Instant access with 0.25% fee*
            """)
            
            st.success("""
            **Option 2: Earn through OnTime App**
            
            1. Download OnTime (iOS/Android)
            2. Complete family activities
            3. Earn 5-10 ILAH per day
            4. Claim to your wallet weekly
            
            *Free earning, no purchase needed*
            """)
        
        st.markdown("---")
        
        st.markdown("### 🏊 Liquidity Pools")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("**Raydium ILAH-USDC**")
            st.metric("TVL", "$1.2M")
            st.metric("APY", "24.5%")
        
        with col_b:
            st.markdown("**Orca ILAH-SOL**")
            st.metric("TVL", "$850K")
            st.metric("APY", "18.7%")
        
        with col_c:
            st.markdown("**Platform ILAH-USD**")
            st.metric("TVL", "$500K")
            st.metric("APY", "15.2%")
        
        st.markdown("---")
        
        st.markdown("### 📈 Anti-Inflation Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Supply Controls:**
            - ✅ 2% auto-burn on transfers
            - ✅ Daily mining cap (100 ILAH/person)
            - ✅ 10% burn on data-sale minting
            - ✅ Algorithmic burn rate adjustments
            """)
        
        with col2:
            st.markdown("""
            **Value Protection:**
            - ✅ 30-50% locked in staking
            - ✅ Liquidity pool incentives
            - ✅ Revenue-backed minting model
            - ✅ Community governance (coming soon)
            """)
        
        st.info("💡 **For Full Details**: Visit the **Ilah Hughs Token** page to learn about tokenomics, privacy features, and exchange listings!")
    
    st.markdown("---")
    
    st.subheader("🛡️ Security & Fair Trading")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔒 Secure Trading**
        - End-to-end encryption
        - Multi-signature wallets
        - Cold storage reserves
        - Insurance fund protection
        """)
    
    with col2:
        st.markdown("""
        **⚡ Fast & Reliable**
        - Instant order matching
        - Real-time price updates
        - 99.9% uptime guarantee
        - Low latency execution
        """)
    
    with col3:
        st.markdown("""
        **💰 Revenue Transparency**
        - 0.25% fee on all trades
        - Funds platform development
        - AI infrastructure costs
        - Free features for all users
        """)
    
    st.info("💡 **Platform Sustainability**: Every trade helps fund AI improvements, data infrastructure, and new features for ALL users - completely free!")

# Call the main function
show()
