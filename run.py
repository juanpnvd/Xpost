import praw
from whatever import tosubs
import random
import os
from keep_alive import keep_alive
import time

keep_alive()


reddit = praw.Reddit(client_id=os.environ['client_id'],
                     client_secret=os.environ['client_secret'],
                     username=os.environ['username'],
                     password=os.environ['password'],
                     user_agent=os.environ['user_agent'])

#get the original post
subreddit = reddit.subreddit('PetsareAmazing')
for submission in subreddit.new(limit=1):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)

target_subreddit=random.choice(tosubs)

#crosspost to another subreddit
submission.crosspost(target_subreddit)
print("Crossposted to ", target_subreddit)
sleep(900)
