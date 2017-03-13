#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wtl
import wtlpywikibot
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import re
import time
import yaml

config = wtl.load_config(config_dir="/etc/redirect_link_fixer/")
username = config["username"]
password = config["password"]
lang = config["lang"]
namespace = config["namespace"]


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
        if p.text != text:
            p.text = text
            p.save(minor=True, botflag=True, async= True)

def get_regex(title):
    title = title.replace(" ", "_")
    rstring = "[_ ]".join(title.split("_"))
    rstring = rstring.replace("//","////")
    return re.compile("\\[\\[" + rstring)


def main():
    site = wtlpywikibot.site(config['lang'])
    wtlpywikibot.login(site,username,password)
    print("Lang: " + lang )

    for red in pg.RedirectFilterPageGenerator(
        pg.AllpagesPageGenerator(site=site, step=10,namespace=namespace),
            no_redirects=False):
        print("> ",red.title())
        pages_to_check = list(pg.ReferringPageGenerator(red, followRedirects=True,
                                                        withTemplateInclusion=False))
        if len(pages_to_check)>0:
            fix_links(red, pages_to_check)
        #deleting Redirect
        red.text += "[[Category:DeleteMe]]"
        red.save(minor=True, botflag=True, async= True)

if __name__ == "__main__":
	main()
