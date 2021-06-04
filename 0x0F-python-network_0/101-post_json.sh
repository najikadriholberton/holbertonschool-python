#!/bin/bash
# add json file as data for POST request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
