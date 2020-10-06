import tweepy
import argparse
parser = argparse.ArgumentParser(description='Provide your tweet')
parser.add_argument('-t', action="store", dest="t")
args = parser.parse_args()

CONSUMER_KEY = 'PE09BM9rVdoVVO8ebt1JCyqc6'
CONSUMER_SECRET = 'apyP1I8ORfUZXNiYLdJFCuQFpineQAtqhDqp1vMp5DyDgjZfwZ'
ACCESS_KEY = '1754295733-gJ0g9E2xhEVCeF4QK5lt0HSKZ1YIday1frq5Nks'
ACCESS_SECRET = 'psLU5YbKaasnvs2nWRu2B5NPmWErVStdwgwiNCEsDP73C'

# Authenticate to Twitter
auth = tweepy.OAuthHandler("PE09BM9rVdoVVO8ebt1JCyqc6", "apyP1I8ORfUZXNiYLdJFCuQFpineQAtqhDqp1vMp5DyDgjZfwZ")
auth.set_access_token("1754295733-gJ0g9E2xhEVCeF4QK5lt0HSKZ1YIday1frq5Nks", "psLU5YbKaasnvs2nWRu2B5NPmWErVStdwgwiNCEsDP73C")

# Create API object
api = tweepy.API(auth)

if args.t:
    api.update_status(args.t)
    print("Your tweet successfully posted!")