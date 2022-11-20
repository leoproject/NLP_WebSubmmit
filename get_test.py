import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import os

tweets_list = []
maxTweets = 100
i = 0
for tweet in sntwitter.TwitterSearchScraper(' "Web Summit" since:2022-10-31 until:2022-11-01').get_items():
    if i > maxTweets:
        break
    tweets_list.append([tweet.date,tweet.url,tweet.user.username, tweet.content, tweet.user.location, tweet.lang])
    i+=1

tweets_df = pd.DataFrame(tweets_list, columns=['date','url','username','content','location','language'])
tweets_df.to_csv("websummit.csv", index=False)