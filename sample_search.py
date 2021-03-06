import optparse
from pprint import pprint
from urllib import quote
import requests

TWITTER_SEARCH = 'http://search.twitter.com/search.json?q='

def search(term):
    response = requests.get(TWITTER_SEARCH + quote(term))
    if response.ok:
        rjson = response.json()
        # Uncomment this line to see the full return from Twitter
        #pprint(rjson)

        # Loop over the results from Twitter
        for tweet in rjson['results']:
            try:
                print u'%s - %s' %(tweet['from_user_name'], tweet['text'])
            except UnicodeEncodeError:
                # Suppress Windows terminal unicode encode errors
                pass
    else:
        response.raise_for_status()

if __name__ == '__main__':
    parser = optparse.OptionParser("Usage: %prog [-h] SEARCHTERM")
    (options, args) = parser.parse_args()

    if len(args) > 0:
        search(args[0])
    else:
        parser.error("You must specify a search term!")
