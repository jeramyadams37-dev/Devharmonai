# AI Crypto Empire Builder

## Overview
The AI Crypto Empire Builder is a Streamlit-based platform designed for cryptocurrency analysis, market tracking, and token creation. It offers real-time market data, AI-driven insights, and tools for managing crypto portfolios and generating marketing content. The project aims to provide a comprehensive suite for users to navigate and capitalize on the cryptocurrency market, leveraging AI for predictive analysis and strategic decision-making.

## User Preferences
Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend
The application uses Streamlit for its UI, providing a multi-page interface with custom CSS for a modern, responsive design. Key pages include:
-   **Home**: Project overview with OnTime Family Planning App promotional banner.
-   **My Wallet**: Portfolio tracking, profit/loss, and AI rebalancing.
-   **Crypto Exchange**: Full trading platform with 0.25% fees, buy/sell interface, order book, and trading history.
-   **Revenue Dashboard**: Platform monetization tracking showing exchange fees, subscription revenue, data sales, and cost breakdown.
-   **Watchlist**: Custom crypto tracking with AI analysis.
-   **Trading Signals**: Saved AI signals with export functionality.
-   **Backtesting**: AI prediction accuracy and hypothetical returns.
-   **Sentiment Analysis**: Market mood tracking.
-   **Marketing**: AI-powered viral content generation.
-   **The Alpha Signal**: Premium weekly podcast hosted by Marcus Sterling (AI persona). Subscription-based ($9.99/week or $99/year, 3-day free trial). Free previews available, full episodes require paid membership. Delivers exclusive market intelligence, buy/sell signals, and scam alerts.
-   **Market Dashboard**: Real-time market data and technical analysis.
-   **AI Analysis**: AI predictions and market insights.
-   **Token Creator/Manager**: Tools for token configuration, launch, and post-launch growth.
-   **Trending & Alerts**: Volume-based alerts and trending coin detection.
-   **Staking**: Staking rewards tracking and management.
-   **Ilah Hughs Token**: A privacy-first, anti-inflationary token with family staking and AI knowledge base integration, exclusive to the OnTime Family App.

### Monetization & Platform Sustainability
The platform generates revenue through multiple streams to cover operational costs and remain FREE for all users:
-   **Exchange Trading Fees**: 0.25% per trade (industry-leading low fee), projected $75K/month at current volume
-   **Premium Subscriptions**: 
    -   Basic (FREE): Core features, 5 AI predictions/day
    -   Pro ($9.99/mo): Unlimited AI predictions, advanced indicators, priority support
    -   Elite ($29.99/mo): AI portfolio manager, backtesting, API access, white-glove support
-   **Data Sales**: Anonymized data from OnTime app users sold to researchers ($23.5K/month projected)
-   **Operating Costs**: $42.5K/month (cloud hosting, AI APIs, databases, development)
-   **Profit Margin**: 51.3% projected, reinvested in features and improvements
-   **Self-Sustainability**: Platform generates 205% of operating costs, ensuring long-term viability

### Backend
The backend is structured around several core components:
-   **CryptoDataFetcher**: Manages CoinGecko API interactions with a 60-second in-memory cache to optimize API calls and ensure data freshness.
-   **TechnicalAnalyzer**: Utilizes `pandas_ta` to calculate various technical indicators (RSI, MACD, Bollinger Bands).
-   **AICryptoExpert**: Provides AI-powered analysis, predictions, and financial intelligence using structured prompt engineering and an embedded knowledge base. It includes retry logic for API resilience.
-   **DatabaseManager**: Handles PostgreSQL database connections and schema management using SQLAlchemy.
-   **WalletManager**: Manages portfolio, watchlist, and trading signal data, integrating with the database and CoinGecko API for real-time valuations.

### AI Integration
The platform integrates with Replit AI Integrations (OpenAI-compatible API) using GPT-5 for its AI capabilities. The AI embodies a **warm, charismatic advisor personality** that exemplifies trade knowledge and profitability while engaging users in strategic planning. This setup uses environment variables for authentication and features robust error handling and retry mechanisms.

**AI Advisor Personality:**
-   **Welcoming Presence**: Greets users warmly and builds rapport through conversational, mentor-like communication
-   **Trade Expertise**: 15+ years of trading knowledge embedded in responses, sharing insights like a trusted friend
-   **Strategic Guidance**: Provides step-by-step action plans and personalized investment strategies
-   **Encouraging Tone**: Celebrates wins, frames risks supportively, and empowers users with confidence
-   **Financial Integrity**: Maintains responsible investing principles while being engaging and optimistic

**AI Capabilities:**
-   **Cryptocurrency Analysis**: Price predictions, on-chain analysis, technical indicators with enthusiastic yet honest insights
-   **Portfolio Rebalancing**: Collaborative wealth management advice with gradual, tax-efficient strategies
-   **Market Sentiment Analysis**: Psychology-driven insights using Fear & Greed framework and contrarian wisdom
-   **Marketing Content Generation**: Ethical, engaging content creation for multiple platforms (Twitter, LinkedIn, blog, video)
-   **Podcast Script Generation**: Weekly "The Alpha Signal" episodes with exclusive market intelligence, hidden opportunities, scam alerts, and insider strategies
-   **Financial Intelligence**: Position sizing, risk assessment, profit-taking strategies with empowering guidance
-   **Tokenomics Optimization**: Strategic token design recommendations
-   **Responsible Investing**: Emergency fund requirements, diversification, DYOR principles emphasized throughout

### Data Flow
-   **Market Data**: Flows from CoinGecko API, through CryptoDataFetcher (with caching), to the Streamlit UI.
-   **AI Analysis**: User input is processed through technical indicators and the AI model, enriched by a knowledge base.
-   **Caching**: In-memory cache with 60-second TTL for market data.
-   **Database Persistence**: User actions related to portfolios, watchlists, and signals are persisted in PostgreSQL via the WalletManager.

## External Dependencies

### APIs and Services
-   **CoinGecko API**: Primary source for real-time cryptocurrency market data, trends, and global statistics.
-   **Replit AI Integrations**: Provides OpenAI-compatible API for AI analysis, predictions, and generative capabilities. Configured via environment variables for secure access.
-   **OnTime Family App Integration**: Mobile app (iOS/Android) that generates ILAH token earnings through family activity tracking and data contribution.

### Python Libraries
-   **Core Framework**: `streamlit`, `openai`, `requests`, `flask`, `flask-cors`.
-   **Data Processing**: `pandas`, `numpy`, `pandas_ta`.
-   **Visualization**: `plotly`.
-   **Reliability**: `tenacity` for API retry logic.
-   **Database**: `SQLAlchemy` for ORM.

### Configuration Management
-   **Environment Variables**: Used for sensitive information such as `AI_INTEGRATIONS_OPENAI_API_KEY`, `AI_INTEGRATIONS_OPENAI_BASE_URL`, `ILAH_API_SECRET`, and PostgreSQL connection details (`DATABASE_URL`, `PGHOST`, etc.). This approach ensures secure credential management and flexible deployment.

## OnTime Integration Architecture

### Integration Components
1. **How It Works Page** (`pages/how_it_works.py`): Comprehensive 4-tab educational interface explaining the OnTime ↔ Crypto platform ecosystem, earning methods, privacy protections, and revenue flow.

2. **ILAH Claiming Interface** (in `pages/ilah_hughs_token.py`): Dedicated "💰 Claim ILAH" tab with three sub-sections:
   - **OnTime App Method**: QR code and claim code generation for seamless mobile claiming
   - **Manual Entry**: Direct wallet address submission with OnTime User ID verification
   - **Claim Status**: Real-time tracking of pending/completed claims with transaction history

3. **API Integration** (`api_server.py` + `ONTIME_INTEGRATION_GUIDE.md`): Complete REST API specification for OnTime developers including:
   - Signature-based authentication
   - User verification and earnings calculation
   - Claim submission and status tracking
   - Token price endpoints
   - Comprehensive code examples (JavaScript/React Native, Python/Flask)

### Integration Flow
1. Users complete activities in OnTime mobile app
2. OnTime tracks activity metrics (days active, data quality, referrals)
3. Platform calculates earned ILAH based on contribution formula
4. Users claim tokens via QR code scan or manual wallet entry
5. Tokens distributed to Solana wallet within 24 hours
6. 60% of data sales revenue minted as ILAH for families

### Recent Changes
**November 4, 2025:**
- Added "The Alpha Signal" podcast feature with AI-generated weekly episodes delivering exclusive market intelligence
- Implemented podcast database persistence with session state fallback
- Created comprehensive podcast script generation with 9 content segments
- Added podcast archive with episode history and downloadable scripts
- Integrated trending coins analysis into podcast content generation
- Renamed podcast to "The Alpha Signal" for more exciting, intriguing brand identity
- **Created podcast subscription system**: 3-day free trial, weekly ($9.99), annual ($99/year) plans
- **Added Marcus Sterling AI host persona**: Former Wall Street analyst with inspiring success story testimonials
- **Implemented subscription gating**: Free previews (intro only) for non-subscribers, full access for paid members
- **Added disclaimer/waiver system**: Signature requirement before subscription with full legal terms
- **Payment routing configured**: All subscription payments deposited to platform owner's account
- **NOTE**: Current email-based identification is demo/prototype. For production, integrate proper authentication (Replit Auth, OAuth, or email verification) to prevent subscription bypass.

**October 29, 2025:**
- Added comprehensive OnTime integration with "How It Works" educational page
- Implemented ILAH token claiming interface with QR code generation
- Created REST API specification and developer documentation
- Added claim history tracking and status monitoring
- Documented revenue sharing model (60% families, 30% operations, 10% AI)