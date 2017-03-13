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


config = wtl.load_config(config_dir="/etc/redirects_delete/")
lang = config["lang"]
username = config["username"]
password = config["password"]
namespace = config["namespace"]
category = config["category"]


def main():
    site = wtlpywikibot.site(config['lang'])
    wtlpywikibot.login(site,username,password)
    print("\nDeleting pages")
    print("--------------")
    print("\nLang: " + lang )

    cat = pywikibot.Category(site, category)

    for p in pg.CategorizedPageGenerator(category=cat,namespaces=namespace):
        if p.isRedirectPage():
            print("Deleting redirect: {}".format(p.title()))
            p.delete("Deleting redirects of the old Courses structure",
                     prompt=False, mark=True)

if __name__ == "__main__":
	main()
