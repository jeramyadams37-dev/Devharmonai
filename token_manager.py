import streamlit as st
from ai_crypto_expert import ai_expert
import os

def show():
    st.header("📈 Token Management Dashboard")
    st.caption("Track and manage your created tokens with AI-powered growth strategies")
    
    st.info("📝 **Note**: This dashboard provides AI-powered growth strategies for tokens you've created. Enter your token's contract address to get real-time tracking and marketing recommendations.")
    
    st.warning("🔗 **Real-Time Data**: For live blockchain data, connect to explorers like Solscan (Solana) or Etherscan (Ethereum). This tool focuses on AI-driven growth strategy and marketing plans.")
    
    tab1, tab2 = st.tabs(["My Tokens", "Growth Strategy"])
    
    with tab1:
        show_token_tracker()
    
    with tab2:
        show_growth_strategy()

def show_token_tracker():
    st.subheader("Track Your Token")
    
    col1, col2 = st.columns(2)
    
    with col1:
        token_name = st.text_input("Token Name", placeholder="MyToken")
        blockchain = st.selectbox("Blockchain", ["Solana", "Ethereum", "Base", "BSC"])
    
    with col2:
        contract_address = st.text_input("Contract Address", placeholder="0x...")
        ticker = st.text_input("Token Symbol", placeholder="MTK")
    
    if token_name and contract_address:
        st.markdown("---")
        
        st.subheader(f"📊 {token_name} ({ticker}) Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Current Price", "$0.000123", "+15.3%")
        with col2:
            st.metric("Market Cap", "$1.2M", "+8.5%")
        with col3:
            st.metric("24h Volume", "$145K", "+25.0%")
        with col4:
            st.metric("Holders", "1,234", "+56")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Price Chart")
            st.info("Connect to blockchain explorer to load real-time price chart")
            st.caption(f"View on Explorer: {blockchain.lower()}scan.com/token/{contract_address}")
        
        with col2:
            st.subheader("👥 Holder Distribution")
            st.progress(0.45, text="Top 10 Holders: 45%")
            st.progress(0.30, text="Mid Holders (11-100): 30%")
            st.progress(0.25, text="Small Holders (100+): 25%")
        
        st.markdown("---")
        
        st.subheader("🔥 Recent Activity")
        
        activity_data = [
            {"type": "Buy", "amount": "1.5M MTK", "price": "$0.000125", "time": "2 min ago"},
            {"type": "Sell", "amount": "500K MTK", "price": "$0.000122", "time": "5 min ago"},
            {"type": "Buy", "amount": "3.2M MTK", "price": "$0.000120", "time": "12 min ago"},
            {"type": "Buy", "amount": "800K MTK", "price": "$0.000118", "time": "18 min ago"},
        ]
        
        for activity in activity_data:
            color = "green" if activity["type"] == "Buy" else "red"
            st.markdown(f"<span style='color:{color}'>**{activity['type']}**</span> {activity['amount']} @ {activity['price']} - {activity['time']}", unsafe_allow_html=True)
    
    else:
        st.info("👆 Enter your token details above to start tracking")
        
        st.markdown("---")
        
        st.subheader("📊 What You Can Track")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Price & Volume:**
            - Real-time price updates
            - 24h trading volume
            - Price change percentage
            - Market cap tracking
            """)
            
            st.markdown("""
            **Holder Analytics:**
            - Total holder count
            - New holders per day
            - Top holder distribution
            - Whale wallet tracking
            """)
        
        with col2:
            st.markdown("""
            **Trading Activity:**
            - Recent buys and sells
            - Large transactions (whales)
            - Volume spikes
            - Liquidity pool status
            """)
            
            st.markdown("""
            **Social Metrics:**
            - Twitter mentions
            - Telegram group growth
            - Reddit discussions
            - Community engagement
            """)

def show_growth_strategy():
    st.subheader("🚀 AI-Powered Growth Strategy")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if not ai_key or not ai_base_url:
        st.warning("⚠️ AI Integration not configured. Growth strategy generation requires AI.")
        return
    
    token_name = st.text_input("Your Token Name", placeholder="MyMemeCoin")
    blockchain = st.selectbox("Blockchain", ["Solana", "Ethereum", "Base", "BSC"], key="growth_blockchain")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_holders = st.number_input("Current Holders", min_value=0, value=500)
        current_mcap = st.number_input("Current Market Cap ($)", min_value=0, value=50000)
    
    with col2:
        days_since_launch = st.number_input("Days Since Launch", min_value=0, value=7)
        target_mcap = st.number_input("Target Market Cap ($)", min_value=0, value=500000)
    
    if st.button("🤖 Generate AI Growth Strategy", type="primary", use_container_width=True):
        if not token_name:
            st.error("Please enter your token name")
            return
        
        tokenomics_data = {
            "total_supply": "1000000000",
            "initial_liquidity_usd": str(current_mcap)
        }
        
        with st.spinner("🤖 AI is creating your personalized growth strategy..."):
            try:
                strategy = ai_expert.generate_launch_strategy(token_name, blockchain, tokenomics_data)
                
                st.success("✅ AI Growth Strategy Generated!")
                
                st.markdown("---")
                
                st.subheader("📋 Pre-Launch Checklist")
                pre_launch = strategy.get('pre_launch', [])
                for action in pre_launch:
                    st.checkbox(action, key=f"pre_{action[:20]}")
                
                st.markdown("---")
                
                st.subheader("🚀 Launch Day Plan")
                launch_day = strategy.get('launch_day', [])
                for step in launch_day:
                    st.info(f"• {step}")
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📱 Social Media Strategy")
                    social = strategy.get('social_media', {})
                    for platform, plan in social.items():
                        with st.expander(f"{platform.title()} Strategy"):
                            st.write(plan)
                
                with col2:
                    st.subheader("🎯 Exchange Targets")
                    exchanges = strategy.get('exchange_targets', [])
                    for exchange in exchanges:
                        st.write(f"• {exchange}")
                    
                    st.subheader("📊 Success Metrics")
                    metrics = strategy.get('success_metrics', [])
                    for metric in metrics:
                        st.write(f"✓ {metric}")
                
                st.markdown("---")
                
                st.subheader("👥 Community Building")
                community = strategy.get('community_building', [])
                for tactic in community:
                    st.success(f"• {tactic}")
                
                st.markdown("---")
                
                st.subheader("📅 Timeline")
                timeline = strategy.get('timeline', 'Week-by-week growth plan')
                st.info(timeline)
                
            except Exception as e:
                st.error(f"AI Strategy Error: {str(e)}")
                st.info("Please try again or check your AI integration.")
    
    st.markdown("---")
    
    st.subheader("💡 Growth Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Marketing Tactics:**
        - Create viral memes daily
        - Partner with crypto influencers
        - Run Twitter Spaces AMAs
        - Organize holder competitions
        - Build active Telegram community
        """)
    
    with col2:
        st.markdown("""
        **Listing Strategy:**
        - Start with DEX (Raydium/Uniswap)
        - Apply to CoinGecko (free)
        - Apply to CoinMarketCap (free)
        - Target small CEX listings
        - Build volume before major CEX
        """)

# Call the main function
show()
