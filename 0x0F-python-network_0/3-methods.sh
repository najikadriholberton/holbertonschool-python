#!/bin/bash
# find the allowed HTTP methods for a certain URL
curl -sI "$1" | grep "Allow: " | cut -d" " -f2-
