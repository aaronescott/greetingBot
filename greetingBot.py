# For Reddit API
import praw
# To make the bot sleep after posting a comment
import time
# To read the config file
import configparser

# Reading config file to get user authentication details
authenticationDetails = configparser.ConfigParser()
authenticationDetails.read('greetingBot.ini')

# Storing user authentication details from config file
clientID = authenticationDetails.get('Authentication', 'ClientID')
clientSecret = authenticationDetails.get('Authentication', 'clientSecret')
userName = authenticationDetails.get('Authentication', 'username')
userPassword = authenticationDetails.get('Authentication', 'password')

# Creating the Reddit object and passing in authentication details through PRAW
greetingBot = praw.Reddit(user_agent = 'greeatingBot v0.1',
                                     client_id = clientID ,
                                     client_secret = clientSecret,
                                     username = userName,
                                     password = userPassword)

# Points greetingBot to the r/learnprogramming subreddit
subreddit = greetingBot.subreddit('learnprogramming')
# Creating a stream of posts/submissions to scan through
posts = subreddit.stream.submissions()

# These are the phrases or keywords that the bot will search for in each post
keywords = ("is my first post here", "I'm new here",
            "I'm new on this site", "I haven't posted here before",
            "my first time posting", "I'm new to programming",
            "I'm very new to programming", "I'm really new to programming" 
            "CS beginner", "beginner programmer",
            "starting to program")


def main():
    print("Searching through posts...")
    # Scanning through the posts on the subreddit
    for post in posts:
        # Boolean flag will determine whether or not a post:
        # 1. Has the phrase in the post
        # 2. Has not previously been commented on by the bot
        flag = False
        submission_text = post.selftext
        submission_author = post.author
        # Scans through each post for each phrase
        for keyword in keywords:
            if keyword in submission_text.lower():
                print("Matching post found!")
                # If phrase is found, flag is changed to true
                flag = True
        # Creating a "comment forest" through PRAW that will iterate through each comment on the post
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if str(comment.author) == userName:
                print("Already commented on this one...")
                print("Searching through posts...")
                # If the bot has already commented on the post, it will adjust flag to false and move on
                flag = False
        # If flag is true at this point, a phrase has been found in the post and the bot has not commented on the post
        if flag:
            msg = "Hey, u/{0}".format(submission_author) + ", it looks like you're new to programming! " \
                                                           "That's great! Keep up the hard work and stay " \
                                                           "positive! Code on!"

            # The bot posts the message and goes to sleep for two minutes
            # This allows newer accounts to use the bot and not be shut down for spam posting
            post.reply(msg)
            print("Encouraging comment posted!")
            print("Going to sleep for two minutes...")
            time.sleep(30)
            print("30 seconds...")
            time.sleep(30)
            print("1 minute...")
            time.sleep(30)
            print("1 minute 30 seconds...")
            time.sleep(30)
            print("Searching through posts...")


if __name__ == "__main__":
        main()
