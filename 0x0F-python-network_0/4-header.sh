#!/bin/bash
# Add custom header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
