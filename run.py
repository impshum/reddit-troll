import praw
from random import choice
from time import sleep
from config import *

print('\nREDDIT TROLL (u/impshum)\n')

mins = timer / 60
print('Searching every {} minutes\n\nPress Ctrl + C to exit'.format(int(mins)))

user_agent = 'Get recent comments and reply by u/impshum'
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)


def reddit():
    for target_user in target_users:
        reduser = reddit.redditor(target_user)
        print('\nKarma for', target_user, int(reduser.link_karma), '\n')

        if comment_on:
            for comment in reduser.submissions.new(limit=count):
                if comment.id in map(str.strip, open("ids.txt")):
                    print('Already commented on', comment.id)
                    sleep(1.5)
                else:
                    with open("ids.txt", 'a') as f:
                        line = '{}\n'.format(comment.id)
                        f.write(line)
                        print('Found:', comment.body.replace('\n', ' '))
                        spamit = choice(replies)
                        print('Reply:', spamit)
                        comment.reply(spamit)
                        sleep(250)
        if submission_on:
            for submission in reduser.submissions.new(limit=count):
                if submission.id in map(str.strip, open("ids.txt")):
                    print('Already commented on', submission.id)
                    sleep(1.5)
                else:
                    with open("ids.txt", 'a') as f:
                        f.write(submission.id + '\n')
                        print('Found:', submission.title.replace('\n', ' '))
                        spamit = choice(replies)
                        print('Reply:', spamit)
                        submission.reply(spamit)
                        submission.downvote()
                        sleep(250)


while True:
    try:
        reddit()
        print('\nSleeping...')
        sleep(timer)
    except KeyboardInterrupt:
        print('\nExiting\n')
        break
