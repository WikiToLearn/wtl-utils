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



def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw)
    print("Lang: " + lang )
    for p in pg.AllpagesPageGenerator(namespace=2800, site=site, step=10):
        print("> ",p.title())
        n = p.text.find("{{noprint-pdf|")
        if n != -1:
            p.text = p.text[:n]
            p.save(minor=True, botflag=True, async= True)

if __name__ == "__main__":
	main()
