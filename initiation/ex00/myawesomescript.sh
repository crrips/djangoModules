#!/bin/sh

short_url="$1"

curl -sI "$short_url" | grep "location" | cut -d " " -f2
