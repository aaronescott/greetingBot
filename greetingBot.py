import praw         #For Reddit API
import time         #To make the bot sleep after a post
import configparser #To read the config file


authenticationDetails = configparser.ConfigParser()
authenticationDetails.read('greetingBot.ini')

clientID = authenticationDetails.get('Authentication', 'ClientID')
clientSecret = authenticationDetails.get('Authentication', 'clientSecret')
userName = authenticationDetails.get('Authentication', 'username') 
userPassword = authenticationDetails.get('Authentication', 'password')

greetingBot = praw.Reddit(user_agent = 'greeatingBot v0.1',
                                     client_id = clientID ,
                                     client_secret = clientSecret,
                                     username = userName,
                                     password = userPassword)

subreddit = greetingBot.subreddit('learnprogramming')
posts = subreddit.stream.submissions()

keywords = ("is my first post here", "I'm new here",
            "I'm new on this site", "I haven't posted here before",
            "my first time posting", "I'm new to programming",
            "I'm very new to programming", "I'm really new to programming" 
            "CS beginner", "beginner programmer",
            "starting to program")


def main():
    print("Searching through posts...")
    for post in posts:
        flag = False
        submission_text = post.selftext
        submission_author = post.author
        for keyword in keywords:
            if keyword in submission_text.lower():
                print("Matching post found!")
                flag = True
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if str(comment.author) == userName:
                print("Already commented on this one...")
                print("Searching through posts...")
                flag = False
        if flag:
            msg = "Hey, u/{0}".format(submission_author) + ", it looks like you're new to programming! " \
                                                           "That's great! Keep up the hard work and stay " \
                                                           "positive! Code on!"
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
