import load
import funcion1
import funcion2
import funcion3
import funcion4

list_tweets = load.info_tweets("farmers-protest-tweets-2021-03-5.json")


print(list_tweets[0].get('retweetedTweet'))

#if (list_tweets[0].get('retweetedTweet') == None):
    #print("YES")

print(funcion1.top10_retweeted(list_tweets))

print((funcion2.top10_users(list_tweets)))

print((funcion3.top10_days(list_tweets)))

print((funcion4.top10_hashtags(list_tweets)))







