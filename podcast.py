import streamlit as st
from ai_crypto_expert import ai_expert
from crypto_data import fetcher
from database import Podcast, Subscription, get_session, init_db, is_database_available
import datetime
import json
from datetime import timedelta

def show():
    st.header("🎙️ The Alpha Signal")
    st.caption("Hosted by Marcus Sterling | Your Weekly Edge in Crypto Markets")
    
    # Host intro banner
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                padding: 1.5rem; 
                border-radius: 15px; 
                margin-bottom: 1.5rem;
                border-left: 5px solid #FFD700;">
        <h3 style="color: #FFD700; margin: 0; font-size: 1.3rem;">🎙️ Your Host: Marcus Sterling</h3>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0; font-size: 0.95rem;">
            Former Wall Street analyst turned crypto strategist. 15+ years building wealth through smart trades and calculated risks. 
            Marcus has helped thousands turn modest investments into life-changing portfolios. His secret? 
            <strong style="color: #FFD700;">Strategic patience, disciplined research, and knowing when to strike.</strong>
        </p>
        <p style="color: rgba(255,255,255,0.85); margin: 0.5rem 0 0 0; font-size: 0.9rem; font-style: italic;">
            "I don't chase hype. I chase <strong>alpha</strong>. Join me every Monday as I decode the market's signals and reveal where the real money is moving." - Marcus
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("📻 **New Episodes Every Monday** - Exclusive market intelligence, hidden opportunities, scam alerts, and insider strategies!")
    
    # Initialize database
    init_db()
    
    # Load podcasts from database
    if 'podcasts' not in st.session_state:
        st.session_state.podcasts = load_podcasts_from_db()
    
    # Get current week number
    current_week = datetime.datetime.now().isocalendar()[1]
    
    # Get or prompt for user email (simple user identification)
    if 'user_email' not in st.session_state:
        st.session_state['user_email'] = None
    
    # Show login/identify prompt if not identified
    if not st.session_state['user_email']:
        st.info("👤 **Enter your email to access The Alpha Signal**")
        user_email = st.text_input("Email Address", placeholder="your.email@example.com", key="user_email_input")
        
        if st.button("Continue", type="primary"):
            if user_email and '@' in user_email:
                st.session_state['user_email'] = user_email
                st.rerun()
            else:
                st.error("Please enter a valid email address")
        
        st.markdown("---")
        st.caption("💡 New user? Start your 3-day FREE trial after entering your email!")
        return  # Don't show podcast content until user is identified
    
    # Check subscription status for this specific user
    has_subscription = check_subscription_status(st.session_state['user_email'])
    
    # Show current user and logout option
    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption(f"👤 Logged in as: {st.session_state['user_email']}")
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state['user_email'] = None
            if 'user_subscription' in st.session_state:
                del st.session_state['user_subscription']
            st.rerun()
    
    st.markdown("---")
    
    # Subscription banner if not subscribed
    if not has_subscription:
        st.warning("""
        🔒 **Premium Content - Subscription Required**
        
        You're viewing a FREE PREVIEW. Subscribe to unlock:
        - Full episode access with all 9 segments
        - Downloadable transcripts  
        - Weekly AI market analysis
        - Exclusive buy/sell signals from Marcus Sterling
        
        **Try 3 days FREE**, then just $9.99/week or $99/year (save 81%!)
        """)
        
        if st.button("🚀 Subscribe Now - Start Free Trial", type="primary", use_container_width=True):
            st.switch_page("pages/podcast_subscription.py")
    else:
        # Show active subscription status
        sub_info = get_subscription_info()
        st.success(f"✅ **Active Subscription**: {sub_info}")
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Latest Episode", "Generate New Episode", "Episode Archive"])
    
    with tab1:
        if st.session_state.podcasts:
            latest = st.session_state.podcasts[0]
            display_podcast_episode(latest, has_subscription)
        else:
            st.info("📢 No episodes yet! Generate your first episode in the 'Generate New Episode' tab.")
            
            # Show sample episode structure
            with st.expander("🎧 What's in Each Episode?"):
                st.markdown("""
                ### Episode Structure (25-30 minutes)
                
                1. **🎬 Intro** (2-3 min) - Warm welcome and episode preview
                2. **📊 Market Overview** (3-4 min) - Current market conditions and sentiment  
                3. **🔥 Trending Analysis** (5-7 min) - Deep dive on trending coins - what's real vs hype
                4. **📈 Bullish Opportunities** (4-5 min) - Strong setups and entry strategies
                5. **📉 Sell Signals** (3-4 min) - When to take profits and warning signs
                6. **⚠️ Scam Alert** (2-3 min) - Red flags and FOMO tactics to avoid
                7. **🧠 Blockchain Education** (3-4 min) - Technology explained simply
                8. **👀 What to Watch** (2-3 min) - Upcoming catalysts and opportunities
                9. **🎯 Closing** (2-3 min) - Key takeaways and weekly strategy
                
                **Why This Podcast is Different:**
                - ✅ Honest analysis - we call out hype and scams
                - ✅ Educational - learn blockchain fundamentals
                - ✅ Actionable - specific buy/sell strategies with reasoning
                - ✅ Balanced - celebrates wins, acknowledges risks
                - ✅ Empowering - helps you make informed decisions
                """)
    
    with tab2:
        st.subheader("🎬 Generate This Week's Episode")
        
        st.info("💡 The AI will analyze current market conditions, trending coins, and create a comprehensive podcast script covering opportunities, risks, and education.")
        
        # Get market data for podcast
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Current Week")
            st.metric("Week Number", f"Week {current_week}", "2025")
            
        with col2:
            st.markdown("### Episode Focus")
            focus = st.selectbox(
                "Primary Theme",
                ["Market Analysis", "Scam Prevention", "Blockchain Education", "Trading Strategies", "Balanced Mix"]
            )
        
        if st.button("🎙️ Generate Episode", type="primary", use_container_width=True):
            with st.spinner("🤖 AI is researching trending coins and crafting this week's episode..."):
                try:
                    # Get trending coins data
                    top_coins = fetcher.get_trending_coins()
                    
                    if top_coins:
                        # Get market data
                        market_data = {
                            "total_market_cap": fetcher.get_global_data().get('data', {}).get('total_market_cap', {}).get('usd', 0),
                            "bitcoin_dominance": fetcher.get_global_data().get('data', {}).get('market_cap_percentage', {}).get('btc', 0),
                            "trending_coins": top_coins[:5],
                            "focus_theme": focus
                        }
                        
                        # Generate podcast
                        podcast = ai_expert.generate_weekly_podcast(
                            trending_coins=top_coins[:5],
                            market_data=market_data,
                            week_number=current_week
                        )
                        
                        # Add metadata
                        podcast['generated_at'] = datetime.datetime.now().isoformat()
                        podcast['week'] = current_week
                        podcast['year'] = 2025
                        
                        # Save to database
                        save_podcast_to_db(podcast)
                        
                        # Reload from database
                        st.session_state.podcasts = load_podcasts_from_db()
                        
                        st.success(f"✅ Episode Generated: {podcast['episode_title']}")
                        st.balloons()
                        
                        # Display the new episode
                        st.rerun()
                    
                    else:
                        st.warning("⚠️ Could not fetch trending coins. Using demo data...")
                        
                        # Demo trending coins
                        demo_coins = [
                            {"name": "Bitcoin", "symbol": "BTC", "price": 45000, "change_24h": 5.2},
                            {"name": "Ethereum", "symbol": "ETH", "price": 2500, "change_24h": 3.8},
                            {"name": "Solana", "symbol": "SOL", "price": 95, "change_24h": 8.1}
                        ]
                        
                        demo_market = {
                            "total_market_cap": 1800000000000,
                            "bitcoin_dominance": 52,
                            "focus_theme": focus
                        }
                        
                        podcast = ai_expert.generate_weekly_podcast(
                            trending_coins=demo_coins,
                            market_data=demo_market,
                            week_number=current_week
                        )
                        
                        podcast['generated_at'] = datetime.datetime.now().isoformat()
                        podcast['week'] = current_week
                        podcast['year'] = 2025
                        
                        # Save to database
                        save_podcast_to_db(podcast)
                        
                        # Reload from database
                        st.session_state.podcasts = load_podcasts_from_db()
                        
                        st.success(f"✅ Episode Generated: {podcast['episode_title']}")
                        st.balloons()
                        st.rerun()
                
                except Exception as e:
                    st.error(f"Error generating podcast: {str(e)}")
                    st.info("Please try again or contact support if the issue persists.")
    
    with tab3:
        st.subheader("📚 Episode Archive")
        
        if st.session_state.podcasts:
            st.markdown(f"**Total Episodes:** {len(st.session_state.podcasts)}")
            
            for idx, podcast in enumerate(st.session_state.podcasts):
                with st.expander(f"🎙️ {podcast['episode_title']} - {podcast.get('duration_estimate', 'N/A')}"):
                    display_podcast_episode(podcast, has_subscription)
        else:
            st.info("📭 No episodes in archive yet. Generate your first episode!")

def display_podcast_episode(podcast, has_subscription=False):
    """Display a podcast episode with full script and segments"""
    
    st.markdown(f"## {podcast['episode_title']}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Episode", f"#{podcast.get('episode_number', 'N/A')}")
    with col2:
        st.metric("Duration", podcast.get('duration_estimate', 'N/A'))
    with col3:
        st.metric("Week", f"Week {podcast.get('week', 'N/A')} - {podcast.get('year', 2025)}")
    
    st.markdown("---")
    
    # Intro - Always show (FREE PREVIEW)
    st.markdown("### 🎬 Introduction - FREE PREVIEW")
    st.markdown(f"**{podcast.get('intro_script', 'N/A')}**")
    
    st.markdown("---")
    
    # If no subscription, show paywall
    if not has_subscription:
        st.error("""
        🔒 **Subscribe to Unlock Full Episode**
        
        This is a FREE PREVIEW. The complete episode includes:
        - 📊 Market Overview & Sentiment Analysis
        - 🔥 Trending Coins Deep Dive
        - 📈 Bullish Opportunities with Entry Strategies
        - 📉 Sell Signals & Exit Strategies
        - ⚠️ Scam Alerts & FOMO Warnings
        - 🧠 Blockchain Education
        - 👀 What to Watch This Week
        - 🎯 Weekly Strategy from Marcus Sterling
        
        **Get instant access with a 3-day FREE TRIAL!**
        """)
        
        if st.button("🚀 Subscribe Now - Try 3 Days Free", key="subscribe_from_episode", type="primary", use_container_width=True):
            st.switch_page("pages/podcast_subscription.py")
        
        return  # Don't show the rest
    
    # PAID CONTENT BELOW - Only for subscribers
    
    # Timestamps navigation
    st.markdown("### ⏱️ Episode Timeline")
    timestamps = podcast.get('timestamps', {})
    if timestamps:
        cols = st.columns(5)
        for idx, (segment, time) in enumerate(list(timestamps.items())[:5]):
            with cols[idx % 5]:
                st.button(f"{time} - {segment.replace('_', ' ').title()}", use_container_width=True)
    
    st.markdown("---")
    
    # Market Overview
    st.markdown("### 📊 Market Overview")
    st.info(podcast.get('market_overview', 'N/A'))
    
    st.markdown("---")
    
    # Trending Analysis
    st.markdown("### 🔥 Trending Coins Analysis")
    
    for coin_analysis in podcast.get('trending_analysis', []):
        verdict = coin_analysis.get('verdict', 'Unknown')
        
        if verdict == "Real Opportunity":
            verdict_color = "success"
        elif verdict == "Proceed with Caution":
            verdict_color = "warning"
        else:
            verdict_color = "error"
        
        with st.container():
            st.markdown(f"#### {coin_analysis.get('coin', 'Unknown Coin')}")
            
            if verdict_color == "success":
                st.success(f"✅ **{verdict}**")
            elif verdict_color == "warning":
                st.warning(f"⚠️ **{verdict}**")
            else:
                st.error(f"🚫 **{verdict}**")
            
            st.markdown(coin_analysis.get('analysis', 'No analysis available'))
            st.markdown("---")
    
    # Bullish Opportunities
    st.markdown("### 📈 Bullish Opportunities")
    
    for opportunity in podcast.get('bullish_opportunities', []):
        with st.expander(f"💎 {opportunity.get('coin', 'Coin')} - {opportunity.get('risk_level', 'Unknown')} Risk"):
            st.markdown(f"**Why Bullish:** {opportunity.get('why_bullish', 'N/A')}")
            st.markdown(f"**Entry Strategy:** {opportunity.get('entry_strategy', 'N/A')}")
            st.markdown(f"**Target Gains:** {opportunity.get('target_gains', 'N/A')}")
    
    st.markdown("---")
    
    # Sell Signals
    st.markdown("### 📉 Sell Signals & Warnings")
    
    for sell_signal in podcast.get('sell_signals', []):
        with st.expander(f"⚠️ {sell_signal.get('coin', 'Coin')} - Time to Consider Exits"):
            st.markdown(f"**Why Sell:** {sell_signal.get('why_sell', 'N/A')}")
            st.markdown(f"**Exit Strategy:** {sell_signal.get('exit_strategy', 'N/A')}")
            
            if sell_signal.get('warning_signs'):
                st.markdown("**Warning Signs:**")
                for sign in sell_signal.get('warning_signs', []):
                    st.markdown(f"- {sign}")
    
    st.markdown("---")
    
    # Scam Alert
    st.markdown("### ⚠️ Scam Alert")
    st.error(podcast.get('scam_alert', 'No scam alerts this week'))
    
    st.markdown("---")
    
    # Blockchain Education
    st.markdown("### 🧠 Blockchain Education")
    st.info(podcast.get('blockchain_education', 'N/A'))
    
    st.markdown("---")
    
    # What to Watch
    st.markdown("### 👀 What to Watch This Week")
    
    for item in podcast.get('what_to_watch', []):
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    # Weekly Strategy
    st.markdown("### 🎯 Your Weekly Strategy")
    st.success(podcast.get('weekly_strategy', 'N/A'))
    
    # Key Takeaways
    st.markdown("### 💡 Key Takeaways")
    
    for takeaway in podcast.get('key_takeaways', []):
        st.markdown(f"✅ {takeaway}")
    
    st.markdown("---")
    
    # Closing
    st.markdown("### 🎬 Closing")
    st.markdown(f"**{podcast.get('closing_script', 'N/A')}**")
    
    # Disclaimer
    st.caption(podcast.get('disclaimer', 'This content is for educational purposes only.'))
    
    # Actions
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📥 Download Script", use_container_width=True):
            # Convert to downloadable text
            script_text = format_podcast_script(podcast)
            st.download_button(
                "💾 Download Full Script",
                data=script_text,
                file_name=f"podcast_week_{podcast.get('week', 'N')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    with col2:
        if st.button("📋 Copy Script", use_container_width=True):
            st.info("Script copied to clipboard! (Feature coming soon)")
    
    with col3:
        if st.button("🔗 Share Episode", use_container_width=True):
            st.info("Sharing feature coming soon!")

def format_podcast_script(podcast):
    """Format podcast as readable script"""
    
    script = f"""
CRYPTO REAL TALK PODCAST
{podcast['episode_title']}
Episode #{podcast.get('episode_number', 'N/A')} - Week {podcast.get('week', 'N/A')}, {podcast.get('year', 2025)}
Duration: {podcast.get('duration_estimate', 'N/A')}

==========================================

INTRO
{podcast.get('intro_script', 'N/A')}

MARKET OVERVIEW
{podcast.get('market_overview', 'N/A')}

TRENDING ANALYSIS
"""
    
    for coin in podcast.get('trending_analysis', []):
        script += f"\n{coin.get('coin', 'Coin')}: {coin.get('verdict', 'Unknown')}\n"
        script += f"{coin.get('analysis', 'N/A')}\n\n"
    
    script += "\nBULLISH OPPORTUNITIES\n"
    for opp in podcast.get('bullish_opportunities', []):
        script += f"\n{opp.get('coin', 'Coin')}\n"
        script += f"{opp.get('why_bullish', 'N/A')}\n"
        script += f"Entry: {opp.get('entry_strategy', 'N/A')}\n"
        script += f"Targets: {opp.get('target_gains', 'N/A')}\n\n"
    
    script += f"\nSCAM ALERT\n{podcast.get('scam_alert', 'N/A')}\n\n"
    script += f"BLOCKCHAIN EDUCATION\n{podcast.get('blockchain_education', 'N/A')}\n\n"
    script += f"WEEKLY STRATEGY\n{podcast.get('weekly_strategy', 'N/A')}\n\n"
    script += f"CLOSING\n{podcast.get('closing_script', 'N/A')}\n\n"
    script += f"DISCLAIMER\n{podcast.get('disclaimer', 'N/A')}\n"
    
    return script

def load_podcasts_from_db():
    """Load all podcasts from database"""
    podcasts = []
    
    if not is_database_available():
        return podcasts
    
    try:
        db = get_session()
        if db:
            db_podcasts = db.query(Podcast).filter(Podcast.published == True).order_by(Podcast.generated_at.desc()).all()
            
            for db_podcast in db_podcasts:
                try:
                    podcast_data = json.loads(db_podcast.podcast_data)
                    podcast_data['id'] = db_podcast.id
                    podcast_data['generated_at'] = db_podcast.generated_at.isoformat() if db_podcast.generated_at else None
                    podcasts.append(podcast_data)
                except json.JSONDecodeError:
                    continue
            
            db.close()
    except Exception as e:
        st.error(f"Error loading podcasts: {str(e)}")
    
    return podcasts

def save_podcast_to_db(podcast_data):
    """Save podcast to database and session state"""
    
    # Always save to session state first (fallback)
    if podcast_data not in st.session_state.podcasts:
        st.session_state.podcasts.insert(0, podcast_data)
    
    # Try to save to database if available
    if not is_database_available():
        st.info("📝 Podcast saved to session. Database will be configured for site-wide publishing.")
        return
    
    try:
        db = get_session()
        if db:
            # Create new podcast record
            new_podcast = Podcast(
                episode_number=podcast_data.get('episode_number', 0),
                week=podcast_data.get('week', 0),
                year=podcast_data.get('year', 2025),
                episode_title=podcast_data.get('episode_title', 'Untitled Episode'),
                duration_estimate=podcast_data.get('duration_estimate', 'N/A'),
                podcast_data=json.dumps(podcast_data),
                published=True
            )
            
            db.add(new_podcast)
            db.commit()
            db.close()
            
            st.success("💾 Podcast saved to database and published site-wide!")
    except Exception as e:
        st.warning(f"Database save failed. Podcast available in your session: {str(e)}")

def check_subscription_status(user_email):
    """Check if user has an active subscription"""
    
    if not user_email:
        return False
    
    # Check session state first
    if 'user_subscription' in st.session_state:
        sub = st.session_state['user_subscription']
        
        # Make sure it's for this user
        if sub.get('email') == user_email:
            # Check if trial is active
            if sub['status'] == 'trial' and sub.get('trial_end_date'):
                if datetime.datetime.now() < sub['trial_end_date']:
                    return True
            
            # Check if paid subscription is active
            if sub['status'] == 'active' and sub.get('subscription_end_date'):
                if datetime.datetime.now() < sub['subscription_end_date']:
                    return True
    
    # Check database if available
    if is_database_available():
        try:
            db = get_session()
            if db:
                # Look for active subscription for THIS specific user email
                subscription = db.query(Subscription).filter(
                    Subscription.email == user_email,
                    Subscription.status.in_(['trial', 'active'])
                ).first()
                
                if subscription:
                    now = datetime.datetime.now()
                    
                    # Check trial
                    if subscription.status == 'trial' and subscription.trial_end_date:
                        if now < subscription.trial_end_date:
                            # Cache in session
                            st.session_state['user_subscription'] = {
                                'email': user_email,
                                'subscription_type': subscription.subscription_type,
                                'status': 'trial',
                                'trial_end_date': subscription.trial_end_date,
                                'created_at': subscription.created_at
                            }
                            db.close()
                            return True
                    
                    # Check paid subscription
                    if subscription.status == 'active' and subscription.subscription_end_date:
                        if now < subscription.subscription_end_date:
                            # Cache in session
                            st.session_state['user_subscription'] = {
                                'email': user_email,
                                'subscription_type': subscription.subscription_type,
                                'status': 'active',
                                'subscription_end_date': subscription.subscription_end_date,
                                'created_at': subscription.created_at
                            }
                            db.close()
                            return True
                
                db.close()
        except Exception as e:
            pass
    
    return False

def get_subscription_info():
    """Get subscription information for display"""
    
    if 'user_subscription' in st.session_state:
        sub = st.session_state['user_subscription']
        
        if sub['status'] == 'trial':
            days_left = (sub['trial_end_date'] - datetime.datetime.now()).days
            return f"Free Trial ({days_left} days remaining)"
        elif sub['status'] == 'active':
            plan_type = sub['subscription_type'].title()
            if sub.get('subscription_end_date'):
                days_left = (sub['subscription_end_date'] - datetime.datetime.now()).days
                return f"{plan_type} Plan ({days_left} days remaining)"
            return f"{plan_type} Plan"
    
    return "No active subscription"

# Call the main function
show()
