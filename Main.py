import load
import funcion1

list_tweets = load.info_tweets("farmers-protest-tweets-2021-03-5.json")


print(list_tweets[0].get('retweetedTweet'))

#if (list_tweets[0].get('retweetedTweet') == None):
    #print("YES")

print(funcion1.top10_retweeted(list_tweets))









