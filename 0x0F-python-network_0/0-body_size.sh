#!/bin/bash
# get the content-length of response in bytes
curl -sI "$1" | grep -i "content-length" | cut -d" " -f2
