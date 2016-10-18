#!/bin/bash
docker build -t wikitolearn/full-pages-list .
docker run -ti \
  -v $(pwd)/config.yaml:/etc/full-pages-list/config.yaml \
  wikitolearn/full-pages-list
