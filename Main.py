import json


def info_tweets(route):
    tweets = []
    tweets_final = []
    file = open(route)

    for line in file:
        tweets.append(json.loads(line))
    
    
    print(tweets[0].get('url'))



info_tweets("farmers-protest-tweets-2021-03-5.json")













