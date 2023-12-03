#!/usr/bin/python3
import subprocess
import os

if __name__ == "__main__":
    username = 'hisreal123'
    user_token = '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'
    repo = 'git@github.com:hisreal123/alx-higher_level_programming.git'

    # Start SSH agent and add key
    ssh_agent_process = subprocess.Popen(['eval', '$(ssh-agent -s)'], stdout=subprocess.PIPE, shell=True)
    ssh_agent_output = ssh_agent_process.communicate()[0]

    # Extract the SSH_AUTH_SOCK and SSH_AGENT_PID values
    for line in ssh_agent_output.splitlines():
        if b'SSH_AUTH_SOCK' in line:
            env_key, env_value = line.split(b'=')
            os.environ[env_key.decode()] = env_value.decode()
        if b'SSH_AGENT_PID' in line:
            env_key, env_value = line.split(b'=')
            os.environ[env_key.decode()] = env_value.decode()

    # Add the SSH key to the agent
    subprocess.run(['ssh-add', '/home/treasure/.ssh/id_ed25519'])

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

        env = os.environ.copy()
        env["GIT_SSH_COMMAND"] = "ssh -o 'StrictHostKeyChecking=no'"
        subprocess.run(['git', 'push', 'origin', 'main'], env=env)
        print('Git push successful!')
