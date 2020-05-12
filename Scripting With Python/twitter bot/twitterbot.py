import tweepy
import time

consumer_key = 'get from twitter'
consumer_secret = 'get from twitter'
access_token = 'get from twitter'
access_token_secret = 'get from twitter'


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



