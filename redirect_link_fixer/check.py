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
    for p in backpages:
        print(">>>fixing page: ",p.title())
        oldtext = p.text
        text = oldtext.replace("[["+oldurl+"]]", "[[" + newurl + "]]")
        if (oldtext != text):
            p.text = text
            p.save()


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
