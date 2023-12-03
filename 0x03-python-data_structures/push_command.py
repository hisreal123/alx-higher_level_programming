#!/usr/bin/python3
import subprocess
import os

if __name__ == "__main__":
    username = 'hisreal123'
    user_token = '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'
    repo = 'git@github.com:hisreal123/alx-higher_level_programming.git'

    # Make sure SSH agent is running and add the key
    # git add .
    subprocess.run(['git', 'add', '.'])
    print("All new files successfully added")

    # git commit
    commit_message = input('Enter commit message: ')
    if not commit_message:
        print('You have not entered a commit message!')
    else:
        subprocess.run(['git', 'commit', '-m', commit_message])
        print("Successfully committed: '{}'".format(commit_message))

        # git push with the personal access token
        subprocess.run(['git', 'push', 'origin', 'main'], env={"GIT_ASKPASS": "echo", "GITHUB_TOKEN": user_token})
        print('Git push successful!')