import streamlit as st
from wallet_manager import wallet_manager
from crypto_data import fetcher
from ai_crypto_expert import ai_expert
import pandas as pd
from datetime import datetime
import os

def show():
    st.header("💼 My Crypto Wallet")
    st.caption("Track your crypto holdings with real-time profit/loss calculations and AI portfolio recommendations")
    
    tab1, tab2, tab3 = st.tabs(["Portfolio Overview", "Add Holdings", "AI Portfolio Analysis"])
    
    with tab1:
        show_portfolio_overview()
    
    with tab2:
        show_add_holdings()
    
    with tab3:
        show_ai_portfolio_analysis()

def show_portfolio_overview():
    st.subheader("📊 Portfolio Summary")
    
    with st.spinner("Loading your portfolio..."):
        portfolio_data = wallet_manager.get_portfolio_value()
    
    if not portfolio_data['items']:
        st.info("👋 Your wallet is empty. Add your first cryptocurrency holding in the 'Add Holdings' tab to start tracking your portfolio!")
        return
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Value", f"${portfolio_data['total_value']:,.2f}")
    
    with col2:
        st.metric("Total Cost", f"${portfolio_data['total_cost']:,.2f}")
    
    with col3:
        profit_loss = portfolio_data['total_profit_loss']
        st.metric("Profit/Loss", f"${profit_loss:,.2f}", 
                 delta=f"{portfolio_data['total_profit_loss_pct']:+.2f}%")
    
    with col4:
        num_holdings = len(portfolio_data['items'])
        st.metric("Holdings", num_holdings)
    
    st.markdown("---")
    
    st.subheader("🪙 Your Holdings")
    
    for item in portfolio_data['items']:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
            
            with col1:
                st.write(f"**{item['name']}** ({item['symbol'].upper()})")
                st.caption(f"{item['amount']} tokens")
            
            with col2:
                st.write(f"**${item['current_value']:,.2f}**")
                st.caption(f"@ ${item['current_price']:,.6f}" if item['current_price'] < 1 else f"@ ${item['current_price']:,.2f}")
            
            with col3:
                st.write(f"Bought: ${item['purchase_price']:,.6f}" if item['purchase_price'] < 1 else f"Bought: ${item['purchase_price']:,.2f}")
                purchase_date_str = item['purchase_date'].strftime("%Y-%m-%d") if item['purchase_date'] else "N/A"
                st.caption(f"on {purchase_date_str}")
            
            with col4:
                profit_loss_color = "green" if item['profit_loss'] > 0 else "red" if item['profit_loss'] < 0 else "gray"
                st.markdown(f"<span style='color:{profit_loss_color};font-weight:bold'>${item['profit_loss']:+,.2f}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:{profit_loss_color}'>{item['profit_loss_pct']:+.2f}%</span>", unsafe_allow_html=True)
            
            with col5:
                if st.button("🗑️", key=f"delete_{item['id']}", help="Remove from portfolio"):
                    if wallet_manager.delete_holding(item['id']):
                        st.success("Removed!")
                        st.rerun()
            
            if item['notes']:
                with st.expander("📝 Notes"):
                    st.write(item['notes'])
            
            st.markdown("---")
    
    st.subheader("📈 Portfolio Allocation")
    
    allocation_data = []
    for item in portfolio_data['items']:
        allocation_pct = (item['current_value'] / portfolio_data['total_value'] * 100) if portfolio_data['total_value'] > 0 else 0
        allocation_data.append({
            'name': item['name'],
            'value': item['current_value'],
            'percentage': allocation_pct
        })
    
    allocation_data.sort(key=lambda x: x['value'], reverse=True)
    
    for alloc in allocation_data:
        st.progress(alloc['percentage'] / 100, text=f"{alloc['name']}: ${alloc['value']:,.2f} ({alloc['percentage']:.1f}%)")

def show_add_holdings():
    st.subheader("➕ Add New Holding")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        crypto_search = st.text_input("Search cryptocurrency", placeholder="Bitcoin, Ethereum, Dogecoin...")
    
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
            
            with st.spinner("Fetching current price..."):
                crypto_data = fetcher.get_crypto_by_id(crypto_id)
            
            current_price = 0
            if crypto_data:
                current_price = crypto_data.get('market_data', {}).get('current_price', {}).get('usd', 0)
                st.info(f"💰 Current Price: ${current_price:,.6f}" if current_price < 1 else f"💰 Current Price: ${current_price:,.2f}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                amount = st.number_input(
                    "Amount (how many tokens)",
                    min_value=0.0,
                    value=1.0,
                    step=0.1,
                    format="%.6f",
                    help="Number of tokens you own"
                )
            
            with col2:
                purchase_price = st.number_input(
                    "Purchase Price (USD per token)",
                    min_value=0.0,
                    value=float(current_price) if current_price > 0 else 0.0,
                    step=0.000001,
                    format="%.6f",
                    help="Price you paid per token"
                )
            
            purchase_date = st.date_input("Purchase Date", value=datetime.now())
            notes = st.text_area("Notes (optional)", placeholder="Add any notes about this investment...")
            
            if amount > 0 and purchase_price > 0:
                total_cost = amount * purchase_price
                st.write(f"**Total Investment:** ${total_cost:,.2f}")
                
                if current_price > 0:
                    current_value = amount * current_price
                    profit_loss = current_value - total_cost
                    profit_loss_pct = (profit_loss / total_cost * 100) if total_cost > 0 else 0
                    
                    st.write(f"**Current Value:** ${current_value:,.2f}")
                    
                    color = "green" if profit_loss > 0 else "red"
                    st.markdown(f"**Profit/Loss:** <span style='color:{color}'>${profit_loss:+,.2f} ({profit_loss_pct:+.2f}%)</span>", unsafe_allow_html=True)
            
            if st.button("💾 Add to Portfolio", type="primary", use_container_width=True):
                if amount <= 0:
                    st.error("Please enter a valid amount")
                elif purchase_price <= 0:
                    st.error("Please enter a valid purchase price")
                else:
                    success = wallet_manager.add_holding(
                        crypto_id=crypto_id,
                        crypto_name=crypto_name,
                        crypto_symbol=crypto_symbol,
                        amount=amount,
                        purchase_price=purchase_price,
                        purchase_date=datetime.combine(purchase_date, datetime.min.time()),
                        notes=notes
                    )
                    
                    if success:
                        st.success(f"✅ Added {amount} {crypto_symbol.upper()} to your portfolio!")
                        st.balloons()
                        st.info("👈 Go to 'Portfolio Overview' tab to see your updated portfolio")
                    else:
                        st.error("Failed to add holding. Please try again.")
        
        else:
            st.warning("No results found. Try: bitcoin, ethereum, dogecoin, shiba-inu, pepe")
    
    else:
        st.info("👆 Search for a cryptocurrency to add to your portfolio")

def show_ai_portfolio_analysis():
    st.subheader("🤖 AI Portfolio Analysis")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if not ai_key or not ai_base_url:
        st.warning("⚠️ AI Integration not configured.")
        return
    
    portfolio_data = wallet_manager.get_portfolio_value()
    
    if not portfolio_data['items']:
        st.info("Add some holdings to your portfolio to get AI analysis and recommendations!")
        return
    
    st.success("✅ AI Portfolio Analyzer Active")
    
    risk_tolerance = st.select_slider(
        "Risk Tolerance",
        options=["Very Conservative", "Conservative", "Moderate", "Aggressive", "Very Aggressive"],
        value="Moderate"
    )
    
    if st.button("🤖 Analyze My Portfolio", type="primary", use_container_width=True):
        with st.spinner("🤖 AI is analyzing your portfolio..."):
            try:
                portfolio_summary = f"""
                Total Portfolio Value: ${portfolio_data['total_value']:,.2f}
                Total Cost Basis: ${portfolio_data['total_cost']:,.2f}
                Profit/Loss: ${portfolio_data['total_profit_loss']:,.2f} ({portfolio_data['total_profit_loss_pct']:+.2f}%)
                Number of Holdings: {len(portfolio_data['items'])}
                
                Holdings Breakdown:
                """
                
                for item in portfolio_data['items']:
                    allocation_pct = (item['current_value'] / portfolio_data['total_value'] * 100) if portfolio_data['total_value'] > 0 else 0
                    portfolio_summary += f"\n- {item['name']} ({item['symbol'].upper()}): {allocation_pct:.1f}% (${item['current_value']:,.2f}), P/L: {item['profit_loss_pct']:+.2f}%"
                
                prompt = f"""
                You are an expert cryptocurrency portfolio manager. Analyze this portfolio and provide recommendations.
                
                USER'S PORTFOLIO:
                {portfolio_summary}
                
                RISK TOLERANCE: {risk_tolerance}
                
                Provide a comprehensive analysis with:
                1. Overall portfolio health assessment
                2. Diversification analysis
                3. Risk assessment based on user's tolerance
                4. Specific rebalancing recommendations
                5. Which assets to buy more of / sell / hold
                6. Position sizing suggestions
                
                Respond ONLY with valid JSON:
                {{
                    "health_score": 85,
                    "health_assessment": "Overall assessment...",
                    "diversification_score": 70,
                    "diversification_analysis": "Analysis...",
                    "risk_assessment": "Risk analysis...",
                    "recommendations": ["Rec 1", "Rec 2", "Rec 3"],
                    "buy_more": ["Asset 1", "Asset 2"],
                    "sell": ["Asset 1"],
                    "hold": ["Asset 1", "Asset 2"]
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
                
                st.markdown("---")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    health_score = analysis.get('health_score', 0)
                    health_color = "green" if health_score >= 70 else "orange" if health_score >= 50 else "red"
                    st.markdown(f"<h2 style='color:{health_color}'>Health: {health_score}/100</h2>", unsafe_allow_html=True)
                
                with col2:
                    div_score = analysis.get('diversification_score', 0)
                    div_color = "green" if div_score >= 70 else "orange" if div_score >= 50 else "red"
                    st.markdown(f"<h2 style='color:{div_color}'>Diversity: {div_score}/100</h2>", unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"<h2>Risk: {risk_tolerance}</h2>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Portfolio Health")
                    st.info(analysis.get('health_assessment', ''))
                    
                    st.subheader("🎯 Diversification")
                    st.info(analysis.get('diversification_analysis', ''))
                
                with col2:
                    st.subheader("⚠️ Risk Assessment")
                    st.warning(analysis.get('risk_assessment', ''))
                    
                    st.subheader("💡 Key Recommendations")
                    for rec in analysis.get('recommendations', []):
                        st.write(f"✅ {rec}")
                
                st.markdown("---")
                
                st.subheader("📋 Action Items")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**🟢 Buy More:**")
                    for asset in analysis.get('buy_more', []):
                        st.success(f"• {asset}")
                
                with col2:
                    st.write("**🔵 Hold:**")
                    for asset in analysis.get('hold', []):
                        st.info(f"• {asset}")
                
                with col3:
                    st.write("**🔴 Consider Selling:**")
                    for asset in analysis.get('sell', []):
                        st.error(f"• {asset}")
                
            except Exception as e:
                st.error(f"AI Analysis Error: {str(e)}")
                st.info("Please try again.")

# Call the main function
show()
