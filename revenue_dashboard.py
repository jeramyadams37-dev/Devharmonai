import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

def show():
    st.header("💰 Revenue Dashboard")
    st.caption("Platform Monetization & Self-Sustainability Metrics")
    
    st.success("🎯 **Mission**: Generate enough revenue to cover all operational costs and provide FREE features to all users")
    
    st.markdown("---")
    
    st.subheader("📊 Real-Time Revenue Streams")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Today's Revenue", "$3,847", "+$512")
        st.caption("💱 Exchange fees, subscriptions")
    
    with col2:
        st.metric("Monthly Revenue", "$87,240", "+15.3%")
        st.caption("📈 On track for $90K target")
    
    with col3:
        st.metric("Operating Costs", "$42,500/mo", "Fully covered")
        st.caption("✅ 205% cost coverage")
    
    with col4:
        st.metric("Profit Margin", "48.7%", "+3.2%")
        st.caption("💰 Reinvested in features")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["💱 Exchange Fees", "💎 Premium Plans", "📊 Data Sales", "📈 Analytics", "⚙️ Cost Breakdown"])
    
    with tab1:
        st.subheader("💱 Crypto Exchange Revenue")
        
        st.info("**Fee Structure**: 0.25% per trade (industry-leading low fee)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Today's Exchange Performance")
            st.metric("Total Volume", "$1,260,000", "+$180K")
            st.metric("Trades Executed", "2,847", "+412")
            st.metric("Fees Collected", "$3,150", "+$450")
            st.metric("Average Trade Size", "$442.67", "-5.2%")
        
        with col2:
            st.markdown("### Popular Trading Pairs")
            
            pairs_data = [
                {"Pair": "BTC/USD", "Volume": "$487K", "Trades": 542, "Fees": "$1,217.50"},
                {"Pair": "ETH/USD", "Volume": "$325K", "Trades": 687, "Fees": "$812.50"},
                {"Pair": "SOL/USD", "Volume": "$198K", "Trades": 498, "Fees": "$495.00"},
                {"Pair": "DOGE/USD", "Volume": "$142K", "Trades": 621, "Fees": "$355.00"},
                {"Pair": "SHIB/USD", "Volume": "$108K", "Trades": 499, "Fees": "$270.00"},
            ]
            
            pairs_df = pd.DataFrame(pairs_data)
            st.dataframe(pairs_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("### 📈 7-Day Exchange Revenue Trend")
        
        dates = [(datetime.now() - timedelta(days=i)).strftime("%m/%d") for i in range(6, -1, -1)]
        revenue_data = {
            "Date": dates,
            "Revenue": [2100 + random.randint(-300, 800) for _ in range(7)]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=revenue_data["Date"],
            y=revenue_data["Revenue"],
            mode='lines+markers',
            name='Daily Revenue',
            line=dict(color='#FFD700', width=3),
            fill='tozeroy',
            fillcolor='rgba(255, 215, 0, 0.2)'
        ))
        
        fig.update_layout(
            title="Exchange Fee Revenue (Last 7 Days)",
            xaxis_title="Date",
            yaxis_title="Revenue ($)",
            hovermode='x unified',
            template='plotly_dark'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("💎 Premium Subscription Plans")
        
        st.markdown("""
        ### Subscription Tiers
        
        We offer tiered plans to monetize advanced features while keeping core functionality FREE:
        """)
        
        plan_col1, plan_col2, plan_col3 = st.columns(3)
        
        with plan_col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 1.5rem; border-radius: 10px; text-align: center;">
                <h3 style="color: white; margin: 0;">🆓 Basic</h3>
                <h2 style="color: white; margin: 1rem 0;">FREE</h2>
                <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem;">
                    ✅ Market tracking<br>
                    ✅ Basic AI analysis<br>
                    ✅ Portfolio tracking<br>
                    ✅ Crypto exchange access<br>
                    ⚡ 5 AI predictions/day
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Active Users", "12,847", "+1,205")
            st.caption("💰 Revenue: $0 (Free tier)")
        
        with plan_col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                        padding: 1.5rem; border-radius: 10px; text-align: center;">
                <h3 style="color: white; margin: 0;">⭐ Pro</h3>
                <h2 style="color: white; margin: 1rem 0;">$9.99/mo</h2>
                <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem;">
                    ✅ Everything in Basic<br>
                    ✅ Unlimited AI predictions<br>
                    ✅ Advanced indicators<br>
                    ✅ Priority support<br>
                    ⚡ Custom alerts
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Active Subscribers", "487", "+42")
            st.caption("💰 Revenue: $4,865/month")
        
        with plan_col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                        padding: 1.5rem; border-radius: 10px; text-align: center;">
                <h3 style="color: white; margin: 0;">💎 Elite</h3>
                <h2 style="color: white; margin: 1rem 0;">$29.99/mo</h2>
                <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem;">
                    ✅ Everything in Pro<br>
                    ✅ AI portfolio manager<br>
                    ✅ Backtesting tools<br>
                    ✅ API access<br>
                    ⚡ White-glove support
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Active Subscribers", "124", "+18")
            st.caption("💰 Revenue: $3,718/month")
        
        st.markdown("---")
        
        st.markdown("### 💰 Subscription Revenue Summary")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Monthly Recurring Revenue (MRR)", "$8,583", "+$698")
        with col2:
            st.metric("Annual Run Rate (ARR)", "$103,000", "+15.2%")
        with col3:
            st.metric("Churn Rate", "2.1%", "-0.4%")
        
        st.success("📈 **Growth Strategy**: Converting 5% of free users to Pro would double subscription revenue!")
    
    with tab3:
        st.subheader("📊 ILAH Token Data Sales")
        
        st.info("💡 **Privacy-First Monetization**: Families using OnTime app earn ILAH when their anonymized data is sold to researchers")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Data Monetization Model")
            
            st.markdown("""
            **How it works:**
            1. Families use OnTime app for scheduling
            2. App collects anonymized usage patterns
            3. Data sold to academic researchers, AI companies
            4. **Families earn ILAH tokens** for data contribution
            5. 10% of minted ILAH is auto-burned (anti-inflation)
            
            **Revenue Sharing:**
            - 60% → ILAH minted for families
            - 30% → Platform operational costs
            - 10% → AI model improvements
            
            **Privacy Protection:**
            - Federated learning (data processed locally)
            - Differential privacy (mathematical anonymization)
            - No personally identifiable information (PII)
            - Cannot reverse-engineer individual families
            """)
        
        with col2:
            st.markdown("### This Month's Data Sales")
            
            st.metric("Data Packages Sold", "47", "+8")
            st.metric("Revenue from Data", "$23,500", "+$4,200")
            st.metric("ILAH Minted (60%)", "14,100 tokens", "For families")
            st.metric("ILAH Burned (10%)", "2,350 tokens", "Anti-inflation")
            st.metric("Platform Share (30%)", "$7,050", "Operating costs")
            
            st.success("✅ Families earned $14,100 worth of ILAH this month!")
        
        st.markdown("---")
        
        st.markdown("### 🎯 Data Buyer Demographics")
        
        buyers_data = [
            {"Buyer Type": "AI Research Labs", "Purchases": 18, "Revenue": "$9,000", "Use Case": "Training scheduling AI"},
            {"Buyer Type": "Academic Institutions", "Purchases": 12, "Revenue": "$6,000", "Use Case": "Family dynamics research"},
            {"Buyer Type": "Product Companies", "Purchases": 9, "Revenue": "$5,400", "Use Case": "UX optimization"},
            {"Buyer Type": "Marketing Firms", "Purchases": 8, "Revenue": "$3,100", "Use Case": "Family targeting insights"},
        ]
        
        buyers_df = pd.DataFrame(buyers_data)
        st.dataframe(buyers_df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("📈 Combined Revenue Analytics")
        
        st.markdown("### Monthly Revenue Breakdown")
        
        revenue_sources = {
            "Source": ["Exchange Fees", "Pro Subscriptions", "Elite Subscriptions", "Data Sales", "Other"],
            "Revenue": [75000, 4865, 3718, 23500, 2157],
            "Percentage": ["68.9%", "4.5%", "3.4%", "21.6%", "2.0%"]
        }
        
        sources_df = pd.DataFrame(revenue_sources)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = go.Figure(data=[go.Pie(
                labels=revenue_sources["Source"],
                values=revenue_sources["Revenue"],
                hole=0.4,
                marker=dict(colors=['#FFD700', '#f093fb', '#fa709a', '#667eea', '#888'])
            )])
            
            fig.update_layout(
                title="Revenue Distribution",
                template='plotly_dark'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.dataframe(sources_df, use_container_width=True, hide_index=True)
            
            st.metric("Total Monthly Revenue", "$109,240")
            st.metric("YoY Growth", "+142%")
        
        st.markdown("---")
        
        st.markdown("### 📊 12-Month Revenue Projection")
        
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        base_revenue = 65000
        projected_revenue = [base_revenue * (1 + (i * 0.08)) for i in range(12)]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=months,
            y=projected_revenue,
            name='Projected Revenue',
            marker=dict(color='#FFD700')
        ))
        
        fig.add_trace(go.Scatter(
            x=months,
            y=[42500] * 12,
            name='Operating Costs',
            line=dict(color='#ff6b6b', dash='dash', width=2)
        ))
        
        fig.update_layout(
            title="Revenue vs Operating Costs (12-Month Forecast)",
            xaxis_title="Month",
            yaxis_title="Amount ($)",
            template='plotly_dark',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("🎯 **Projection**: By December, monthly revenue will reach $126K (197% growth) while costs remain flat at $42.5K")
    
    with tab5:
        st.subheader("⚙️ Operating Cost Breakdown")
        
        st.markdown("### Monthly Infrastructure & Operational Costs")
        
        col1, col2 = st.columns(2)
        
        with col1:
            costs_data = [
                {"Category": "☁️ Cloud Hosting (AWS)", "Monthly Cost": "$12,500", "Percentage": "29.4%"},
                {"Category": "🤖 AI API Credits (OpenAI)", "Monthly Cost": "$8,750", "Percentage": "20.6%"},
                {"Category": "💾 Database (PostgreSQL)", "Monthly Cost": "$4,200", "Percentage": "9.9%"},
                {"Category": "🔐 Security & SSL", "Monthly Cost": "$2,800", "Percentage": "6.6%"},
                {"Category": "📊 Data APIs (CoinGecko)", "Monthly Cost": "$3,500", "Percentage": "8.2%"},
                {"Category": "👨‍💻 Development & Support", "Monthly Cost": "$8,000", "Percentage": "18.8%"},
                {"Category": "📧 Email & Communications", "Monthly Cost": "$1,250", "Percentage": "2.9%"},
                {"Category": "📈 Analytics & Monitoring", "Monthly Cost": "$1,500", "Percentage": "3.5%"},
            ]
            
            costs_df = pd.DataFrame(costs_data)
            st.dataframe(costs_df, use_container_width=True, hide_index=True)
            
            st.metric("Total Monthly Costs", "$42,500")
            st.caption("✅ Fully covered by revenue")
        
        with col2:
            fig = go.Figure(data=[go.Pie(
                labels=[item["Category"] for item in costs_data],
                values=[float(item["Monthly Cost"].replace("$", "").replace(",", "")) for item in costs_data],
                hole=0.4
            )])
            
            fig.update_layout(
                title="Cost Distribution",
                template='plotly_dark'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("### 💰 Profitability Analysis")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Monthly Profit", "$44,740", "+$8,120")
        with col2:
            st.metric("Profit Margin", "51.3%", "+2.8%")
        with col3:
            st.metric("Cost Coverage Ratio", "205%", "+12%")
        with col4:
            st.metric("Runway", "Infinite", "Self-sustaining")
        
        st.success("🎉 **Achievement Unlocked**: Platform is fully self-sustaining and profitable!")
        
        st.info("""
        💡 **Profit Reinvestment Strategy**:
        - 40% → New features development
        - 30% → AI model improvements
        - 20% → Marketing & user acquisition
        - 10% → Emergency fund/buffer
        
        This ensures continuous improvement while maintaining FREE access for all users!
        """)
    
    st.markdown("---")
    
    st.header("🎯 Platform Sustainability Goals")
    
    goal_col1, goal_col2, goal_col3 = st.columns(3)
    
    with goal_col1:
        st.markdown("""
        ### ✅ Achieved
        - Profitable operations (51% margin)
        - All costs covered (205% ratio)
        - Growing user base (+15% MoM)
        - Diversified revenue streams
        """)
    
    with goal_col2:
        st.markdown("""
        ### 🚀 In Progress
        - Scale to 50K users (currently 13K)
        - Launch mobile app (OnTime)
        - Double subscription conversion
        - Expand data partnerships
        """)
    
    with goal_col3:
        st.markdown("""
        ### 🎯 Future Goals
        - $200K/month revenue
        - 100K active users
        - International expansion
        - Blockchain integration
        """)
    
    st.success("🌟 **Mission Success**: The platform generates enough revenue to offer FREE advanced features to ALL users while remaining profitable!")

# Call the main function
show()
