from twitterdbutils import TwitterDBUtils
import time
import random
import pandas as pd
import sqlalchemy

class TwitterAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = TwitterDBUtils(user, password, database, host)
        # Create an SQLAlchemy engine from the MySQL connection
        self.engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

    def postTweet(self):
        start_time = time.time()
        tweets_sample = pd.read_csv('tweet.csv')
        tweet_idList = []
        for i in range(len(tweets_sample['TWEET_TEXT'])):
            tweet_id = i
            tweet_idList.append(tweet_id)
        tweets_sample['TWEET_ID'] = tweet_idList
        # SQL statement for inserting a tweet using NOW() for current timestamp
        for index, row in tweets_sample.iterrows():
            user_id = row['USER_ID']
            tweet_id = row['TWEET_ID']
            tweet_text = row['TWEET_TEXT']
            sql = "INSERT INTO TWEET (user_id, tweet_id, tweet_text, tweet_ts) VALUES (%s, %s, %s, NOW())"
            # Values to be inserted
            val = (user_id, tweet_id, tweet_text)
            # Insert the tweet into the database
            self.dbu.insert_one(sql, val)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")

    def getTimeline(self):
        start_time = time.time()
        tweet = pd.read_sql("SELECT * FROM TWEET", self.engine)
        follows_sample = pd.read_csv('follows.csv')
        user_idList = list(tweet.user_id)
        random_user = random.choice(user_idList)
        print("Generating tweets for User" + str(random_user))
        # Filter the DataFrame for the desired user_id
        user_data = follows_sample[follows_sample['USER_ID'] == random_user]
        user_follows = [x for x in user_data.FOLLOWS_ID]
        new_data = tweet[tweet['user_id'].isin(user_follows)]
        # Sort the filtered data by the 'timestamp' column in descending order to get the most current timestamp first
        sorted_user_data = new_data.sort_values(by='tweet_ts', ascending=False)
        # Get the row with the most current timestamp
        result_row = sorted_user_data.iloc[0:10]
        print(result_row)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")


