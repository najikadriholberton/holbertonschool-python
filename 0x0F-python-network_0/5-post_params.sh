#!/bin/bash
# POST with params
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
