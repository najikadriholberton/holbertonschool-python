#!/bin/bash
# find the allowed HTTP methods for a certain URL
curl -siX OPTIONS "$1" | grep -i Allow | cut -d" " -f2-
