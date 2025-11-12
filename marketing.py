import streamlit as st
from openai import OpenAI
import os
import json

def show():
    st.header("🚀 Viral Marketing Generator")
    st.caption("AI-powered content creation for social media campaigns and viral marketing")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Twitter Threads", "Meme Ideas", "Social Media Posts", "Marketing Strategy"])
    
    with tab1:
        show_twitter_generator()
    
    with tab2:
        show_meme_generator()
    
    with tab3:
        show_social_posts()
    
    with tab4:
        show_marketing_strategy()

def show_twitter_generator():
    st.subheader("🐦 Twitter Thread Generator")
    
    st.write("Generate viral Twitter threads for your cryptocurrency")
    
    col1, col2 = st.columns(2)
    
    with col1:
        crypto_name = st.text_input("Cryptocurrency Name", placeholder="My Amazing Coin")
    
    with col2:
        thread_style = st.selectbox("Thread Style", [
            "Educational & Informative",
            "Hype & Excitement",
            "Community Building",
            "Technical Analysis",
            "Meme Culture",
            "FOMO & Urgency"
        ])
    
    key_features = st.text_area(
        "Key Features/USPs (one per line)",
        placeholder="Fast transactions\nLow fees\nCommunity-driven\nUnique tokenomics",
        height=100
    )
    
    target_audience = st.selectbox("Target Audience", [
        "Crypto Beginners",
        "DeFi Enthusiasts",
        "Meme Coin Traders",
        "Institutional Investors",
        "NFT Community",
        "General Crypto Twitter"
    ])
    
    if st.button("🚀 Generate Twitter Thread", type="primary", use_container_width=True):
        if not crypto_name:
            st.error("Please enter a cryptocurrency name")
            return
        
        with st.spinner("🤖 AI is crafting your viral Twitter thread..."):
            try:
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                prompt = f"""
                Create a viral Twitter thread for {crypto_name}.
                
                Style: {thread_style}
                Target Audience: {target_audience}
                Key Features: {key_features}
                
                The thread should:
                - Be engaging and hook readers immediately
                - Use emojis strategically
                - Include call-to-actions
                - Build anticipation and FOMO
                - Be shareable and retweetable
                - Follow Twitter best practices
                
                Respond ONLY with valid JSON:
                {{
                    "thread": [
                        {{"tweet_number": 1, "content": "Hook tweet with emoji and attention grabber"}},
                        {{"tweet_number": 2, "content": "Content tweet"}},
                        ...
                    ],
                    "hashtags": ["#hashtag1", "#hashtag2"],
                    "engagement_tips": ["tip1", "tip2"]
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=2000
                )
                
                result = json.loads(response.choices[0].message.content or "{}")
                
                st.success("✅ Twitter Thread Generated!")
                
                st.markdown("---")
                
                thread = result.get('thread', [])
                
                st.subheader("📱 Your Viral Thread")
                
                full_thread = ""
                
                for tweet in thread:
                    tweet_num = tweet.get('tweet_number', 0)
                    content = tweet.get('content', '')
                    
                    full_thread += f"{content}\n\n"
                    
                    with st.container():
                        st.markdown(f"**Tweet {tweet_num}/{len(thread)}**")
                        st.info(content)
                        st.caption(f"Characters: {len(content)}/280")
                        st.markdown("---")
                
                hashtags = result.get('hashtags', [])
                if hashtags:
                    st.subheader("🏷️ Recommended Hashtags")
                    st.write(" ".join(hashtags))
                
                st.markdown("---")
                
                st.subheader("💡 Engagement Tips")
                tips = result.get('engagement_tips', [])
                for tip in tips:
                    st.success(f"✅ {tip}")
                
                st.markdown("---")
                
                st.subheader("📋 Copy Full Thread")
                st.text_area("Full Thread (Ready to Copy)", full_thread, height=300)
                
                st.download_button(
                    label="📥 Download Thread",
                    data=full_thread,
                    file_name=f"{crypto_name.replace(' ', '_')}_twitter_thread.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error generating thread: {str(e)}")

def show_meme_generator():
    st.subheader("🎨 Meme Idea Generator")
    
    st.write("Get creative meme ideas for viral crypto marketing")
    
    crypto_name = st.text_input("Cryptocurrency Name", placeholder="My Meme Coin", key="meme_crypto")
    
    meme_theme = st.selectbox("Meme Theme", [
        "To The Moon 🚀",
        "Diamond Hands 💎",
        "FOMO Culture",
        "Whale Watching 🐋",
        "Bear vs Bull",
        "Community Strength",
        "Tech Innovation",
        "Funny/Relatable"
    ])
    
    current_trend = st.text_input("Current Trend (optional)", placeholder="Popular meme format or viral trend")
    
    if st.button("🎨 Generate Meme Ideas", type="primary", use_container_width=True):
        if not crypto_name:
            st.error("Please enter a cryptocurrency name")
            return
        
        with st.spinner("🤖 AI is creating meme ideas..."):
            try:
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                prompt = f"""
                Generate viral meme ideas for {crypto_name}.
                
                Theme: {meme_theme}
                Current Trend: {current_trend if current_trend else "Not specified"}
                
                Create meme concepts that are:
                - Funny and shareable
                - Relatable to crypto community
                - Build brand awareness
                - Encourage engagement
                
                Respond ONLY with valid JSON:
                {{
                    "meme_ideas": [
                        {{
                            "title": "Meme title",
                            "format": "Meme format (e.g., Drake meme, Distracted boyfriend)",
                            "description": "Detailed description of the meme",
                            "text_top": "Top text",
                            "text_bottom": "Bottom text",
                            "caption": "Social media caption",
                            "viral_potential": "High|Medium|Low"
                        }}
                    ]
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=2000
                )
                
                result = json.loads(response.choices[0].message.content or "{}")
                
                st.success("✅ Meme Ideas Generated!")
                
                st.markdown("---")
                
                meme_ideas = result.get('meme_ideas', [])
                
                for i, meme in enumerate(meme_ideas, 1):
                    with st.expander(f"💡 Meme Idea #{i}: {meme.get('title', 'Untitled')}", expanded=True):
                        st.markdown(f"**Format:** {meme.get('format', 'Custom')}")
                        st.write(meme.get('description', ''))
                        
                        st.markdown("---")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("**Top Text:**")
                            st.info(meme.get('text_top', ''))
                        
                        with col2:
                            st.markdown("**Bottom Text:**")
                            st.info(meme.get('text_bottom', ''))
                        
                        st.markdown("---")
                        
                        st.markdown("**Caption:**")
                        st.success(meme.get('caption', ''))
                        
                        viral_potential = meme.get('viral_potential', 'Medium')
                        color = "green" if viral_potential == "High" else "orange" if viral_potential == "Medium" else "gray"
                        st.markdown(f"**Viral Potential:** <span style='color:{color}'>{viral_potential}</span>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error generating meme ideas: {str(e)}")

def show_social_posts():
    st.subheader("📱 Social Media Post Generator")
    
    st.write("Create engaging posts for multiple platforms")
    
    crypto_name = st.text_input("Cryptocurrency Name", placeholder="My Coin", key="social_crypto")
    
    platform = st.selectbox("Platform", [
        "All Platforms",
        "Twitter/X",
        "Instagram",
        "TikTok",
        "Reddit",
        "Telegram",
        "Discord"
    ])
    
    post_type = st.selectbox("Post Type", [
        "Announcement",
        "Community Update",
        "Price Milestone",
        "Partnership",
        "AMA/Event",
        "Educational",
        "Engagement/Poll"
    ])
    
    message = st.text_area("Key Message", placeholder="What do you want to communicate?", height=100)
    
    if st.button("📱 Generate Social Posts", type="primary", use_container_width=True):
        if not crypto_name or not message:
            st.error("Please fill in all required fields")
            return
        
        with st.spinner("🤖 AI is creating social media posts..."):
            try:
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                prompt = f"""
                Create social media posts for {crypto_name}.
                
                Platform: {platform}
                Post Type: {post_type}
                Message: {message}
                
                Create platform-optimized content that:
                - Matches platform culture and best practices
                - Uses appropriate tone and style
                - Includes relevant emojis and formatting
                - Drives engagement and action
                
                Respond ONLY with valid JSON:
                {{
                    "posts": [
                        {{
                            "platform": "Platform name",
                            "content": "Post content",
                            "hashtags": ["#tag1", "#tag2"],
                            "call_to_action": "CTA text",
                            "engagement_tip": "How to maximize engagement"
                        }}
                    ]
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=2000
                )
                
                result = json.loads(response.choices[0].message.content or "{}")
                
                st.success("✅ Social Media Posts Generated!")
                
                st.markdown("---")
                
                posts = result.get('posts', [])
                
                for post in posts:
                    platform_name = post.get('platform', 'Unknown')
                    
                    with st.expander(f"📱 {platform_name}", expanded=True):
                        content = post.get('content', '')
                        st.text_area(f"{platform_name} Post", content, height=150, key=f"post_{platform_name}")
                        
                        hashtags = post.get('hashtags', [])
                        if hashtags:
                            st.markdown(f"**Hashtags:** {' '.join(hashtags)}")
                        
                        cta = post.get('call_to_action', '')
                        if cta:
                            st.info(f"**CTA:** {cta}")
                        
                        tip = post.get('engagement_tip', '')
                        if tip:
                            st.success(f"💡 **Tip:** {tip}")
                
            except Exception as e:
                st.error(f"Error generating posts: {str(e)}")

def show_marketing_strategy():
    st.subheader("🎯 Marketing Strategy Generator")
    
    st.write("Get a comprehensive marketing strategy for your cryptocurrency")
    
    crypto_name = st.text_input("Cryptocurrency Name", placeholder="My Crypto", key="strategy_crypto")
    
    budget = st.selectbox("Marketing Budget", [
        "Under $1,000",
        "$1,000 - $5,000",
        "$5,000 - $10,000",
        "$10,000 - $50,000",
        "Over $50,000"
    ])
    
    goals = st.multiselect("Marketing Goals", [
        "Increase Awareness",
        "Build Community",
        "Drive Token Sales",
        "Get Listings",
        "Attract Investors",
        "Create Viral Moments",
        "Establish Thought Leadership"
    ])
    
    timeline = st.selectbox("Timeline", [
        "1 Week Blitz",
        "1 Month Campaign",
        "3 Month Strategy",
        "6+ Month Long-term"
    ])
    
    if st.button("🚀 Generate Marketing Strategy", type="primary", use_container_width=True):
        if not crypto_name or not goals:
            st.error("Please fill in cryptocurrency name and select at least one goal")
            return
        
        with st.spinner("🤖 AI is crafting your comprehensive marketing strategy..."):
            try:
                ai_key = os.getenv("AI_INTEGRATIONS_OPENAI_API_KEY")
                ai_base_url = os.getenv("AI_INTEGRATIONS_OPENAI_BASE_URL")
                
                if not ai_key or not ai_base_url:
                    st.error("AI API keys not configured")
                    return
                
                client = OpenAI(api_key=ai_key, base_url=ai_base_url)
                
                goals_str = ", ".join(goals)
                
                prompt = f"""
                Create a comprehensive marketing strategy for {crypto_name}.
                
                Budget: {budget}
                Goals: {goals_str}
                Timeline: {timeline}
                
                Provide a detailed, actionable marketing strategy. Respond ONLY with valid JSON:
                {{
                    "executive_summary": "Brief overview of the strategy",
                    "target_audience": "Who to target and why",
                    "key_channels": [
                        {{
                            "channel": "Channel name",
                            "tactics": ["tactic1", "tactic2"],
                            "budget_allocation": "Percentage or range",
                            "expected_results": "What to expect"
                        }}
                    ],
                    "content_calendar": [
                        {{
                            "week": "Week 1-2",
                            "focus": "Focus area",
                            "activities": ["activity1", "activity2"]
                        }}
                    ],
                    "influencer_strategy": "How to leverage influencers",
                    "community_building": ["tactic1", "tactic2"],
                    "metrics_to_track": ["metric1", "metric2"],
                    "quick_wins": ["Quick win 1", "Quick win 2"],
                    "long_term_plays": ["Long-term strategy 1", "Long-term strategy 2"]
                }}
                """
                
                response = client.chat.completions.create(
                    model="gpt-5",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    max_completion_tokens=3000
                )
                
                result = json.loads(response.choices[0].message.content or "{}")
                
                st.success("✅ Marketing Strategy Generated!")
                
                st.markdown("---")
                
                st.subheader("📋 Executive Summary")
                st.info(result.get('executive_summary', ''))
                
                st.markdown("---")
                
                st.subheader("🎯 Target Audience")
                st.write(result.get('target_audience', ''))
                
                st.markdown("---")
                
                st.subheader("📢 Marketing Channels")
                
                channels = result.get('key_channels', [])
                for channel in channels:
                    with st.expander(f"📱 {channel.get('channel', 'Channel')}", expanded=False):
                        st.markdown(f"**Budget Allocation:** {channel.get('budget_allocation', 'TBD')}")
                        
                        st.markdown("**Tactics:**")
                        for tactic in channel.get('tactics', []):
                            st.write(f"• {tactic}")
                        
                        st.markdown(f"**Expected Results:** {channel.get('expected_results', 'TBD')}")
                
                st.markdown("---")
                
                st.subheader("📅 Content Calendar")
                
                calendar = result.get('content_calendar', [])
                for period in calendar:
                    st.markdown(f"**{period.get('week', 'Week')}** - Focus: {period.get('focus', 'TBD')}")
                    for activity in period.get('activities', []):
                        st.write(f"• {activity}")
                    st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("⚡ Quick Wins")
                    quick_wins = result.get('quick_wins', [])
                    for win in quick_wins:
                        st.success(f"✅ {win}")
                
                with col2:
                    st.subheader("🎯 Long-term Plays")
                    long_term = result.get('long_term_plays', [])
                    for play in long_term:
                        st.info(f"📈 {play}")
                
                st.markdown("---")
                
                st.subheader("👥 Influencer Strategy")
                st.write(result.get('influencer_strategy', ''))
                
                st.markdown("---")
                
                st.subheader("🤝 Community Building")
                community = result.get('community_building', [])
                for item in community:
                    st.write(f"• {item}")
                
                st.markdown("---")
                
                st.subheader("📊 Metrics to Track")
                metrics = result.get('metrics_to_track', [])
                for metric in metrics:
                    st.write(f"📈 {metric}")
                
            except Exception as e:
                st.error(f"Error generating strategy: {str(e)}")

# Call the main function
show()
