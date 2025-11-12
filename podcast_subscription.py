import streamlit as st
from database import Subscription, DisclaimerAcceptance, get_session, init_db, is_database_available
import datetime
from datetime import timedelta

def show():
    st.header("🎙️ The Alpha Signal - Premium Access")
    st.caption("Subscribe to Unlock Exclusive Market Intelligence from Marcus Sterling")
    
    # Initialize database
    init_db()
    
    # Pricing cards
    st.markdown("---")
    st.subheader("💎 Choose Your Plan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; 
                    border-radius: 15px; 
                    text-align: center;
                    height: 400px;">
            <h3 style="color: white; margin: 0;">🎁 Free Trial</h3>
            <h1 style="color: #FFD700; margin: 1rem 0;">$0</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 1rem;">3 Days Free</p>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <ul style="color: rgba(255,255,255,0.9); text-align: left; line-height: 1.8;">
                <li>✅ Full podcast access</li>
                <li>✅ Market intelligence reports</li>
                <li>✅ Scam alerts & buy signals</li>
                <li>✅ No credit card required</li>
                <li>⚠️ Cancel anytime before trial ends</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start Free Trial", key="trial_btn", use_container_width=True):
            st.session_state['subscription_flow'] = 'trial'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 2rem; 
                    border-radius: 15px; 
                    text-align: center;
                    height: 400px;
                    border: 3px solid #FFD700;">
            <h3 style="color: white; margin: 0;">⭐ Weekly</h3>
            <h1 style="color: #FFD700; margin: 1rem 0;">$9.99</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 1rem;">Per Week</p>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <ul style="color: rgba(255,255,255,0.9); text-align: left; line-height: 1.8;">
                <li>✅ Everything in Free Trial</li>
                <li>✅ Weekly AI analysis</li>
                <li>✅ Priority support</li>
                <li>✅ Downloadable transcripts</li>
                <li>✅ Cancel anytime</li>
            </ul>
            <p style="color: #FFD700; font-weight: bold; margin-top: 1rem;">MOST POPULAR</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💳 Subscribe Weekly", key="weekly_btn", use_container_width=True):
            st.session_state['subscription_flow'] = 'weekly'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 2rem; 
                    border-radius: 15px; 
                    text-align: center;
                    height: 400px;">
            <h3 style="color: white; margin: 0;">👑 Annual</h3>
            <h1 style="color: #FFD700; margin: 1rem 0;">$99</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 1rem;">Per Year</p>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <ul style="color: rgba(255,255,255,0.9); text-align: left; line-height: 1.8;">
                <li>✅ Everything in Weekly</li>
                <li>✅ <strong>Save 81% annually</strong></li>
                <li>✅ Lifetime archive access</li>
                <li>✅ Exclusive bonus content</li>
                <li>✅ VIP support</li>
            </ul>
            <p style="color: #FFD700; font-weight: bold; margin-top: 1rem;">BEST VALUE</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💎 Subscribe Annually", key="annual_btn", use_container_width=True):
            st.session_state['subscription_flow'] = 'annual'
            st.rerun()
    
    st.markdown("---")
    
    # Subscription flow
    if 'subscription_flow' in st.session_state and st.session_state['subscription_flow']:
        show_subscription_form(st.session_state['subscription_flow'])
    
    # Success stories section
    st.markdown("---")
    st.subheader("🏆 Success Stories from Marcus Sterling's Followers")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: rgba(255, 215, 0, 0.1); 
                    padding: 1.5rem; 
                    border-radius: 10px; 
                    border-left: 4px solid #FFD700;
                    margin-bottom: 1rem;">
            <h4 style="color: #FFD700; margin: 0;">Sarah T. - Turned $5K into $47K</h4>
            <p style="margin: 0.5rem 0; font-style: italic;">
                "I was skeptical about crypto until I started following Marcus. His calm, strategic approach 
                helped me avoid the meme coin traps and focus on projects with real potential. In 8 months, 
                my portfolio grew 840%. Marcus doesn't just give signals—he teaches you WHY."
            </p>
            <p style="color: #888; font-size: 0.85rem; margin: 0;">- Verified subscriber since Jan 2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255, 215, 0, 0.1); 
                    padding: 1.5rem; 
                    border-radius: 10px; 
                    border-left: 4px solid #FFD700;
                    margin-bottom: 1rem;">
            <h4 style="color: #FFD700; margin: 0;">James M. - Quit His Day Job</h4>
            <p style="margin: 0.5rem 0; font-style: italic;">
                "Marcus warned me about three major rug pulls that would've wiped me out. His scam alerts 
                alone saved me $23K. But the real value? His weekly episodes taught me how to think like 
                a professional trader. I'm now trading full-time and couldn't be happier."
            </p>
            <p style="color: #888; font-size: 0.85rem; margin: 0;">- Verified subscriber since Mar 2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Payment info
    st.markdown("---")
    st.info("💳 **Secure Payment Processing** - All payments are processed securely and deposited directly to the platform owner's verified account. Your financial information is encrypted and never stored on our servers.")

def show_subscription_form(plan_type):
    st.markdown("---")
    st.subheader(f"📝 Complete Your {plan_type.title()} Subscription")
    
    # Step 1: Disclaimer
    with st.expander("⚠️ STEP 1: Read and Accept Disclaimer (Required)", expanded=True):
        st.markdown("""
        ### IMPORTANT DISCLAIMER - PLEASE READ CAREFULLY
        
        By subscribing to The Alpha Signal podcast and associated services, you acknowledge and agree to the following:
        
        **1. Not Financial Advice**
        - The content provided is for educational and informational purposes only
        - This is NOT personalized financial, investment, trading, or legal advice
        - You should consult with licensed financial professionals before making investment decisions
        
        **2. Risk Acknowledgment**
        - Cryptocurrency trading involves substantial risk of loss
        - You may lose some or all of your invested capital
        - Past performance does not guarantee future results
        - Markets are volatile and unpredictable
        
        **3. No Guarantees**
        - We make no guarantees or promises about potential returns or profits
        - Success stories shared are individual results and not typical
        - You are solely responsible for your investment decisions
        
        **4. Do Your Own Research (DYOR)**
        - You must conduct your own research before making any trades
        - Verify all information independently
        - Never invest more than you can afford to lose
        
        **5. Payment Terms**
        - Subscription fees are non-refundable after the trial period
        - All payments are deposited to the platform owner's account
        - You may cancel your subscription at any time
        - Free trial automatically converts to paid subscription unless canceled
        
        **6. Content Ownership**
        - All podcast content, analysis, and materials are proprietary
        - You may not redistribute, copy, or share subscriber-only content
        - Content is for personal use only
        
        By signing below, you confirm that you have read, understood, and agree to these terms.
        """)
        
        st.markdown("---")
        
        full_name = st.text_input("Full Legal Name *", placeholder="Enter your full name as signature")
        email = st.text_input("Email Address *", placeholder="your.email@example.com")
        signature = st.text_input("Type Your Full Name to Sign *", placeholder="Type your name again to confirm")
        
        accept_terms = st.checkbox("✅ I have read and accept all terms in the disclaimer above", value=False)
        
        if full_name and email and signature and accept_terms:
            if full_name.strip().lower() == signature.strip().lower():
                st.success("✅ Disclaimer accepted and signed!")
                
                if 'disclaimer_signed' not in st.session_state:
                    st.session_state['disclaimer_signed'] = {
                        'full_name': full_name,
                        'email': email,
                        'signature': signature,
                        'signed_at': datetime.datetime.now()
                    }
            else:
                st.error("❌ Signature must match your full name exactly")
                return
        else:
            st.warning("⚠️ Please complete all fields and accept the terms to continue")
            return
    
    # Step 2: Payment Information
    if 'disclaimer_signed' in st.session_state:
        with st.expander("💳 STEP 2: Payment Information", expanded=True):
            st.markdown(f"""
            ### {plan_type.title()} Plan Summary
            - **Plan**: {plan_type.title()}
            - **Price**: {'$0 for 3 days, then $9.99/week' if plan_type == 'trial' else '$9.99/week' if plan_type == 'weekly' else '$99/year'}
            - **Billing**: {'After 3-day trial' if plan_type == 'trial' else 'Weekly' if plan_type == 'weekly' else 'Annually'}
            """)
            
            st.markdown("---")
            st.info("🔒 **Note**: This is a demonstration system. In production, you would integrate with Stripe, PayPal, or another payment processor. Payments will be routed to the account you configure in your payment processor dashboard.")
            
            # Demo payment form
            st.text_input("Card Number", placeholder="4242 4242 4242 4242", type="password")
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Expiry Date", placeholder="MM/YY")
            with col2:
                st.text_input("CVV", placeholder="123", type="password")
            
            st.text_input("Cardholder Name", value=st.session_state['disclaimer_signed']['full_name'])
            
            st.markdown("---")
            
            # Payment routing info
            st.markdown("""
            **💰 Payment Deposit Information**
            
            All subscription payments are securely processed and deposited to:
            - **Account Holder**: [Platform Owner Name]
            - **Payment Processor**: [Your configured processor - Stripe/PayPal/etc]
            - **Routing**: Direct deposit to owner's verified business account
            
            You will receive a receipt via email after each successful payment.
            """)
            
            if st.button("🔒 Complete Subscription", type="primary", use_container_width=True):
                # Save subscription
                if save_subscription(
                    email=st.session_state['disclaimer_signed']['email'],
                    full_name=st.session_state['disclaimer_signed']['full_name'],
                    signature=st.session_state['disclaimer_signed']['signature'],
                    plan_type=plan_type
                ):
                    st.balloons()
                    st.success(f"""
                    ✅ **Subscription Activated!**
                    
                    Welcome to The Alpha Signal, {st.session_state['disclaimer_signed']['full_name']}!
                    
                    - Your {plan_type} subscription is now active
                    - Check your email for confirmation and access details
                    - {'Your 3-day free trial starts now!' if plan_type == 'trial' else 'You now have full access to all episodes!'}
                    
                    Marcus Sterling and the team look forward to helping you build wealth strategically!
                    """)
                    
                    # Clear session
                    del st.session_state['subscription_flow']
                    del st.session_state['disclaimer_signed']
                    
                    st.info("Click on 'The Alpha Signal' in the sidebar to start listening!")

def save_subscription(email, full_name, signature, plan_type):
    """Save subscription to database"""
    
    # Calculate dates
    now = datetime.datetime.now()
    
    if plan_type == 'trial':
        trial_start = now
        trial_end = now + timedelta(days=3)
        sub_start = None
        sub_end = None
        status = "trial"
    elif plan_type == 'weekly':
        trial_start = None
        trial_end = None
        sub_start = now
        sub_end = now + timedelta(days=7)
        status = "active"
    else:  # annual
        trial_start = None
        trial_end = None
        sub_start = now
        sub_end = now + timedelta(days=365)
        status = "active"
    
    # Save to session state
    if 'user_subscription' not in st.session_state:
        st.session_state['user_subscription'] = {
            'email': email,
            'subscription_type': plan_type,
            'status': status,
            'trial_end_date': trial_end,
            'subscription_end_date': sub_end,
            'created_at': now
        }
    
    # Try to save to database
    if not is_database_available():
        st.warning("⚠️ Database not available. Subscription saved to session only.")
        return True
    
    try:
        db = get_session()
        if not db:
            st.warning("⚠️ Could not get database session. Subscription saved to session only.")
            return True
        
        # Save disclaimer
        disclaimer = DisclaimerAcceptance(
            email=email,
            full_name=full_name,
            signature=signature,
            disclaimer_text="Podcast Subscription Disclaimer - Full terms accepted",
            accepted_at=now
        )
        db.add(disclaimer)
        
        # Save subscription
        subscription = Subscription(
            email=email,
            subscription_type=plan_type,
            status=status,
            trial_start_date=trial_start,
            trial_end_date=trial_end,
            subscription_start_date=sub_start,
            subscription_end_date=sub_end,
            disclaimer_accepted=True,
            disclaimer_accepted_at=now
        )
        db.add(subscription)
        
        # Commit the transaction
        db.commit()
        
        # Verify it was saved by querying it back
        saved_sub = db.query(Subscription).filter(Subscription.email == email).first()
        
        db.close()
        
        if saved_sub:
            st.success(f"✅ Subscription saved to database! Email: {email}, Status: {status}")
            return True
        else:
            st.error("❌ Database commit succeeded but record not found! Please contact support.")
            return False
            
    except Exception as e:
        if 'db' in locals() and db:
            try:
                db.rollback()
                db.close()
            except:
                pass
        st.error(f"❌ Database error: {str(e)}")
        st.info("💾 Subscription saved to session. You can use the app, but your subscription may not persist.")
        return True
    
    return False

# Call the main function
show()
