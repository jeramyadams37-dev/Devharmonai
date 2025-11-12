import streamlit as st
import datetime
from database import (
    AutoTradingSettings, NotificationPreferences, AutoTradeHistory,
    SessionLocal, engine, Base
)

st.set_page_config(page_title="AI Wallet Manager", page_icon="🤖", layout="wide")

def is_database_available():
    return engine is not None and SessionLocal is not None

def get_session():
    if is_database_available():
        try:
            return SessionLocal()
        except:
            return None
    return None

def initialize_database():
    if engine:
        try:
            Base.metadata.create_all(bind=engine)
            return True
        except Exception as e:
            st.error(f"Database initialization error: {str(e)}")
            return False
    return False

def get_or_create_settings(email):
    """Get or create auto-trading settings for user"""
    if not is_database_available():
        return None
    
    try:
        db = get_session()
        if db:
            settings = db.query(AutoTradingSettings).filter(
                AutoTradingSettings.email == email
            ).first()
            
            if not settings:
                settings = AutoTradingSettings(
                    email=email,
                    auto_trading_enabled=False,
                    risk_level="conservative",
                    max_trade_amount=100.0,
                    stop_loss_percentage=10.0,
                    take_profit_percentage=20.0,
                    diversification_limit=5,
                    waiver_accepted=False,
                    education_completed=False
                )
                db.add(settings)
                db.commit()
                db.refresh(settings)
            
            result = {
                'auto_trading_enabled': settings.auto_trading_enabled,
                'risk_level': settings.risk_level,
                'max_trade_amount': settings.max_trade_amount,
                'stop_loss_percentage': settings.stop_loss_percentage,
                'take_profit_percentage': settings.take_profit_percentage,
                'diversification_limit': settings.diversification_limit,
                'waiver_accepted': settings.waiver_accepted,
                'education_completed': settings.education_completed,
                'waiver_accepted_at': settings.waiver_accepted_at,
                'education_completed_at': settings.education_completed_at
            }
            db.close()
            return result
    except Exception as e:
        st.error(f"Error loading settings: {str(e)}")
    
    return None

def save_settings(email, settings_data):
    """Save auto-trading settings to database"""
    if not is_database_available():
        return False
    
    try:
        db = get_session()
        if db:
            settings = db.query(AutoTradingSettings).filter(
                AutoTradingSettings.email == email
            ).first()
            
            if settings:
                for key, value in settings_data.items():
                    setattr(settings, key, value)
                settings.updated_at = datetime.datetime.utcnow()
                db.commit()
                db.close()
                return True
            
            db.close()
    except Exception as e:
        st.error(f"Error saving settings: {str(e)}")
    
    return False

def get_or_create_notifications(email):
    """Get or create notification preferences for user"""
    if not is_database_available():
        return None
    
    try:
        db = get_session()
        if db:
            prefs = db.query(NotificationPreferences).filter(
                NotificationPreferences.email == email
            ).first()
            
            if not prefs:
                prefs = NotificationPreferences(
                    email=email,
                    email_notifications=True,
                    sms_notifications=False,
                    trade_alerts=True,
                    auto_trade_confirmations=True,
                    price_alerts=True,
                    weekly_summary=True
                )
                db.add(prefs)
                db.commit()
                db.refresh(prefs)
            
            result = {
                'phone_number': prefs.phone_number,
                'email_notifications': prefs.email_notifications,
                'sms_notifications': prefs.sms_notifications,
                'trade_alerts': prefs.trade_alerts,
                'auto_trade_confirmations': prefs.auto_trade_confirmations,
                'price_alerts': prefs.price_alerts,
                'weekly_summary': prefs.weekly_summary
            }
            db.close()
            return result
    except Exception as e:
        st.error(f"Error loading notification preferences: {str(e)}")
    
    return None

def save_notifications(email, prefs_data):
    """Save notification preferences to database"""
    if not is_database_available():
        return False
    
    try:
        db = get_session()
        if db:
            prefs = db.query(NotificationPreferences).filter(
                NotificationPreferences.email == email
            ).first()
            
            if prefs:
                for key, value in prefs_data.items():
                    setattr(prefs, key, value)
                prefs.updated_at = datetime.datetime.utcnow()
                db.commit()
                db.close()
                return True
            
            db.close()
    except Exception as e:
        st.error(f"Error saving notification preferences: {str(e)}")
    
    return False

def get_auto_trade_history(email, limit=50):
    """Get auto-trade history for user"""
    if not is_database_available():
        return []
    
    try:
        db = get_session()
        if db:
            trades = db.query(AutoTradeHistory).filter(
                AutoTradeHistory.email == email
            ).order_by(AutoTradeHistory.executed_at.desc()).limit(limit).all()
            
            result = [{
                'crypto_name': t.crypto_name,
                'crypto_symbol': t.crypto_symbol,
                'trade_type': t.trade_type,
                'amount': t.amount,
                'price': t.price,
                'total_value': t.total_value,
                'ai_reasoning': t.ai_reasoning,
                'confidence_score': t.confidence_score,
                'executed_at': t.executed_at,
                'notification_sent': t.notification_sent
            } for t in trades]
            
            db.close()
            return result
    except Exception as e:
        st.error(f"Error loading trade history: {str(e)}")
    
    return []

def show_education_module():
    """Display educational content before enabling auto-trading"""
    st.markdown("""
    ## 📚 Auto-Trading Education Module
    
    Before enabling auto-trading, it's crucial you understand how it works and the risks involved.
    
    ### What is Auto-Trading?
    Auto-trading allows our AI to automatically execute buy and sell orders on your behalf based on:
    - Real-time market analysis
    - Technical indicators (RSI, MACD, Bollinger Bands)
    - AI-powered predictions
    - Your configured risk parameters
    
    ### How It Works:
    1. **AI Analysis**: Our AI continuously monitors the market 24/7
    2. **Signal Generation**: When conditions meet your criteria, a trade signal is generated
    3. **Automatic Execution**: The trade is executed automatically within your limits
    4. **Notification**: You receive immediate notification of the trade
    
    ### Risk Parameters You Control:
    - **Max Trade Amount**: Maximum $ per single trade
    - **Stop Loss**: Automatic sell if price drops X%
    - **Take Profit**: Automatic sell if price rises X%
    - **Diversification**: Maximum number of different coins
    
    ### Important Risks to Understand:
    
    ⚠️ **Market Volatility**: Crypto markets are highly volatile. Prices can change dramatically.
    
    ⚠️ **AI Limitations**: While our AI is sophisticated, it cannot predict every market movement.
    
    ⚠️ **Automatic Execution**: Trades happen automatically - you may not be able to stop them.
    
    ⚠️ **Loss Potential**: You can lose some or all of your investment.
    
    ⚠️ **No Guarantees**: Past performance does not guarantee future results.
    
    ### Best Practices:
    ✅ Start with small amounts until you're comfortable
    ✅ Set conservative stop-loss limits
    ✅ Diversify across multiple coins
    ✅ Regularly review your auto-trade history
    ✅ Never invest more than you can afford to lose
    
    ### Emergency Controls:
    - You can disable auto-trading at any time
    - All trades are logged and visible in your history
    - Notifications keep you informed of all activity
    
    ---
    
    ⚡ **Ready to proceed?** Make sure you understand these concepts before enabling auto-trading.
    """)

def show_waiver_form(email):
    """Display waiver acceptance form"""
    st.markdown("""
    ## ⚖️ Auto-Trading Legal Waiver
    
    **IMPORTANT LEGAL AGREEMENT - READ CAREFULLY**
    
    By enabling auto-trading, you acknowledge and agree to the following:
    
    ### 1. Risk Acknowledgment
    I understand that cryptocurrency trading involves substantial risk of loss. I may lose some or all of my invested capital.
    
    ### 2. No Guarantees
    I understand that the AI trading system provides no guarantees of profit. Past performance does not indicate future results.
    
    ### 3. Automatic Execution
    I authorize the AI system to execute trades automatically on my behalf within my configured parameters.
    
    ### 4. Personal Responsibility
    I take full responsibility for all trades executed by the AI system. I will not hold the platform liable for losses.
    
    ### 5. Not Financial Advice
    I understand the AI system provides automated trading, not personalized financial advice. I should consult a financial advisor.
    
    ### 6. Technical Risks
    I understand there are technical risks including system failures, connectivity issues, and software bugs.
    
    ### 7. Market Risks
    I understand crypto markets are unregulated and subject to extreme volatility, manipulation, and liquidity issues.
    
    ### 8. Right to Disable
    I understand I can disable auto-trading at any time, but trades in progress may complete.
    
    ### 9. Age and Capacity
    I confirm I am 18+ years old and legally capable of entering into this agreement.
    
    ### 10. No Refunds
    I understand that losses from auto-trading are not refundable and are my sole responsibility.
    
    ---
    
    **BY SIGNING BELOW, I ACKNOWLEDGE I HAVE READ, UNDERSTOOD, AND AGREE TO ALL TERMS ABOVE.**
    """)
    
    st.markdown("### Your Agreement:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input("Full Legal Name", key="waiver_name")
    
    with col2:
        signature = st.text_input("Type Your Full Name Again to Sign", key="waiver_signature")
    
    st.checkbox("I have read and understand all the terms above", key="waiver_checkbox")
    
    if st.button("✍️ Accept Waiver & Enable Auto-Trading", type="primary", use_container_width=True):
        if not full_name or not signature:
            st.error("Please enter your full name in both fields")
        elif full_name != signature:
            st.error("Signatures do not match. Please type your full name exactly the same in both fields.")
        elif not st.session_state.get('waiver_checkbox'):
            st.error("Please confirm you have read and understood the terms")
        else:
            settings_data = {
                'waiver_accepted': True,
                'waiver_accepted_at': datetime.datetime.utcnow()
            }
            
            if save_settings(email, settings_data):
                st.success("✅ Waiver accepted! You can now enable auto-trading.")
                st.balloons()
                st.rerun()
            else:
                st.error("Error saving waiver acceptance. Please try again.")

def main():
    initialize_database()
    
    st.title("🤖 AI Wallet Manager")
    st.markdown("**Automated Trading Powered by Artificial Intelligence**")
    
    if 'user_email' not in st.session_state:
        st.session_state['user_email'] = None
    
    if not st.session_state['user_email']:
        st.info("👤 **Enter your email to access AI Wallet Manager**")
        user_email = st.text_input("Email Address", placeholder="your.email@example.com", key="wallet_email_input")
        
        if st.button("Continue", type="primary"):
            if user_email and '@' in user_email:
                st.session_state['user_email'] = user_email
                st.rerun()
            else:
                st.error("Please enter a valid email address")
        
        return
    
    email = st.session_state['user_email']
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption(f"👤 Logged in as: {email}")
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state['user_email'] = None
            st.rerun()
    
    st.markdown("---")
    
    settings = get_or_create_settings(email)
    
    if not settings:
        st.error("Unable to load settings. Database may be unavailable.")
        return
    
    tabs = st.tabs(["🎯 Auto-Trading", "📚 Education", "⚖️ Legal Waiver", "🔔 Notifications", "📊 Trade History"])
    
    with tabs[0]:
        st.markdown("### Auto-Trading Configuration")
        
        if not settings['education_completed']:
            st.warning("⚠️ **Education Required**: Please complete the Education module before enabling auto-trading.")
        
        if not settings['waiver_accepted']:
            st.warning("⚠️ **Legal Waiver Required**: Please accept the legal waiver before enabling auto-trading.")
        
        can_enable = settings['education_completed'] and settings['waiver_accepted']
        
        auto_enabled = st.toggle(
            "🤖 Enable Auto-Trading",
            value=settings['auto_trading_enabled'],
            disabled=not can_enable,
            help="AI will automatically execute trades based on your settings" if can_enable else "Complete education and accept waiver first"
        )
        
        if auto_enabled != settings['auto_trading_enabled']:
            if save_settings(email, {'auto_trading_enabled': auto_enabled}):
                if auto_enabled:
                    st.success("✅ Auto-trading enabled! AI is now monitoring markets.")
                else:
                    st.info("Auto-trading disabled.")
                st.rerun()
        
        st.markdown("---")
        st.markdown("### Risk Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            risk_level = st.select_slider(
                "Risk Level",
                options=["Conservative", "Moderate", "Aggressive"],
                value=settings['risk_level'].capitalize()
            )
            
            max_trade = st.number_input(
                "Max Trade Amount ($)",
                min_value=10.0,
                max_value=10000.0,
                value=settings['max_trade_amount'],
                step=10.0,
                help="Maximum dollar amount per single trade"
            )
            
            stop_loss = st.slider(
                "Stop Loss (%)",
                min_value=5.0,
                max_value=50.0,
                value=settings['stop_loss_percentage'],
                step=1.0,
                help="Automatically sell if price drops this much"
            )
        
        with col2:
            take_profit = st.slider(
                "Take Profit (%)",
                min_value=10.0,
                max_value=100.0,
                value=settings['take_profit_percentage'],
                step=5.0,
                help="Automatically sell if price rises this much"
            )
            
            diversification = st.slider(
                "Diversification Limit",
                min_value=1,
                max_value=20,
                value=settings['diversification_limit'],
                step=1,
                help="Maximum number of different coins to trade"
            )
        
        if st.button("💾 Save Settings", type="primary", use_container_width=True):
            new_settings = {
                'risk_level': risk_level.lower(),
                'max_trade_amount': max_trade,
                'stop_loss_percentage': stop_loss,
                'take_profit_percentage': take_profit,
                'diversification_limit': diversification
            }
            
            if save_settings(email, new_settings):
                st.success("Settings saved successfully!")
                st.rerun()
            else:
                st.error("Error saving settings")
        
        if settings['auto_trading_enabled']:
            st.markdown("---")
            st.success(f"""
            ✅ **Auto-Trading Active**
            - Risk Level: {settings['risk_level'].capitalize()}
            - Max Trade: ${settings['max_trade_amount']}
            - Stop Loss: {settings['stop_loss_percentage']}%
            - Take Profit: {settings['take_profit_percentage']}%
            - Max Coins: {settings['diversification_limit']}
            """)
    
    with tabs[1]:
        show_education_module()
        
        if not settings['education_completed']:
            st.markdown("---")
            if st.button("✅ I Understand - Mark Education Complete", type="primary", use_container_width=True):
                education_data = {
                    'education_completed': True,
                    'education_completed_at': datetime.datetime.utcnow()
                }
                
                if save_settings(email, education_data):
                    st.success("✅ Education completed! You can now proceed to the Legal Waiver.")
                    st.balloons()
                    st.rerun()
        else:
            st.success(f"✅ Education completed on {settings['education_completed_at'].strftime('%Y-%m-%d')}")
    
    with tabs[2]:
        if not settings['waiver_accepted']:
            show_waiver_form(email)
        else:
            st.success(f"✅ Legal waiver accepted on {settings['waiver_accepted_at'].strftime('%Y-%m-%d %H:%M:%S')}")
            st.info("You have authorized the AI to execute trades on your behalf within your configured parameters.")
    
    with tabs[3]:
        st.markdown("### Notification Preferences")
        
        prefs = get_or_create_notifications(email)
        
        if prefs:
            st.markdown("#### Notification Channels")
            
            col1, col2 = st.columns(2)
            
            with col1:
                email_notifs = st.toggle(
                    "📧 Email Notifications",
                    value=prefs['email_notifications'],
                    help=f"Send notifications to {email}"
                )
            
            with col2:
                phone = st.text_input(
                    "📱 Phone Number (Optional)",
                    value=prefs['phone_number'] or "",
                    placeholder="+1234567890",
                    help="For SMS notifications"
                )
                
                sms_notifs = st.toggle(
                    "💬 SMS Notifications",
                    value=prefs['sms_notifications'],
                    disabled=not phone,
                    help="Requires phone number"
                )
            
            st.markdown("---")
            st.markdown("#### Notification Types")
            
            col1, col2 = st.columns(2)
            
            with col1:
                trade_alerts = st.checkbox(
                    "📊 Trade Alerts",
                    value=prefs['trade_alerts'],
                    help="Get notified of manual trades"
                )
                
                auto_trade_alerts = st.checkbox(
                    "🤖 Auto-Trade Confirmations",
                    value=prefs['auto_trade_confirmations'],
                    help="Get notified when AI executes a trade"
                )
            
            with col2:
                price_alerts = st.checkbox(
                    "💰 Price Alerts",
                    value=prefs['price_alerts'],
                    help="Get notified of significant price changes"
                )
                
                weekly_summary = st.checkbox(
                    "📈 Weekly Summary",
                    value=prefs['weekly_summary'],
                    help="Receive weekly performance report"
                )
            
            if st.button("💾 Save Notification Preferences", type="primary", use_container_width=True):
                new_prefs = {
                    'phone_number': phone if phone else None,
                    'email_notifications': email_notifs,
                    'sms_notifications': sms_notifs if phone else False,
                    'trade_alerts': trade_alerts,
                    'auto_trade_confirmations': auto_trade_alerts,
                    'price_alerts': price_alerts,
                    'weekly_summary': weekly_summary
                }
                
                if save_notifications(email, new_prefs):
                    st.success("Notification preferences saved!")
                    st.rerun()
                else:
                    st.error("Error saving preferences")
    
    with tabs[4]:
        st.markdown("### Auto-Trade History")
        
        trades = get_auto_trade_history(email)
        
        if trades:
            for trade in trades:
                trade_color = "green" if trade['trade_type'] == 'buy' else "red"
                trade_icon = "📈" if trade['trade_type'] == 'buy' else "📉"
                
                with st.expander(f"{trade_icon} {trade['trade_type'].upper()} {trade['crypto_symbol']} - ${trade['total_value']:.2f} ({trade['executed_at'].strftime('%Y-%m-%d %H:%M')})"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Cryptocurrency:** {trade['crypto_name']}")
                        st.markdown(f"**Amount:** {trade['amount']:.8f} {trade['crypto_symbol']}")
                        st.markdown(f"**Price:** ${trade['price']:.2f}")
                        st.markdown(f"**Total Value:** ${trade['total_value']:.2f}")
                    
                    with col2:
                        st.markdown(f"**Type:** {trade['trade_type'].upper()}")
                        st.markdown(f"**Confidence:** {trade['confidence_score']}%")
                        st.markdown(f"**Executed:** {trade['executed_at'].strftime('%Y-%m-%d %H:%M:%S')}")
                        st.markdown(f"**Notification:** {'✅ Sent' if trade['notification_sent'] else '❌ Not sent'}")
                    
                    if trade['ai_reasoning']:
                        st.markdown("**AI Reasoning:**")
                        st.info(trade['ai_reasoning'])
        else:
            st.info("No auto-trades executed yet. Enable auto-trading to let AI start managing your portfolio!")

if __name__ == "__main__":
    main()
