#!/bin/bash
docker build -t wikitolearn/math-checker .
LOCAL_INPUT=""
if test -d input
then
    LOCAL_INPUT="-v "$(pwd)"/input/:/opt/input/"
fi
docker run -ti \
  -v $(pwd)/config.yaml:/etc/math-checker/config.yaml \
  $LOCAL_INPUT \
  wikitolearn/math-checker
