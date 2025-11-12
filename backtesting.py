import streamlit as st
from wallet_manager import wallet_manager
from crypto_data import fetcher
import pandas as pd
from datetime import datetime, timedelta

def show():
    st.header("📈 AI Backtesting Dashboard")
    st.caption("Track AI prediction accuracy and historical performance")
    
    tab1, tab2, tab3 = st.tabs(["Signal Performance", "Hypothetical Returns", "Strategy Analysis"])
    
    with tab1:
        show_signal_performance()
    
    with tab2:
        show_hypothetical_returns()
    
    with tab3:
        show_strategy_analysis()

def show_signal_performance():
    st.subheader("🎯 Trading Signal Accuracy")
    
    signals = wallet_manager.get_trading_signals(limit=100)
    
    if not signals:
        st.info("No historical signals available. Start analyzing cryptocurrencies and saving signals!")
        return
    
    st.success(f"Analyzing {len(signals)} historical signals")
    
    signal_performance = []
    
    for signal in signals:
        if signal.created_at:
            try:
                crypto_data = fetcher.get_crypto_by_id(signal.crypto_id)
                if crypto_data:
                    market_data = crypto_data.get('market_data', {})
                    current_price = market_data.get('current_price', {}).get('usd', 0)
                    
                    if signal.current_price and current_price:
                        price_change = ((current_price - signal.current_price) / signal.current_price) * 100
                        
                        hours_elapsed = (datetime.now() - signal.created_at).total_seconds() / 3600
                        
                        was_correct = False
                        if signal.signal_type in ['BUY', 'STRONG BUY']:
                            was_correct = price_change > 0
                        elif signal.signal_type in ['SELL', 'STRONG SELL']:
                            was_correct = price_change < 0
                        else:
                            was_correct = abs(price_change) < 3
                        
                        signal_performance.append({
                            'crypto': signal.crypto_name,
                            'signal': signal.signal_type,
                            'confidence': signal.confidence,
                            'signal_price': signal.current_price,
                            'current_price': current_price,
                            'price_change': price_change,
                            'hours_elapsed': hours_elapsed,
                            'was_correct': was_correct,
                            'timestamp': signal.created_at
                        })
            except:
                pass
    
    if signal_performance:
        df = pd.DataFrame(signal_performance)
        
        accuracy = (df['was_correct'].sum() / len(df)) * 100
        avg_confidence = df['confidence'].mean()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Overall Accuracy", f"{accuracy:.1f}%")
        
        with col2:
            correct_signals = df['was_correct'].sum()
            st.metric("Correct Signals", f"{correct_signals}/{len(df)}")
        
        with col3:
            st.metric("Avg Confidence", f"{avg_confidence:.1f}%")
        
        with col4:
            avg_return = df['price_change'].mean()
            st.metric("Avg Price Move", f"{avg_return:+.2f}%")
        
        st.markdown("---")
        
        st.subheader("📊 Signal Breakdown")
        
        signal_type_accuracy = df.groupby('signal').agg({
            'was_correct': ['sum', 'count'],
            'price_change': 'mean',
            'confidence': 'mean'
        }).round(2)
        
        for signal_type in df['signal'].unique():
            signal_df = df[df['signal'] == signal_type]
            correct = signal_df['was_correct'].sum()
            total = len(signal_df)
            accuracy_pct = (correct / total * 100) if total > 0 else 0
            avg_move = signal_df['price_change'].mean()
            
            with st.expander(f"{signal_type} - {accuracy_pct:.1f}% accuracy ({correct}/{total})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Average Price Move:** {avg_move:+.2f}%")
                    st.write(f"**Avg Confidence:** {signal_df['confidence'].mean():.1f}%")
                
                with col2:
                    st.write(f"**Correct Predictions:** {correct}")
                    st.write(f"**Total Signals:** {total}")
        
        st.markdown("---")
        
        st.subheader("📋 Recent Signal History")
        
        recent_df = df.sort_values('timestamp', ascending=False).head(10)
        
        for _, row in recent_df.iterrows():
            status_icon = "✅" if row['was_correct'] else "❌"
            color = "green" if row['was_correct'] else "red"
            
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
            
            with col1:
                st.write(f"**{row['crypto']}**")
                st.caption(row['timestamp'].strftime("%Y-%m-%d %H:%M"))
            
            with col2:
                st.write(f"{row['signal']}")
                st.write(f"Confidence: {row['confidence']}%")
            
            with col3:
                st.markdown(f"<span style='color:{color}'>{row['price_change']:+.2f}%</span>", unsafe_allow_html=True)
                st.caption(f"{row['hours_elapsed']:.1f}h elapsed")
            
            with col4:
                st.markdown(f"<h3>{status_icon}</h3>", unsafe_allow_html=True)
            
            st.markdown("---")
    
    else:
        st.info("Not enough data to calculate performance metrics. Save more signals and check back later!")

def show_hypothetical_returns():
    st.subheader("💰 Hypothetical Returns Analysis")
    
    st.info("This shows what your returns would have been if you followed AI signals with real trades")
    
    signals = wallet_manager.get_trading_signals(limit=100)
    
    if not signals:
        st.warning("No signals available for backtesting")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        initial_capital = st.number_input("Initial Capital ($)", min_value=100.0, value=10000.0, step=100.0)
    
    with col2:
        position_size = st.slider("Position Size (%)", min_value=10, max_value=100, value=100)
    
    results = []
    current_capital = initial_capital
    
    for signal in signals:
        if signal.created_at:
            try:
                crypto_data = fetcher.get_crypto_by_id(signal.crypto_id)
                if crypto_data:
                    market_data = crypto_data.get('market_data', {})
                    current_price = market_data.get('current_price', {}).get('usd', 0)
                    
                    if signal.current_price and current_price:
                        price_change_pct = ((current_price - signal.current_price) / signal.current_price) * 100
                        
                        if signal.signal_type in ['BUY', 'STRONG BUY']:
                            position_value = current_capital * (position_size / 100)
                            pnl = position_value * (price_change_pct / 100)
                            current_capital += pnl
                            
                            results.append({
                                'crypto': signal.crypto_name,
                                'signal': signal.signal_type,
                                'entry_price': signal.current_price,
                                'current_price': current_price,
                                'price_change': price_change_pct,
                                'position_size': position_value,
                                'pnl': pnl,
                                'capital': current_capital,
                                'timestamp': signal.created_at
                            })
                        
                        elif signal.signal_type in ['SELL', 'STRONG SELL']:
                            position_value = current_capital * (position_size / 100)
                            pnl = position_value * (-price_change_pct / 100)
                            current_capital += pnl
                            
                            results.append({
                                'crypto': signal.crypto_name,
                                'signal': signal.signal_type,
                                'entry_price': signal.current_price,
                                'current_price': current_price,
                                'price_change': price_change_pct,
                                'position_size': position_value,
                                'pnl': pnl,
                                'capital': current_capital,
                                'timestamp': signal.created_at
                            })
            except:
                pass
    
    if results:
        total_return = ((current_capital - initial_capital) / initial_capital) * 100
        total_pnl = current_capital - initial_capital
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Initial Capital", f"${initial_capital:,.2f}")
        
        with col2:
            st.metric("Current Capital", f"${current_capital:,.2f}", delta=f"{total_return:+.2f}%")
        
        with col3:
            pnl_color = "normal" if total_pnl >= 0 else "inverse"
            st.metric("Total P&L", f"${total_pnl:+,.2f}", delta_color=pnl_color)
        
        st.markdown("---")
        
        st.subheader("📊 Trade History")
        
        df = pd.DataFrame(results)
        
        winning_trades = len(df[df['pnl'] > 0])
        losing_trades = len(df[df['pnl'] < 0])
        win_rate = (winning_trades / len(df) * 100) if len(df) > 0 else 0
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Trades", len(df))
        
        with col2:
            st.metric("Winning Trades", winning_trades)
        
        with col3:
            st.metric("Losing Trades", losing_trades)
        
        with col4:
            st.metric("Win Rate", f"{win_rate:.1f}%")
        
        st.markdown("---")
        
        for _, trade in df.sort_values('timestamp', ascending=False).head(10).iterrows():
            pnl_color = "green" if trade['pnl'] > 0 else "red"
            pnl_icon = "📈" if trade['pnl'] > 0 else "📉"
            
            col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
            
            with col1:
                st.write(f"**{trade['crypto']}**")
                st.caption(trade['timestamp'].strftime("%Y-%m-%d %H:%M"))
            
            with col2:
                st.write(f"{trade['signal']}")
                st.write(f"${trade['entry_price']:.6f}" if trade['entry_price'] < 1 else f"${trade['entry_price']:.2f}")
            
            with col3:
                st.markdown(f"<span style='color:{pnl_color}'>{trade['price_change']:+.2f}%</span>", unsafe_allow_html=True)
                st.caption(f"Position: ${trade['position_size']:,.2f}")
            
            with col4:
                st.markdown(f"<h4 style='color:{pnl_color}'>{pnl_icon} ${trade['pnl']:+,.2f}</h4>", unsafe_allow_html=True)
            
            st.markdown("---")
    
    else:
        st.warning("Not enough data for backtesting. Signals need time to develop before performance can be measured.")

def show_strategy_analysis():
    st.subheader("🧠 AI Strategy Performance")
    
    signals = wallet_manager.get_trading_signals(limit=100)
    
    if not signals:
        st.info("No data available for strategy analysis")
        return
    
    st.write(f"Analyzing {len(signals)} signals across different time periods")
    
    signal_data = []
    
    for signal in signals:
        if signal.created_at:
            try:
                crypto_data = fetcher.get_crypto_by_id(signal.crypto_id)
                if crypto_data:
                    market_data = crypto_data.get('market_data', {})
                    current_price = market_data.get('current_price', {}).get('usd', 0)
                    
                    if signal.current_price and current_price:
                        price_change = ((current_price - signal.current_price) / signal.current_price) * 100
                        hours_elapsed = (datetime.now() - signal.created_at).total_seconds() / 3600
                        
                        signal_data.append({
                            'signal_type': signal.signal_type,
                            'confidence': signal.confidence,
                            'price_change': price_change,
                            'hours_elapsed': hours_elapsed,
                            'crypto': signal.crypto_name
                        })
            except:
                pass
    
    if signal_data:
        df = pd.DataFrame(signal_data)
        
        st.subheader("📊 Confidence vs Performance")
        
        high_conf = df[df['confidence'] >= 80]
        med_conf = df[(df['confidence'] >= 60) & (df['confidence'] < 80)]
        low_conf = df[df['confidence'] < 60]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### High Confidence (≥80%)")
            if len(high_conf) > 0:
                avg_return = high_conf['price_change'].mean()
                st.metric("Average Return", f"{avg_return:+.2f}%")
                st.metric("Signals", len(high_conf))
            else:
                st.info("No high confidence signals")
        
        with col2:
            st.markdown("### Medium Confidence (60-79%)")
            if len(med_conf) > 0:
                avg_return = med_conf['price_change'].mean()
                st.metric("Average Return", f"{avg_return:+.2f}%")
                st.metric("Signals", len(med_conf))
            else:
                st.info("No medium confidence signals")
        
        with col3:
            st.markdown("### Low Confidence (<60%)")
            if len(low_conf) > 0:
                avg_return = low_conf['price_change'].mean()
                st.metric("Average Return", f"{avg_return:+.2f}%")
                st.metric("Signals", len(low_conf))
            else:
                st.info("No low confidence signals")
        
        st.markdown("---")
        
        st.subheader("🎯 Best Performing Signals")
        
        signal_type_performance = df.groupby('signal_type').agg({
            'price_change': ['mean', 'std', 'count']
        }).round(2)
        
        for signal_type in df['signal_type'].unique():
            type_df = df[df['signal_type'] == signal_type]
            avg_return = type_df['price_change'].mean()
            count = len(type_df)
            
            color = "green" if avg_return > 0 else "red" if avg_return < 0 else "gray"
            
            st.markdown(f"**{signal_type}**: <span style='color:{color}'>{avg_return:+.2f}% average</span> ({count} signals)", unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.subheader("💡 Strategy Insights")
        
        insights = []
        
        if len(high_conf) > 0 and high_conf['price_change'].mean() > 0:
            insights.append("✅ High-confidence signals are showing positive returns on average")
        
        if len(df[df['signal_type'].isin(['BUY', 'STRONG BUY'])]) > 0:
            buy_signals = df[df['signal_type'].isin(['BUY', 'STRONG BUY'])]
            if buy_signals['price_change'].mean() > 0:
                insights.append(f"✅ Buy signals are performing well with {buy_signals['price_change'].mean():+.2f}% average return")
        
        best_signal = df.groupby('signal_type')['price_change'].mean().idxmax()
        best_return = df.groupby('signal_type')['price_change'].mean().max()
        insights.append(f"🏆 Best performing signal type: {best_signal} ({best_return:+.2f}%)")
        
        total_signals = len(df)
        insights.append(f"📊 Total signals tracked: {total_signals}")
        
        for insight in insights:
            st.info(insight)
    
    else:
        st.warning("Not enough data for strategy analysis. Continue using the platform and saving signals!")

# Call the main function
show()
