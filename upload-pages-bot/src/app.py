#!/usr/bin/env python
import wtl
import wtlpywikibot
import pywikibot
import os
import os.path
import time

config = wtl.load_config(config_dir="/etc/upload-pages-bot/")
username=config['username']
password=config['password']
rootpage=config['rootpage']
if rootpage != False and not rootpage.endswith('/'):
    rootpage = rootpage + "/"
elif isinstance(rootpage,bool):
    rootpage = ""

site = wtlpywikibot.site(config['lang'])
wtlpywikibot.login(site,username,password)
print()
print("Upload Information")
print("------------------")
print()
print("Site: " + config['lang'] )

try:
    pages = {}
    root_dir="/opt/input/"
    for path, subdirs, files in os.walk(root_dir):
        for name in files:
            filename = os.path.join(path, name)
            if os.path.splitext(filename)[1]==".mw":
                page_title = os.path.splitext(filename)[0][(len(root_dir)):]
                pages[rootpage+page_title] = None
                with open(filename, 'r') as input_file:
                    pages[rootpage+page_title] = input_file.read()
                    input_file.close()

    for page_title in pages:
        print("Page: {}".format(page_title))
    print()
    print()
    print()
    time.sleep(5)

    if len(pages) > 0:
#        wtlpywikibot.login(site,username,password)
        for page_title in pages:
            page = pywikibot.Page(site,page_title)
            if page.text.strip() != pages[page_title].strip():
                page.text = pages[page_title].strip()
                page.save(minor=False, botflag=True)
    else:
        print("No pages")
except pywikibot.exceptions.FatalServerError as e:
    pprint(e)
