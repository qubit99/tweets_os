import tweepy
import time
import sys

auth = tweepy.OAuthHandler("ZjOJyhUlkTomFQneaEL6yy3Dh",
                           "yFB03FSLX1cvjegekUUHWFl8JWEpc8MGErbHYl5iU4Huvkk7bT")
auth.set_access_token(
    "1140608961642545153-XwJGOGtoAjDlYwEqcxwYHXRGmwUSPr", "WAPAt88rHJlAgBzx3ZtfBa3mNMAq5PrycT5nXxy0uoUFe")

api = tweepy.API(auth)


time_start = time.time()

mobile_os_dict = {"iPhone": 0, "Android": 0, "web app": 0}


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            tweetid = status.id
            val = (api.get_status(tweetid).source)
            if val == 'Twitter for Android':
                mobile_os_dict["Android"] += 1
            elif val == 'Twitter for iPhone':
                mobile_os_dict["iPhone"] += 1
            elif val == 'Twitter Web App':
                mobile_os_dict["web app"] += 1
            else:
                pass
            print(mobile_os_dict)
        except:
            pass

        # the code below is to terminate the collection of data after a certain time
        if time.time() > time_start+1000:
            print(mobile_os_dict)
            sys.exit(0)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(
    auth=api.auth, listener=myStreamListener, tweet_mode='extended')

myStream.filter(track=["a", "e", "i", "o", "u"],
                locations=[64.6, 5.06, 97.55, 35.91], stall_warnings=True)
