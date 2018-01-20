#!/usr/bin/env python
import wtl
import wtlpywikibot
import pywikibot
import os
import os.path
import time

config = wtl.load_config(config_dir="/etc/download-pages-bot/")

site = wtlpywikibot.site(config['lang'])
print("")
print("Download Information")
print("------------------")
print("")
print("Site: " + config['lang'] )
print("")

try:
    root_dir="/opt/output/"
    # print(page.text)
    for item_page in site.allpages(prefix=config['rootpagename'], namespace=config['rootpagenamespace']):
        title = item_page.title()
        print(title)
        path = root_dir + os.path.dirname(title)
        if not os.path.isdir(path):
            os.mkdir(path)
        with open(root_dir + title + ".mw", "w") as fh:
            fh.write(item_page.text)
except pywikibot.exceptions.FatalServerError as e:
    pprint(e)
