import streamlit as st
from crypto_data import fetcher
from openai import OpenAI
import os
import json

def show():
    st.header("😊 Market Sentiment Analysis")
    st.caption("AI-powered sentiment tracking across cryptocurrency markets")
    
    tab1, tab2, tab3 = st.tabs(["Overall Market Sentiment", "Individual Crypto Sentiment", "Sentiment Trends"])
    
    with tab1:
        show_overall_sentiment()
    
    with tab2:
        show_individual_sentiment()
    
    with tab3:
        show_sentiment_trends()

def show_overall_sentiment():
    st.subheader("🌍 Global Cryptocurrency Market Sentiment")
    
    if st.button("🔍 Analyze Current Market Sentiment", type="primary", use_container_width=True):
        with st.spinner("🤖 AI is analyzing market sentiment across multiple sources..."):
            try:
                top_cryptos = fetcher.get_top_cryptos(limit=20)
                trending = fetcher.get_trending_cryptos()
                
                market_summary = "Top 20 Cryptocurrencies:\n"
                for crypto in top_cryptos[:20]:
                    name = crypto.get('name', 'Unknown')
                    price_change = crypto.get('price_change_percentage_24h', 0)
                    volume_change = crypto.get('total_volume', 0)
                    market_summary += f"- {name}: {price_change:+.2f}% (24h)\n"
                
                trending_summary = "\nTrending Coins:\n"
                if trending:
                    for coin in trending[:5]:
                        trending_summary += f"- {coin.get('name', 'Unknown')}\n"
                
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                prompt = f"""
                Analyze the overall cryptocurrency market sentiment based on this data:
                
                {market_summary}
                {trending_summary}
                
                Provide a comprehensive sentiment analysis. Respond ONLY with valid JSON:
                {{
                    "overall_sentiment": "Very Bullish|Bullish|Neutral|Bearish|Very Bearish",
                    "sentiment_score": 0-100,
                    "market_mood": "Fear|Greed|Extreme Fear|Extreme Greed|Neutral",
                    "key_observations": ["observation1", "observation2", "observation3"],
                    "bullish_factors": ["factor1", "factor2"],
                    "bearish_factors": ["factor1", "factor2"],
                    "recommendation": "Brief trading recommendation",
                    "sectors": {{
                        "meme_coins": "Bullish|Neutral|Bearish",
                        "defi": "Bullish|Neutral|Bearish",
                        "layer1": "Bullish|Neutral|Bearish",
                        "layer2": "Bullish|Neutral|Bearish"
                    }}
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=1500
                )
                
                analysis = json.loads(response.choices[0].message.content or "{}")
                
                overall_sentiment = analysis.get('overall_sentiment', 'Neutral')
                sentiment_score = analysis.get('sentiment_score', 50)
                market_mood = analysis.get('market_mood', 'Neutral')
                
                sentiment_colors = {
                    'Very Bullish': '#00ff00',
                    'Bullish': '#90EE90',
                    'Neutral': '#FFA500',
                    'Bearish': '#FF6347',
                    'Very Bearish': '#ff0000'
                }
                
                sentiment_color = sentiment_colors.get(overall_sentiment, '#FFA500')
                
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, {sentiment_color}22, {sentiment_color}44); 
                            padding: 2rem; border-radius: 10px; border-left: 5px solid {sentiment_color};'>
                    <h2 style='color: {sentiment_color}; margin:0;'>{overall_sentiment}</h2>
                    <h3 style='margin-top: 0.5rem;'>Sentiment Score: {sentiment_score}/100</h3>
                    <h4 style='margin-top: 0.5rem;'>Market Mood: {market_mood}</h4>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📈 Bullish Factors")
                    bullish_factors = analysis.get('bullish_factors', [])
                    for factor in bullish_factors:
                        st.success(f"✅ {factor}")
                
                with col2:
                    st.subheader("📉 Bearish Factors")
                    bearish_factors = analysis.get('bearish_factors', [])
                    for factor in bearish_factors:
                        st.warning(f"⚠️ {factor}")
                
                st.markdown("---")
                
                st.subheader("🔍 Key Observations")
                observations = analysis.get('key_observations', [])
                for obs in observations:
                    st.info(f"• {obs}")
                
                st.markdown("---")
                
                st.subheader("💡 Trading Recommendation")
                recommendation = analysis.get('recommendation', 'Monitor the market closely')
                st.success(recommendation)
                
                st.markdown("---")
                
                st.subheader("🏗️ Sector Sentiment")
                sectors = analysis.get('sectors', {})
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    meme_sentiment = sectors.get('meme_coins', 'Neutral')
                    meme_color = "green" if meme_sentiment == "Bullish" else "red" if meme_sentiment == "Bearish" else "gray"
                    st.markdown(f"**Meme Coins**")
                    st.markdown(f"<h4 style='color:{meme_color}'>{meme_sentiment}</h4>", unsafe_allow_html=True)
                
                with col2:
                    defi_sentiment = sectors.get('defi', 'Neutral')
                    defi_color = "green" if defi_sentiment == "Bullish" else "red" if defi_sentiment == "Bearish" else "gray"
                    st.markdown(f"**DeFi**")
                    st.markdown(f"<h4 style='color:{defi_color}'>{defi_sentiment}</h4>", unsafe_allow_html=True)
                
                with col3:
                    l1_sentiment = sectors.get('layer1', 'Neutral')
                    l1_color = "green" if l1_sentiment == "Bullish" else "red" if l1_sentiment == "Bearish" else "gray"
                    st.markdown(f"**Layer 1**")
                    st.markdown(f"<h4 style='color:{l1_color}'>{l1_sentiment}</h4>", unsafe_allow_html=True)
                
                with col4:
                    l2_sentiment = sectors.get('layer2', 'Neutral')
                    l2_color = "green" if l2_sentiment == "Bullish" else "red" if l2_sentiment == "Bearish" else "gray"
                    st.markdown(f"**Layer 2**")
                    st.markdown(f"<h4 style='color:{l2_color}'>{l2_sentiment}</h4>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Sentiment analysis error: {str(e)}")

def show_individual_sentiment():
    st.subheader("🎯 Individual Cryptocurrency Sentiment")
    
    crypto_search = st.text_input("Search cryptocurrency for sentiment analysis", placeholder="Bitcoin, Ethereum, Dogecoin...")
    
    if crypto_search:
        with st.spinner("Searching..."):
            results = fetcher.search_crypto(crypto_search)
        
        if results:
            crypto_options = {f"{r['name']} ({r['symbol'].upper()})": r for r in results[:10]}
            selected_display = st.selectbox("Select cryptocurrency", list(crypto_options.keys()))
            selected_crypto = crypto_options[selected_display]
            
            crypto_id = selected_crypto['id']
            crypto_name = selected_crypto['name']
            
            if st.button(f"🔍 Analyze {crypto_name} Sentiment", type="primary", use_container_width=True):
                with st.spinner(f"🤖 AI is analyzing {crypto_name} sentiment..."):
                    try:
                        crypto_data = fetcher.get_crypto_by_id(crypto_id)
                        historical_data = fetcher.get_historical_data(crypto_id, days=7)
                        
                        if not crypto_data:
                            st.error("Failed to load cryptocurrency data")
                            return
                        
                        market_data = crypto_data.get('market_data', {})
                        current_price = market_data.get('current_price', {}).get('usd', 0)
                        price_change_24h = market_data.get('price_change_percentage_24h', 0)
                        price_change_7d = market_data.get('price_change_percentage_7d', 0)
                        volume_24h = market_data.get('total_volume', {}).get('usd', 0)
                        market_cap = market_data.get('market_cap', {}).get('usd', 0)
                        
                        ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                        ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                        
                        if not ai_key or not ai_base_url:
                            st.error("AI API keys not configured")
                            return
                        
                        client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                        
                        prompt = f"""
                        Analyze the sentiment for {crypto_name} based on this data:
                        
                        Current Price: ${current_price}
                        24h Change: {price_change_24h:+.2f}%
                        7d Change: {price_change_7d:+.2f}%
                        24h Volume: ${volume_24h:,.0f}
                        Market Cap: ${market_cap:,.0f}
                        
                        Provide sentiment analysis. Respond ONLY with valid JSON:
                        {{
                            "sentiment": "Very Bullish|Bullish|Neutral|Bearish|Very Bearish",
                            "sentiment_score": 0-100,
                            "social_sentiment": "Positive|Negative|Neutral",
                            "price_action_sentiment": "Bullish|Bearish|Neutral",
                            "volume_sentiment": "Strong|Weak|Normal",
                            "key_factors": ["factor1", "factor2", "factor3"],
                            "community_mood": "Brief description of community sentiment",
                            "upcoming_catalysts": ["catalyst1", "catalyst2"],
                            "risks": ["risk1", "risk2"],
                            "short_term_outlook": "24-48h outlook",
                            "confidence": 0-100
                        }}
                        """
                        
                        response = client.chat.completions.create(
                            model="gpt-5",
                            messages=[{"role": "user", "content": prompt}],
                            response_format={"type": "json_object"},
                            max_completion_tokens=1500
                        )
                        
                        analysis = json.loads(response.choices[0].message.content or "{}")
                        
                        sentiment = analysis.get('sentiment', 'Neutral')
                        sentiment_score = analysis.get('sentiment_score', 50)
                        
                        sentiment_colors = {
                            'Very Bullish': '#00ff00',
                            'Bullish': '#90EE90',
                            'Neutral': '#FFA500',
                            'Bearish': '#FF6347',
                            'Very Bearish': '#ff0000'
                        }
                        
                        sentiment_color = sentiment_colors.get(sentiment, '#FFA500')
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Price", f"${current_price:,.2f}" if current_price > 1 else f"${current_price:.6f}")
                        
                        with col2:
                            st.metric("24h Change", f"{price_change_24h:+.2f}%", delta=f"{price_change_24h:+.2f}%")
                        
                        with col3:
                            st.metric("7d Change", f"{price_change_7d:+.2f}%", delta=f"{price_change_7d:+.2f}%")
                        
                        st.markdown("---")
                        
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, {sentiment_color}22, {sentiment_color}44); 
                                    padding: 2rem; border-radius: 10px; border-left: 5px solid {sentiment_color};'>
                            <h2 style='color: {sentiment_color}; margin:0;'>{sentiment}</h2>
                            <h3 style='margin-top: 0.5rem;'>Sentiment Score: {sentiment_score}/100</h3>
                            <h4 style='margin-top: 0.5rem;'>Confidence: {analysis.get('confidence', 0)}%</h4>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("---")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            social = analysis.get('social_sentiment', 'Neutral')
                            social_color = "green" if social == "Positive" else "red" if social == "Negative" else "gray"
                            st.markdown(f"**Social Sentiment**")
                            st.markdown(f"<h4 style='color:{social_color}'>{social}</h4>", unsafe_allow_html=True)
                        
                        with col2:
                            price_action = analysis.get('price_action_sentiment', 'Neutral')
                            price_color = "green" if price_action == "Bullish" else "red" if price_action == "Bearish" else "gray"
                            st.markdown(f"**Price Action**")
                            st.markdown(f"<h4 style='color:{price_color}'>{price_action}</h4>", unsafe_allow_html=True)
                        
                        with col3:
                            volume = analysis.get('volume_sentiment', 'Normal')
                            volume_color = "green" if volume == "Strong" else "red" if volume == "Weak" else "gray"
                            st.markdown(f"**Volume**")
                            st.markdown(f"<h4 style='color:{volume_color}'>{volume}</h4>", unsafe_allow_html=True)
                        
                        st.markdown("---")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("🚀 Upcoming Catalysts")
                            catalysts = analysis.get('upcoming_catalysts', [])
                            for catalyst in catalysts:
                                st.success(f"✅ {catalyst}")
                        
                        with col2:
                            st.subheader("⚠️ Risks")
                            risks = analysis.get('risks', [])
                            for risk in risks:
                                st.warning(f"⚠️ {risk}")
                        
                        st.markdown("---")
                        
                        st.subheader("🔑 Key Factors")
                        key_factors = analysis.get('key_factors', [])
                        for factor in key_factors:
                            st.info(f"• {factor}")
                        
                        st.markdown("---")
                        
                        st.subheader("💬 Community Mood")
                        community_mood = analysis.get('community_mood', 'N/A')
                        st.write(community_mood)
                        
                        st.subheader("⏱️ Short-term Outlook (24-48h)")
                        outlook = analysis.get('short_term_outlook', 'N/A')
                        st.info(outlook)
                        
                    except Exception as e:
                        st.error(f"Sentiment analysis error: {str(e)}")
        
        else:
            st.warning("No results found. Try: bitcoin, ethereum, dogecoin")

def show_sentiment_trends():
    st.subheader("📊 Sentiment Trends & Patterns")
    
    st.info("This section shows how market sentiment has evolved over time")
    
    if st.button("📈 Analyze Sentiment Trends", type="primary", use_container_width=True):
        with st.spinner("🤖 AI is analyzing sentiment trends..."):
            try:
                top_cryptos = fetcher.get_top_cryptos(limit=10)
                
                trend_data = []
                for crypto in top_cryptos:
                    name = crypto.get('name', 'Unknown')
                    price_change_24h = crypto.get('price_change_percentage_24h', 0)
                    price_change_7d = crypto.get('price_change_percentage_7d', 0)
                    volume = crypto.get('total_volume', 0)
                    
                    trend_data.append({
                        'name': name,
                        'change_24h': price_change_24h,
                        'change_7d': price_change_7d,
                        'volume': volume
                    })
                
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                trend_summary = "\n".join([f"{d['name']}: 24h: {d['change_24h']:+.2f}%, 7d: {d['change_7d']:+.2f}%" for d in trend_data])
                
                prompt = f"""
                Analyze the sentiment trend based on this price movement data:
                
                {trend_summary}
                
                Identify patterns and trends. Respond ONLY with valid JSON:
                {{
                    "trend_direction": "Improving|Declining|Stable",
                    "momentum": "Accelerating|Decelerating|Steady",
                    "pattern_detected": "Pattern description",
                    "key_insights": ["insight1", "insight2", "insight3"],
                    "sentiment_shift": "Becoming more bullish|Becoming more bearish|Unchanged",
                    "next_24h_prediction": "Prediction for next 24 hours",
                    "confidence": 0-100
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=1000
                )
                
                analysis = json.loads(response.choices[0].message.content or "{}")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    trend = analysis.get('trend_direction', 'Stable')
                    trend_color = "green" if trend == "Improving" else "red" if trend == "Declining" else "gray"
                    st.markdown(f"**Trend Direction**")
                    st.markdown(f"<h3 style='color:{trend_color}'>{trend}</h3>", unsafe_allow_html=True)
                
                with col2:
                    momentum = analysis.get('momentum', 'Steady')
                    momentum_color = "green" if momentum == "Accelerating" else "orange" if momentum == "Decelerating" else "gray"
                    st.markdown(f"**Momentum**")
                    st.markdown(f"<h3 style='color:{momentum_color}'>{momentum}</h3>", unsafe_allow_html=True)
                
                with col3:
                    confidence = analysis.get('confidence', 0)
                    st.markdown(f"**Confidence**")
                    st.markdown(f"<h3>{confidence}%</h3>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                st.subheader("📈 Sentiment Shift")
                sentiment_shift = analysis.get('sentiment_shift', 'Unchanged')
                shift_color = "green" if "bullish" in sentiment_shift.lower() else "red" if "bearish" in sentiment_shift.lower() else "gray"
                st.markdown(f"<h4 style='color:{shift_color}'>{sentiment_shift}</h4>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                st.subheader("🔍 Pattern Detected")
                pattern = analysis.get('pattern_detected', 'No clear pattern')
                st.info(pattern)
                
                st.markdown("---")
                
                st.subheader("💡 Key Insights")
                insights = analysis.get('key_insights', [])
                for insight in insights:
                    st.success(f"• {insight}")
                
                st.markdown("---")
                
                st.subheader("⏱️ Next 24h Prediction")
                prediction = analysis.get('next_24h_prediction', 'Market conditions uncertain')
                st.warning(prediction)
                
            except Exception as e:
                st.error(f"Trend analysis error: {str(e)}")

# Call the main function
show()
