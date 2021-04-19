import tweepy
import re
import string
import config

# Authenticate Twitter Credentials
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            if not status.truncated:
                tweet = status.text
            else:
                tweet = status.extended_tweet['full_text']

            tweet = self.clean_tweet(tweet)
            print(tweet)
            if self.check_for_giveaway(tweet):
                try:
                    self.enter_giveaway(status.id, tweet)
                except Exception as e:
                    print(e)


    def clean_tweet(self, tweet):
        '''Returns the raw text of a tweet'''
        # Remove Links
        text = re.sub(r'http\S+', '', tweet)

        # Remove Emojis
        regrex_pattern = re.compile(pattern="["
                                            u"\U0001F600-\U0001F64F"  # emoticons
                                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                            u"\U00002500-\U00002BEF"  # chinese char
                                            u"\U00002702-\U000027B0"
                                            u"\U00002702-\U000027B0"
                                            u"\U000024C2-\U0001F251"
                                            u"\U0001f926-\U0001f937"
                                            u"\U00010000-\U0010ffff"
                                            u"\u2640-\u2642" 
                                            u"\u2600-\u2B55"
                                            u"\u200d"
                                            u"\u23cf"
                                            u"\u23e9"
                                            u"\u231a"
                                            u"\ufe0f"  # dingbats
                                            u"\u3030"
                                            "]+", flags=re.UNICODE)
        text = regrex_pattern.sub(r'', text)

        # Remove punctuation and numbers
        text = "".join([char for char in text if char not in string.punctuation])
        text = re.sub("[0-9]+", '', text)

        # Remove new lines
        text = text.replace('\n', ' ')

        return text.lower()


    def check_for_giveaway(self, tweet):
        '''Determines if Tweet is a giveaway'''
        if 'giveaway' in tweet:
            return True
        return False


    def follows_accounts(self, tweet):
        '''Follows accounts in the tweet'''
        accounts = []
        words = tweet.split(' ')
        for word in words:
            if '@' in word:
                api.create_friendship(word.replace('@', ''))


    def enter_giveaway(self, id, tweet):
        '''Enters giveaway by following all the instructions in the tweet'''
        if 'follow' in tweet:
            self.follows_accounts(tweet) 

        if 'like' in tweet:
            api.create_favorite(id)

        # if 'comment' in tweet or 'reply' in tweet:
        #     api.update_status('', in_reply_to_status_id=id)

        if 'retweet' in tweet:
            api.retweet(id)


if __name__ == '__main__':
        myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
        stream = myStream.filter(track=['giveaway'])