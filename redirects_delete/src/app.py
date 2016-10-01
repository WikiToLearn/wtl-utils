# -*- coding: utf-8 -*-
import wtlpywikibot
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import re
import time
import yaml


stream = open('config.yaml', 'r')
config = yaml.load(stream, Loader=yaml.Loader)
lang = config["pywikibot"]["lang"]
user = config["pywikibot"]["user"]
passw = config["pywikibot"]["password"]
namespace = config["namespace"]
category = config["category"]


def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw)
    print("Lang: " + lang )

    cat = pywikibot.Category(site, category)

    for p in pg.CategorizedPageGenerator(category=cat,namespaces=namespace):
        if p.isRedirectPage():
            print("Deleting redirect: {}".format(p.title()))
            p.delete("Deleting redirects of the old Courses structure",
                     prompt=False, mark=True)

if __name__ == "__main__":
	main()
