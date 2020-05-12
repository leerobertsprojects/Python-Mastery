import tweepy
import time

consumer_key = 'ljpvY5Ep2mqkAp3cgKcjjIn3E'
consumer_secret = 'hhRwqs5JwPW479C8roFx2S80EYjqJud1BL43rPZiz8mgT7eWNc'
access_token = '20541396-yCjl1I0SBQAAO2uqHUtgqhShih43lk18WFcFrtqB6'
access_token_secret = '1MxLFxmHPqoV2kveYBGaK7FhW5zUF2cCOdYMLuoCTF75X'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError and StopIteration:
        time.sleep(1)

search_string = 'cyberfreak1701'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    tweet.favorite()
    # tweet.retweet() to retweet a tweet instead of just liking the tweet.
    print(f'{tweet.text} i just liked this tweet')



# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Jason Bradbury':
#         follower.unfollow()
#         print(f'{follower.name} has been unfollowed')



