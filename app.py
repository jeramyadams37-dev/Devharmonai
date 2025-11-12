import streamlit as st
import os

st.set_page_config(
    page_title="AI Crypto Empire Builder",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

from database import init_db
init_db()

st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }
    .feature-box {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        margin: 1rem 0;
    }
    .metric-card {
        padding: 1rem;
        border-radius: 8px;
        background: rgba(255, 215, 0, 0.1);
        border-left: 4px solid #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🚀 AI Crypto Empire Builder</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Track Markets · Predict Movements · Create Your Own Cryptocurrency</p>', unsafe_allow_html=True)

st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; 
                border-radius: 15px; 
                text-align: center; 
                margin: 1rem 0 2rem 0;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">
        <h2 style="color: white; margin: 0; font-size: 1.8rem;">📱 OnTime Family Planning App</h2>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0; font-size: 1.1rem;">
            The official platform for the Ilah Hughs Token (ILAH)
        </p>
        <p style="color: rgba(255,255,255,0.85); margin: 0.8rem 0; font-size: 0.95rem;">
            🎯 Schedule Family Activities • 💰 Earn ILAH Rewards • 🔒 Privacy-First Design
        </p>
        <div style="margin-top: 1rem;">
            <a href="#" style="display: inline-block; background: white; color: #667eea; 
                               padding: 0.75rem 2rem; border-radius: 25px; text-decoration: none; 
                               font-weight: bold; margin: 0.5rem;">
                📥 Download for iOS
            </a>
            <a href="#" style="display: inline-block; background: white; color: #764ba2; 
                               padding: 0.75rem 2rem; border-radius: 25px; text-decoration: none; 
                               font-weight: bold; margin: 0.5rem;">
                📥 Download for Android
            </a>
        </div>
        <p style="color: rgba(255,255,255,0.7); margin-top: 1rem; font-size: 0.85rem;">
            ⭐ Earn ILAH tokens by using the app • Stake with family • Zero transaction fees
        </p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Select Page",
        ["🏠 Home", "💼 My Wallet", "💱 Crypto Exchange", "💰 Revenue Dashboard", "🔄 How It Works", "💎 Staking Rewards", "👁️ Watchlist", "📊 Trading Signals", "📈 Backtesting", "😊 Sentiment Analysis", "🚀 Marketing", "🎙️ The Alpha Signal", "💳 Subscribe to Podcast", "📊 Market Dashboard", "🤖 AI Analysis", "🪙 Create Token", "💎 Ilah Hughs Token", "📈 Token Manager", "🔥 Trending & Alerts"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.subheader("AI Status")
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if ai_key and ai_base_url:
        st.success("✅ AI Integration Active")
        st.caption("Using Replit AI Integrations")
    else:
        st.warning("⚠️ AI Integration Setup Needed")
        st.caption("Click 'Setup AI' to configure")
    
    st.divider()
    st.caption("💰 Built for Maximum Profit")
    st.caption("🔒 Secure & Fast")

if page == "🏠 Home":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Portfolio Tracking", "NEW", "Track your holdings")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Cryptocurrencies", "100+", "Trump, Doge, Shib, Pepe")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("AI Accuracy", "67-82%", "CNN-LSTM Models")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Token Creation", "2 Chains", "Solana & Ethereum")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("🎯 Platform Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💼 Crypto Wallet (NEW!)
        - **Portfolio Tracking**: Add and track all your crypto holdings
        - **Real-Time P/L**: Live profit/loss calculations
        - **AI Portfolio Analysis**: Get personalized rebalancing recommendations
        - **Risk Assessment**: Portfolio health and diversification scoring
        - **Smart Suggestions**: AI tells you what to buy, sell, or hold
        """)
        
        st.markdown("""
        ### 📊 Market Intelligence
        - **Real-Time Tracking**: Monitor 100+ cryptocurrencies with live price updates
        - **AI Predictions**: Multi-timeframe forecasts (1h to 30 days)
        - **Technical Analysis**: RSI, MACD, Bollinger Bands, MVRV, SOPR
        - **Volume Analysis**: Detect unusual activity before pumps
        - **Whale Tracking**: Monitor large holder movements
        """)
    
    with col2:
        st.markdown("""
        ### 🪙 Token Creation
        - **Multi-Chain Support**: Create tokens on Solana or Ethereum
        - **AI Tokenomics Optimizer**: Recommended supply and pricing
        - **Launch Strategy**: Marketing plans and viral content
        - **Liquidity Guidance**: Uniswap & Raydium pool setup
        - **Cost Efficient**: 0.1-0.3 SOL or 0.01 ETH
        """)
        
        st.markdown("""
        ### 📈 Token Management
        - **Real-Time Metrics**: Track your token's price and volume
        - **Holder Analytics**: Monitor wallet distribution
        - **Marketing AI**: Auto-generate promotion content
        - **Launch Timing**: Optimal market entry recommendations
        - **Profit Maximization**: Data-driven growth strategies
        """)
    
    st.markdown("---")
    
    st.header("🧠 AI Knowledge Base")
    
    with st.expander("📚 Blockchain Analysis Techniques"):
        st.markdown("""
        **On-Chain Metrics:**
        - Exchange Reserves: Track sell pressure indicators
        - Whale Activity: Monitor large transactions (>1,000 BTC)
        - UTXO Age: Analyze coin distribution patterns
        - Hash Rate: Network security and miner confidence
        - Active Addresses: Network growth indicators
        
        **Advanced Models:**
        - MVRV Ratio: Market value vs realized value (>3.5 = overheated)
        - SOPR: Spent output profit ratio (profit/loss tracking)
        - NVT Ratio: Network value to transactions
        - Stock-to-Flow: Scarcity-based prediction models
        """)
    
    with st.expander("🎭 Meme Coin Trading Patterns"):
        st.markdown("""
        **Key Patterns:**
        - Triangular consolidation followed by 300-500% breakouts
        - Exchange reserve decreases = reduced sell pressure
        - Whale accumulation before pump events
        - Social sentiment spikes 24-72h before price moves
        
        **Trump Coin Specifics:**
        - Current Price: ~$7.14 (Down 90% from $75 ATH)
        - High Volatility: Political events drive 20-70% swings
        - Support Levels: $7.50 critical, $6.80 breakdown zone
        - Resistance: $8.80-$9.00 barrier
        """)
    
    with st.expander("🔮 Prediction Strategies"):
        st.markdown("""
        **Multi-Timeframe Analysis:**
        - 1 Hour: Scalping opportunities and momentum shifts
        - 4 Hour: Intraday trend confirmation
        - 24 Hour: Daily trading signals
        - 7 Day: Swing trading setups
        - 30 Day: Position trading and macro trends
        
        **Signal Confidence Scoring:**
        - 80-100%: Strong buy/sell with multiple confirmations
        - 60-79%: Moderate confidence, partial positions
        - 40-59%: Weak signal, wait for confirmation
        - <40%: No clear signal, avoid trading
        """)
    
    st.markdown("---")
    
    st.header("🚀 Quick Start Guide")
    
    tab1, tab2, tab3 = st.tabs(["Market Analysis", "Token Creation", "AI Predictions"])
    
    with tab1:
        st.markdown("""
        1. Navigate to **Market Dashboard**
        2. Select cryptocurrency from dropdown
        3. Choose timeframe for analysis
        4. View real-time charts with indicators
        5. Check AI prediction signals
        """)
    
    with tab2:
        st.markdown("""
        1. Go to **Create Token** page
        2. Choose blockchain (Solana or Ethereum)
        3. Configure token parameters (name, symbol, supply)
        4. Get AI tokenomics recommendations
        5. Follow launch strategy guidance
        6. Connect wallet to deploy (external)
        """)
    
    with tab3:
        st.markdown("""
        1. Open **AI Analysis** page
        2. Select cryptocurrency to analyze
        3. AI examines on-chain metrics, volume, sentiment
        4. Receive buy/sell/hold recommendation
        5. View confidence score and reasoning
        6. Set up alerts for price targets
        """)
    
    st.info("💡 **Tip**: The AI uses comprehensive blockchain knowledge including meme coin patterns, whale tracking, and volume anomaly detection to maximize your profit potential.")

elif page == "💼 My Wallet":
    try:
        from pages import wallet
        wallet.show()
    except Exception as e:
        st.error(f"Error loading wallet: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "💱 Crypto Exchange":
    try:
        from pages import crypto_exchange
        crypto_exchange.show()
    except Exception as e:
        st.error(f"Error loading crypto exchange: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "💰 Revenue Dashboard":
    try:
        from pages import revenue_dashboard
        revenue_dashboard.show()
    except Exception as e:
        st.error(f"Error loading revenue dashboard: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "🔄 How It Works":
    try:
        from pages import how_it_works
        exec(open("pages/how_it_works.py").read())
    except Exception as e:
        st.error(f"Error loading How It Works page: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "💎 Staking Rewards":
    try:
        from pages import staking
        staking.show()
    except Exception as e:
        st.error(f"Error loading staking: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "👁️ Watchlist":
    try:
        from pages import watchlist
        watchlist.show()
    except Exception as e:
        st.error(f"Error loading watchlist: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "📊 Trading Signals":
    try:
        from pages import signals
        signals.show()
    except Exception as e:
        st.error(f"Error loading signals: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "📈 Backtesting":
    try:
        from pages import backtesting
        backtesting.show()
    except Exception as e:
        st.error(f"Error loading backtesting: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "😊 Sentiment Analysis":
    try:
        from pages import sentiment
        sentiment.show()
    except Exception as e:
        st.error(f"Error loading sentiment: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "🚀 Marketing":
    try:
        from pages import marketing
        marketing.show()
    except Exception as e:
        st.error(f"Error loading marketing: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "🎙️ The Alpha Signal":
    try:
        from pages import podcast
        podcast.show()
    except Exception as e:
        st.error(f"Error loading podcast: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "💳 Subscribe to Podcast":
    try:
        from pages import podcast_subscription
        podcast_subscription.show()
    except Exception as e:
        st.error(f"Error loading subscription page: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "📊 Market Dashboard":
    from pages import market_dashboard
    market_dashboard.show()

elif page == "🤖 AI Analysis":
    from pages import ai_analysis
    ai_analysis.show()

elif page == "🪙 Create Token":
    from pages import token_creator
    token_creator.show()

elif page == "💎 Ilah Hughs Token":
    try:
        from pages import ilah_hughs_token
        ilah_hughs_token.show()
    except Exception as e:
        st.error(f"Error loading Ilah Hughs Token page: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

elif page == "📈 Token Manager":
    from pages import token_manager
    token_manager.show()

elif page == "🔥 Trending & Alerts":
    from pages import trending_alerts
    trending_alerts.show()
