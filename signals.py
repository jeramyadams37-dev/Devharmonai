import streamlit as st
from wallet_manager import wallet_manager
import pandas as pd
import json
from datetime import datetime

def show():
    st.header("📊 Trading Signals")
    st.caption("View, manage, and export your AI-generated trading signals")
    
    tab1, tab2 = st.tabs(["Saved Signals", "Export Signals"])
    
    with tab1:
        show_saved_signals()
    
    with tab2:
        show_export_signals()

def show_saved_signals():
    st.subheader("💾 Your Saved Trading Signals")
    
    signals = wallet_manager.get_trading_signals(limit=100)
    
    if not signals:
        st.info("👋 No trading signals saved yet. Analyze cryptocurrencies in the AI Analysis page and save the signals!")
        return
    
    st.success(f"Found {len(signals)} saved signals")
    
    filter_option = st.selectbox("Filter by signal type", ["All Signals", "STRONG BUY", "BUY", "HOLD", "SELL", "STRONG SELL"])
    
    filtered_signals = signals if filter_option == "All Signals" else [s for s in signals if s.signal_type == filter_option]
    
    st.write(f"Showing {len(filtered_signals)} signals")
    
    for signal in filtered_signals:
        signal_colors = {
            'STRONG BUY': '#00ff00',
            'BUY': '#90EE90',
            'HOLD': '#FFA500',
            'SELL': '#FF6347',
            'STRONG SELL': '#ff0000'
        }
        
        signal_color = signal_colors.get(signal.signal_type, '#FFA500')
        
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            
            with col1:
                st.markdown(f"<h4>{signal.crypto_name}</h4>", unsafe_allow_html=True)
                created_time = signal.created_at.strftime("%Y-%m-%d %H:%M") if signal.created_at else "Unknown"
                st.caption(f"📅 {created_time}")
            
            with col2:
                st.markdown(f"<h3 style='color:{signal_color}'>{signal.signal_type}</h3>", unsafe_allow_html=True)
                st.write(f"Confidence: {signal.confidence}%")
            
            with col3:
                st.write(f"**Price:** ${signal.current_price:,.2f}" if signal.current_price > 1 else f"**Price:** ${signal.current_price:.6f}")
                if signal.target_price:
                    st.write(f"🎯 ${signal.target_price:,.2f}")
            
            with col4:
                if signal.stop_loss:
                    st.write(f"🛑 SL: ${signal.stop_loss:,.2f}")
                
                st.caption(f"Exported: {'✅' if signal.exported else '❌'}")
            
            if signal.reasoning:
                with st.expander("💡 Reasoning"):
                    st.write(signal.reasoning)
            
            st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("📈 Signal Statistics")
    
    signal_counts = {}
    for signal in signals:
        signal_type = signal.signal_type
        signal_counts[signal_type] = signal_counts.get(signal_type, 0) + 1
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Strong Buy", signal_counts.get('STRONG BUY', 0))
    with col2:
        st.metric("Buy", signal_counts.get('BUY', 0))
    with col3:
        st.metric("Hold", signal_counts.get('HOLD', 0))
    with col4:
        st.metric("Sell", signal_counts.get('SELL', 0))
    with col5:
        st.metric("Strong Sell", signal_counts.get('STRONG SELL', 0))

def show_export_signals():
    st.subheader("📤 Export Trading Signals")
    
    signals = wallet_manager.get_trading_signals(limit=100)
    
    if not signals:
        st.info("No signals to export. Save some AI trading signals first!")
        return
    
    st.success(f"Ready to export {len(signals)} signals")
    
    export_format = st.radio("Export Format", ["CSV", "JSON"], horizontal=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        include_reasoning = st.checkbox("Include AI Reasoning", value=True)
    
    with col2:
        only_new = st.checkbox("Only export new (not previously exported)", value=False)
    
    signals_to_export = signals
    if only_new:
        signals_to_export = [s for s in signals if not s.exported]
        st.write(f"Found {len(signals_to_export)} new signals to export")
    
    if not signals_to_export:
        st.warning("No new signals to export. All signals have been exported already.")
        return
    
    if export_format == "CSV":
        data = []
        for signal in signals_to_export:
            row = {
                'Timestamp': signal.created_at.strftime("%Y-%m-%d %H:%M:%S") if signal.created_at else "",
                'Cryptocurrency': signal.crypto_name,
                'Signal': signal.signal_type,
                'Confidence': signal.confidence,
                'Price': signal.current_price,
                'Target': signal.target_price if signal.target_price else "",
                'Stop_Loss': signal.stop_loss if signal.stop_loss else "",
            }
            
            if include_reasoning:
                row['Reasoning'] = signal.reasoning if signal.reasoning else ""
            
            data.append(row)
        
        df = pd.DataFrame(data)
        csv = df.to_csv(index=False)
        
        st.subheader("Preview")
        st.dataframe(df, use_container_width=True)
        
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"trading_signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            type="primary",
            use_container_width=True
        )
    
    else:
        data = []
        for signal in signals_to_export:
            signal_dict = {
                'timestamp': signal.created_at.isoformat() if signal.created_at else None,
                'cryptocurrency': {
                    'id': signal.crypto_id,
                    'name': signal.crypto_name
                },
                'signal': {
                    'type': signal.signal_type,
                    'confidence': signal.confidence
                },
                'prices': {
                    'current': signal.current_price,
                    'target': signal.target_price,
                    'stop_loss': signal.stop_loss
                }
            }
            
            if include_reasoning:
                signal_dict['reasoning'] = signal.reasoning
            
            data.append(signal_dict)
        
        json_str = json.dumps(data, indent=2)
        
        st.subheader("Preview")
        st.code(json_str[:500] + "..." if len(json_str) > 500 else json_str, language="json")
        
        st.download_button(
            label="📥 Download JSON",
            data=json_str,
            file_name=f"trading_signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            type="primary",
            use_container_width=True
        )
    
    st.markdown("---")
    
    st.subheader("🔗 Integration Guide")
    
    with st.expander("How to use exported signals"):
        st.markdown("""
        ### Automated Trading Integration
        
        **CSV Format:**
        - Import into Excel/Google Sheets for manual review
        - Use with trading bots that accept CSV input
        - Analyze historical signal performance
        
        **JSON Format:**
        - Perfect for API integrations
        - Compatible with automated trading systems
        - Easy to parse programmatically
        
        ### Example Usage (Python):
        ```python
        import json
        import pandas as pd
        
        # Load JSON signals
        with open('trading_signals.json', 'r') as f:
            signals = json.load(f)
        
        # Process signals
        for signal in signals:
            if signal['signal']['type'] == 'BUY' and signal['signal']['confidence'] > 80:
                crypto = signal['cryptocurrency']['name']
                price = signal['prices']['current']
                print(f"High-confidence BUY signal for {crypto} at ${price}")
        
        # Or use CSV with pandas
        df = pd.read_csv('trading_signals.csv')
        buy_signals = df[df['Signal'] == 'BUY']
        ```
        
        ### Popular Trading Bot Platforms:
        - **3Commas**: Supports CSV signal imports
        - **Cryptohopper**: API integration with JSON
        - **Bitsgap**: Manual signal execution
        - **TradeSanta**: Custom strategy bots
        
        ⚠️ **Disclaimer**: Always review signals before executing trades. Past performance does not guarantee future results.
        """)

# Call the main function
show()
