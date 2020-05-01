
import tweepy
from twitter_makeup import MakeUp

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

makeup = MakeUp(api)

file_path = 'data/new-banner-2.jpeg'
file_path = 'data/new-banner-1.jpeg'
makeup.change_banner_picture(file_path)
