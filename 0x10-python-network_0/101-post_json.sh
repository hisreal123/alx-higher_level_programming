#!/bin/bash
# Displays only the status code of the response.
URL = $1
FILENAME = $2
const response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$FILENAME" "$URL");
echo "$response"
