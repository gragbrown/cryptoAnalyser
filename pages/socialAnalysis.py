import streamlit as st
from pages import utility
import streamlit.components.v1 as components
from lunarcrush import LunarCrush
import requests
import pandas as pd 

def theTweet(url):
    api="https://publish.twitter.com/oembed?url={}".format(url)
    response=requests.get(api)
    res = response.json()["html"] 
    return res

def app():
    st.header("Social Analysis")
    symbol = st.multiselect("Select The Coin(s)", utility.symbols[:3000])
    if len(symbol) == 1:
        df = utility.lunarData(symbol)

        socialImpactScore = df['social_impact_score'][1]
        correlationRank = df['correlation_rank'][1]
        galaxyScore = df['galaxy_score'][1]
        volatility = df['volatility'][1]

        col1, col2 = st.columns((1,1))
        col1.subheader(f"Social Impact Score: {socialImpactScore}")
        col1.subheader(f"Correlation Score: {correlationRank}")
        
        col2.subheader(f"Galaxy Score: {galaxyScore}")
        col2.subheader(f"Volatility Score: {volatility}")

        st.dataframe(df)

        # st.json(data)

        influencers = utility.socialData(symbol)
    
        with st.expander("Twitter"):

            st.header("Number Of Bullish vs Bearish Post")
            bvb = utility.bullvsbear(symbol)
            st.bar_chart(bvb)

            st.header("tweet")
            tweetdf = utility.dataForOne(symbol,"tweets")
            st.line_chart(tweetdf)

            st.header("perChange Tweets vs perChange price")
            pctdf = utility.perChange(symbol, 'tweets')
            st.line_chart(pctdf)

            st.header("tweet_spam")
            tweetSpamdf = utility.dataForOne(symbol,"tweet_spam")
            st.line_chart(tweetSpamdf)

            st.header("tweet_followers")
            tweetFollowersdf = utility.dataForOne(symbol,"tweet_followers")
            st.bar_chart(tweetFollowersdf)

            st.header("perChange TweetFollowers vs perChange price")
            testdf1 = utility.perChange(symbol, 'tweet_followers')
            st.line_chart(testdf1)

            st.header("tweet_retweets")
            tweetRetweetsdf = utility.dataForOne(symbol,"tweet_retweets")
            st.area_chart(tweetRetweetsdf)

            st.header("perChange TweetFollowers vs perChange price")
            testdf2 = utility.perChange(symbol, 'tweet_retweets')
            st.line_chart(testdf2)
            
            lc=LunarCrush()
            feed = lc.get_feeds('BTC')
            urls=pd.json_normalize(feed['data'])['url']
            for i in range(min(5,urls.size)):
                res=theTweet(urls[i])
                components.html(res,height= 500)
 

        with st.expander("reddit"):
            st.header("Reddit Posts")
            redditPostsdf = utility.dataForOne(symbol,"reddit_posts")
            st.line_chart(redditPostsdf)

            st.header("perChange RedditPosts vs perChange price")
            testdf3 = utility.perChange(symbol, 'reddit_posts')
            st.line_chart(testdf3)

            st.header("Reddit Posts Scores")
            redditPostsScoredf = utility.dataForOne(symbol,"reddit_posts_score")
            st.line_chart(redditPostsScoredf)

            st.header("perChange RedditPostsScore vs perChange price")
            testdf4 = utility.perChange(symbol, 'reddit_posts_score')
            st.line_chart(testdf4)

# with st.expander("Compare"):
#     symbols = st.multiselect("Select Coins", utility.symbols[:3000])
    if len(symbol)>1:
        SICdf = utility.compMultiCryptoBasesAttr(symbol, 'social_impact_score')
        st.header("Social Impace Score")
        st.line_chart(SICdf)

        st.header("tweet")
        tweetdf = utility.compMultiCryptoBasesAttr(symbol, "tweets")
        st.bar_chart(tweetdf)

        st.header("tweet_spam")
        tweetSpamdf = utility.compMultiCryptoBasesAttr(symbol,"tweet_spam")
        st.bar_chart(tweetSpamdf)

        st.header("tweet_followers")
        tweetFollowersdf = utility.compMultiCryptoBasesAttr(symbol, "tweet_followers")
        st.line_chart(tweetFollowersdf)

        st.header("tweet_retweets")
        tweetRetweetsdf = utility.compMultiCryptoBasesAttr(symbol, "tweet_retweets")
        st.area_chart(tweetRetweetsdf)




