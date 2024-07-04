#!/bin/bash
# Displays only the status code of the response.
curl -s POST -H  "Content-Type: application/json" -d "$2" "$1"
