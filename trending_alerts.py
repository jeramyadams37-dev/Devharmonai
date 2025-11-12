import streamlit as st
from crypto_data import fetcher
import pandas as pd

def show():
    st.header("🔥 Trending Coins & Alerts")
    st.caption("Detect trending cryptocurrencies and set up alerts for pre-pump opportunities")
    
    tab1, tab2, tab3 = st.tabs(["Trending Now", "Volume Alerts", "Price Alerts"])
    
    with tab1:
        show_trending()
    
    with tab2:
        show_volume_alerts()
    
    with tab3:
        show_price_alerts()

def show_trending():
    st.subheader("🔥 Trending Cryptocurrencies")
    
    with st.spinner("Loading trending coins..."):
        trending_data = fetcher.get_trending_coins()
    
    if trending_data and 'coins' in trending_data:
        trending_coins = trending_data['coins']
        
        st.success(f"Found {len(trending_coins)} trending coins based on search volume and social engagement")
        
        for idx, coin_data in enumerate(trending_coins[:15], 1):
            coin = coin_data.get('item', {})
            
            col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
            
            with col1:
                st.write(f"**#{idx}**")
            
            with col2:
                name = coin.get('name', 'Unknown')
                symbol = coin.get('symbol', '')
                st.write(f"**{name}** ({symbol})")
            
            with col3:
                market_cap_rank = coin.get('market_cap_rank', 'N/A')
                st.write(f"Rank: #{market_cap_rank}")
            
            with col4:
                price_btc = coin.get('price_btc', 0)
                st.write(f"{price_btc:.8f} BTC")
            
            st.markdown("---")
    
    else:
        st.error("Failed to load trending coins")
    
    st.markdown("---")
    
    st.subheader("📊 What Makes a Coin Trending?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Search Volume Indicators:**
        - Sudden spike in Google searches
        - Increased CoinGecko page views
        - Rising Twitter mentions
        - Reddit discussion volume
        """)
    
    with col2:
        st.markdown("""
        **Trading Signals:**
        - Volume spike >1.5x average
        - Price movement >15% in 24h
        - New exchange listings
        - Whale accumulation patterns
        """)

def show_volume_alerts():
    st.subheader("📊 Volume Anomaly Detection")
    
    st.info("🔍 Detecting unusual volume patterns that often precede 10-15% price movements within 72 hours")
    
    with st.spinner("Analyzing volume patterns..."):
        top_cryptos = fetcher.get_top_cryptos(limit=100)
    
    if not top_cryptos:
        st.error("Failed to load market data")
        return
    
    volume_alerts = []
    
    for crypto in top_cryptos:
        total_volume = crypto.get('total_volume', 0)
        market_cap = crypto.get('market_cap', 1)
        
        volume_to_mcap = (total_volume / market_cap * 100) if market_cap > 0 else 0
        
        if volume_to_mcap > 15:
            volume_alerts.append({
                'name': crypto['name'],
                'symbol': crypto['symbol'].upper(),
                'volume': total_volume,
                'market_cap': market_cap,
                'volume_ratio': volume_to_mcap,
                'price_change': crypto.get('price_change_percentage_24h', 0)
            })
    
    volume_alerts.sort(key=lambda x: x['volume_ratio'], reverse=True)
    
    st.subheader(f"⚡ High Volume Alerts ({len(volume_alerts)} detected)")
    
    for alert in volume_alerts[:10]:
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
            
            with col1:
                st.write(f"**{alert['name']}** ({alert['symbol']})")
            
            with col2:
                st.write(f"Volume: ${alert['volume']/1e9:.2f}B")
            
            with col3:
                ratio_color = "red" if alert['volume_ratio'] > 30 else "orange"
                st.markdown(f"<span style='color:{ratio_color}'>**{alert['volume_ratio']:.1f}%** of MCap</span>", unsafe_allow_html=True)
            
            with col4:
                price_color = "green" if alert['price_change'] > 0 else "red"
                st.markdown(f"<span style='color:{price_color}'>{alert['price_change']:+.2f}%</span>", unsafe_allow_html=True)
            
            st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("📈 Volume Analysis Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Volume/Market Cap Ratios:**
        - **>30%**: Extremely high volume - potential breakout or manipulation
        - **15-30%**: High volume - strong trading interest
        - **5-15%**: Normal healthy volume
        - **<5%**: Low volume - potential low liquidity
        """)
    
    with col2:
        st.markdown("""
        **What to Watch:**
        - Volume spike + price increase = bullish momentum
        - Volume spike + price decrease = selling pressure
        - Volume spike + flat price = accumulation or distribution
        - Sustained high volume = institutional interest
        """)

def show_price_alerts():
    st.subheader("🎯 Price Movement Alerts")
    
    with st.spinner("Detecting significant price movements..."):
        top_cryptos = fetcher.get_top_cryptos(limit=100)
    
    if not top_cryptos:
        st.error("Failed to load market data")
        return
    
    st.subheader("🚀 Top Gainers (24h)")
    
    gainers = [c for c in top_cryptos if c.get('price_change_percentage_24h', 0) > 0]
    gainers.sort(key=lambda x: x.get('price_change_percentage_24h', 0), reverse=True)
    
    for gainer in gainers[:10]:
        col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
        
        with col1:
            st.write(f"**{gainer['name']}** ({gainer['symbol'].upper()})")
        
        with col2:
            price = gainer['current_price']
            st.write(f"${price:,.6f}" if price < 1 else f"${price:,.2f}")
        
        with col3:
            change = gainer.get('price_change_percentage_24h', 0)
            st.markdown(f"<span style='color:green'>+{change:.2f}%</span>", unsafe_allow_html=True)
        
        with col4:
            mcap = gainer['market_cap']
            st.write(f"${mcap/1e9:.2f}B" if mcap > 1e9 else f"${mcap/1e6:.2f}M")
        
        st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("📉 Top Losers (24h)")
    
    losers = [c for c in top_cryptos if c.get('price_change_percentage_24h', 0) < 0]
    losers.sort(key=lambda x: x.get('price_change_percentage_24h', 0))
    
    for loser in losers[:10]:
        col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
        
        with col1:
            st.write(f"**{loser['name']}** ({loser['symbol'].upper()})")
        
        with col2:
            price = loser['current_price']
            st.write(f"${price:,.6f}" if price < 1 else f"${price:,.2f}")
        
        with col3:
            change = loser.get('price_change_percentage_24h', 0)
            st.markdown(f"<span style='color:red'>{change:.2f}%</span>", unsafe_allow_html=True)
        
        with col4:
            mcap = loser['market_cap']
            st.write(f"${mcap/1e9:.2f}B" if mcap > 1e9 else f"${mcap/1e6:.2f}M")
        
        st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("🔔 Custom Price Alerts (Coming Soon)")
    
    st.info("Set custom price alerts to get notified when cryptocurrencies reach your target prices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Cryptocurrency", placeholder="Bitcoin")
        st.number_input("Alert Price ($)", min_value=0.0, value=100000.0)
    
    with col2:
        st.selectbox("Alert Type", ["Price Above", "Price Below"])
        st.button("Set Alert", disabled=True, help="Feature coming soon")
    
    st.caption("💡 **Tip**: Price alerts will be delivered via browser notifications and can be configured for multiple timeframes (1h, 4h, 24h movements)")

# Call the main function
show()
