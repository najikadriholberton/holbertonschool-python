#!/bin/bash
# Show status code of response
curl -s -o /dev/null -Iw "%{http_code}" "$1"
