import twitter


api = twitter.Api(consumer_key='0196N5LqCBzTGkLMh4BMTofNw',
  consumer_secret='ngTCI56zTQCte5jpY94IadYqgFM3iUL9RcWDqZpJElVwTVibRJ',
  access_token_key='982885505170735104-aoJUPrlPC22mCjnCbUO5qgouMpjnvQK',
  access_token_secret='aGujsK9HeKhqu20eCRXwzvhglbhcrYNQdJZfFHq7Krgsq')


def search(input):
    dir = 'B:/Dropbox/Dropbox/Level 5000/CS4242/Project/Data/Data/' + input + '.txt'
    print dir
    t = api.GetUserTimeline(screen_name=input, count=200)
    with open(dir, 'a') as file:
        for i in range(0, t.__len__()):
            file.write('%s\n' % t[i])
    file.close()

if __name__ == '__main__':
    print(api.VerifyCredentials())
    search("ladygaga")