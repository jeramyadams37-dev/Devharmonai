import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from crypto_data import fetcher
from technical_analysis import analyzer

def show():
    st.header("📊 Market Dashboard")
    st.caption("Real-time cryptocurrency tracking with advanced technical analysis")
    
    tab1, tab2, tab3 = st.tabs(["Market Overview", "Detailed Analysis", "Meme Coins"])
    
    with tab1:
        show_market_overview()
    
    with tab2:
        show_detailed_analysis()
    
    with tab3:
        show_meme_coins()

def show_market_overview():
    st.subheader("Top Cryptocurrencies by Market Cap")
    
    with st.spinner("Loading market data..."):
        cryptos = fetcher.get_top_cryptos(limit=50)
    
    if not cryptos:
        st.error("Failed to load market data. Please try again.")
        return
    
    global_data = fetcher.get_global_market_data()
    
    if global_data:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_mcap = global_data.get('total_market_cap', {}).get('usd', 0)
            st.metric("Total Market Cap", f"${total_mcap/1e12:.2f}T")
        with col2:
            btc_dominance = global_data.get('market_cap_percentage', {}).get('btc', 0)
            st.metric("BTC Dominance", f"{btc_dominance:.1f}%")
        with col3:
            total_volume = global_data.get('total_volume', {}).get('usd', 0)
            st.metric("24h Volume", f"${total_volume/1e9:.1f}B")
        with col4:
            active_cryptos = global_data.get('active_cryptocurrencies', 0)
            st.metric("Active Cryptos", f"{active_cryptos:,}")
    
    st.markdown("---")
    
    df_cryptos = pd.DataFrame(cryptos)
    df_display = df_cryptos[[
        'market_cap_rank', 'name', 'symbol', 'current_price', 
        'price_change_percentage_24h', 'market_cap', 'total_volume'
    ]].copy()
    
    df_display.columns = ['Rank', 'Name', 'Symbol', 'Price', '24h %', 'Market Cap', 'Volume']
    df_display['Price'] = df_display['Price'].apply(lambda x: f"${x:,.2f}" if x > 1 else f"${x:.6f}")
    df_display['24h %'] = df_display['24h %'].apply(lambda x: f"{x:+.2f}%" if pd.notna(x) else "N/A")
    df_display['Market Cap'] = df_display['Market Cap'].apply(lambda x: f"${x/1e9:.2f}B" if x > 1e9 else f"${x/1e6:.2f}M")
    df_display['Volume'] = df_display['Volume'].apply(lambda x: f"${x/1e9:.2f}B" if x > 1e9 else f"${x/1e6:.2f}M")
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)

def show_detailed_analysis():
    st.subheader("Detailed Technical Analysis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        crypto_search = st.text_input("Search cryptocurrency", placeholder="Bitcoin, Ethereum, Trump...")
    
    with col2:
        timeframe = st.selectbox("Timeframe", ["7 Days", "14 Days", "30 Days", "90 Days", "180 Days", "1 Year"])
    
    days_map = {
        "7 Days": 7,
        "14 Days": 14,
        "30 Days": 30,
        "90 Days": 90,
        "180 Days": 180,
        "1 Year": 365
    }
    
    if crypto_search:
        with st.spinner("Searching..."):
            results = fetcher.search_crypto(crypto_search)
        
        if results:
            crypto_options = {f"{r['name']} ({r['symbol'].upper()})": r['id'] for r in results[:10]}
            selected_crypto_display = st.selectbox("Select cryptocurrency", list(crypto_options.keys()))
            selected_crypto_id = crypto_options[selected_crypto_display]
        else:
            st.warning("No results found. Try searching for: bitcoin, ethereum, dogecoin, shiba-inu, pepe, official-trump")
            return
    else:
        st.info("👆 Search for a cryptocurrency above to begin analysis")
        return
    
    if selected_crypto_id:
        with st.spinner("Loading data..."):
            crypto_info = fetcher.get_crypto_by_id(selected_crypto_id)
            historical_data = fetcher.get_historical_data(selected_crypto_id, days=days_map[timeframe])
        
        if crypto_info and not historical_data.empty:
            market_data = crypto_info.get('market_data', {})
            current_price = market_data.get('current_price', {}).get('usd', 0)
            price_change_24h = market_data.get('price_change_percentage_24h', 0)
            market_cap = market_data.get('market_cap', {}).get('usd', 0)
            total_volume = market_data.get('total_volume', {}).get('usd', 0)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Current Price", f"${current_price:,.2f}" if current_price > 1 else f"${current_price:.6f}")
            with col2:
                st.metric("24h Change", f"{price_change_24h:+.2f}%", delta=f"{price_change_24h:+.2f}%")
            with col3:
                st.metric("Market Cap", f"${market_cap/1e9:.2f}B" if market_cap > 1e9 else f"${market_cap/1e6:.2f}M")
            with col4:
                st.metric("24h Volume", f"${total_volume/1e9:.2f}B" if total_volume > 1e9 else f"${total_volume/1e6:.2f}M")
            
            historical_data = analyzer.calculate_indicators(historical_data)
            
            fig = make_subplots(
                rows=3, cols=1,
                shared_xaxes=True,
                vertical_spacing=0.05,
                row_heights=[0.5, 0.25, 0.25],
                subplot_titles=('Price with Bollinger Bands', 'RSI', 'MACD')
            )
            
            fig.add_trace(go.Candlestick(
                x=historical_data['timestamp'],
                open=historical_data['price'],
                high=historical_data['price'],
                low=historical_data['price'],
                close=historical_data['price'],
                name='Price'
            ), row=1, col=1)
            
            if 'bb_upper' in historical_data.columns:
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['bb_upper'],
                    name='BB Upper',
                    line=dict(color='rgba(250, 0, 0, 0.3)', width=1)
                ), row=1, col=1)
                
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['bb_middle'],
                    name='BB Middle',
                    line=dict(color='rgba(0, 0, 250, 0.3)', width=1)
                ), row=1, col=1)
                
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['bb_lower'],
                    name='BB Lower',
                    line=dict(color='rgba(0, 250, 0, 0.3)', width=1)
                ), row=1, col=1)
            
            if 'rsi' in historical_data.columns:
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['rsi'],
                    name='RSI',
                    line=dict(color='purple', width=2)
                ), row=2, col=1)
                
                fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
                fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
            
            if 'macd' in historical_data.columns:
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['macd'],
                    name='MACD',
                    line=dict(color='blue', width=2)
                ), row=3, col=1)
                
                fig.add_trace(go.Scatter(
                    x=historical_data['timestamp'],
                    y=historical_data['macd_signal'],
                    name='Signal',
                    line=dict(color='orange', width=2)
                ), row=3, col=1)
            
            fig.update_layout(
                height=800,
                showlegend=True,
                xaxis_rangeslider_visible=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Technical Indicators")
            momentum = analyzer.calculate_momentum_indicators(historical_data)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("RSI", f"{momentum.get('rsi', 'N/A')}", momentum.get('rsi_signal', 'N/A'))
            with col2:
                st.metric("MACD Trend", momentum.get('macd_trend', 'N/A'))
            with col3:
                st.metric("Volume", f"{momentum.get('volume_ratio', 'N/A')}x", momentum.get('volume_signal', 'N/A'))
            
            patterns = analyzer.detect_patterns(historical_data)
            if patterns:
                st.subheader("Detected Patterns")
                for pattern in patterns:
                    with st.expander(f"🔍 {pattern['pattern']} - {pattern['signal']}"):
                        st.write(pattern['description'])
            
            levels = analyzer.calculate_support_resistance(historical_data)
            if levels['support'] or levels['resistance']:
                st.subheader("Support & Resistance Levels")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Support Levels:**")
                    for level in levels['support']:
                        st.write(f"${level:,.2f}")
                with col2:
                    st.write("**Resistance Levels:**")
                    for level in levels['resistance']:
                        st.write(f"${level:,.2f}")

def show_meme_coins():
    st.subheader("🎭 Meme Coin Tracker")
    st.caption("Specialized tracking for DOGE, SHIB, PEPE, TRUMP and more")
    
    with st.spinner("Loading meme coins..."):
        meme_coins = fetcher.get_meme_coins()
    
    if not meme_coins:
        st.error("Failed to load meme coin data.")
        return
    
    for coin in meme_coins:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])
            
            with col1:
                st.write(f"**{coin['name']}** ({coin['symbol'].upper()})")
            
            with col2:
                price = coin['current_price']
                st.write(f"${price:,.6f}" if price < 1 else f"${price:,.2f}")
            
            with col3:
                change_24h = coin.get('price_change_percentage_24h', 0)
                color = "green" if change_24h > 0 else "red"
                st.markdown(f"<span style='color:{color}'>{change_24h:+.2f}%</span>", unsafe_allow_html=True)
            
            with col4:
                mcap = coin['market_cap']
                st.write(f"${mcap/1e9:.2f}B" if mcap > 1e9 else f"${mcap/1e6:.2f}M")
            
            with col5:
                volume = coin['total_volume']
                st.write(f"${volume/1e9:.2f}B" if volume > 1e9 else f"${volume/1e6:.2f}M")
            
            st.markdown("---")
    
    st.info("💡 **Tip**: Trump coin typically shows high volatility around political events. SHIB has been in triangular consolidation for over a year, potentially preparing for a breakout.")

# Call the main function
show()
