#!/usr/bin/env python
import wtl
import wtlpywikibot
import pywikibot
import os
import os.path

config = wtl.load_config(config_dir="/etc/full-pages-list/")

site = pywikibot.Site(config['lang'],'wikitolearn')

namespaces = site.namespaces()
for ns in namespaces:
    print("#### {}".format(namespaces[ns]))
    try:
        for page in site.allpages(namespace=ns):
            print(page.title())
    except Exception as e:
        print(e)
