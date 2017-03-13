#!/bin/bash
docker build -t wikitolearn/redirect_link_fixer .
docker run -ti \
  -v $(pwd)/config.yaml:/etc/redirect_link_fixer/config.yaml \
  wikitolearn/redirect_link_fixer
