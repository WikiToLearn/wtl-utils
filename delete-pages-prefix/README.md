This bot deletes all the pages with the indicated Prefix in the url.

Run it mounting a config file in /opt/src
docker run -ti --rm -v $(path_to_config):/opt/src/config.yaml wikitolearn/delete-pages-prefix
