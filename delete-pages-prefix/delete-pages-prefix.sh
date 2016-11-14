#!/bin/bash
docker build -t wikitolearn/delete-pages-prefix .
docker run -ti \
  -v $(pwd)/config.yaml:/etc/delete-pages-prefix/config.yaml \
  wikitolearn/delete-pages-prefix
