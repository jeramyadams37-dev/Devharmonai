import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.title("🔄 How It Works")
st.markdown("### Understanding the OnTime Family App ↔ Crypto Platform Ecosystem")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["🌟 Overview", "💰 Earning ILAH", "🔒 Privacy & Security", "📊 Revenue Flow"])

with tab1:
    st.markdown("## 🌟 The Complete Ecosystem")
    
    st.markdown("""
    Our platform connects two powerful applications to create a sustainable, family-friendly cryptocurrency ecosystem:
    
    ### 📱 OnTime Family Planning App
    A mobile application (iOS & Android) that helps families:
    - Schedule activities and manage calendars
    - Coordinate tasks among family members
    - Track completed goals and milestones
    - Share quality time together
    
    ### 💎 AI Crypto Empire Builder (This Platform)
    A comprehensive cryptocurrency platform offering:
    - Real-time market analysis and trading
    - AI-powered predictions and insights
    - Portfolio management tools
    - ILAH token ecosystem management
    """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🏠 Step 1: Use OnTime")
        st.info("""
        **Families download OnTime and:**
        - Complete daily tasks
        - Share family moments
        - Use scheduling features
        - Build healthy habits
        
        **Result:** Generate valuable anonymized activity data
        """)
    
    with col2:
        st.markdown("### 💵 Step 2: Data Monetization")
        st.success("""
        **Platform sells anonymized data to:**
        - Academic researchers
        - Family behavior scientists
        - Public health organizations
        - App developers
        
        **Result:** Revenue of ~$23,500/month
        """)
    
    with col3:
        st.markdown("### 🪙 Step 3: Earn ILAH")
        st.warning("""
        **Revenue is distributed as:**
        - **60%** → ILAH tokens for families
        - **30%** → Platform operations
        - **10%** → AI improvements
        
        **Result:** Families earn passive income!
        """)

with tab2:
    st.markdown("## 💰 How to Earn ILAH Tokens")
    
    st.markdown("### 🎯 Earning Methods")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Data Contribution Rewards")
        st.markdown("""
        **Automatic Earnings:**
        - ✅ **Daily Active Use**: 5 ILAH/day
        - ✅ **Weekly Engagement**: 50 ILAH/week bonus
        - ✅ **Monthly Consistency**: 250 ILAH/month bonus
        - ✅ **Data Quality Score**: Up to 100 ILAH/month
        
        **Total Potential:** ~500-700 ILAH/month per family
        """)
        
        st.markdown("#### 🎁 Milestone Rewards")
        st.markdown("""
        - First week active: **100 ILAH**
        - First month active: **500 ILAH**
        - 100 tasks completed: **250 ILAH**
        - Refer a family: **200 ILAH each**
        """)
    
    with col2:
        st.markdown("#### 📈 Current ILAH Value")
        
        try:
            fig = go.Figure()
            
            fig.add_trace(go.Indicator(
                mode = "number+delta",
                value = 0.42,
                number = {'prefix': "$", 'font': {'size': 60}},
                delta = {'position': "bottom", 'reference': 0.38, 'increasing': {'color': "green"}},
                title = {'text': "ILAH Token Price<br><span style='font-size:0.6em;color:gray'>Last 24h</span>"},
                domain = {'x': [0, 1], 'y': [0, 1]}
            ))
            
            fig.update_layout(height=250, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("""
            **💵 Monthly Earning Potential:**
            - 600 ILAH/month × $0.42 = **$252/month**
            - Plus staking rewards: ~8% APY
            - Family income: **$300-400/month** 🎉
            """)
        except Exception as e:
            st.warning("Unable to load current ILAH price")
    
    st.markdown("---")
    
    st.markdown("### 🔄 How to Claim Your ILAH")
    
    st.markdown("""
    #### Step-by-Step Claiming Process:
    
    1. **📱 Open OnTime App**
       - Navigate to "Wallet" tab
       - View your accumulated ILAH balance
    
    2. **🔗 Connect to Crypto Platform**
       - Tap "Claim ILAH" button
       - Enter your Solana wallet address
       - Or scan QR code from this platform
    
    3. **✅ Verify & Transfer**
       - OnTime sends claim request to this platform
       - Platform verifies your activity data
       - ILAH tokens transferred to your wallet within 24 hours
    
    4. **💎 Manage Your ILAH**
       - Stake for 8% APY rewards
       - Use in OnTime premium features
       - Hold for long-term value appreciation
    """)
    
    st.success("""
    **🎁 First-Time Setup Bonus:**
    Connect your wallet and claim for the first time to receive **100 ILAH bonus!**
    """)

with tab3:
    st.markdown("## 🔒 Privacy & Security")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛡️ Your Data is Protected")
        st.markdown("""
        We take privacy seriously with multiple layers of protection:
        
        #### 🔐 Anonymization Process
        - **Zero Personal Information**: No names, addresses, or contacts
        - **Device ID Hashing**: Your device is assigned a random ID
        - **Data Aggregation**: Combined with 1,000+ other families
        - **Differential Privacy**: Mathematical noise prevents re-identification
        
        #### 🌐 Federated Learning
        - AI trains on your device, not our servers
        - Only aggregated insights leave your phone
        - Raw data never uploaded to cloud
        - You retain full control
        
        #### 📜 Compliance
        - ✅ GDPR compliant (EU privacy law)
        - ✅ CCPA compliant (California privacy law)
        - ✅ COPPA compliant (children's privacy)
        - ✅ SOC 2 Type II certified
        """)
    
    with col2:
        st.markdown("### 🎛️ Your Control Panel")
        st.markdown("""
        #### You Decide What to Share
        
        **Data Categories (Opt-in/Opt-out):**
        - ⚙️ Activity patterns (times of day)
        - ⚙️ Task completion rates
        - ⚙️ Calendar usage frequency
        - ⚙️ Feature engagement metrics
        
        **Always Excluded (Never Shared):**
        - ❌ Personal names or identities
        - ❌ Location data or addresses
        - ❌ Contact lists or phone numbers
        - ❌ Calendar event details
        - ❌ Private messages or notes
        
        **Your Rights:**
        - 📊 View all data collected about you
        - 🗑️ Delete your data anytime
        - ⏸️ Pause data collection
        - 📧 Export your data
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 What Data is Actually Sold?")
    
    st.code("""
Example Anonymized Data Point:
{
    "device_id": "hash_a7f2k9x4p1",
    "activity_type": "task_completed",
    "timestamp": "2025-10-29T14:30:00Z",
    "day_of_week": "Tuesday",
    "engagement_score": 0.85,
    "cohort": "family_3_5_members"
}
    """, language="json")
    
    st.info("""
    **Notice:** No personal information! Just patterns that help researchers understand family behavior trends.
    """)

with tab4:
    st.markdown("## 📊 Revenue Flow & Distribution")
    
    st.markdown("### 💵 How Money Flows Through the Ecosystem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📥 Revenue Sources")
        
        try:
            revenue_data = {
                'Source': ['Data Sales', 'Exchange Fees', 'Premium Subscriptions'],
                'Monthly': [23500, 75000, 8600],
                'Color': ['#9b59b6', '#3498db', '#2ecc71']
            }
            
            fig = go.Figure(data=[go.Pie(
                labels=revenue_data['Source'],
                values=revenue_data['Monthly'],
                hole=0.4,
                marker_colors=revenue_data['Color'],
                textinfo='label+percent+value',
                texttemplate='%{label}<br>$%{value:,.0f}<br>%{percent}'
            )])
            
            fig.update_layout(
                title="Monthly Revenue: $109,100",
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning("Unable to load revenue chart")
    
    with col2:
        st.markdown("#### 📤 Revenue Distribution")
        
        try:
            fig = go.Figure()
            
            categories = ['Families (ILAH)', 'Operations', 'AI Development', 'Profit/Reinvest']
            values = [14100, 7050, 2350, 44740]
            colors = ['#e74c3c', '#f39c12', '#9b59b6', '#27ae60']
            
            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                marker_color=colors,
                text=['$' + f'{v:,.0f}' for v in values],
                textposition='outside'
            ))
            
            fig.update_layout(
                title="Where Does $109K Go Each Month?",
                yaxis_title="Amount ($)",
                height=400,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning("Unable to load distribution chart")
    
    st.markdown("---")
    
    st.markdown("### 🔢 Detailed Breakdown")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="💰 Data Sales Revenue",
            value="$23,500/mo",
            delta="Growing"
        )
        st.markdown("""
        **Distribution:**
        - 60% → $14,100 in ILAH to families
        - 30% → $7,050 for operations
        - 10% → $2,350 for AI
        """)
    
    with col2:
        st.metric(
            label="👥 Active OnTime Families",
            value="2,847",
            delta="+12% this month"
        )
        st.markdown("""
        **Earnings per Family:**
        - Average: $5/month
        - Top 10%: $15-20/month
        - Potential: Up to $30/month
        """)
    
    with col3:
        st.metric(
            label="🪙 ILAH Distributed Monthly",
            value="33,571 ILAH",
            delta="+8% this month"
        )
        st.markdown("""
        **Token Economics:**
        - Current price: $0.42/ILAH
        - Daily mining: 100 ILAH max
        - Staking APY: 8%
        """)
    
    st.markdown("---")
    
    st.success("""
    ### ✨ Why This Model Works
    
    **Traditional App:** Sells your data → Keeps 100% profit → You get nothing
    
    **Our Model:** Sells anonymized data → Shares 60% with families → Everyone wins!
    
    🎯 **Result:** Sustainable platform that rewards families for their participation while respecting privacy.
    """)

st.markdown("---")

st.markdown("## 🚀 Ready to Get Started?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📱 Step 1: Download OnTime")
    st.markdown("""
    Get the OnTime Family Planning App:
    - [📱 Download for iOS](https://apps.apple.com/app/ontime-family)
    - [🤖 Download for Android](https://play.google.com/store/apps/details?id=com.ontime.family)
    """)

with col2:
    st.markdown("### 👨‍👩‍👧‍👦 Step 2: Use Daily")
    st.markdown("""
    Start earning by:
    - Adding family members
    - Creating tasks & events
    - Completing daily goals
    - Building consistency
    """)

with col3:
    st.markdown("### 💎 Step 3: Claim ILAH")
    st.markdown("""
    Connect your wallet:
    - Link Solana address
    - Claim accumulated tokens
    - Start staking for rewards
    - Watch your earnings grow!
    """)

st.info("""
**💡 Pro Tip:** The more consistently you use OnTime, the more ILAH you earn. Families using the app 
daily can earn 600+ ILAH per month (~$250 value) plus 8% staking rewards!
""")

st.markdown("---")

st.markdown(f"""
<div style='text-align: center; color: #888; padding: 20px;'>
    <p>Last updated: {datetime.now().strftime('%B %d, %Y')}</p>
    <p>Questions? Contact support@ontimefamily.app</p>
</div>
""", unsafe_allow_html=True)

# Call the main function
show()
