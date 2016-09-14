#!/bin/bash
docker run -ti --rm \
    -e PASSWORD=$1 \
    -e PYWIKIBOT_LANG=$2 \
    -e MODE=$3 \
    -e PREFIX=$4 \
    wikitolearn/course-fixer-old:latest
