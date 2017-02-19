#!/bin/bash
docker build -t wikitolearn/full-pages-list .
if test ! -d output
then
  mkdir output
fi
docker run -ti \
  --net=host \
  -v $(pwd)/config.yaml:/etc/full-pages-list/config.yaml \
  -v $(pwd)/output/:/srv/output/ \
  -e OUTPUT_OWNER_UID=`id -u` \
  -e OUTPUT_OWNER_GID=`id -g` \
  wikitolearn/full-pages-list
