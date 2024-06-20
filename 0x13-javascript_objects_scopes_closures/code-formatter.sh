#!/bin/bash
# Function to commit and push changes to Git
gitCommit() {
  local commitMessage="$1"
  git add . && git commit -m "$commitMessage" && git push origin main

  if [ $? -eq 0 ]; then
    echo "=============== Successfully Committed ✅ =============================="
  else
    echo "Error pushing latest changes."
    exit 1
  fi
}

# Function to format files using semistandard and commit the changes
format() {
  local file="$1"
  local commitMessage="$2"

  if [ -z "$file" ]; then
    echo "No argument passed for formatting!!"
    exit 1
  fi

  semistandard --fix "$file"

  if [ $? -eq 0 ]; then
    echo "=============== Successfully Fixed File ✅ =============================="
    gitCommit "$commitMessage"
  else
    echo "Error fixing file with semistandard."
    exit 1
  fi
}

# Main script execution
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file> <commit-message>"
  exit 1
fi

format "$1" "$2"
