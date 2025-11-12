import streamlit as st
from crypto_data import fetcher
from technical_analysis import analyzer
from ai_crypto_expert import ai_expert
import os

def show():
    st.header("🤖 AI Crypto Analysis")
    st.caption("AI-powered predictions using blockchain intelligence and meme coin expertise")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if not ai_key or not ai_base_url:
        st.warning("⚠️ AI Integration not configured. AI analysis features require Replit AI Integrations.")
        st.info("The integration should be automatically set up. If you see this message, please try restarting the app.")
        return
    
    if 'user_email' not in st.session_state:
        st.session_state['user_email'] = None
    
    if not st.session_state['user_email']:
        st.info("👤 **Enter your email to access AI Analysis**")
        user_email = st.text_input("Email Address", placeholder="your.email@example.com", key="ai_email_input")
        
        if st.button("Continue", type="primary"):
            if user_email and '@' in user_email:
                st.session_state['user_email'] = user_email
                st.rerun()
            else:
                st.error("Please enter a valid email address")
        
        st.markdown("---")
        st.caption("💡 Free users get general market analysis. Subscribe to The Alpha Signal for specific buy/sell signals!")
        return
    
    col_user1, col_user2 = st.columns([3, 1])
    with col_user1:
        st.caption(f"👤 Logged in as: {st.session_state['user_email']}")
    with col_user2:
        if st.button("🚪 Logout", key="ai_logout", use_container_width=True):
            st.session_state['user_email'] = None
            st.rerun()
    
    st.success("✅ AI Analysis Engine Active - Using Replit AI Integrations")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        crypto_search = st.text_input("Search cryptocurrency for AI analysis", 
                                      placeholder="Bitcoin, Trump, Dogecoin, Shiba Inu...")
    
    with col2:
        analysis_type = st.selectbox("Analysis Type", ["Full Analysis", "Quick Scan"])
    
    if crypto_search:
        with st.spinner("Searching..."):
            results = fetcher.search_crypto(crypto_search)
        
        if results:
            crypto_options = {f"{r['name']} ({r['symbol'].upper()})": r['id'] for r in results[:10]}
            selected_crypto_display = st.selectbox("Select cryptocurrency", list(crypto_options.keys()))
            selected_crypto_id = crypto_options[selected_crypto_display]
            
            if st.button("🚀 Analyze with AI", type="primary", use_container_width=True):
                analyze_cryptocurrency(selected_crypto_id, selected_crypto_display, analysis_type)
        else:
            st.warning("No results found. Try: bitcoin, ethereum, dogecoin, shiba-inu, pepe, official-trump")
    else:
        st.info("👆 Enter a cryptocurrency name to start AI analysis")
        
        st.markdown("---")
        st.subheader("AI Knowledge Base")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.expander("📊 On-Chain Analysis"):
                st.markdown("""
                - **Exchange Reserves**: Tracks sell pressure
                - **Whale Activity**: >1,000 BTC movements
                - **UTXO Age Distribution**: Holder confidence
                - **Hash Rate**: Network security
                - **Active Addresses**: Adoption metrics
                """)
            
            with st.expander("🎯 Prediction Models"):
                st.markdown("""
                - **MVRV Ratio**: Market overheating indicator
                - **SOPR**: Profit/loss tracking
                - **NVT Ratio**: Network valuation
                - **Stock-to-Flow**: Scarcity modeling
                """)
        
        with col2:
            with st.expander("🎭 Meme Coin Expertise"):
                st.markdown("""
                - **Trump Coin**: Political event tracking
                - **DOGE**: Institutional interest patterns
                - **SHIB**: Triangular consolidation analysis
                - **PEPE**: Whale accumulation signals
                """)
            
            with st.expander("⚠️ Risk Detection"):
                st.markdown("""
                - **Pump & Dump**: Pattern recognition
                - **Rug Pull**: Smart contract analysis
                - **Volume Anomalies**: Manipulation detection
                - **Social Manipulation**: Coordinated campaigns
                """)

def analyze_cryptocurrency(crypto_id, crypto_name, analysis_type):
    with st.spinner("Loading market data..."):
        crypto_info = fetcher.get_crypto_by_id(crypto_id)
        historical_data = fetcher.get_historical_data(crypto_id, days=30)
    
    if not crypto_info or historical_data.empty:
        st.error("Failed to load cryptocurrency data.")
        return
    
    market_data = crypto_info.get('market_data', {})
    current_price = market_data.get('current_price', {}).get('usd', 0)
    price_change_24h = market_data.get('price_change_percentage_24h', 0)
    market_cap = market_data.get('market_cap', {}).get('usd', 0)
    total_volume = market_data.get('total_volume', {}).get('usd', 0)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Price", f"${current_price:,.2f}" if current_price > 1 else f"${current_price:.6f}")
    with col2:
        st.metric("24h Change", f"{price_change_24h:+.2f}%", delta=f"{price_change_24h:+.2f}%")
    with col3:
        st.metric("Market Cap", f"${market_cap/1e9:.2f}B" if market_cap > 1e9 else f"${market_cap/1e6:.2f}M")
    with col4:
        st.metric("Volume", f"${total_volume/1e9:.2f}B" if total_volume > 1e9 else f"${total_volume/1e6:.2f}M")
    
    with st.spinner("Calculating technical indicators..."):
        historical_data = analyzer.calculate_indicators(historical_data)
        technical_data = analyzer.calculate_momentum_indicators(historical_data)
    
    st.markdown("---")
    
    with st.spinner("🤖 AI is analyzing market data, on-chain metrics, and patterns... This may take a moment."):
        try:
            ai_analysis = ai_expert.analyze_crypto(
                crypto_name,
                current_price,
                price_change_24h,
                total_volume,
                market_cap,
                technical_data
            )
            
            signal = ai_analysis.get('signal', 'HOLD')
            confidence = ai_analysis.get('confidence', 0)
            
            signal_colors = {
                'STRONG BUY': '#00ff00',
                'BUY': '#90EE90',
                'HOLD': '#FFA500',
                'SELL': '#FF6347',
                'STRONG SELL': '#ff0000'
            }
            
            signal_color = signal_colors.get(signal, '#FFA500')
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {signal_color}22, {signal_color}44); 
                        padding: 2rem; border-radius: 10px; border-left: 5px solid {signal_color};'>
                <h2 style='color: {signal_color}; margin:0;'>🎯 {signal}</h2>
                <h3 style='margin-top: 0.5rem;'>Confidence: {confidence}%</h3>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("✅ Key Factors")
                key_factors = ai_analysis.get('key_factors', [])
                for factor in key_factors:
                    st.success(f"• {factor}")
                
                st.subheader("📈 Price Predictions")
                short_term = ai_analysis.get('short_term_prediction', 'Neutral')
                medium_term = ai_analysis.get('medium_term_prediction', 'Neutral')
                
                st.write(f"**24h Outlook:** {short_term}")
                st.write(f"**7d Outlook:** {medium_term}")
            
            with col2:
                st.subheader("⚠️ Risks")
                risks = ai_analysis.get('risks', [])
                for risk in risks:
                    st.warning(f"• {risk}")
                
                st.subheader("💰 Price Levels")
                entry = ai_analysis.get('entry_price')
                exit_price = ai_analysis.get('exit_price')
                stop_loss = ai_analysis.get('stop_loss')
                
                if entry:
                    st.write(f"**Entry Price:** ${entry:,.2f}")
                if exit_price:
                    st.write(f"**Target Price:** ${exit_price:,.2f}")
                if stop_loss:
                    st.write(f"**Stop Loss:** ${stop_loss:,.2f}")
            
            st.markdown("---")
            
            st.subheader("🧠 AI Reasoning")
            reasoning = ai_analysis.get('reasoning', 'Analysis complete.')
            st.info(reasoning)
            
            st.markdown("---")
            
            # Financial Intelligence Section
            st.subheader("💼 Financial Intelligence & Money Management")
            
            col1, col2 = st.columns(2)
            
            with col1:
                risk_level = ai_analysis.get('risk_level', 'Medium')
                risk_colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red', 'Extreme': 'darkred'}
                risk_color = risk_colors.get(risk_level, 'orange')
                st.markdown(f"**Risk Level:** <span style='color:{risk_color}; font-weight:bold;'>{risk_level}</span>", unsafe_allow_html=True)
                
                position_size = ai_analysis.get('position_size_recommendation', '1-2% of portfolio')
                st.write(f"**Position Size:** {position_size}")
                
                st.markdown("**Profit Taking Strategy:**")
                profit_strategy = ai_analysis.get('profit_taking_strategy', 'Take profits gradually')
                st.success(profit_strategy)
            
            with col2:
                st.markdown("**Financial Health Checklist:**")
                health_check = ai_analysis.get('financial_health_check', [
                    "Only invest what you can afford to lose",
                    "Have an emergency fund",
                    "Diversify across multiple assets"
                ])
                for check in health_check:
                    st.warning(f"✓ {check}")
            
            st.markdown("---")
            
            if st.button("💾 Save This Signal", type="secondary", use_container_width=True):
                from wallet_manager import wallet_manager
                success = wallet_manager.save_trading_signal(
                    crypto_id=crypto_id,
                    crypto_name=crypto_name,
                    signal_type=signal,
                    confidence=confidence,
                    current_price=current_price,
                    target_price=exit_price if exit_price else None,
                    stop_loss=stop_loss if stop_loss else None,
                    reasoning=reasoning[:500] if reasoning else None
                )
                
                if success:
                    st.success("✅ Signal saved! View all saved signals in the Trading Signals page.")
                else:
                    st.error("Failed to save signal.")
            
        except Exception as e:
            st.error(f"AI Analysis Error: {str(e)}")
            st.info("Please try again or select a different cryptocurrency.")

# Call the main function
show()
