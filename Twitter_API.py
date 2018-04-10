from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API

access_token='982885505170735104-aoJUPrlPC22mCjnCbUO5qgouMpjnvQK'
access_token_secret='aGujsK9HeKhqu20eCRXwzvhglbhcrYNQdJZfFHq7Krgsq'
consumer_key='0196N5LqCBzTGkLMh4BMTofNw'
consumer_secret='ngTCI56zTQCte5jpY94IadYqgFM3iUL9RcWDqZpJElVwTVibRJ'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['love'])