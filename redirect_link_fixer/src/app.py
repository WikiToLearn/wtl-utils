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


def fix_links(red, backpages):
    oldurl = red.title()
    newurl = red.getRedirectTarget().title()
    print(">>>new url: ", newurl)
    r = get_regex(oldurl)
    for p in backpages:
        print(">>>fixing page: ",p.title())
        text = p.text[:]
        for m in r.finditer(p.text):
            text = text.replace(m.group(0), "[["+ newurl)
            print(m.group(0))
        p.text = text
        p.save(minor=True, botflag=True, async= True)

def get_regex(title):
    title = title.replace(" ", "_")
    rstring = "[_ ]".join(title.split("_"))
    rstring = rstring.replace("//","////")
    return re.compile("\\[\\[" + rstring)


def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw)
    print("Lang: " + lang )

    for red in pg.RedirectFilterPageGenerator(
        pg.AllpagesPageGenerator(site=site, step=10), no_redirects=False):
        print("> ",red.title())
        pages_to_check = list(pg.ReferringPageGenerator(red, withTemplateInclusion=False))
        if len(pages_to_check)>0:
            fix_links(red, pages_to_check)
            red.add
            #deleting Redirect
            red.text += "[[Category:ToDelete]]"
            red.save(minor=True, botflag=True, async= True)

if __name__ == "__main__":
	main()
