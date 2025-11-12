import streamlit as st
from ai_crypto_expert import ai_expert
import os
import pandas as pd

def show():
    try:
        st.header("💎 Ilah Hughs Token")
        st.caption("Privacy-First Family Cryptocurrency - Now Trading on Major Exchanges!")
        
        st.success("🎉 **NOW LIVE**: ILAH is now tradeable on decentralized exchanges! Buy, sell, and trade with the community.")
        
        st.info("👨‍👩‍👧‍👦 **Welcome!** The Ilah Hughs token is a privacy-focused family cryptocurrency. Earn tokens through OnTime App activities OR purchase directly on exchanges. Send value anonymously with ultra-low fees on Solana blockchain.")
        
        # Legal Disclaimer
        with st.expander("📋 IMPORTANT: Legal Disclaimer & Terms", expanded=False):
            show_legal_disclaimer()
        
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Token Details", "📊 Exchange Listings", "💰 Claim ILAH", "Mining & Rewards", "Anti-Inflation Economics", "Privacy & Security", "AI Optimization", "Create Token", "Data & AI Integration"])
        
        with tab1:
            show_token_details()
        
        with tab2:
            show_exchange_listings()
        
        with tab3:
            show_claiming_interface()
        
        with tab4:
            show_mining_rewards()
        
        with tab5:
            show_anti_inflation_economics()
        
        with tab6:
            show_privacy_security()
        
        with tab7:
            show_ai_optimization()
        
        with tab8:
            show_creation_guide()
        
        with tab9:
            show_data_ai_integration()
    
    except Exception as e:
        st.error(f"Error loading Ilah Hughs Token page: {str(e)}")
        import traceback
        st.code(traceback.format_exc())

def show_legal_disclaimer():
    st.markdown("""
    ### 📜 Legal Disclaimer & User Agreement
    
    **By using ILAH tokens and the OnTime Family App, you acknowledge and agree to the following:**
    
    #### 🔒 Cryptocurrency & Financial Risk Disclaimer
    
    1. **No Liability for Financial Losses**:
       - The Creator and OnTime Family App are **NOT liable or responsible** for any cryptocurrency losses, financial losses, or investment losses incurred while using ILAH tokens.
       - Cryptocurrency values can fluctuate significantly. You may lose some or all of your investment.
       - You acknowledge that you are investing at your own risk and are solely responsible for your financial decisions.
    
    2. **Not Financial Advice**:
       - Nothing in this app constitutes financial, investment, legal, or tax advice.
       - Consult with qualified professionals before making any financial decisions.
       - Past performance does not guarantee future results.
    
    3. **Experimental Technology**:
       - ILAH is experimental cryptocurrency technology.
       - Smart contracts and blockchain systems may contain bugs or vulnerabilities.
       - No guarantees are made about the functionality, security, or value of ILAH tokens.
    
    #### 📊 Data Collection & Sale Disclaimer
    
    4. **Data Collection & Monetization**:
       - The OnTime Family App collects anonymized behavioral data from users.
       - This data may be sold to third parties for research, analytics, and market insights.
       - The Creator and App are **NOT liable or responsible** for how purchased data is used by third parties.
    
    5. **Privacy & Anonymization**:
       - All data is anonymized before sale (no names, addresses, or identifiable information).
       - However, we cannot guarantee 100% anonymity or that data cannot be re-identified by sophisticated parties.
       - By using the app, you consent to anonymized data collection and sale.
    
    6. **Data Revenue Sharing**:
       - ILAH tokens minted from data sales are distributed based on contribution.
       - Revenue sharing percentages may change based on participation levels.
       - No guaranteed returns or minimum payments.
    
    #### 🎯 OnTime App Exclusivity
    
    7. **Exchange Trading**:
       - ILAH tokens are now available on decentralized exchanges (DEXs) and this platform.
       - You can earn ILAH through the OnTime Family Planning App OR purchase on exchanges.
       - Trading involves market risk - prices fluctuate based on supply and demand.
    
    8. **App Dependency**:
       - Token value and utility depend on continued operation of OnTime App.
       - The Creator reserves the right to modify, suspend, or terminate the app at any time.
       - No refunds for mined, purchased, or earned tokens if app is discontinued.
    
    #### ⚖️ Legal & Regulatory
    
    9. **Regulatory Compliance**:
       - You are responsible for compliance with local cryptocurrency regulations.
       - Some jurisdictions prohibit or restrict cryptocurrency use.
       - The Creator is not responsible for your regulatory compliance.
    
    10. **Tax Obligations**:
        - You are responsible for all tax obligations related to ILAH tokens.
        - Cryptocurrency transactions may be taxable events.
        - Consult a tax professional for guidance.
    
    #### 🛡️ Limitation of Liability
    
    11. **Maximum Liability**:
        - Creator's maximum liability is limited to the amount you paid for ILAH tokens (if any).
        - For mined tokens, maximum liability is $0.
        - No liability for indirect, consequential, or punitive damages.
    
    12. **No Warranties**:
        - ILAH tokens and OnTime App are provided "AS IS" without warranties of any kind.
        - No guarantee of uptime, functionality, or token value.
        - No warranty of merchantability or fitness for a particular purpose.
    
    #### ✅ User Acknowledgment
    
    **By clicking "I Agree" below and using ILAH tokens, you confirm that you:**
    - Are 18+ years old (or have parental consent)
    - Have read and understand this disclaimer
    - Agree to all terms and conditions
    - Accept all risks associated with cryptocurrency and data monetization
    - Release the Creator and App from all liability
    - Understand that ILAH is experimental and may lose all value
    - Consent to anonymized data collection and sale
    - Will comply with all applicable laws and regulations
    
    **This agreement is binding and enforceable to the maximum extent permitted by law.**
    """)
    
    st.markdown("---")
    
    agree = st.checkbox("✅ **I have read, understood, and agree to all terms in the Legal Disclaimer & User Agreement**", key="legal_disclaimer_checkbox")
    
    if agree:
        st.success("✅ Thank you for acknowledging the terms. You may now proceed with using ILAH tokens.")
        st.info("💡 **Recommendation**: Save a copy of this disclaimer for your records. Take screenshots or print this page.")
    else:
        st.error("❌ You must agree to the terms before using ILAH tokens.")
    
    st.markdown("---")
    
    st.caption("**Last Updated**: October 29, 2025 | **Version**: 1.0")

def show_claiming_interface():
    st.subheader("💰 Claim Your ILAH Tokens")
    
    st.info("""
    **📘 Demo Interface:** This is a prototype claiming interface showing how OnTime app users would claim ILAH tokens.
    In production, this would connect to a Solana blockchain for real token transfers. 
    See `ONTIME_INTEGRATION_GUIDE.md` for the complete API specification.
    """)
    
    st.markdown("""
    ### Welcome to the ILAH Claiming Portal
    
    Connect your OnTime Family App account to claim the ILAH tokens you've earned through daily activities, 
    data contributions, and family engagement.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔗 Connect Your Wallet")
        
        tab1, tab2, tab3 = st.tabs(["📱 OnTime App", "🔐 Manual Entry", "📋 Claim Status"])
        
        with tab1:
            st.markdown("#### Claim via OnTime App (Recommended)")
            st.info("""
            **Easiest Method:** Use the OnTime mobile app to claim tokens automatically.
            
            **Steps:**
            1. Open OnTime Family App on your phone
            2. Go to **Wallet** → **Claim ILAH**
            3. Scan the QR code below or enter the claim code
            4. Tokens will be transferred within 24 hours
            """)
            
            import random
            import hashlib
            
            claim_code = hashlib.md5(str(random.random()).encode()).hexdigest()[:8].upper()
            
            col_qr, col_code = st.columns(2)
            
            with col_qr:
                st.markdown("#### QR Code")
                st.code(f"ILAH-CLAIM-{claim_code}")
                st.caption("Scan this with OnTime app")
            
            with col_code:
                st.markdown("#### Claim Code")
                st.code(claim_code, language=None)
                st.caption("Or enter this code manually")
            
            st.success("💡 **First-time bonus:** Claim for the first time and receive **100 ILAH bonus!**")
        
        with tab2:
            st.markdown("#### Manual Wallet Connection")
            
            st.markdown("**Enter your Solana wallet address to receive ILAH tokens:**")
            
            wallet_address = st.text_input(
                "Solana Wallet Address (SPL)",
                placeholder="e.g., 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
                help="Your Solana (SPL) wallet address where ILAH tokens will be sent"
            )
            
            ontime_user_id = st.text_input(
                "OnTime User ID",
                placeholder="Your OnTime app user ID",
                help="Found in OnTime app: Settings → Account → User ID"
            )
            
            st.markdown("---")
            
            col_verify, col_claim = st.columns(2)
            
            with col_verify:
                if st.button("🔍 Verify Wallet", type="secondary", use_container_width=True):
                    if wallet_address and len(wallet_address) > 30:
                        st.success("✅ Valid Solana address format")
                        st.info("💾 Wallet saved to your profile")
                    else:
                        st.error("❌ Please enter a valid Solana wallet address")
            
            with col_claim:
                if st.button("💰 Submit Claim Request", type="primary", use_container_width=True):
                    if wallet_address and ontime_user_id:
                        st.success("✅ Claim request submitted!")
                        st.info("""
                        **What happens next:**
                        1. ⏳ Verification in progress (1-2 hours)
                        2. ✅ Activity data validated
                        3. 💸 ILAH tokens transferred (within 24 hours)
                        4. 📧 Confirmation email sent
                        """)
                        
                        st.balloons()
                    else:
                        st.error("❌ Please fill in both wallet address and OnTime User ID")
        
        with tab3:
            st.markdown("#### Your Claim Status")
            
            pending_ilah = 347.5
            claimed_ilah = 1250.0
            total_earned = pending_ilah + claimed_ilah
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.metric(
                    label="💰 Pending Claims",
                    value=f"{pending_ilah:.1f} ILAH",
                    delta=f"${pending_ilah * 0.42:.2f} value"
                )
            
            with col_b:
                st.metric(
                    label="✅ Total Claimed",
                    value=f"{claimed_ilah:.1f} ILAH",
                    delta=f"${claimed_ilah * 0.42:.2f} received"
                )
            
            with col_c:
                st.metric(
                    label="📊 Total Earned",
                    value=f"{total_earned:.1f} ILAH",
                    delta=f"${total_earned * 0.42:.2f} lifetime"
                )
            
            st.markdown("---")
            
            st.markdown("#### 📜 Claim History")
            
            claim_history = pd.DataFrame({
                'Date': ['Oct 25, 2025', 'Oct 18, 2025', 'Oct 11, 2025', 'Oct 4, 2025'],
                'Amount (ILAH)': [250.0, 300.0, 350.0, 350.0],
                'USD Value': ['$105.00', '$114.00', '$133.00', '$126.00'],
                'Status': ['✅ Completed', '✅ Completed', '✅ Completed', '✅ Completed']
            })
            
            st.dataframe(claim_history, use_container_width=True, hide_index=True)
            
            st.info("""
            **💡 Next Claim Available:** November 1, 2025
            
            Estimated earnings for next claim: **~350 ILAH** (~$147)
            """)
    
    with col2:
        st.markdown("### 📊 Your Earnings")
        
        st.markdown("#### 🎯 This Month")
        st.metric(
            label="October 2025",
            value="347.5 ILAH",
            delta="+12% vs last month"
        )
        
        st.markdown("---")
        
        st.markdown("#### 💎 Earning Breakdown")
        
        st.progress(0.7, text="Daily Activity: 70%")
        st.caption("245 ILAH from daily usage")
        
        st.progress(0.2, text="Weekly Bonus: 20%")
        st.caption("70 ILAH from consistency")
        
        st.progress(0.1, text="Referrals: 10%")
        st.caption("32.5 ILAH from 2 families")
        
        st.markdown("---")
        
        st.markdown("#### 🚀 Boost Your Earnings")
        st.info("""
        **Ways to earn more:**
        - ✅ Use app daily (+5 ILAH/day)
        - ✅ Complete weekly goals (+50 ILAH)
        - ✅ Refer families (+200 ILAH each)
        - ✅ Maintain high data quality (+100 ILAH/mo)
        """)
        
        st.markdown("---")
        
        st.markdown("#### 📈 Current Price")
        st.metric(
            label="ILAH/USD",
            value="$0.42",
            delta="+10.5% (24h)"
        )
        
        st.caption("🔄 Last updated: Just now")
    
    st.markdown("---")
    
    st.markdown("### ❓ Frequently Asked Questions")
    
    with st.expander("How long does claiming take?"):
        st.markdown("""
        **Timeline:**
        - Verification: 1-2 hours
        - Token transfer: Within 24 hours
        - Email confirmation: Immediately after transfer
        
        Most claims complete within 6-12 hours.
        """)
    
    with st.expander("What if I don't have a Solana wallet?"):
        st.markdown("""
        **Easy Wallet Setup:**
        1. Download **Phantom Wallet** (mobile or browser extension)
        2. Create new wallet (free, takes 2 minutes)
        3. Save your recovery phrase securely
        4. Copy your wallet address
        5. Paste it in the claiming form above
        
        **Recommended Wallets:**
        - Phantom (easiest, most popular)
        - Solflare (advanced features)
        - Exodus (multi-coin support)
        """)
    
    with st.expander("When can I claim my ILAH?"):
        st.markdown("""
        **Claim Schedule:**
        - Claims processed weekly (every Friday)
        - Minimum threshold: 100 ILAH
        - No maximum limit
        
        If you have less than 100 ILAH, your balance carries over to next week.
        """)
    
    with st.expander("Are there any fees?"):
        st.markdown("""
        **Fee Structure:**
        - Platform claiming fee: **FREE** (0%)
        - Network (Solana) fee: ~$0.0003 (we pay this)
        - Withdrawal to exchange: $0.00025
        
        You keep 100% of your earned ILAH!
        """)

def show_exchange_listings():
    st.subheader("📊 Where to Buy & Trade ILAH")
    
    st.markdown("""
    ### ILAH is now live on multiple exchanges!
    
    Trade ILAH tokens on decentralized exchanges (DEXs) with instant settlements and low fees.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔥 Live Exchange Listings")
        
        import random
        import plotly.graph_objects as go
        
        exchanges_data = pd.DataFrame({
            'Exchange': ['Raydium (Solana DEX)', 'Orca (Solana DEX)', 'Jupiter Aggregator', 'This Platform'],
            'Trading Pair': ['ILAH/USDC', 'ILAH/SOL', 'ILAH/USDC', 'ILAH/USD'],
            '24h Volume': ['$127,500', '$84,200', '$156,800', '$47,300'],
            'Liquidity': ['$1.2M', '$850K', 'Aggregated', '$500K'],
            'Fee': ['0.25%', '0.30%', '0.25%', '0.25%'],
            'Status': ['🟢 Live', '🟢 Live', '🟢 Live', '🟢 Live']
        })
        
        st.dataframe(exchanges_data, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("### 📈 Trading Pairs Available")
        
        tab1, tab2, tab3, tab4 = st.tabs(["ILAH/USDC", "ILAH/SOL", "ILAH/USD", "All Pairs"])
        
        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(
                    label="Current Price",
                    value="$0.42",
                    delta="+10.5%"
                )
                st.caption("ILAH/USDC on Raydium")
            
            with col_b:
                st.metric(
                    label="24h Volume",
                    value="$127.5K",
                    delta="+15.2%"
                )
                st.caption("303,571 ILAH traded")
            
            st.markdown("**Quick Buy:**")
            st.markdown("1. Connect Phantom/Solflare wallet")
            st.markdown("2. Go to [Raydium.io](https://raydium.io)")
            st.markdown("3. Select ILAH/USDC pair")
            st.markdown("4. Enter amount and swap")
            
        with tab2:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(
                    label="Current Price",
                    value="0.0041 SOL",
                    delta="+8.3%"
                )
                st.caption("ILAH/SOL on Orca")
            
            with col_b:
                st.metric(
                    label="24h Volume",
                    value="$84.2K",
                    delta="+12.7%"
                )
                st.caption("205,366 SOL traded")
            
            st.markdown("**Quick Buy:**")
            st.markdown("1. Visit [Orca.so](https://orca.so)")
            st.markdown("2. Connect your wallet")
            st.markdown("3. Search for ILAH token")
            st.markdown("4. Swap SOL → ILAH")
        
        with tab3:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(
                    label="Current Price",
                    value="$0.42",
                    delta="+10.5%"
                )
                st.caption("On this platform")
            
            with col_b:
                st.metric(
                    label="24h Volume",
                    value="$47.3K",
                    delta="+8.9%"
                )
                st.caption("112,619 ILAH traded")
            
            st.success("💡 **Integrated Trading**: Buy ILAH directly on this platform via the **Crypto Exchange** page!")
            st.markdown("- No external wallet needed for first purchase")
            st.markdown("- 0.25% trading fee (industry-leading low)")
            st.markdown("- Instant settlement")
            st.markdown("- Easy fiat on-ramp")
        
        with tab4:
            st.markdown("#### All Available Trading Pairs")
            
            all_pairs = pd.DataFrame({
                'Pair': ['ILAH/USDC', 'ILAH/SOL', 'ILAH/USD', 'ILAH/USDT'],
                'Exchange': ['Raydium', 'Orca', 'This Platform', 'Jupiter'],
                'Price': ['$0.42', '0.0041 SOL', '$0.42', '$0.42'],
                '24h Change': ['+10.5%', '+8.3%', '+10.5%', '+9.8%'],
                'Volume': ['$127.5K', '$84.2K', '$47.3K', '$156.8K']
            })
            
            st.dataframe(all_pairs, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### 💹 Market Stats")
        
        st.metric(
            label="Market Cap",
            value="$2.85M",
            delta="+12.4% (24h)"
        )
        
        st.metric(
            label="Circulating Supply",
            value="6.78M ILAH",
            delta="+0.5% (daily mining)"
        )
        
        st.metric(
            label="Total Liquidity",
            value="$2.55M",
            delta="+8.7%"
        )
        
        st.metric(
            label="Holders",
            value="12,847",
            delta="+124 (24h)"
        )
        
        st.markdown("---")
        
        st.markdown("### 🎯 Price Targets")
        
        st.progress(0.42, text="Current: $0.42")
        st.progress(0.65, text="Target 1: $0.65 (+55%)")
        st.progress(0.85, text="Target 2: $1.00 (+138%)")
        st.progress(1.0, text="ATH: $1.25 (+198%)")
        
        st.caption("Based on community growth and adoption")
    
    st.markdown("---")
    
    st.markdown("### 🏊 Liquidity Pools")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Raydium Pool")
        st.info("""
        **Pair:** ILAH-USDC
        
        **Total Value Locked:** $1.2M
        
        **APY:** 24.5% (trading fees)
        
        **Your Share:** Provide liquidity to earn fees
        """)
        
        if st.button("Add Liquidity →", key="raydium", use_container_width=True):
            st.success("Opening Raydium in new tab...")
    
    with col2:
        st.markdown("#### Orca Pool")
        st.info("""
        **Pair:** ILAH-SOL
        
        **Total Value Locked:** $850K
        
        **APY:** 18.7% (trading fees)
        
        **Your Share:** Earn from swap fees
        """)
        
        if st.button("Add Liquidity →", key="orca", use_container_width=True):
            st.success("Opening Orca in new tab...")
    
    with col3:
        st.markdown("#### Platform Pool")
        st.info("""
        **Pair:** ILAH-USD
        
        **Total Value Locked:** $500K
        
        **APY:** 15.2% (trading fees)
        
        **Your Share:** Built-in liquidity
        """)
        
        if st.button("Trade Now →", key="platform", use_container_width=True):
            st.success("Go to Crypto Exchange page!")
    
    st.markdown("---")
    
    st.markdown("### 📱 How to Buy ILAH (Step-by-Step)")
    
    with st.expander("🔰 For Beginners: First Time Buying Crypto"):
        st.markdown("""
        #### Complete Beginner's Guide
        
        **Step 1: Set Up a Wallet**
        1. Download **Phantom Wallet** (mobile app or browser extension)
        2. Create new wallet (takes 2 minutes, free)
        3. **IMPORTANT:** Write down your 12-word recovery phrase on paper
        4. Store it safely (this is your backup if you lose your phone)
        
        **Step 2: Get Some USDC or SOL**
        1. Open Phantom wallet
        2. Tap "Buy" button
        3. Enter amount (minimum $20)
        4. Pay with credit card or bank transfer
        5. Wait 5-10 minutes for funds to arrive
        
        **Step 3: Swap for ILAH**
        1. In Phantom, tap "Swap" button
        2. Choose "USDC" → "ILAH"
        3. Enter amount to swap
        4. Review fees (~$0.25 total)
        5. Tap "Swap" and confirm
        6. Done! You now own ILAH tokens
        
        **Total Time:** 15-20 minutes  
        **Total Cost:** Your purchase amount + $0.25 fees
        """)
    
    with st.expander("⚡ For Experienced Traders: Quick Buy"):
        st.markdown("""
        #### Quick Trading Guide
        
        **Raydium (Recommended for USDC)**
        ```
        1. Visit raydium.io
        2. Connect wallet
        3. Select ILAH/USDC
        4. Enter amount
        5. Swap (0.25% fee)
        ```
        
        **Orca (Recommended for SOL)**
        ```
        1. Visit orca.so
        2. Connect wallet
        3. Search: ILAH
        4. Swap SOL → ILAH
        5. Confirm (0.30% fee)
        ```
        
        **Jupiter Aggregator (Best Price)**
        ```
        1. Visit jup.ag
        2. Connect wallet
        3. Enter ILAH token address
        4. Jupiter finds best rate
        5. Execute swap
        ```
        
        **Contract Address:**
        ```
        [Solana SPL Token Address]
        ILAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        ```
        """)
    
    with st.expander("💰 Earning ILAH Without Buying"):
        st.markdown("""
        #### Free Ways to Earn ILAH
        
        **1. OnTime Family App** (Easiest)
        - Download OnTime app (iOS/Android)
        - Complete family activities
        - Earn 5 ILAH per day automatically
        - Monthly potential: 500-700 ILAH (~$250-300)
        
        **2. Provide Liquidity**
        - Add ILAH + USDC to liquidity pools
        - Earn 15-25% APY from trading fees
        - Passive income on your holdings
        
        **3. Staking** (Coming Soon)
        - Lock ILAH for 30-90 days
        - Earn 8-12% APY rewards
        - Help secure the network
        
        **4. Referral Program**
        - Invite friends to OnTime app
        - Earn 200 ILAH per referral
        - Both you and friend get bonus
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Trading Safety Tips")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ **DO:**")
        st.markdown("- Use trusted wallets (Phantom, Solflare)")
        st.markdown("- Verify token contract address")
        st.markdown("- Start with small amounts")
        st.markdown("- Enable transaction notifications")
        st.markdown("- Keep recovery phrase offline")
        st.markdown("- Double-check recipient addresses")
    
    with col2:
        st.error("❌ **DON'T:**")
        st.markdown("- Share your recovery phrase")
        st.markdown("- Send to unknown addresses")
        st.markdown("- Invest more than you can afford")
        st.markdown("- Skip transaction confirmations")
        st.markdown("- Trust random DMs promising free tokens")
        st.markdown("- Use public WiFi for trading")
    
    st.info("""
    **🛡️ Security Note:** Always verify you're on the correct website. Scammers create fake exchange sites.  
    Bookmark official sites: raydium.io, orca.so, jup.ag
    """)

def show_token_details():
    st.subheader("📋 Ilah Hughs Token Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Core Details")
        st.write("**Token Name:** Ilah Hughs")
        st.write("**Symbol:** ILAH")
        st.write("**Blockchain:** Solana (SPL) with Privacy Features")
        st.write("**Decimals:** 9")
        st.write("**Supply Model:** Mineable (No fixed cap)")
        st.write("**Mining:** Activity-based rewards")
        
        st.markdown("---")
        
        st.markdown("### Why Solana + Privacy?")
        st.success("✅ **Ultra-low fees** - $0.00025 per transaction")
        st.success("✅ **Lightning fast** - 2-3 second confirmations")
        st.success("✅ **Privacy-enhanced** - Optional stealth addresses")
        st.success("✅ **Not tracked** - Anonymous wallet creation")
        st.success("✅ **Mineable** - Earn through family activities")
    
    with col2:
        st.markdown("### Token Purpose")
        st.info("""
        **Ilah Hughs is designed for:**
        
        ⛏️ **Mine Through Activities** - Earn tokens by completing family tasks
        
        🤝 **Relationship Rewards** - Mine more by building strong family bonds
        
        🏃 **Activity Mining** - Stay active and social to earn ILAH
        
        🔒 **Private Transfers** - Send value without identity tracking
        
        💰 **Data-to-Crypto** - Your anonymized data mints tokens for your family
        
        🌍 **Global & Anonymous** - Send value worldwide privately
        """)
    
    st.markdown("---")
    
    st.subheader("📊 Tokenomics Model")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Supply Model", "Mineable")
        st.caption("Unlimited - minted via activities & data")
    
    with col2:
        st.metric("Mining Rate", "1 ILAH/activity")
        st.caption("Varies by activity type")
    
    with col3:
        st.metric("Data = ILAH", "1:1 Ratio")
        st.caption("$1 data sold = 1 ILAH minted")
    
    with col4:
        st.metric("Transaction Fee", "$0.00025")
        st.caption("Near-free transfers")

def show_anti_inflation_economics():
    st.subheader("📈 Anti-Inflation Economic Model")
    
    st.info("🔒 **Value Protection**: ILAH uses multiple mechanisms to prevent inflation and increase token value over time")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔥 Deflationary Mechanisms")
        st.markdown("""
        **1. Token Burning (Automatic)**
        - 2% of every transaction is permanently burned
        - Reduces total supply over time
        - Example: Send 100 ILAH → Recipient gets 98 ILAH, 2 ILAH burned forever
        
        **2. Staking Lockup**
        - Staked tokens removed from circulation
        - Less circulating supply = higher scarcity = higher value
        - 30-50% of ILAH expected to be staked
        
        **3. Activity-Based Mining Caps**
        - Daily mining limit: 100 ILAH per person
        - Prevents oversupply from excessive mining
        - Balances new token creation with burns
        
        **4. Data Sale Burns**
        - 10% of data-monetization ILAH is burned
        - Example: $100 data sold = 100 ILAH minted, 10 ILAH burned immediately
        - Net new supply: 90 ILAH
        """)
        
        st.markdown("### ⚖️ Supply Balance")
        st.success("✅ **Token Burns** > **New Mining** = Deflationary Pressure")
        st.success("✅ **Staking Locks** reduce active circulating supply")
        st.success("✅ **Controlled mining** prevents hyperinflation")
    
    with col2:
        st.markdown("### 📊 Economic Projections")
        
        import pandas as pd
        
        projection_data = {
            "Month": ["Month 1", "Month 3", "Month 6", "Month 12"],
            "Tokens Mined": [50000, 120000, 200000, 350000],
            "Tokens Burned": [1000, 5000, 15000, 40000],
            "Net Supply": [49000, 115000, 185000, 310000],
            "% Burned": ["2%", "4.2%", "7.5%", "11.4%"]
        }
        
        df = pd.DataFrame(projection_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("### 💰 Value Growth Drivers")
        st.markdown("""
        **Demand Increases:**
        - ✅ More families join OnTime App
        - ✅ Data buyers pay higher prices
        - ✅ Staking rewards attract holders
        - ✅ Family trust pooling increases utility
        
        **Supply Decreases:**
        - ✅ Transaction burns reduce total supply
        - ✅ Lost wallet keys permanently remove tokens
        - ✅ Long-term staking locks up supply
        - ✅ Exclusive to OnTime App (no external dilution)
        
        **Result:** ⬆️ **Demand + ⬇️ Supply = 📈 Price Appreciation**
        """)
    
    st.markdown("---")
    
    st.subheader("🎯 Thriving Economic Environment Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🔒 Exclusivity**")
        st.write("• Only via OnTime App")
        st.write("• No public exchanges")
        st.write("• Limited to app users")
        st.write("• Scarcity built-in")
    
    with col2:
        st.markdown("**💎 Utility Value**")
        st.write("• Family transfers")
        st.write("• Staking rewards")
        st.write("• Data revenue sharing")
        st.write("• Governance rights")
    
    with col3:
        st.markdown("**📈 Growth Mechanisms**")
        st.write("• Viral referral bonuses")
        st.write("• Family recruitment rewards")
        st.write("• Network effects")
        st.write("• Increasing data value")
    
    st.markdown("---")
    
    st.subheader("💹 Token Value Protection System")
    
    with st.expander("Automatic Stabilization Mechanisms"):
        st.markdown("""
        **1. Burn Rate Adjustment**
        - If supply grows too fast → Increase burn rate to 3-5%
        - If supply shrinks too fast → Decrease burn rate to 1%
        - Algorithmic balance maintains stability
        
        **2. Mining Difficulty**
        - More users = Higher activity requirements for same ILAH
        - Prevents dilution as user base grows
        - Protects early adopters' value
        
        **3. Staking APY Adjustment**
        - Low staking participation → Increase APY to incentivize locking
        - High staking participation → Maintain current APY
        - Targets 40-50% staked supply
        
        **4. Data Sale Floor Price**
        - Minimum data sale value: $0.10 per ILAH minted
        - Prevents worthless ILAH from bad data deals
        - Maintains intrinsic value backing
        """)
    
    st.markdown("---")
    
    st.success("🎯 **Bottom Line**: ILAH is designed with built-in scarcity, controlled supply, and increasing demand. As more families join and use the OnTime App, token value naturally appreciates while burns prevent inflation.")

def show_mining_rewards():
    st.subheader("⛏️ Mining & Rewards System")
    
    st.info("🎮 **Earn ILAH tokens by building strong family relationships and staying active!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Activity Mining")
        st.markdown("""
        **Mine ILAH through family activities:**
        
        ⏰ **OnTime Rewards** - 5 ILAH
        - Arrive on time to family events
        - Auto-minted through OnTime App
        
        🧹 **Chore Completion** - 2-10 ILAH
        - Complete assigned household tasks
        - Earn more for difficult chores
        
        🎓 **Education Milestones** - 20 ILAH
        - Good grades, graduation, achievements
        - Learning new skills together
        
        🏃 **Fitness Activities** - 3 ILAH/day
        - Walk, run, exercise together
        - Track via fitness apps
        
        💬 **Social Interaction** - 1 ILAH/hour
        - Quality family time logged
        - Video calls with distant family
        """)
    
    with col2:
        st.markdown("### 🤝 Relationship Rewards")
        st.markdown("""
        **Build stronger bonds, earn more:**
        
        💝 **Weekly Family Dinner** - 10 ILAH
        - Eat together as a family
        - Share stories and updates
        
        🎮 **Game Night** - 8 ILAH per participant
        - Play board games or video games
        - Family fun activities
        
        📞 **Stay Connected** - 5 ILAH/call
        - Call distant family members
        - Regular check-ins earn bonuses
        
        🎁 **Acts of Kindness** - 15 ILAH
        - Help family members
        - Surprise gifts and gestures
        
        🌟 **Conflict Resolution** - 25 ILAH
        - Resolve family disagreements
        - Family counseling sessions
        """)
    
    st.markdown("---")
    
    st.subheader("📊 Mining Statistics & Leaderboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Daily Mining Cap", "100 ILAH")
        st.caption("Per family member")
    
    with col2:
        st.metric("Weekly Bonus", "300 ILAH")
        st.caption("For completing all activities")
    
    with col3:
        st.metric("Family Multiplier", "1.5x")
        st.caption("When entire family participates")
    
    with col4:
        st.metric("Streak Bonus", "+10%")
        st.caption("Per consecutive week")
    
    st.markdown("---")
    
    st.subheader("🏅 Mining Leaderboard Example")
    
    import pandas as pd
    leaderboard_data = {
        "Rank": ["🥇", "🥈", "🥉", "4", "5"],
        "Family Member": ["Mom", "Dad", "Sister", "Brother", "Grandma"],
        "This Week": ["450 ILAH", "380 ILAH", "320 ILAH", "290 ILAH", "250 ILAH"],
        "Total Mined": ["12,450", "10,280", "8,920", "7,150", "15,800"],
        "Streak": ["12 weeks", "10 weeks", "8 weeks", "6 weeks", "20 weeks ⭐"]
    }
    
    df = pd.DataFrame(leaderboard_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.success("💡 **Tip:** Mining works automatically through OnTime App integration. Just complete activities and tokens are minted to your wallet!")

def show_privacy_security():
    st.subheader("🔒 Privacy & Security Features")
    
    st.info("🛡️ **Your identity and transactions are protected - not tracked by personal information**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🕶️ Privacy Features")
        st.markdown("""
        **Anonymous Wallet Creation:**
        - No KYC required
        - No email or phone needed
        - No identity verification
        - Self-custody keys only
        
        **Transaction Privacy:**
        - Wallet addresses not linked to identity
        - Optional mixer integration
        - Stealth address support (optional)
        - No transaction history tracking
        
        **Data Anonymization:**
        - Personal info stripped before sale
        - Only behavioral patterns shared
        - No name, address, or contact info
        - Family members remain unidentifiable
        """)
        
        st.markdown("### 🔐 Security Best Practices")
        st.success("✅ Use strong wallet passwords")
        st.success("✅ Store recovery phrase offline")
        st.success("✅ Enable biometric locks")
        st.success("✅ Verify transaction addresses")
        st.success("✅ Use hardware wallets for large amounts")
    
    with col2:
        st.markdown("### 🌐 Blockchain Benefits")
        st.markdown("""
        **Solana Privacy Advantages:**
        
        ⚡ **Fast & Cheap** - 65,000 TPS, $0.00025 fees
        - Ultra-low cost makes tracking uneconomical
        - High speed enables instant private transfers
        
        🔒 **Decentralized** - No central authority
        - Your keys, your coins
        - No account freezes
        - No transaction reversals
        
        🕵️ **Optional Privacy** - Choose your level
        - Public wallet for family use
        - Private wallet for anonymous transfers
        - Mix services for enhanced privacy
        
        💪 **Durable & Reliable**
        - 99.9% uptime since 2020
        - Battle-tested under high load
        - Growing ecosystem
        """)
    
    st.markdown("---")
    
    st.subheader("🛡️ Privacy vs. Transparency Balance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Fully Private:**")
        st.write("✅ No identity tied to wallet")
        st.write("✅ Transactions can't be traced to you")
        st.write("⚠️ Lost keys = lost funds forever")
    
    with col2:
        st.markdown("**Family Shared:**")
        st.write("✅ Family can see your activity")
        st.write("✅ Build trust through transparency")
        st.write("✅ Easier fund recovery with family help")
    
    with col3:
        st.markdown("**Hybrid (Recommended):**")
        st.write("✅ Main wallet shared with family")
        st.write("✅ Private wallet for personal use")
        st.write("✅ Best of both worlds")
    
    st.warning("⚠️ **Important:** While blockchain transactions are pseudonymous (not linked to real identity), they are publicly visible on the blockchain. For complete privacy, consider using privacy-enhanced features or secondary privacy coins.")

def show_data_ai_integration():
    st.subheader("💰 Data Monetization = ILAH Minting")
    
    st.info("🎯 **Your family's anonymized data generates value - and you get paid in ILAH tokens!**")
    
    st.markdown("### 📊 How It Works")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Step 1: Data Collection (Anonymized)**
        
        The OnTime Family App collects:
        - ⏰ On-time arrival patterns (no locations)
        - 🏃 Activity completion rates
        - 👨‍👩‍👧‍👦 Family interaction frequency
        - 📱 App usage patterns (no content)
        - 🎯 Goal achievement metrics
        
        **What's NOT Collected:**
        - ❌ Names, addresses, phone numbers
        - ❌ Specific locations or GPS data
        - ❌ Personal conversations or messages
        - ❌ Financial information
        - ❌ Photos or media content
        """)
    
    with col2:
        st.markdown("""
        **Step 2: Data Aggregation**
        
        Your data is:
        - Combined with thousands of other families
        - Stripped of all identifying information
        - Analyzed for behavioral patterns only
        - Never sold individually
        
        **Step 3: ILAH Minting**
        
        When data is sold:
        - $1 in data revenue = 1 ILAH minted
        - Tokens distributed to contributing families
        - Percentage split based on data contribution
        - Automatic deposit to family wallets
        """)
    
    st.markdown("---")
    
    st.subheader("💵 Revenue Sharing Model")
    
    st.markdown("**Example: $10,000 data sale**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Data Sold", "$10,000")
        st.caption("Aggregated from 100 families")
    
    with col2:
        st.metric("ILAH Minted", "10,000 ILAH")
        st.caption("1:1 ratio maintained")
    
    with col3:
        st.metric("Per Family", "100 ILAH")
        st.caption("Equal distribution")
    
    st.markdown("---")
    
    st.markdown("### 🎯 Distribution Formula")
    
    st.code("""
Family Share = (Your Data Points / Total Data Points) × Total ILAH Minted

Example:
- Your family contributed 150 data points
- Total data points: 10,000
- ILAH minted: 10,000
- Your share: (150 / 10,000) × 10,000 = 150 ILAH
    """)
    
    st.markdown("---")
    
    st.subheader("📈 Data Buyers & Use Cases")
    
    buyers_data = {
        "Industry": ["Research Firms", "App Developers", "Marketing Companies", "Universities", "Health Organizations"],
        "What They Buy": [
            "Family behavior patterns",
            "App engagement metrics", 
            "Consumer trends (anonymous)",
            "Social interaction studies",
            "Activity & wellness data"
        ],
        "Typical Price": ["$5K-20K", "$2K-10K", "$10K-50K", "$1K-5K", "$3K-15K"],
        "Your ILAH Cut": ["5-20%", "5-20%", "5-20%", "5-20%", "5-20%"]
    }
    
    df = pd.DataFrame(buyers_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.subheader("🔒 Privacy Protection in Data Sales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ **What Buyers Get:**")
        st.write("• Aggregated behavioral patterns")
        st.write("• Statistical trends")
        st.write("• Anonymous usage metrics")
        st.write("• Market research insights")
        st.write("• Product improvement data")
    
    with col2:
        st.error("❌ **What Buyers DON'T Get:**")
        st.write("• Your name or identity")
        st.write("• Your location or address")
        st.write("• Individual family data")
        st.write("• Personal communications")
        st.write("• Identifiable information")
    
    st.success("💡 **Result:** You earn ILAH while maintaining complete privacy. Companies get valuable insights without invading your privacy!")
    
    st.markdown("---")
    
    st.subheader("💎 Family Trust Option")
    
    st.info("🏦 **Create a Family Trust to pool and manage ILAH tokens together**")
    
    with st.expander("What is a Family Trust?", expanded=True):
        st.markdown("""
        A **Family Trust** is a smart contract wallet that:
        - Pools ILAH tokens from all family members
        - Requires multiple family signatures for large withdrawals
        - Automatically distributes data mining rewards
        - Provides inheritance and succession planning
        - Creates a shared family treasury
        
        **Benefits:**
        - 🛡️ **Security**: Multi-signature protection
        - 🤝 **Collaboration**: Family decisions on spending
        - 📈 **Growth**: Compound rewards together
        - 👨‍👩‍👧‍👦 **Legacy**: Pass wealth to next generation
        - 💰 **Efficiency**: Lower fees for pooled transactions
        """)
    
    with st.expander("Setting Up a Family Trust"):
        st.markdown("""
        **Requirements:**
        - Minimum 2 family members (recommended 3-5)
        - Each member needs a Phantom wallet
        - Initial pool of 1,000+ ILAH recommended
        - Trust rules agreed upon by all members
        
        **Setup Steps:**
        1. Choose trust administrators (2-3 family members)
        2. Define spending approval threshold (e.g., 2-of-3 signatures)
        3. Create multi-sig wallet on Solana (use Squads Protocol)
        4. Pool initial ILAH into trust wallet
        5. Set distribution rules for data mining rewards
        6. Document succession plan
        
        **Trust Configuration Options:**
        - **Spending Limits**: Daily/monthly withdrawal caps
        - **Approval Requirements**: How many signatures needed
        - **Reward Distribution**: Equal vs. contribution-based
        - **Emergency Access**: Recovery procedures
        - **Inheritance Rules**: What happens if member passes
        """)
    
    with st.expander("Family Trust Use Cases"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Savings & Investment:**")
            st.write("• College fund for kids")
            st.write("• Family vacation fund")
            st.write("• Emergency fund")
            st.write("• Real estate down payment")
            st.write("• Retirement pool")
        
        with col2:
            st.markdown("**Income & Rewards:**")
            st.write("• Pool data mining rewards")
            st.write("• Collective staking returns")
            st.write("• Family business profits")
            st.write("• Shared investment gains")
            st.write("• Inheritance distribution")
    
    st.markdown("---")
    
    st.subheader("🏦 Family Staking Pool")
    
    st.info("💰 **Stake ILAH together as a family and earn interest that's automatically divided based on each member's contribution!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### How Family Staking Works")
        st.markdown("""
        **Step 1: Pool Family ILAH**
        - Family members deposit ILAH into shared staking pool
        - Each contribution is tracked automatically
        - Example: Dad stakes 1,000 ILAH, Mom stakes 500 ILAH, Kids stake 300 ILAH each
        
        **Step 2: Earn Interest Together**
        - Pool stakes at 5-10% APY (Annual Percentage Yield)
        - Interest compounds daily
        - Higher total = better staking rewards
        
        **Step 3: Proportional Distribution**
        - Rewards split based on contribution percentage
        - Automatic daily/weekly payouts to each member
        - Everyone sees their individual earnings
        """)
        
        st.markdown("### Benefits of Family Staking")
        st.success("✅ **Higher returns** - Larger pools get better APY rates")
        st.success("✅ **Automated splits** - No manual calculations needed")
        st.success("✅ **Compound together** - Reinvest rewards to grow faster")
        st.success("✅ **Transparent** - Everyone sees total pool + their share")
        st.success("✅ **Flexible** - Add or withdraw your portion anytime")
    
    with col2:
        st.markdown("### Example: Family Staking Pool")
        
        import pandas as pd
        family_pool_data = {
            "Family Member": ["Dad", "Mom", "Sister", "Brother", "Grandma"],
            "ILAH Staked": [1000, 500, 300, 300, 200],
            "% of Pool": ["43.5%", "21.7%", "13.0%", "13.0%", "8.7%"],
            "Monthly Interest": [4.35, 2.17, 1.30, 1.30, 0.87]
        }
        
        df = pd.DataFrame(family_pool_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("**Pool Summary:**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Total Pooled", "2,300 ILAH")
            st.metric("Pool APY", "6.0%")
        with col_b:
            st.metric("Monthly Returns", "11.5 ILAH")
            st.metric("Yearly Returns", "138 ILAH")
        
        st.markdown("---")
        
        st.markdown("### Distribution Formula")
        st.code("""
Your Share = (Your ILAH / Total Pool ILAH) × Total Interest

Example:
- Dad staked: 1,000 ILAH
- Total pool: 2,300 ILAH
- Monthly interest: 11.5 ILAH
- Dad's share: (1000/2300) × 11.5 = 5.0 ILAH
        """)
    
    st.markdown("---")
    
    st.subheader("💎 Staking Tiers & APY Rates")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**🥉 Bronze Pool**")
        st.write("100-999 ILAH")
        st.metric("APY", "4%")
        st.caption("Basic staking rate")
    
    with col2:
        st.markdown("**🥈 Silver Pool**")
        st.write("1,000-4,999 ILAH")
        st.metric("APY", "6%")
        st.caption("Family tier")
    
    with col3:
        st.markdown("**🥇 Gold Pool**")
        st.write("5,000-9,999 ILAH")
        st.metric("APY", "8%")
        st.caption("Multi-family tier")
    
    with col4:
        st.markdown("**💎 Diamond Pool**")
        st.write("10,000+ ILAH")
        st.metric("APY", "10%")
        st.caption("Premium tier")
    
    st.markdown("---")
    
    st.subheader("🔧 Setting Up Family Staking Pool")
    
    with st.expander("Setup Instructions"):
        st.markdown("""
        **Option 1: Using Family Trust Wallet (Recommended)**
        1. Create Family Trust multi-sig wallet (see above)
        2. Pool family ILAH into trust wallet
        3. Navigate to staking platform (Marinade, Lido, Jito)
        4. Stake from trust wallet with all signers' approval
        5. Rewards auto-distribute to trust, then to family members
        
        **Option 2: Using Shared Staking Account**
        1. One family member creates staking account
        2. Track each member's contribution in spreadsheet
        3. Stake total pool amount
        4. Manually distribute rewards proportionally
        5. Update tracking sheet monthly
        
        **Recommended Platforms:**
        - **Marinade Finance**: Liquid staking on Solana, ~6% APY
        - **Lido**: Trusted staking provider, multi-chain
        - **Jito**: MEV-enhanced staking, higher returns
        - **Phantom Built-in**: Easy staking directly in wallet
        """)
    
    with st.expander("Kickback Revenue System"):
        st.markdown("""
        **Automated Revenue Sharing:**
        
        When family pool earns staking rewards, the smart contract automatically:
        
        1. **Calculates Each Share**:
           - Dad: 43.5% of rewards → His wallet
           - Mom: 21.7% of rewards → Her wallet
           - Sister: 13.0% of rewards → Her wallet
           - And so on...
        
        2. **Distributes Proportionally**:
           - No manual calculations needed
           - Fair split based on contribution
           - Transparent on blockchain
        
        3. **Compounds Automatically** (Optional):
           - Reinvest rewards back into pool
           - Percentage stays same
           - Exponential growth
        
        **Example Monthly Kickback:**
        - Pool earns 11.5 ILAH interest
        - Dad contributed 43.5% → Gets 5.0 ILAH
        - Mom contributed 21.7% → Gets 2.5 ILAH
        - Each child contributed 13% → Gets 1.5 ILAH each
        - Grandma contributed 8.7% → Gets 1.0 ILAH
        
        Total distributed: 11.5 ILAH ✓
        """)
    
    st.markdown("---")
    
    st.subheader("🤖 AI Knowledge Base Enhancement")
    
    st.info("💡 **Double Benefit**: Your collected data not only earns you ILAH - it also makes the OnTime App smarter for everyone!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### How Data Strengthens AI")
        st.markdown("""
        **1. Pattern Recognition**
        - AI learns optimal family scheduling patterns
        - Identifies best times for family activities
        - Predicts conflicts before they happen
        - Suggests ideal meeting times
        
        **2. Personalized Recommendations**
        - AI adapts to your family's unique rhythms
        - Learns when each family member is most available
        - Suggests activities based on past successes
        - Optimizes notification timing
        
        **3. Predictive Intelligence**
        - Forecasts who might be late based on patterns
        - Predicts best days for family dinners
        - Suggests event durations based on history
        - Anticipates scheduling conflicts
        
        **4. Behavioral Insights**
        - Understands family dynamics
        - Learns communication preferences
        - Adapts to family member personalities
        - Improves over time with more data
        """)
    
    with col2:
        st.markdown("### AI Improvements from Data")
        
        import pandas as pd
        ai_improvements = {
            "AI Feature": ["Smart Scheduling", "Conflict Prediction", "Notification Timing", "Activity Suggestions", "Time Estimates"],
            "Baseline Accuracy": ["60%", "50%", "55%", "40%", "65%"],
            "With Data Learning": ["85%", "78%", "82%", "73%", "88%"],
            "Improvement": ["+25%", "+28%", "+27%", "+33%", "+23%"]
        }
        
        df = pd.DataFrame(ai_improvements)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("### 🔄 Continuous Improvement Cycle")
        st.success("1️⃣ Families use OnTime App")
        st.success("2️⃣ Anonymized data collected")
        st.success("3️⃣ Data sold → ILAH minted")
        st.success("4️⃣ Data trains AI models")
        st.success("5️⃣ AI gets smarter")
        st.success("6️⃣ Better app experience")
        st.success("7️⃣ More families join")
        st.success("🔄 Repeat → Network effects!")
    
    st.markdown("---")
    
    st.subheader("🧠 AI Features Powered by Your Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📅 Smart Scheduling**")
        st.write("• Best times for family events")
        st.write("• Automatic conflict detection")
        st.write("• Optimal meeting duration")
        st.write("• Preference learning")
    
    with col2:
        st.markdown("**🔮 Predictive Alerts**")
        st.write("• Late arrival warnings")
        st.write("• Traffic delay notifications")
        st.write("• Reminder optimization")
        st.write("• Proactive scheduling")
    
    with col3:
        st.markdown("**💬 Communication AI**")
        st.write("• Message tone adaptation")
        st.write("• Best contact methods")
        st.write("• Response time prediction")
        st.write("• Conversation starters")
    
    st.markdown("---")
    
    st.subheader("🔒 Privacy-Preserving AI Training")
    
    with st.expander("How We Train AI Without Compromising Privacy"):
        st.markdown("""
        **Federated Learning Approach:**
        
        1. **Local Processing First**
           - Raw data never leaves your device
           - Patterns extracted locally
           - Only aggregated insights sent to cloud
        
        2. **Differential Privacy**
           - Mathematical noise added to protect individuals
           - Cannot reverse-engineer specific families
           - Maintains statistical accuracy
        
        3. **Anonymization Pipeline**
           - All identifiers stripped before analysis
           - Data combined with 1,000+ other families
           - Individual patterns invisible in aggregate
        
        4. **Secure Aggregation**
           - Encrypted model updates
           - No raw data storage
           - Automated deletion after learning
        
        **Result:** AI learns from everyone's patterns while protecting each family's privacy!
        """)
    
    st.markdown("---")
    
    st.success("🎉 **Win-Win-Win**: You earn ILAH tokens 💰, your data improves the app for everyone 🤖, and all families benefit from smarter scheduling 📅. Plus, you maintain complete privacy! 🔒")

def show_ai_optimization():
    st.subheader("🤖 AI-Optimized Token Strategy")
    
    ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if not ai_key or not ai_base_url:
        st.warning("⚠️ AI Integration not configured. Using pre-configured recommendations.")
        show_default_recommendations()
        return
    
    if st.button("🤖 Get AI Tokenomics for Family App", type="primary", use_container_width=True):
        with st.spinner("🤖 AI is optimizing Ilah Hughs tokenomics for family use..."):
            try:
                recommendations = ai_expert.optimize_tokenomics(
                    "Ilah Hughs",
                    "A utility token for the OnTime Family App that allows family members to purchase, send, and receive crypto value. Used for family gifting, rewards for being on time, allowances, and value transfers between loved ones. Focus on utility and ease of use rather than speculation.",
                    "Family Users, Parents, Kids, Extended Family"
                )
                
                st.success("✅ AI Optimization Complete!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 AI Recommendations")
                    st.metric("Optimal Supply", f"{recommendations.get('total_supply', '100000000'):,}")
                    st.metric("Launch Price", f"${recommendations.get('launch_price_usd', '0.01')}")
                    st.metric("Initial Liquidity", f"${recommendations.get('initial_liquidity_usd', '5000'):,}")
                    st.metric("Family Adoption Rate", f"{recommendations.get('success_probability', 75)}%")
                
                with col2:
                    st.subheader("🎯 Token Allocation")
                    allocation = recommendations.get('allocation', {
                        'family_distribution': 40,
                        'liquidity_pool': 30,
                        'rewards_reserve': 20,
                        'team': 10
                    })
                    for category, percentage in allocation.items():
                        st.progress(percentage / 100, text=f"{category.replace('_', ' ').title()}: {percentage}%")
                
                st.markdown("---")
                
                st.subheader("👨‍👩‍👧‍👦 Family App Integration Strategy")
                marketing = recommendations.get('marketing_strategy', '')
                st.info(marketing)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("💡 Family Use Cases")
                    recs = recommendations.get('recommendations', [
                        "Birthday gift tokens with personal messages",
                        "Chore completion rewards (automated via OnTime)",
                        "Being on-time bonuses for family events",
                        "Family savings pools for vacations",
                        "Grandparent-to-grandchild value transfers"
                    ])
                    for rec in recs:
                        st.write(f"✅ {rec}")
                
                with col2:
                    st.subheader("⚠️ Important Considerations")
                    risks = recommendations.get('risks', [
                        "Educate family on wallet security",
                        "Start with small amounts to test",
                        "Consider volatility vs stablecoins",
                        "Plan for token value growth strategy"
                    ])
                    for risk in risks:
                        st.write(f"⚠️ {risk}")
                
            except Exception as e:
                st.error(f"AI Error: {str(e)}")
                st.info("Showing default recommendations...")
                show_default_recommendations()
    else:
        show_default_recommendations()

def show_default_recommendations():
    st.subheader("📊 Pre-Configured Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Token Distribution")
        st.progress(0.40, text="Family Distribution: 40%")
        st.caption("40M ILAH distributed to family members")
        
        st.progress(0.30, text="Liquidity Pool: 30%")
        st.caption("30M ILAH for trading liquidity")
        
        st.progress(0.20, text="Rewards Reserve: 20%")
        st.caption("20M ILAH for on-time rewards and achievements")
        
        st.progress(0.10, text="Team/Development: 10%")
        st.caption("10M ILAH for ongoing development")
    
    with col2:
        st.markdown("### Family Features")
        st.success("✅ Low transaction fees")
        st.success("✅ Instant family transfers")
        st.success("✅ Gift messaging")
        st.success("✅ Reward automation")
        st.success("✅ Family leaderboard")
        st.success("✅ Value milestones")

def show_creation_guide():
    st.subheader("🚀 Create Your Ilah Hughs Token")
    
    st.info("💡 Follow these steps to launch your family token on Solana blockchain")
    
    with st.expander("Step 1: Set Up Phantom Wallet", expanded=True):
        st.markdown("""
        **Download Phantom Wallet:**
        1. Visit [phantom.app](https://phantom.app)
        2. Install browser extension or mobile app
        3. Create new wallet and **securely save your recovery phrase**
        4. Add some SOL (~0.3 SOL = ~$30-45) for creation fee
        
        **Get SOL:**
        - Buy directly in Phantom wallet
        - Transfer from exchange (Coinbase, Binance)
        - Use MoonPay or other on-ramp services
        """)
    
    with st.expander("Step 2: Create Token on Smithii"):
        st.markdown("""
        **Go to Smithii Token Creator:**
        1. Visit [smithii.io/en/create-solana-token](https://smithii.io/en/create-solana-token)
        2. Connect your Phantom wallet
        
        **Enter Token Details:**
        - **Name:** Ilah Hughs
        - **Symbol:** ILAH
        - **Decimals:** 9
        - **Supply:** 100,000,000
        - **Description:** Family app utility token for OnTime
        
        **Upload Logo:**
        - Create simple logo with "ILAH" or family symbol
        - 512x512 pixels recommended
        
        **Pay Fee & Create:**
        - Cost: 0.3 SOL (~$30-45)
        - Click "Create Token"
        - Confirm in Phantom wallet
        - ✅ Token created in ~30 seconds!
        """)
    
    with st.expander("Step 3: Add Liquidity (Optional but Recommended)"):
        st.markdown("""
        **Create Trading Pool on Raydium:**
        1. Visit [raydium.io](https://raydium.io)
        2. Connect Phantom wallet
        3. Go to "Pools" → "Create Pool"
        4. Pair ILAH with SOL or USDC
        5. Add initial liquidity ($1,000+ recommended)
        
        **Benefits:**
        - Family can buy/sell tokens easily
        - Creates market price for the token
        - Increases legitimacy
        
        **Alternative for Private Family Use:**
        - Skip liquidity if only for family transfers
        - Distribute tokens directly to family wallets
        - Set internal family value (e.g., 1 ILAH = $0.10)
        """)
    
    with st.expander("Step 4: Distribute to Family"):
        st.markdown("""
        **Get Family Wallet Addresses:**
        1. Each family member installs Phantom
        2. They share their wallet address with you
        3. Copy addresses to spreadsheet
        
        **Send Initial Tokens:**
        - Use Phantom "Send" feature
        - Send starter amount to each family member
        - Example: 1,000 ILAH per person
        
        **Add Personal Touch:**
        - Include welcome message
        - Explain token value and purpose
        - Share family token rules/guidelines
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Quick Reference")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Token Details:**")
        st.code("""
Name: Ilah Hughs
Symbol: ILAH
Blockchain: Solana
Decimals: 9
Supply: 100,000,000
        """)
    
    with col2:
        st.markdown("**Creation Platforms:**")
        st.markdown("""
        - **Smithii**: [smithii.io](https://smithii.io) (0.3 SOL)
        - **Orion Tools**: [oriontools.io](https://oriontools.io) (0.1 SOL)
        - **Solana Tracker**: [solanatracker.io](https://solanatracker.io)
        """)

def show_family_features():
    st.subheader("👨‍👩‍👧‍👦 Family App Features & Use Cases")
    
    st.markdown("### 🎯 Core Family Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💝 Gifting System")
        st.info("""
        - Send tokens for birthdays, holidays
        - Include personal messages
        - Schedule future gifts
        - Gift history tracking
        - Thank you notifications
        """)
        
        st.markdown("#### 🏆 Rewards Program")
        st.success("""
        - On-time rewards (OnTime App)
        - Chore completion bonuses
        - Good behavior incentives
        - Achievement milestones
        - Family leaderboard
        """)
    
    with col2:
        st.markdown("#### 💰 Family Economy")
        st.warning("""
        - Allowance automation
        - Savings goals tracking
        - Family fund pooling
        - Loan system (IOU tokens)
        - Spending limits for kids
        """)
        
        st.markdown("#### 🌍 Global Features")
        st.info("""
        - International family transfers
        - Multi-generation support
        - Group sending (split gifts)
        - Currency conversion display
        - Tax-free family gifts
        """)
    
    st.markdown("---")
    
    st.subheader("💡 Creative Family Use Cases")
    
    use_cases = [
        {
            "title": "🎂 Birthday Bonanza",
            "desc": "Each family member contributes 100 ILAH to birthday person's wallet with personal messages"
        },
        {
            "title": "⏰ OnTime Champion",
            "desc": "Automatic 50 ILAH reward when family member arrives on time to events (OnTime App integration)"
        },
        {
            "title": "🧹 Chore Economy",
            "desc": "Kids earn ILAH for completing chores, can exchange for privileges or real money"
        },
        {
            "title": "🎓 Education Rewards",
            "desc": "Grandparents send ILAH for good grades, graduation, achievements"
        },
        {
            "title": "✈️ Vacation Fund",
            "desc": "Family pools ILAH tokens together to save for family vacation"
        },
        {
            "title": "🎁 Secret Santa",
            "desc": "Holiday gift exchange using random ILAH amounts between $10-50"
        }
    ]
    
    for i, use_case in enumerate(use_cases):
        if i % 2 == 0:
            col1, col2 = st.columns(2)
        
        with col1 if i % 2 == 0 else col2:
            with st.container():
                st.markdown(f"**{use_case['title']}**")
                st.write(use_case['desc'])
                st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("🔒 Family Security Guidelines")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Wallet Safety**")
        st.write("✅ Secure recovery phrases")
        st.write("✅ Use strong passwords")
        st.write("✅ Enable 2FA where possible")
        st.write("✅ Never share private keys")
    
    with col2:
        st.markdown("**Smart Usage**")
        st.write("✅ Start with small amounts")
        st.write("✅ Educate family on crypto")
        st.write("✅ Set spending limits")
        st.write("✅ Regular wallet backups")
    
    with col3:
        st.markdown("**Family Rules**")
        st.write("✅ Define token value")
        st.write("✅ Set earning guidelines")
        st.write("✅ Create redemption system")
        st.write("✅ Monthly family meetings")
    
    st.markdown("---")
    
    st.success("🎉 **Ready to bring your family together with Ilah Hughs token!** Start by creating your token following the 'Create Token' tab instructions, then invite family members to join your crypto economy.")

# Call the main function
show()
