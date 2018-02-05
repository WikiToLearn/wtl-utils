#!/bin/bash
if test ! -d $(pwd)/output/
then
  mkdir $(pwd)/output/
fi
docker build -t wikitolearn/download-pages-bot .
docker run -ti \
  -v $(pwd)/config.yaml:/etc/download-pages-bot/config.yaml \
  -v $(pwd)/output/:/opt/output/ \
  wikitolearn/download-pages-bot
