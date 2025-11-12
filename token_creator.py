import streamlit as st
from ai_crypto_expert import ai_expert
import os

def show():
    st.header("🪙 Create Your Cryptocurrency")
    st.caption("Launch your own token on Solana or Ethereum with AI-optimized tokenomics")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if not ai_key or not ai_base_url:
        st.warning("⚠️ AI Integration not configured. Tokenomics optimization requires AI.")
    
    tab1, tab2, tab3 = st.tabs(["Token Configuration", "Platform Comparison", "Launch Guide"])
    
    with tab1:
        show_token_configuration()
    
    with tab2:
        show_platform_comparison()
    
    with tab3:
        show_launch_guide()

def show_token_configuration():
    st.subheader("Configure Your Token")
    
    col1, col2 = st.columns(2)
    
    with col1:
        blockchain = st.selectbox(
            "Select Blockchain",
            ["Solana (SPL)", "Ethereum (ERC-20)"],
            help="Solana: Faster & cheaper. Ethereum: Larger ecosystem."
        )
        
        token_name = st.text_input("Token Name", placeholder="MyToken")
        token_symbol = st.text_input("Token Symbol", placeholder="MTK", max_chars=10)
        
    with col2:
        total_supply = st.number_input(
            "Total Supply",
            min_value=1000,
            max_value=1000000000000,
            value=1000000000,
            format="%d",
            help="Total number of tokens to create"
        )
        
        decimals = st.number_input(
            "Decimals",
            min_value=0,
            max_value=18,
            value=9 if "Solana" in blockchain else 18,
            help="Number of decimal places"
        )
    
    token_purpose = st.text_area(
        "Token Purpose",
        placeholder="Describe what your token is for (e.g., Community meme coin, DeFi utility, NFT project token...)",
        height=100
    )
    
    target_market = st.multiselect(
        "Target Market",
        ["Meme Coin Traders", "DeFi Users", "NFT Collectors", "Gaming Community", "Crypto Investors", "Political Supporters"],
        default=["Meme Coin Traders"]
    )
    
    if st.button("🤖 Get AI Tokenomics Recommendations", type="primary", use_container_width=True):
        if not token_name or not token_symbol or not token_purpose:
            st.error("Please fill in all required fields (Name, Symbol, Purpose)")
            return
        
        with st.spinner("🤖 AI is analyzing successful meme coins and optimizing your tokenomics..."):
            try:
                recommendations = ai_expert.optimize_tokenomics(
                    token_name,
                    token_purpose,
                    ", ".join(target_market)
                )
                
                st.success("✅ AI Tokenomics Optimization Complete!")
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Recommended Parameters")
                    st.metric("Total Supply", f"{recommendations.get('total_supply', '1000000000'):,}")
                    st.metric("Launch Price", f"${recommendations.get('launch_price_usd', '0.0001')}")
                    st.metric("Initial Liquidity", f"${recommendations.get('initial_liquidity_usd', '10000'):,}")
                    st.metric("Success Probability", f"{recommendations.get('success_probability', 50)}%")
                
                with col2:
                    st.subheader("🎯 Token Allocation")
                    allocation = recommendations.get('allocation', {})
                    for category, percentage in allocation.items():
                        st.progress(percentage / 100, text=f"{category.replace('_', ' ').title()}: {percentage}%")
                
                st.markdown("---")
                
                st.subheader("🚀 Marketing Strategy")
                marketing = recommendations.get('marketing_strategy', '')
                st.info(marketing)
                
                st.subheader("⏰ Best Launch Timing")
                timing = recommendations.get('best_launch_timing', '')
                st.success(timing)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("💡 Recommendations")
                    recs = recommendations.get('recommendations', [])
                    for rec in recs:
                        st.write(f"✅ {rec}")
                
                with col2:
                    st.subheader("⚠️ Risks to Consider")
                    risks = recommendations.get('risks', [])
                    for risk in risks:
                        st.write(f"⚠️ {risk}")
                
            except Exception as e:
                st.error(f"AI Analysis Error: {str(e)}")
                st.info("Using default tokenomics parameters...")
    
    st.markdown("---")
    
    st.subheader("📝 Token Creation Summary")
    
    estimated_cost = "0.1-0.3 SOL (~$15-$45)" if "Solana" in blockchain else "0.01 ETH (~$25-$40)"
    
    summary_data = {
        "Blockchain": blockchain,
        "Token Name": token_name or "Not set",
        "Symbol": token_symbol or "Not set",
        "Total Supply": f"{total_supply:,}",
        "Decimals": decimals,
        "Estimated Cost": estimated_cost,
        "Creation Time": "< 1 minute"
    }
    
    for key, value in summary_data.items():
        st.write(f"**{key}:** {value}")
    
    st.warning("⚠️ **Important**: This AI wizard optimizes your tokenomics and provides launch strategies. For security reasons, actual token deployment requires connecting your wallet (Phantom for Solana, MetaMask for Ethereum) to external platforms like Smithii, Orion Tools, or similar token creators. The platforms listed below will handle the blockchain transactions.")
    
    st.info("💡 **Why External Deployment?** Blockchain token creation requires private key signing. For your security, we provide the strategy and parameters, then you execute the deployment through trusted platforms that handle wallet connections securely.")
    
    with st.expander("🔗 Recommended Token Creation Platforms"):
        if "Solana" in blockchain:
            st.markdown("""
            **Solana Token Creators:**
            - **Smithii**: smithii.io/en/create-solana-token (0.3 SOL)
            - **Orion Tools**: oriontools.io (0.1 SOL)
            - **Solana Tracker**: solanatracker.io/solana-token-creator
            - **SlerfTools**: slerf.tools/en-us/token-creator/solana (0.129 SOL)
            """)
        else:
            st.markdown("""
            **Ethereum Token Creators:**
            - **Smithii**: smithii.io/en/erc20-token-generator (0.01 ETH)
            - **CreateMyToken**: createmytoken.com (Free + gas)
            - **SmartContracts.Tools**: smartcontracts.tools/token-generator
            """)

def show_platform_comparison():
    st.subheader("Blockchain Platform Comparison")
    
    comparison_data = {
        "Feature": ["Speed (TPS)", "Transaction Cost", "Token Standard", "Creation Cost", "Ecosystem Size", "Best For"],
        "Solana (SPL)": ["60,000+", "$0.00025", "SPL Token", "$15-45", "Growing", "Meme coins, Fast trading"],
        "Ethereum (ERC-20)": ["15-30", "$1-50+", "ERC-20", "$25-40", "Largest", "DeFi, Established projects"]
    }
    
    import pandas as pd
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Solana Advantages")
        st.markdown("""
        - **Ultra-fast**: 60,000+ transactions per second
        - **Low cost**: ~$0.00025 per transaction
        - **Meme coin hub**: Home to many successful meme coins
        - **Quick creation**: Tokens live in under 1 minute
        - **Low barrier**: Cheap to create and trade
        """)
    
    with col2:
        st.subheader("✅ Ethereum Advantages")
        st.markdown("""
        - **Largest ecosystem**: Most DeFi protocols and users
        - **Established**: Proven security and stability
        - **Institutional**: More institutional adoption
        - **Layer 2s**: Scaling solutions available
        - **Smart contracts**: Advanced programmability
        """)

def show_launch_guide():
    st.subheader("🚀 Step-by-Step Launch Guide")
    
    steps = [
        {
            "title": "Pre-Launch (24-48h before)",
            "tasks": [
                "Finalize tokenomics based on AI recommendations",
                "Design token logo and metadata",
                "Set up social media accounts (Twitter, Telegram)",
                "Create website or landing page",
                "Build early community on Discord/Telegram",
                "Prepare marketing materials and memes"
            ]
        },
        {
            "title": "Token Creation",
            "tasks": [
                "Connect wallet (Phantom for Solana, MetaMask for Ethereum)",
                "Use recommended platform (Smithii, Orion Tools, etc.)",
                "Input token parameters from AI optimization",
                "Upload logo and metadata",
                "Pay creation fee (0.1-0.3 SOL or 0.01 ETH)",
                "Verify token creation on blockchain explorer"
            ]
        },
        {
            "title": "Liquidity Setup",
            "tasks": [
                "Create liquidity pool on DEX (Raydium for Solana, Uniswap for Ethereum)",
                "Add initial liquidity (recommended $10,000+)",
                "Set slippage tolerance (5-15% for new tokens)",
                "Lock liquidity (optional but builds trust)",
                "Verify pool creation"
            ]
        },
        {
            "title": "Launch Day",
            "tasks": [
                "Announce token contract address on social media",
                "Post on Reddit (r/CryptoMoonShots, r/SatoshiStreetBets)",
                "Share on Twitter with relevant hashtags",
                "Engage community in Telegram/Discord",
                "Monitor price and volume",
                "Respond to community questions"
            ]
        },
        {
            "title": "Post-Launch (Week 1)",
            "tasks": [
                "Apply for CoinGecko listing (free)",
                "Apply for CoinMarketCap listing (free)",
                "Continue social media marketing",
                "Partner with influencers",
                "Host AMAs and community events",
                "Track metrics and adjust strategy"
            ]
        }
    ]
    
    for i, step in enumerate(steps, 1):
        with st.expander(f"Step {i}: {step['title']}", expanded=(i==1)):
            for task in step['tasks']:
                st.checkbox(task, key=f"task_{i}_{task[:20]}")
    
    st.markdown("---")
    
    st.subheader("📊 Success Metrics to Track")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Holder Count", "Target: 1,000+", "First week")
    with col2:
        st.metric("24h Volume", "Target: $50K+", "Healthy trading")
    with col3:
        st.metric("Social Following", "Target: 5,000+", "Community size")
    
    st.info("💡 **Pro Tip**: The most successful meme coins combine strong community engagement, viral marketing, and strategic timing. Use AI recommendations for optimal launch windows during high market volume hours.")

# Call the main function
show()
