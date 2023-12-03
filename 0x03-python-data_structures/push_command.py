#!/usr/bin/python3
import subprocess

if __name__ == "__main__":
    # SSH-formatted repository URL
    repo = 'git@github.com:hisreal123/alx-higher_level_programming.git'

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
        subprocess.run(['git', 'push', 'origin', 'main'])
        print('Git push successful!')
