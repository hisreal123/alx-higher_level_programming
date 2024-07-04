#!/bin/bash
# Displays only the status code of the response.
curl -s POST -H -d "Content-Type: application/json" $2 $1
