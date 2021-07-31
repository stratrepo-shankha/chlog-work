import tweepy


class TwitterAPI:
    def __init__(self, apikey, apisecretkey, accesstoken, accesstokensecret) -> None:
        self.apikey = apikey
        self.apisecretkey = apisecretkey
        self.accesstoken = accesstoken
        self.accesstokensecret = accesstokensecret

        self.__api = self.__auth()

        self.__check_auth()

    def __auth(self) -> tweepy.API:
        auth = tweepy.OAuthHandler(self.apikey, self.apisecretkey)
        auth.set_access_token(self.accesstoken, self.accesstokensecret)

        api = tweepy.API(auth)

        return api

    def __check_auth(self) -> None:
        api = self.__api

        try:
            api.verify_credentials()
            print("\n\nAuthenticating...\n\n.\n.\n\nSuccessful...\n\n")
        except:
            raise Exception("Error during authentication")

    def get_timeline(self) -> list:
        api = self.__api

        timeline = api.home_timeline()

        return ['{} said {}'.format(tweet.user.name, tweet.text) for tweet in timeline]

    def timelinesearch(self, key: str) -> list:
        api = self.__api

        tweets = []
        statuses = api.user_timeline(key, tweet_mode='extended')

        for status in statuses:
            if hasattr(status, "retweeted_status"):
                tweets.append({
                    'type': 'retweet',
                    'text': status.retweeted_status.full_text,
                    'additionalinfo': status.__dict__['_json']
                })
            else:
                tweets.append({
                    'type': 'original',
                    'text': status.full_text,
                    'additionalinfo': status.__dict__['_json']
                })
        return tweets

    @property
    def api(self) -> tweepy.API:
        return self.__api

    def searchtweets(self):
        pass
