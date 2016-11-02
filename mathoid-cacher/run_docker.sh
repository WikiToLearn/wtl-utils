#!/bin/bash
docker run -ti --rm \
    -e PYWIKIBOT_LANG=$1 \
    wikitolearn/mathoid-cacher:0.1
