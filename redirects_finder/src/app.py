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


def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw)
    print("Lang: " + lang )
    pages_error = []
    redirects = {}

    for p in pg.AllpagesPageGenerator(site=site, step=20, namespace=namespace, includeredirects=False):
        print("> ",p.title())
        for pp in p.linkedPages():
            if pp.isRedirectPage():
                print(">>> Found redirect: {}".format(pp.title()))
                pages_error.append(p)
                if pp.title() in redirects:
                    redirects[pp.title()] += 1
                else:
                    redirects[pp.title()] = 1
    print("\n\nPages with links to redirects:\n")
    for a in set(pages_error):
        print(">>> ", a)
    print("\n\nRedirects used:\n")
    for a in redirects:
        print(">>> ", a +" = "+ str(redirects[a]))

if __name__ == "__main__":
	main()
