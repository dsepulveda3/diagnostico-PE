
import json


def info_tweets(route):
    list_tweets = []
    #tweets_final = []
    file = open(route)

    for line_info in file:
        list_tweets.append(json.loads(line_info))
    
    
    #print(tweets[0].get('url'))
    return list_tweets






