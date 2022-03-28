

def top10_retweeted(list_tweets):
    top_10_retweeted = []

    for i in range(0,10):
        url_mayor = list_tweets[0].get('url') 
        retweeted_mayor = 0
        position_mayor = 0
        if (list_tweets[0].get('retweetedTweet') == None):
            retweeted_mayor = 0
        elif (list_tweets[0].get('retweetedTweet') != None):
            retweeted_mayor = int(list_tweets[0].get('retweetedTweet'))
        list_tweets.pop(0)
        
        for i in range (0, len(list_tweets)):
            retweeted_actual = 0
            if (list_tweets[i].get('retweetedTweet') == None):
                retweeted_actual = 0
            elif (list_tweets[i].get('retweetedTweet') != None):
                retweeted_actual = int(list_tweets[0].get('retweetedTweet'))

            if (retweeted_actual > retweeted_mayor):
                url_mayor = list_tweets[i].get('url')
                retweeted_mayor = retweeted_actual
                position = 1
        top_10_retweeted.append(url_mayor)
        list_tweets.pop(position_mayor)

    return top_10_retweeted

    '''
    for i in range(0,10):
        info = []
        url = list_tweets[i].get('url')
        retweeted = list_tweets[i].get('url')
        info.append(url)
        info.append(retweeted)
        top_10_retweeted.append(info)

    for j in range (10, len(list_tweets)):
        retweeted_actual = 0 
        if (i[1] == "null"):
            retweeted_actual = 0
        elif (i[1] != "null"):
            retweeted_actual = i[1]

        for i in range(len(top_10_retweeted)):
            retweeted_top10 = 0 
            if (i[1] == "null"):
                retweeted_top10 = 0
            elif (i[1] != "null"):
                retweeted_top10 = i[1]

            if (retweeted_actual > retweeted_top10)
    '''
    retweeted = print(list_tweets[2].get('retweetedTweet'))
    return retweeted