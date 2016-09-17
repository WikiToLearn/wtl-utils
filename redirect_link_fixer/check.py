# -*- coding: utf-8 -*-
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import re
import time

config = __import__("user-config")


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
        p.save(minor=True, botflag=True)

def get_regex(title):
    title = title.replace(" ", "_")
    rstring = "[_ ]".join(title.split("_"))
    rstring = rstring.replace("//","////")
    return re.compile("\\[\\[" + rstring)


def main():
    print("Connecting to " + config.mylang + \
          " domain for the " + config.family + " family")
    site = pywikibot.Site()
    site.login()

    BASE_SITE = site.family.langs[config.mylang]
    print("Base URL: " + BASE_SITE)

    for red in pg.RedirectFilterPageGenerator(
        pg.AllpagesPageGenerator(site=site, step=10), no_redirects=False):
        print("> ",red.title())
        pages_to_check = list(pg.ReferringPageGenerator(red, withTemplateInclusion=False))
        if len(pages_to_check)>0:
            fix_links(red, pages_to_check)
            #deleting Redirect
            #red.delete(reason="migration done", prompt=False, mark=False)
