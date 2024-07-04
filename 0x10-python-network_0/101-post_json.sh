#!/bin/bash
# Displays only the status code of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
