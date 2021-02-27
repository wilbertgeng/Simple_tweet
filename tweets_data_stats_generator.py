import datetime
class TweetsDataStatsGenerator(object):

    def __init__(self, tweets_api_service):
        self.tweets_api_service = tweets_api_service

    # Retrieves the highest number of tweets that were created on any given day by the given user.
    # A day's time period here is defined from 00:00:00 to 23:59:59
    # If there are no tweets for the given user, this method should raise a ValueError.
    def get_most_tweets_for_any_day(self, user_name) -> int:
        """TODO Implement
        """
        date_tweets = {}
        for tweet in self.tweets_api_service:
            date_time_obj = datetime.datetime.strptime(tweet["createdAt"], "%Y-%m-%dT%H:%M:%S")
            date = date_time_obj.date()
            if date in date_tweets:
                date_tweets[date] += 1
            else:
                date_tweets[date] = 1
        res = 0
        for value in date_tweets.values():
            res = max(res, value)
        if res:
            #print(res)
            return res
        else:
             raise ValueError

        #    print('Time:', date_time_obj.time())
        #    print('Date-time:', date_time_obj)


    # Finds the ID of longest tweet for the given user.
    # You can assume there will only be one tweet that is the longest.
    # If there are no tweets for the given user, this method should raise a ValueError.
    def get_longest_tweet(self, user_name) -> str:
        """TODO Implement
        """
        users = {}
        length_max = float('-inf')
        id_max_length = ''
        for tweet in self.tweets_api_service:
            if tweet["text"]:
                id = tweet["id"]
                txt = tweet["text"]
                if len(txt) > length_max:
                    length_max = len(txt)
                    id_max_length = id
            else:
                raise ValueError
        #print(id_max_length, length_max)
        return id_max_length

    # Retrieves the most number of days between tweets by the given user.
    # This should always be rounded down to the complete number of days, i.e. if the time is 12 days & 3 hours, this
    # method should return 12.
    # If there are no tweets for the given user, this method should raise a ValueError.
    def find_most_days_between_tweets(self, user_name) -> int:
        """TODO Implement
        """
        days_diff = []
        for tweet in self.tweets_api_service:
            date_time_obj = datetime.datetime.strptime(tweet["createdAt"], "%Y-%m-%dT%H:%M:%S")
            date = date_time_obj.date()
            days_diff.append(date)
        #print((max(days_diff) - min(days_diff)).days)
        if not days_diff:
            raise ValueError
        else:
            return (max(days_diff) - min(days_diff)).days


    # Retrieves the most popular hash tag tweeted by the given user.
    # Note that the string returned by this method should include the hashtag itself.
    # For example, if the most popular hash tag is "#Python", this method should return "#Python".
    # If there are no tweets for the given user, this method should raise a ValueError.
    def get_most_popular_hash_tag(self, user_name) -> str:
        """TODO Implement
        """
        tag_cnt = {}

        for tweet in self.tweets_api_service:
            if tweet["text"]:
                txt = tweet["text"]
                for i in range(len(txt)):
                    if txt[i] == "#":
                        tag = txt[i:]
                        if tag in tag_cnt:
                            tag_cnt[tag] += 1
                        else:
                            tag_cnt[tag] = 1
        cnt_max = 0
        res = ''
        for tag, cnt in tag_cnt.items():
            if cnt > cnt_max:
                cnt_max = cnt
                res = tag
        #print(type(res))
        #print(cnt_max)

        if not tag_cnt:
            raise ValueError
        else:
            return res

















###### Bottom #####
