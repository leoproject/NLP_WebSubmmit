# Analysis of Tweets about Web Summit 2022
First of all, I would like to warn you that I did not attend the Web Summit 2022, which took place during November 1-4, 2022 in Lisbon as has been the case in recent years. Thus, I decided to collect tweets posted related to the event between October 31st and November 4th because I believe that one day before people start posting about the event they are going to attend, in this case the Web Summit, as the participants may be going to the event itself.



![logo websummit](/images/wbs2022.png "Logo")

To extract the tweets I thought to use the famous library, Tweepy, because with this library the extraction of tweets to access the Twitter API is easy and practical. However, the Twitter API went through recent changes in the free version making it possible to only collect data from one week behind the date being collected. I thought about extracting the data on November 17, so it was no longer useful to use this library.

Consequently, I started researching other alternatives and found the snscrape library. With this library we are able to do data scraping on many social networks, including Twitter, without the restriction of Tweepy.

To extract, I created script in python [get_websummit.py](get_test.py). So I stored all tweets per day in a csv file, you can see in the [datasets folder](/datasets/). The collection of tweets were from October 31 to November 4, 2022. From this extraction I selected the following information from each tweet: date of publication, url, username of the user who published it, the text of the tweet, location where it was published and the language used to write it.

The total data collected was 4,378 tweets, which surprised me because I expected a lot more. Of the total number of tweets published, there were a total of 2,641 different users. When checking the distribution of number of published tweets we noticed that during the 5 days analyzed. October 31, a Monday, had a lower number of tweets published as well as on November 3, Thursday, the penultimate day of the event had a higher number of tweets published.


![Tweets per day](https://plotly.com/~leonardojs/1/)




 <iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~leonardojs/1.embed"></iframe>

