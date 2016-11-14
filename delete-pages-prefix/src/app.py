# -*- coding: utf-8 -*-
import wtlpywikibot
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import re
import time
import yaml


stream = open('/etc/delete-pages-prefix/config.yaml', 'r')
config = yaml.load(stream, Loader=yaml.Loader)
lang = config["pywikibot"]["lang"]
user = config["pywikibot"]["user"]
passw = config["pywikibot"]["password"]
namespace = config["namespace"]
prefix = config["prefix"]


def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw, sysop=True)
    print("Lang: " + lang )

    for p in pg.PrefixingPageGenerator(prefix, namespace=namespace, site = site):
        if p.exists():
            print("Deleting page: {}".format(p.title()))
            p.delete("Mass delete", prompt=False)

if __name__ == "__main__":
	main()
