import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import os

list_test = { 0:' "Web Summit" since:2022-10-31 until:2022-11-01',
              1:' "Web Summit" since:2022-11-01 until:2022-11-02',
              2:' "Web Summit" since:2022-11-02 until:2022-11-03',
              3:' "Web Summit" since:2022-11-03 until:2022-11-04',
              4:' "Web Summit" since:2022-11-04 until:2022-11-05'}


for index,query in list_test.items():
    tweets_list = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets_list.append([tweet.date,tweet.url,tweet.user.username, tweet.content, tweet.user.location, tweet.lang, tweet.user.co])
    tweets_df = pd.DataFrame(tweets_list, columns=['date','url','username','tweet','location','language'])
    name = "SNSCRAPE/datasets/websummit_day_{}.csv".format(index)
    tweets_df.to_csv(name, index=False)