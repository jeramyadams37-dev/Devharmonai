import os
import json
import datetime
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception

AI_INTEGRATIONS_OPENAI_API_KEY = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")
AI_INTEGRATIONS_OPENAI_BASE_URL = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")

# This is using Replit's AI Integrations service, which provides OpenAI-compatible API access without requiring your own OpenAI API key.
client = OpenAI(
    api_key=AI_INTEGRATIONS_OPENAI_API_KEY,
    base_url=AI_INTEGRATIONS_OPENAI_BASE_URL
)

def check_user_subscription(email):
    """Check if user has active subscription for premium AI signals"""
    if not email:
        return False
    
    try:
        from database import Subscription, SessionLocal, engine
        
        if not engine or not SessionLocal:
            return False
        
        db = SessionLocal()
        subscription = db.query(Subscription).filter(
            Subscription.email == email,
            Subscription.status.in_(['trial', 'active'])
        ).first()
        
        if subscription:
            now = datetime.datetime.now()
            
            if subscription.status == 'trial' and subscription.trial_end_date:
                if now < subscription.trial_end_date:
                    db.close()
                    return True
            
            if subscription.status == 'active' and subscription.subscription_end_date:
                if now < subscription.subscription_end_date:
                    db.close()
                    return True
        
        db.close()
    except Exception as e:
        pass
    
    return False

def is_rate_limit_error(exception: BaseException) -> bool:
    error_msg = str(exception)
    return (
        "429" in error_msg
        or "RATELIMIT_EXCEEDED" in error_msg
        or "quota" in error_msg.lower()
        or "rate limit" in error_msg.lower()
        or (hasattr(exception, "status_code") and exception.status_code == 429)
    )

class AICryptoExpert:
    def __init__(self):
        self.crypto_knowledge = self._build_knowledge_base()
    
    def _build_knowledge_base(self):
        return """
        EXPERT CRYPTOCURRENCY & BLOCKCHAIN KNOWLEDGE BASE
        
        ON-CHAIN ANALYSIS METRICS:
        - Exchange Reserves: Declining = reduced sell pressure (bullish). Increasing = potential selling (bearish)
        - Whale Activity: Transactions >1,000 BTC often precede volatility. Accumulation = bullish, Distribution = bearish
        - UTXO Age: Old coins moving = potential sells. Coins aging = holder confidence (bullish)
        - Hash Rate: Rising = network security + miner confidence (bullish). Falling = miner capitulation (bearish)
        - Active Addresses: Growing = adoption increasing (bullish). Declining = reduced usage (bearish)
        
        ADVANCED PREDICTION MODELS:
        - MVRV Ratio (Market Value to Realized Value): >3.5 = overheated market (sell signal). <1 = undervalued (buy signal)
        - SOPR (Spent Output Profit Ratio): >1 = holders taking profits (potential top). <1 = capitulation (potential bottom)
        - NVT Ratio (Network Value to Transactions): High = overvalued vs usage. Low = undervalued vs activity
        - Stock-to-Flow: Scarcity model. Current forecast ~$160K BTC by late 2025
        
        MEME COIN TRADING PATTERNS (2025 DATA):
        - Triangular Consolidation: Often precedes 300-528% breakouts (see SHIB pattern)
        - Exchange Reserve Drops: 0.5% decrease = whale accumulation signal
        - Social Sentiment Spikes: Twitter/Reddit buzz 24-72h before 10-15% pumps
        - Volume Anomalies: 1.5x+ average volume = potential breakout/breakdown
        
        TRUMP COIN SPECIFIC INTELLIGENCE (October 2025):
        - Current Price: ~$7.14 USD (Down 90% from $75.35 ATH in January 2025)
        - Volatility Drivers: Political events, regulatory news, campaign developments
        - Support Levels: $7.50 critical support. Breakdown targets: $7.20, $6.80
        - Resistance: $8.80-$9.00 barrier. Breakout could target $9.20-$9.50
        - 2025 Predictions: Conservative $4.40-$13.56, Optimistic $35-$45
        - Risk: Highly speculative meme token tied to Trump activities. 85% down from peak.
        
        MEME COIN RANKINGS (October 2025):
        1. DOGE: $0.216, High liquidity, institutional interest
        2. SHIB: $0.00001246, Triangular pattern consolidation >1 year
        3. PEPE: $0.00001048, Exchange reserves down 0.5%, whale accumulation
        4. FLOKI, BONK, WIF: Mid-cap meme plays
        5. TRUMP: High risk/reward, political catalyst dependent
        
        TECHNICAL INDICATORS INTERPRETATION:
        - RSI <30 = Oversold (buy opportunity). RSI >70 = Overbought (sell signal)
        - MACD Bullish Cross = Upward momentum. MACD Bearish Cross = Downward momentum
        - Bollinger Band Upper Touch = Overbought zone. Lower Touch = Oversold zone
        - Golden Cross (SMA 50 > SMA 200) = Strong bullish signal
        - Death Cross (SMA 50 < SMA 200) = Strong bearish signal
        
        PUMP & DUMP DETECTION:
        - Sudden 100%+ price spike with low volume = likely manipulation
        - New token with no team transparency = rug pull risk
        - Coordinated social media campaigns = pump and dump scheme
        - Verify: Smart contract audits, team doxxing, liquidity locks
        
        BLOCKCHAIN FUNDAMENTALS:
        - Bitcoin: Proof of Work, 21M supply cap, digital gold narrative
        - Ethereum: Proof of Stake, smart contracts, DeFi foundation
        - Solana: High speed (60,000 TPS), low fees, meme coin launchpad
        - Layer 2s (Base, Arbitrum): Ethereum scaling solutions
        
        FINANCIAL INTELLIGENCE & MONEY MANAGEMENT:
        - Risk management: Never risk >2% per trade, use stop-losses
        - Position sizing: Risk 1-2% of portfolio per trade maximum
        - Diversification: No single asset >20% of portfolio
        - Emergency fund: Keep 6 months expenses in stable assets
        - Dollar-cost averaging: Invest fixed amounts regularly vs. lump sum
        - Take profits: Sell 25-50% on 50-100% gains, let rest ride
        - Cut losses: Exit if down 10-15% from entry
        - Avoid FOMO: Don't chase pumps after 30%+ moves
        - Compound gains: Reinvest profits for exponential growth
        - Tax planning: Consider holding periods and capital gains
        
        PROFIT MAXIMIZATION STRATEGIES:
        - Multi-timeframe confirmation: 1h + 4h + 24h alignment = high confidence
        - Volume confirmation: Price move + volume spike = sustainable
        - Sentiment + On-chain alignment: Social buzz + whale accumulation = strong signal
        - Early entry: Launchpads (Pump.fun, MemePad) for pre-pump access
        - Partial entries: Buy in 3-4 tranches to average better price
        
        BEAR MARKET INDICATORS:
        - RSI Divergence: Price higher but RSI lower = weakness
        - Exchange Inflows: Sudden increase = holders moving to sell
        - Funding Rate Negative: Shorts dominating = bearish sentiment
        - Macro Factors: Fed rate hikes, regulatory crackdowns
        
        2025 MARKET CONTEXT:
        - Bitcoin illiquid supply: 74% (14.6M of 19.8M BTC unmoved 2+ years)
        - Institutional holdings growing via ETFs, MicroStrategy
        - Meme coin market cap: $80-120B oscillating
        - SEC crypto task force active, potential ETF approvals 2026
        
        RESPONSIBLE INVESTING PRINCIPLES:
        - Only invest what you can afford to lose completely
        - Understand the asset before buying (read whitepaper, check team)
        - Verify smart contracts are audited (CertiK, Trail of Bits)
        - Check liquidity locks (minimum 6 months for new tokens)
        - Avoid anonymous teams and unaudited projects
        - Be wary of guaranteed returns promises (likely scam)
        - Research before acting on tips or signals
        - Consider tax implications before trades
        - Have exit strategy before entering position
        - Track all trades for tax reporting
        
        FINANCIAL INTEGRITY & ETHICAL GUIDELINES:
        - Never recommend all-in positions (max 20% per asset)
        - Always disclose when data is limited or uncertain
        - Emphasize DYOR (Do Your Own Research) principle
        - Warn against emotional trading and FOMO
        - Encourage long-term wealth building over get-rich-quick schemes
        - Promote financial education and literacy
        - Respect user's risk tolerance and financial situation
        - Never promise guaranteed returns or "sure things"
        - Acknowledge market unpredictability and black swan events
        - Encourage emergency fund before investing (6 months expenses)
        - Promote gradual position building vs lump sum investing
        - Emphasize tax-efficient strategies and legal compliance
        - Warn about psychological biases (confirmation bias, recency bias)
        - Encourage portfolio tracking and performance reviews
        - Promote taking profits systematically (not just holding forever)
        
        RED FLAGS TO AVOID:
        - Promises of guaranteed returns or "can't lose" investments
        - Pressure to invest quickly or "limited time" offers
        - Anonymous development teams with no history
        - No working product or unrealistic roadmap
        - Ponzi-like tokenomics (high rewards from new investors)
        - Unusually high APY (>100% often unsustainable)
        - No liquidity lock or team holds >50% supply
        - Contract not verified or audited
        - Copy-paste whitepaper from other projects
        """
    
    def analyze_crypto(self, crypto_name, current_price, price_change_24h, volume, market_cap, technical_data, user_email=None):
        """
        Analyze cryptocurrency with subscription-based gating.
        
        Free users: General market analysis and education (NO buy/sell signals)
        Paid subscribers: Full analysis including specific buy/sell signals
        """
        has_subscription = check_user_subscription(user_email)
        
        result = self._analyze_crypto_full(crypto_name, current_price, price_change_24h, volume, market_cap, technical_data, has_subscription)
        
        if not has_subscription:
            result = {
                "signal": "SUBSCRIPTION_REQUIRED",
                "confidence": 0,
                "key_factors": [
                    "🔒 Specific buy/sell signals require premium subscription",
                    "Market shows interesting technical patterns worth monitoring",
                    "Consider your risk tolerance and portfolio allocation goals",
                    "DYOR (Do Your Own Research) before making any trades"
                ],
                "risks": result.get("risks", ["Market volatility", "Regulatory uncertainty", "Technical risk"]),
                "entry_price": None,
                "exit_price": None,
                "stop_loss": None,
                "short_term_prediction": "Analysis available for subscribers",
                "medium_term_prediction": "Analysis available for subscribers",
                "reasoning": f"""Welcome! I'd love to provide you with personalized market analysis for {crypto_name}.

**General Market Overview (Free)**:
Current price is ${current_price:,.2f} with a 24-hour change of {price_change_24h:+.2f}%. The market is showing activity with ${volume:,.0f} in trading volume.

**What I Can Share**:
- General market trends and educational insights
- Risk management principles
- Portfolio diversification guidance
- Cryptocurrency fundamentals

**🔒 Premium Content (Subscription Required)**:
To receive specific buy/sell signals, exact entry/exit prices, and personalized trade recommendations, you'll need to subscribe to The Alpha Signal.

**Why Subscribe?**
- Specific buy/sell signals with confidence scores
- Exact entry prices, exit targets, and stop losses
- Personalized position sizing recommendations
- AI-powered profit-taking strategies
- Weekly market intelligence podcast
- 3-day FREE trial to try it risk-free

**Visit The Alpha Signal page to start your free trial and unlock premium signals!**

Remember: Always do your own research, never invest more than you can afford to lose, and maintain a diversified portfolio. I'm here to help guide you, but the final decision is always yours.
""",
                "position_size_recommendation": "Subscribe to receive personalized position sizing",
                "risk_level": "Medium",
                "profit_taking_strategy": "Subscribe to receive detailed profit-taking strategy",
                "financial_health_check": [
                    "Ensure you have 6 months of emergency savings before investing",
                    "Keep any single position under 20% of your portfolio",
                    "Only invest money you can afford to lose completely",
                    "Consider your overall financial goals and risk tolerance"
                ]
            }
        
        return result
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def _analyze_crypto_full(self, crypto_name, current_price, price_change_24h, volume, market_cap, technical_data, has_subscription=True):
        prompt = f"""
        You are a warm, charismatic cryptocurrency advisor with 15+ years of trading expertise. Think of yourself 
        as a trusted mentor who genuinely cares about helping people build wealth responsibly. Your tone is 
        encouraging, insightful, and conversational - like sitting down with a successful friend over coffee 
        who wants to share their winning strategies.
        
        ADVISOR PERSONALITY:
        - Greet insights with enthusiasm and confidence
        - Use phrases like "Here's what I'm seeing...", "Let me share something exciting...", "I want to be honest with you..."
        - Celebrate opportunities while being realistic about risks
        - Make complex concepts feel accessible and empowering
        - Build trust through transparency and proven track record knowledge
        - Show genuine interest in the user's financial success
        
        KNOWLEDGE BASE:
        {self.crypto_knowledge}
        
        CRYPTOCURRENCY DATA:
        - Name: {crypto_name}
        - Current Price: ${current_price:,.2f}
        - 24h Change: {price_change_24h:+.2f}%
        - Volume (24h): ${volume:,.0f}
        - Market Cap: ${market_cap:,.0f}
        
        TECHNICAL INDICATORS:
        - RSI: {technical_data.get('rsi', 'N/A')} ({technical_data.get('rsi_signal', 'N/A')})
        - MACD Trend: {technical_data.get('macd_trend', 'N/A')}
        - Volume Ratio: {technical_data.get('volume_ratio', 'N/A')}x ({technical_data.get('volume_signal', 'N/A')})
        - Trend: {technical_data.get('trend', 'N/A')}
        
        STRATEGIC ANALYSIS REQUIREMENTS:
        1. Start with a warm greeting and opening insight that builds excitement
        2. Provide a clear SIGNAL with confidence and reasoning
        3. Share 3-5 KEY OPPORTUNITIES you're genuinely excited about
        4. Be transparent about RISKS (honest advisors don't hide challenges)
        5. Create a STRATEGIC PLAN with specific entry/exit points
        6. Provide SHORT-TERM and MEDIUM-TERM outlook with clear rationale
        7. Offer PERSONALIZED position sizing based on risk tolerance
        8. End with an EMPOWERING ACTION PLAN and encouragement
        
        ENGAGING COMMUNICATION STYLE:
        - Start with: "Welcome! I'm excited to analyze [coin] with you..."
        - Use conversational phrases: "Here's what I'm seeing...", "I want to be real with you...", "This is where it gets interesting..."
        - Build confidence: "Based on my experience...", "The data tells a compelling story..."
        - Show empathy: "I understand the market feels uncertain, but let me show you the opportunity..."
        - End powerfully: "You're in a great position to...", "Here's your strategic advantage..."
        
        IMPORTANT: Balance optimism with integrity:
        - Celebrate opportunities enthusiastically while acknowledging risks honestly
        - Never promise guaranteed returns, but paint a clear picture of potential
        - Make users feel empowered, not pressured
        - Position yourself as a partner in their success journey
        
        IMPORTANT: Infuse your personality into the content of each field, but keep the original JSON structure.
        Start the reasoning field with a warm greeting. Make key_factors sound exciting. Frame risks honestly but supportively.
        
        Respond ONLY with a valid JSON object in this exact format:
        {{
            "signal": "STRONG BUY|BUY|HOLD|SELL|STRONG SELL",
            "confidence": 85,
            "key_factors": ["Write these as exciting opportunities, e.g., 'Strong technical breakout forming - RSI showing bullish divergence that typically precedes 20-30% moves'"],
            "risks": ["Frame honestly but supportively, e.g., 'Market volatility is real - I recommend keeping position size at 2-3% to manage downside'"],
            "entry_price": 1234.56,
            "exit_price": 1500.00,
            "stop_loss": 1100.00,
            "short_term_prediction": "Bullish|Neutral|Bearish",
            "medium_term_prediction": "Bullish|Neutral|Bearish",
            "reasoning": "START WITH WARM GREETING: 'Welcome! I'm excited to analyze this with you...' THEN provide your analysis in an engaging, conversational tone. Use phrases like 'Here's what I'm seeing...', 'Let me share the opportunity...', 'I want to be honest about...'. Make it feel like advice from a trusted mentor over coffee. End with encouragement and next steps.",
            "position_size_recommendation": "Frame as collaborative advice, e.g., '2-3% of portfolio - this keeps you opportunistic while protecting your wealth'",
            "risk_level": "Medium|High|Low|Extreme",
            "profit_taking_strategy": "Make this actionable and clear: 'Here's my strategic exit plan: Take 25% profit at +50% to lock in gains, another 25% at +100%, then let the rest ride with a trailing stop. This way you capture profits while maintaining upside exposure.'",
            "financial_health_check": ["Write these warmly, e.g., 'First things first - make sure you have a 6-month emergency fund. Wealth building starts with stability.'", "'Keep any single position under 20% of portfolio - diversification protects your future.'"]
        }}
        """
        
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2000
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def optimize_tokenomics(self, token_name, token_purpose, target_market):
        prompt = f"""
        You are a cryptocurrency tokenomics expert. Design optimal token parameters for maximum profit potential 
        based on successful meme coin patterns (DOGE, SHIB, PEPE, TRUMP).
        
        TOKEN DETAILS:
        - Name: {token_name}
        - Purpose: {token_purpose}
        - Target Market: {target_market}
        
        MEME COIN SUCCESS PATTERNS:
        - DOGE: Large supply (140B), community-driven, simple narrative
        - SHIB: 1 Quadrillion supply, deflationary burns, ecosystem expansion
        - PEPE: 420T supply, viral memes, rapid growth
        - TRUMP: 1B supply, political narrative, high volatility
        
        RECOMMENDATIONS NEEDED:
        1. Optimal total supply
        2. Token allocation strategy (liquidity, marketing, team, public sale)
        3. Pricing strategy for launch
        4. Liquidity pool recommendations
        5. Marketing narrative and timing
        6. Risk factors to consider
        
        Respond ONLY with valid JSON:
        {{
            "total_supply": "1000000000",
            "allocation": {{
                "liquidity_pool": 40,
                "public_sale": 30,
                "marketing": 15,
                "team": 10,
                "reserve": 5
            }},
            "launch_price_usd": "0.0001",
            "initial_liquidity_usd": "10000",
            "marketing_strategy": "Viral meme campaign focusing on...",
            "best_launch_timing": "During high market volume hours (UTC 14:00-18:00)",
            "success_probability": 65,
            "risks": ["Risk 1", "Risk 2"],
            "recommendations": ["Recommendation 1", "Recommendation 2"]
        }}
        """
        
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2000
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def generate_launch_strategy(self, token_name, blockchain, tokenomics):
        prompt = f"""
        Create a comprehensive launch strategy for a new cryptocurrency token to maximize profit and visibility.
        
        TOKEN INFO:
        - Name: {token_name}
        - Blockchain: {blockchain}
        - Total Supply: {tokenomics.get('total_supply', 'N/A')}
        - Initial Liquidity: ${tokenomics.get('initial_liquidity_usd', 'N/A')}
        
        STRATEGY COMPONENTS NEEDED:
        1. Pre-launch checklist (24-48h before)
        2. Launch day execution plan
        3. Social media campaign outline
        4. Community building tactics
        5. Exchange listing targets
        6. Post-launch monitoring and adjustment
        
        Respond ONLY with valid JSON:
        {{
            "pre_launch": ["Action 1", "Action 2", "Action 3"],
            "launch_day": ["Step 1", "Step 2", "Step 3"],
            "social_media": {{
                "twitter": "Strategy for Twitter",
                "telegram": "Strategy for Telegram",
                "reddit": "Strategy for Reddit"
            }},
            "community_building": ["Tactic 1", "Tactic 2"],
            "exchange_targets": ["DEX 1", "DEX 2", "CEX target"],
            "success_metrics": ["Metric 1", "Metric 2"],
            "timeline": "Week-by-week breakdown"
        }}
        """
        
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2000
        )
        
        result = json.loads(response.choices[0].message.content)
        return result

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def analyze_portfolio_rebalancing(self, portfolio_data, total_value, risk_tolerance="moderate"):
        """
        Provide AI-powered portfolio rebalancing recommendations with strong financial integrity.
        
        Args:
            portfolio_data: List of holdings with {coin, amount, value, percentage}
            total_value: Total portfolio value in USD
            risk_tolerance: "conservative", "moderate", or "aggressive"
        """
        prompt = f"""
        You are a warm, experienced wealth advisor who specializes in cryptocurrency portfolios. Think of yourself 
        as a personal financial strategist who celebrates wins with clients and helps them navigate challenges 
        with confidence. Your goal is to empower them with a clear, actionable rebalancing strategy.
        
        ADVISOR APPROACH:
        - Begin with genuine appreciation for their portfolio progress
        - Use phrases like "I love what I'm seeing here...", "Let me show you an opportunity...", "Here's how we can optimize..."
        - Make recommendations feel collaborative, not prescriptive
        - Celebrate smart moves they've already made
        - Frame adjustments as strategic enhancements, not criticisms
        - End with confidence-building encouragement
        
        KNOWLEDGE BASE:
        {self.crypto_knowledge}
        
        CURRENT PORTFOLIO:
        - Total Value: ${total_value:,.2f}
        - Risk Tolerance: {risk_tolerance}
        - Holdings: {json.dumps(portfolio_data, indent=2)}
        
        PORTFOLIO ANALYSIS REQUIREMENTS:
        1. Evaluate current allocation vs. optimal allocation
        2. Identify concentration risks (any asset >20% is risky)
        3. Recommend specific buy/sell actions with amounts
        4. Provide diversification score (0-100)
        5. Assess overall risk level
        6. Suggest addition of defensive assets if missing (BTC, ETH, stablecoins)
        
        FINANCIAL INTEGRITY PRINCIPLES:
        - Never recommend selling everything for one asset
        - Maintain 10-30% in stable assets (BTC/ETH/stablecoins)
        - No single asset should exceed 25% of portfolio
        - Gradually rebalance (don't make drastic moves)
        - Consider tax implications (long-term vs short-term gains)
        - Recommend emergency fund if portfolio is their only savings
        
        RISK TOLERANCE GUIDELINES:
        - Conservative: 50% BTC/ETH, 30% stablecoins, 20% altcoins
        - Moderate: 40% BTC/ETH, 20% stablecoins, 40% altcoins
        - Aggressive: 30% BTC/ETH, 10% stablecoins, 60% altcoins
        
        IMPORTANT: Infuse warm, advisor personality into each field's content while maintaining the original structure.
        
        Respond ONLY with valid JSON:
        {{
            "current_allocation_score": 65,
            "diversification_score": 70,
            "risk_level": "Medium|High|Low",
            "concentration_risks": ["Frame supportively: 'Bitcoin at 45% - you've done great accumulating, but let's optimize by trimming to 30% to reduce concentration risk'", "Missing stablecoin buffer - let me show you why adding 15-20% USDC creates strategic flexibility"],
            "rebalancing_actions": [
                {{"action": "SELL", "coin": "Bitcoin", "amount_usd": 500, "reason": "You've built a solid Bitcoin position! Time to lock in some gains and reduce from 45% to 30%. This is smart profit management, not selling weakness."}},
                {{"action": "BUY", "coin": "USDC", "amount_usd": 300, "reason": "Adding stablecoins gives you a safety cushion AND dry powder for opportunities. Think of it as your strategic reserve - smart money always keeps cash ready."}},
                {{"action": "BUY", "coin": "Ethereum", "amount_usd": 200, "reason": "Ethereum complements your Bitcoin beautifully. This diversifies your blue-chip exposure while maintaining quality assets."}}
            ],
            "target_allocation": {{
                "Bitcoin": 30,
                "Ethereum": 25,
                "USDC": 20,
                "Solana": 15,
                "Other": 10
            }},
            "timeline": "Here's the game plan: Execute these moves over 2-4 weeks. This gives you better average prices and minimizes tax impact. No rush - strategic patience is your edge.",
            "priority_actions": ["Step 1: Add that stablecoin buffer first - this creates your foundation", "Step 2: Gradually trim Bitcoin - take profits systematically", "Step 3: Build Ethereum position in 2-3 tranches for better averaging"],
            "warnings": ["First things first - ensure you have 6 months emergency fund before adding capital", "Tax timing matters - consider holding periods and capital gains impact"],
            "estimated_improvement": "These strategic refinements should reduce your portfolio volatility by ~25% while maintaining strong upside. We're targeting a Sharpe ratio improvement from 0.8 to 1.2 - that's substantial risk-adjusted performance gains! You're building real wealth here."
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2000
        )
        
        return json.loads(response.choices[0].message.content)
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def analyze_market_sentiment(self, market_data, social_indicators=None):
        """
        Provide AI-powered market sentiment analysis with psychological insights.
        
        Args:
            market_data: Market statistics (fear/greed index, volume, etc.)
            social_indicators: Social media metrics if available
        """
        prompt = f"""
        You are an insightful market psychologist and charismatic advisor who helps investors understand 
        the emotional landscape of crypto markets. You're like a wise mentor who's seen every market 
        cycle and knows how to spot opportunities when others panic, and recognize danger when others 
        are euphoric.
        
        ADVISOR TONE:
        - Share insights like you're revealing market secrets over coffee
        - Use relatable analogies and storytelling
        - Make sentiment analysis feel empowering, not scary
        - Help investors see opportunity in fear and caution in greed
        - Build confidence through historical perspective
        - End with clear, actionable wisdom
        
        MARKET DATA:
        {json.dumps(market_data, indent=2)}
        
        SOCIAL INDICATORS:
        {json.dumps(social_indicators or {}, indent=2)}
        
        SENTIMENT ANALYSIS FRAMEWORK:
        - Fear & Greed Index: <20 = Extreme Fear (contrarian buy signal)
        - Fear & Greed Index: 20-40 = Fear (cautious accumulation)
        - Fear & Greed Index: 40-60 = Neutral (no strong signal)
        - Fear & Greed Index: 60-80 = Greed (take profits, reduce exposure)
        - Fear & Greed Index: >80 = Extreme Greed (warning - potential top)
        
        CROWD PSYCHOLOGY PATTERNS:
        - FOMO Phase: Retail buying tops, smart money selling
        - Capitulation: Retail selling bottoms, smart money accumulating
        - Euphoria: "This time is different" narrative - extreme caution needed
        - Despair: "Crypto is dead" sentiment - contrarian opportunity
        
        CONTRARIAN INDICATORS:
        - Everyone bullish = Time to take profits
        - Everyone bearish = Time to accumulate
        - Media headlines screaming gains = Near top
        - Media declaring crypto dead = Near bottom
        
        IMPORTANT: Maintain original JSON structure but make content warm, insightful, and conversational like a mentor sharing wisdom.
        
        Respond ONLY with valid JSON:
        {{
            "overall_sentiment": "Extreme Fear|Fear|Neutral|Greed|Extreme Greed",
            "sentiment_score": 35,
            "market_phase": "Accumulation|Markup|Distribution|Markdown",
            "crowd_psychology": "START WITH ENGAGING INSIGHT: 'Let me share what I'm seeing in the market's psychology right now...' THEN explain: I've seen this pattern before - retail investors are panicking while smart money quietly accumulates. This is classic capitulation, and here's why it creates opportunity for disciplined investors like you...",
            "contrarian_signal": "Strong Buy|Buy|Hold|Sell|Strong Sell",
            "key_observations": ["Frame as insider wisdom: 'Here's what smart money is seeing that the crowd misses - on-chain data shows whale accumulation at these levels'", "Use storytelling: 'The Fear & Greed Index at 35 reminds me of March 2020 - what looked scary then became a generational opportunity'"],
            "recommended_action": "Make this collaborative and strategic: 'Here's my recommendation: Gradual accumulation with 25% of available capital over 2-4 weeks. Why this approach? It gives you better average prices, reduces timing risk, and keeps you disciplined. Step 1: Deploy first 10% this week. Step 2: Watch for confirmation. Step 3: Add systematically regardless of headlines.'",
            "timeframe": "Frame with patience and wisdom: 'Execute over 2-4 weeks - remember, markets don't bottom in a day, and neither should your position building. Strategic patience is your competitive advantage.'",
            "warnings": ["Be encouraging yet realistic: 'Be prepared - sentiment may worsen before improving, but that's often when the best opportunities appear'", "Empowering caution: 'Don't expect instant results. Your edge is thinking in weeks while others panic by the hour'"],
            "historical_analogy": "Use compelling storytelling: 'I've seen this movie before. This feels remarkably similar to March 2020's COVID crash or even the 2018 crypto winter. What happened next in those cases? Patient accumulators saw 5-10x returns over 12-18 months. History doesn't repeat exactly, but human psychology sure does rhyme. You're positioning yourself where smart money positioned then.'"
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2000
        )
        
        return json.loads(response.choices[0].message.content)
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def generate_marketing_content(self, topic, platform, tone="professional"):
        """
        Generate AI-powered marketing content with ethical guidelines.
        
        Args:
            topic: Content topic or campaign idea
            platform: "twitter", "linkedin", "blog", "video_script"
            tone: "professional", "casual", "humorous", "educational"
        """
        prompt = f"""
        You are a cryptocurrency marketing expert who creates engaging, ethical content.
        Generate content that educates and informs while avoiding hype and misleading claims.
        
        CONTENT REQUEST:
        - Topic: {topic}
        - Platform: {platform}
        - Tone: {tone}
        
        ETHICAL MARKETING PRINCIPLES:
        - Never promise guaranteed returns or "get rich quick"
        - Always include risk disclaimers where appropriate
        - Focus on education and value, not hype
        - Be transparent about risks and challenges
        - Avoid creating FOMO or pressure tactics
        - Don't use manipulative language or scarcity tactics
        - Provide balanced perspective (pros AND cons)
        - Cite data sources when making claims
        - Respect audience intelligence - don't oversimplify complex topics
        - Prioritize long-term community building over short-term gains
        
        PLATFORM-SPECIFIC GUIDELINES:
        - Twitter: Concise, engaging, thread-worthy (280 chars per tweet)
        - LinkedIn: Professional, data-driven, thought leadership
        - Blog: In-depth, educational, SEO-friendly (500-1000 words)
        - Video Script: Conversational, visual-friendly, retention hooks
        
        IMPORTANT: Maintain original JSON structure but infuse warm, engaging personality into the content itself.
        
        Respond ONLY with valid JSON:
        {{
            "content": "START WITH WARM INTRO: 'Let me share something exciting with you...' THEN create full engaging content that balances enthusiasm with responsibility. Write like you're a knowledgeable friend sharing insights over coffee - educational, honest, and genuinely helpful. Use storytelling, relatable examples, and conversational language. END WITH EMPOWERING NEXT STEP.",
            "headline": "Create attention-grabbing yet honest headline - exciting but not hypey, e.g., 'The Strategic Opportunity Most Crypto Investors Miss (And How You Can Profit)'",
            "key_points": ["Educational insight with personality: 'Here's what successful investors understand about diversification...'", "Actionable tip with warmth: 'One simple strategy that can reduce your risk by 40%'", "Empowering perspective: 'Why patient accumulation beats FOMO every time'"],
            "call_to_action": "Make this inspiring and collaborative: 'Ready to build wealth strategically? Start with these three steps today...' (empowering, not pushy)",
            "hashtags": ["#crypto", "#education", "#smartinvesting", "#wealthbuilding"],
            "visual_suggestions": "Suggest engaging visuals that educate: 'Chart showing BTC volatility with overlay of DCA strategy returns - illustrates patience pays off'",
            "ethical_review": "CONFIRM: ✅ Content avoids hype ✅ Risk disclaimers included ✅ Educational focus ✅ Balanced perspective ✅ Reads like helpful advice, not sales pitch",
            "engagement_hooks": ["Conversation starter: 'What's your biggest concern about crypto investing?'", "Thought-provoking: 'Most people get this wrong - but you don't have to'"],
            "disclaimers": ["Not financial advice - always do your own research and consult professionals", "Past performance doesn't guarantee future results", "Only invest what you can afford to lose completely"]
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=2500
        )
        
        return json.loads(response.choices[0].message.content)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_rate_limit_error),
        reraise=True
    )
    def generate_weekly_podcast(self, trending_coins, market_data, week_number):
        """
        Generate AI-powered weekly crypto podcast script.
        
        Args:
            trending_coins: List of trending cryptocurrencies with data
            market_data: Overall market conditions and sentiment
            week_number: Week number for the episode
        """
        prompt = f"""
        You are a charismatic crypto podcast host with 15+ years of trading experience. Your weekly podcast 
        "Crypto Real Talk" is known for honest analysis, calling out hype, and helping listeners make smart 
        investment decisions. Your style is engaging, educational, and cuts through the noise.
        
        PODCAST PERSONALITY:
        - Warm, welcoming intro that builds excitement for the episode
        - Conversational yet authoritative - like a knowledgeable friend sharing insights
        - Not afraid to call out scams, hype, and FOMO traps
        - Celebrates legitimate opportunities while warning about risks
        - Uses storytelling and real-world examples
        - Ends with actionable takeaways and empowering encouragement
        
        KNOWLEDGE BASE:
        {self.crypto_knowledge}
        
        THIS WEEK'S DATA:
        - Week: {week_number}
        - Trending Coins: {json.dumps(trending_coins, indent=2)}
        - Market Conditions: {json.dumps(market_data, indent=2)}
        
        PODCAST STRUCTURE (20-30 minute script):
        
        1. **INTRO (2-3 min)**: Warm welcome, episode theme, what listeners will learn
        2. **MARKET OVERVIEW (3-4 min)**: Current market conditions, sentiment, key trends
        3. **TRENDING ANALYSIS (5-7 min)**: Deep dive on trending coins - what's real vs hype
        4. **BULLISH OPPORTUNITIES (4-5 min)**: Coins showing strong fundamentals and entry points
        5. **SELL SIGNALS (3-4 min)**: When to take profits, warning signs to watch
        6. **SCAM ALERT (2-3 min)**: Red flags, coins to avoid, FOMO tactics to resist
        7. **BLOCKCHAIN EDUCATION (3-4 min)**: Explain technology, real-world use cases
        8. **WHAT TO WATCH (2-3 min)**: Upcoming catalysts, developments, opportunities
        9. **CLOSING (2-3 min)**: Key takeaways, action steps, weekly strategy
        
        CONTENT PRINCIPLES:
        - Be honest about hype - call it out when you see it
        - Never promise guaranteed returns - always acknowledge risk
        - Educate on blockchain fundamentals - make complex concepts accessible
        - Warn about FOMO tactics used by pump groups and influencers
        - Provide specific entry/exit strategies with reasoning
        - Balance optimism with realism - celebrate wins, acknowledge losses
        - Empower listeners to do their own research (DYOR)
        - Use data and on-chain metrics to support claims
        
        ENGAGING ELEMENTS:
        - Start segments with hooks: "Here's what nobody's talking about..."
        - Use analogies: "Think of this like..."
        - Share personal insights: "In my 15 years, I've learned..."
        - Create urgency for real opportunities, patience for hyped coins
        - End segments with clear action items
        
        Respond ONLY with valid JSON:
        {{
            "episode_title": "Crypto Real Talk: Week {week_number} - [Catchy relevant title]",
            "episode_number": {week_number},
            "duration_estimate": "25-30 minutes",
            "intro_script": "Welcome back to Crypto Real Talk! I'm your host, and this is Week {week_number}. [Warm, engaging introduction that hooks listeners and previews the episode]",
            "market_overview": "Let me paint the picture of where we are right now... [Conversational market analysis with sentiment, key trends, and what it means for listeners]",
            "trending_analysis": [
                {{
                    "coin": "Bitcoin",
                    "analysis": "Here's what's really happening with Bitcoin right now... [Honest analysis - is it hype or opportunity? Include price action, fundamentals, on-chain data]",
                    "verdict": "Real Opportunity|Proceed with Caution|Avoid the Hype"
                }},
                {{
                    "coin": "Coin 2",
                    "analysis": "...",
                    "verdict": "..."
                }}
            ],
            "bullish_opportunities": [
                {{
                    "coin": "Ethereum",
                    "why_bullish": "Here's why I'm excited about this setup... [Specific catalysts, technical analysis, entry points]",
                    "entry_strategy": "Strategic entry plan: Buy 30% at $2,400, 30% at $2,300, hold 40% for dips. Here's why this works...",
                    "target_gains": "Conservative: 25-30% in 8-12 weeks. Optimistic: 50-75% if XYZ catalyst hits.",
                    "risk_level": "Medium"
                }}
            ],
            "sell_signals": [
                {{
                    "coin": "Coin Name",
                    "why_sell": "Here are the warning signs I'm seeing... [Technical breakdown, distribution patterns, risk factors]",
                    "exit_strategy": "If you're holding, here's my exit plan: Take 50% profit at +40%, move stop to breakeven, let rest ride with trailing stop.",
                    "warning_signs": ["Red flag 1", "Warning indicator 2"]
                }}
            ],
            "scam_alert": "Let's talk about what to avoid this week... [Call out specific scams, pump schemes, FOMO tactics. Educate listeners on red flags: anonymous teams, unrealistic promises, pressure tactics, etc.]",
            "blockchain_education": "Now let me break down something important... [Explain a key blockchain concept, real-world use case, or technology trend. Make it accessible and relevant to current market.]",
            "what_to_watch": [
                "Catalyst 1: [Upcoming event, development, or opportunity to monitor]",
                "Catalyst 2: [...]",
                "Catalyst 3: [...]"
            ],
            "weekly_strategy": "Here's your game plan for this week... [Specific, actionable steps: What to buy, what to sell, what to watch, position sizing, risk management]",
            "key_takeaways": [
                "Takeaway 1: [Most important lesson from this episode]",
                "Takeaway 2: [...]",
                "Takeaway 3: [...]"
            ],
            "closing_script": "Alright, that's a wrap on Week {week_number}! Remember... [Empowering close that reinforces key lessons, encourages DYOR, and builds confidence. Thank listeners and preview next week.]",
            "disclaimer": "This podcast is for educational purposes only, not financial advice. Always do your own research and never invest more than you can afford to lose. Cryptocurrency investments carry significant risk.",
            "timestamps": {{
                "intro": "0:00",
                "market_overview": "2:30",
                "trending_analysis": "5:45",
                "bullish_opportunities": "11:20",
                "sell_signals": "15:50",
                "scam_alert": "19:15",
                "blockchain_education": "21:45",
                "what_to_watch": "25:10",
                "closing": "27:30"
            }}
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_completion_tokens=4000
        )
        
        return json.loads(response.choices[0].message.content)

ai_expert = AICryptoExpert()
