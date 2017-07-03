import praw
import time

reddit = praw.Reddit(client_id= 'T-Owd2rp7eb8Yw',
                     client_secret= '1MI2SQi3zh81pd5rplYd1ngUCxA',
                     user_agent= 'osx:hivemindapp:v0.1 (by /u/LeHuntsman)')

# Set how many hours you want to go back by
HOURS = 3
#Calculate exactly how many HOURS back you want to go
PERIOD = time.time() - (HOURS*60*60)

# Get all submissions within a given period of time for a subreddit
# Returns a list of submission ids
def get_todays(sub):
    result = []
    for submission in reddit.subreddit(sub).new(limit=None):
        if submission.created_utc < PERIOD:
            return result
        else:
            result.append(submission)

def get_comments(list_of_submissions):
    for submission in list_of_submissions:
        print(submission.title)
        print(submission.selftext)
        for comment in submission.comments.list():
            print(comment.body)

# Main function
post_list = get_todays('learnpython')
print(post_list)
get_comments(post_list)
