#!/bin/bash
docker run -ti --rm \
    -e PASSWORD=$1 \
    -e PYWIKIBOT_LANG=$2 \
    -e MODE=$3 \
    -e PREFIX=$4 \
    -v $(pwd)/pages:/w2lbot/pages \
    wikitolearn/course-fixer-old:latest
