# greetingBot - The Friendly Reddit Bot

This is a simple Reddit bot written in Python which makes use of the Python Reddit API Wrapper, or PRAW. Although a simple project, 
it is good exposure to APIs and API wrappers. Because it is built using PRAW and is designed for Reddit, it is limited in some ways 
to abide by Reddit's API guidelines.

# How greetingBot Got it's Start

Originally designed as suicide_prevention_bot, this project had good intentions at it's core from the start. Using the same basic 
mechanisms currently in use by greetingBot, suicide_prevention_bot would scan posts on Reddit's r/depression subreddit for users whose 
posts contained keywords which indicated suicidal tendencies. However, after a discussion about it's implementation with the r/depression 
mods, the project was determined to be flawed from a psychological standpoint. The project was then reimagined as greetingBot, a more 
lighthearted project which would greet, and hopefully encourage, users who indicated that they were beginner programmers in their posts. 

# How greetingBot Works

greetingBot uses PRAW's comment stream to continually monitor new posts made in subreddit it has been assigned. Upon starting the bot, it 
will check the previous 100 posts for keywords which indicate the post was written by a new programmer. From this point on, it will 
continually monitor new posts posted to the subreddit. For each post that it finds that contains these keywords, the bot will check 
whether or not it has already replied on the post. If it has, it will move on. However, if it hasn't, it will stop to post an encouraging 
reply to the new programmer, urging him or her to pursue his or her passion.

# How to Run greetingBot

Running greetingBot yourself is incredibly simple:
  - First, ensure that you have Python and PRAW installed on your machine.
  - Create a developer account with Reddit and note your authentication details.
  - Next, download the code found in this repository.
  - Edit the greetingBot.ini file to ensure that your information is in the file in place of the placeholders.
  - Ensure that the format of the greetingBot.ini file is the same as shown in this repository. Namely, each authentication field should
    be at the start of a new line in the file.
  - Finally, run the program using this command, from the appropriate directory: python greetingBot.py
That's it! You're running greetingBot.

This bot is open-source, so feel free to change the code or use some or all of it in your own project!
