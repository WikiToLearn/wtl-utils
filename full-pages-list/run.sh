#!/bin/bash
docker build -t wikitolearn/full-pages-list .
docker run -ti \
  --net=host \
  -v $(pwd)/config.yaml:/etc/full-pages-list/config.yaml \
  wikitolearn/full-pages-list
