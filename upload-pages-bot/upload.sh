#!/bin/bash
docker build -t wikitolearn/upload-pages-bot .
docker run -ti \
  -v $(pwd)/config.yaml:/etc/upload-pages-bot/config.yaml \
  -v $(pwd)/input/:/opt/input/ \
  wikitolearn/upload-pages-bot
