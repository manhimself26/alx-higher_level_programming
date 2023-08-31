#!/usr/bin/bash
#takes in URL sends
curl -sI "$1" | grep 'Content-length:' | cut -d' ' -f2
