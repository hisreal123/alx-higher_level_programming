#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import subprocess

    username = 'hisreal123'
    user_token = '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'
    repo = 'git@github.com:hisreal123/alx-higher_level_programming.git'

    # git add .
    subprocess.run(['git', 'add', '.'])
    print("All new files successfully added")

    # git commit
    commit_message = input('Enter commit message: ')
    if not commit_message:
        print('You have no entered commit message nigga !!')
    else:
        subprocess.run(['git', 'commit', '-m', commit_message])
        print("successfully committed !!: '{}'".format(commit_message))

        subprocess.run(['git', 'push', 'origin', 'main'], env={"GIT_SSH_COMMAND": "ssh -o 'StrictHostKeyChecking=no'"})
        print('Git push successful!')
