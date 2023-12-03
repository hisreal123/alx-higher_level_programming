#!/usr/bin/python3
import subprocess

if __name__ == "__main__":
    # SSH-formatted repository URL
    repo = ''
    remote_output = subprocess.run(['git', 'remote', '-v',], capture_output=True, text=True)
    if "origin" in remote_output.stdout:
        repo = remote_output.stdout.split("origin")[1].split()[0]
    print(repo)

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
        print('Git push successful! to {} '.format(repo))
