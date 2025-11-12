import streamlit as st
from wallet_manager import wallet_manager
from crypto_data import fetcher
from ai_crypto_expert import ai_expert
import os

def show():
    st.header("👁️ My Watchlist")
    st.caption("Track cryptocurrencies you're interested in with AI-powered alerts and analysis")
    
    tab1, tab2 = st.tabs(["My Watchlist", "Add to Watchlist"])
    
    with tab1:
        show_watchlist()
    
    with tab2:
        show_add_to_watchlist()

def show_watchlist():
    st.subheader("📋 Tracked Cryptocurrencies")
    
    watchlist_items = wallet_manager.get_watchlist()
    
    if not watchlist_items:
        st.info("👋 Your watchlist is empty. Add cryptocurrencies you want to track in the 'Add to Watchlist' tab!")
        return
    
    st.success(f"Tracking {len(watchlist_items)} cryptocurrencies")
    
    for item in watchlist_items:
        with st.container():
            try:
                crypto_data = fetcher.get_crypto_by_id(item.crypto_id)
                
                if crypto_data:
                    market_data = crypto_data.get('market_data', {})
                    current_price = market_data.get('current_price', {}).get('usd', 0)
                    price_change_24h = market_data.get('price_change_percentage_24h', 0)
                    market_cap = market_data.get('market_cap', {}).get('usd', 0)
                    volume_24h = market_data.get('total_volume', {}).get('usd', 0)
                    
                    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
                    
                    with col1:
                        st.write(f"**{item.crypto_name}** ({item.crypto_symbol.upper()})")
                        if item.notes:
                            st.caption(f"📝 {item.notes[:50]}...")
                    
                    with col2:
                        st.write(f"**${current_price:,.6f}**" if current_price < 1 else f"**${current_price:,.2f}**")
                        change_color = "green" if price_change_24h > 0 else "red" if price_change_24h < 0 else "gray"
                        st.markdown(f"<span style='color:{change_color}'>{price_change_24h:+.2f}% (24h)</span>", unsafe_allow_html=True)
                    
                    with col3:
                        if item.target_price:
                            distance_to_target = ((current_price - item.target_price) / item.target_price * 100) if item.target_price > 0 else 0
                            target_color = "green" if distance_to_target >= 0 else "orange"
                            st.write(f"🎯 Target: ${item.target_price:,.2f}")
                            st.markdown(f"<span style='color:{target_color}'>{distance_to_target:+.1f}% to target</span>", unsafe_allow_html=True)
                        else:
                            st.write("No target set")
                    
                    with col4:
                        st.write(f"MCap: ${market_cap/1e9:.2f}B" if market_cap > 1e9 else f"MCap: ${market_cap/1e6:.2f}M")
                        st.write(f"Vol: ${volume_24h/1e9:.2f}B" if volume_24h > 1e9 else f"Vol: ${volume_24h/1e6:.2f}M")
                    
                    with col5:
                        if st.button("🗑️", key=f"remove_{item.id}", help="Remove from watchlist"):
                            if wallet_manager.remove_from_watchlist(item.id):
                                st.success("Removed!")
                                st.rerun()
                
            except Exception as e:
                st.error(f"Error loading {item.crypto_name}: {str(e)}")
            
            st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("🤖 AI Watchlist Analysis")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if ai_key and ai_base_url and watchlist_items:
        if st.button("🚀 Analyze Entire Watchlist with AI", type="primary", use_container_width=True):
            with st.spinner("🤖 AI is analyzing all cryptocurrencies in your watchlist..."):
                try:
                    watchlist_summary = "Cryptocurrencies being tracked:\n"
                    for item in watchlist_items:
                        try:
                            crypto_data = fetcher.get_crypto_by_id(item.crypto_id)
                            if crypto_data:
                                market_data = crypto_data.get('market_data', {})
                                current_price = market_data.get('current_price', {}).get('usd', 0)
                                price_change_24h = market_data.get('price_change_percentage_24h', 0)
                                watchlist_summary += f"\n- {item.crypto_name} ({item.crypto_symbol.upper()}): ${current_price:,.2f}, 24h: {price_change_24h:+.2f}%"
                                if item.target_price:
                                    watchlist_summary += f", Target: ${item.target_price:,.2f}"
                        except:
                            pass
                    
                    prompt = f"""
                    Analyze this cryptocurrency watchlist and provide trading recommendations.
                    
                    {watchlist_summary}
                    
                    For each cryptocurrency, provide:
                    1. Buy/Sell/Hold recommendation
                    2. Confidence level (1-100)
                    3. Brief reasoning
                    4. Short-term outlook (24-48h)
                    
                    Respond ONLY with valid JSON:
                    {{
                        "recommendations": [
                            {{
                                "name": "Bitcoin",
                                "symbol": "BTC",
                                "action": "BUY|SELL|HOLD",
                                "confidence": 85,
                                "reasoning": "Brief reasoning...",
                                "outlook": "Bullish|Neutral|Bearish"
                            }}
                        ],
                        "top_pick": "Cryptocurrency name with highest potential",
                        "avoid": "Cryptocurrency to avoid if any"
                    }}
                    """
                    
                    from openai import OpenAI
                    client = OpenAI(
                        api_key=ai_key,
                        base_url=ai_base_url
                    )
                    
                    response = client.chat.completions.create(
                        model="gpt-5",
                        messages=[{"role": "user", "content": prompt}],
                        response_format={"type": "json_object"},
                        max_completion_tokens=2000
                    )
                    
                    import json
                    analysis = json.loads(response.choices[0].message.content or "{}")
                    
                    st.success("✅ AI Analysis Complete!")
                    
                    st.markdown("---")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        top_pick = analysis.get('top_pick', 'N/A')
                        st.markdown(f"### 🏆 Top Pick: {top_pick}")
                    
                    with col2:
                        avoid = analysis.get('avoid', 'None')
                        st.markdown(f"### ⚠️ Avoid: {avoid}")
                    
                    st.markdown("---")
                    
                    st.subheader("📊 Individual Recommendations")
                    
                    recommendations = analysis.get('recommendations', [])
                    for rec in recommendations:
                        action = rec.get('action', 'HOLD')
                        confidence = rec.get('confidence', 0)
                        
                        action_colors = {
                            'BUY': '#00ff00',
                            'HOLD': '#FFA500',
                            'SELL': '#ff0000'
                        }
                        action_color = action_colors.get(action, '#FFA500')
                        
                        with st.expander(f"{rec.get('name', 'Unknown')} ({rec.get('symbol', '').upper()}) - {action}"):
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.markdown(f"<h3 style='color:{action_color}'>{action}</h3>", unsafe_allow_html=True)
                                st.write(f"**Confidence:** {confidence}%")
                            
                            with col2:
                                outlook = rec.get('outlook', 'Neutral')
                                outlook_color = "green" if outlook == "Bullish" else "red" if outlook == "Bearish" else "gray"
                                st.markdown(f"**Outlook:** <span style='color:{outlook_color}'>{outlook}</span>", unsafe_allow_html=True)
                            
                            st.info(rec.get('reasoning', ''))
                
                except Exception as e:
                    st.error(f"AI Analysis Error: {str(e)}")

def show_add_to_watchlist():
    st.subheader("➕ Add Cryptocurrency to Watchlist")
    
    crypto_search = st.text_input("Search cryptocurrency", placeholder="Bitcoin, Trump, Dogecoin...")
    
    if crypto_search:
        with st.spinner("Searching..."):
            results = fetcher.search_crypto(crypto_search)
        
        if results:
            crypto_options = {f"{r['name']} ({r['symbol'].upper()})": r for r in results[:10]}
            selected_display = st.selectbox("Select cryptocurrency", list(crypto_options.keys()))
            selected_crypto = crypto_options[selected_display]
            
            st.markdown("---")
            
            crypto_id = selected_crypto['id']
            crypto_name = selected_crypto['name']
            crypto_symbol = selected_crypto['symbol']
            
            with st.spinner("Fetching current data..."):
                crypto_data = fetcher.get_crypto_by_id(crypto_id)
            
            if crypto_data:
                market_data = crypto_data.get('market_data', {})
                current_price = market_data.get('current_price', {}).get('usd', 0)
                price_change_24h = market_data.get('price_change_percentage_24h', 0)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Current Price", f"${current_price:,.6f}" if current_price < 1 else f"${current_price:,.2f}")
                
                with col2:
                    st.metric("24h Change", f"{price_change_24h:+.2f}%", delta=f"{price_change_24h:+.2f}%")
                
                with col3:
                    market_cap = market_data.get('market_cap', {}).get('usd', 0)
                    st.metric("Market Cap", f"${market_cap/1e9:.2f}B" if market_cap > 1e9 else f"${market_cap/1e6:.2f}M")
            
            target_price = st.number_input(
                "Target Price (optional)",
                min_value=0.0,
                value=0.0,
                step=0.01,
                format="%.6f",
                help="Set a target price to track progress towards your goal"
            )
            
            notes = st.text_area(
                "Notes (optional)",
                placeholder="Why are you tracking this? Any specific signals or patterns to watch?",
                height=100
            )
            
            if st.button("💾 Add to Watchlist", type="primary", use_container_width=True):
                success = wallet_manager.add_to_watchlist(
                    crypto_id=crypto_id,
                    crypto_name=crypto_name,
                    crypto_symbol=crypto_symbol,
                    target_price=target_price if target_price > 0 else None,
                    notes=notes
                )
                
                if success:
                    st.success(f"✅ Added {crypto_name} to your watchlist!")
                    st.balloons()
                    st.info("👈 Go to 'My Watchlist' tab to see all tracked cryptocurrencies")
                else:
                    st.warning(f"{crypto_name} is already in your watchlist!")
        
        else:
            st.warning("No results found. Try: bitcoin, ethereum, dogecoin, shiba-inu, pepe, official-trump")
    
    else:
        st.info("👆 Search for a cryptocurrency to add to your watchlist")

# Call the main function
show()
