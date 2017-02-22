#!/usr/bin/env python
import wtl
import wtlpywikibot
import pywikibot
import os
import os.path

config = wtl.load_config(config_dir="/etc/filtered-pages-list/")

langs = config['langs']

for lang in langs:
    site = pywikibot.Site(lang,'wikitolearn')

    namespaces = site.namespaces()
    for ns in namespaces:
        file_name = "/srv/output/{}-{}.txt".format(lang,namespaces[ns])
        file_object  = open(file_name, "w")
        print("#### {}".format(namespaces[ns]))
        file_object.write("#### {}\n".format(namespaces[ns]))
        try:
            for page in site.allpages(namespace=ns):
                print(page.title())
                file_object.write("{}\n".format(page.title()))
        except Exception as e:
            print(e)
        file_object.close()
        os.chown(file_name, int(os.environ['OUTPUT_OWNER_UID']),int(os.environ['OUTPUT_OWNER_GID']))
