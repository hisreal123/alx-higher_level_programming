#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import subprocess

    subprocess.run(['git', 'add', '.'])
    print("All new files successfully added")

    commit_message = input('Enter commit message: ')
    if not commit_message:
        print('You have no entered commit message nigga !!')
    else:
        subprocess.run(['git', 'commit', '-m', commit_message])
        print("successfully committed !!: '{}'".format(commit_message))
