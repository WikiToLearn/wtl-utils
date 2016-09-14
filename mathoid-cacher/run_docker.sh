#!/bin/bash
docker run -ti --rm \
    -e PASSWORD=$1 \
    -e PYWIKIBOT_LANG=$2 \
    wikitolearn/mathoid-cacher
