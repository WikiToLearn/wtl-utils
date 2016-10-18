#!/usr/bin/env python
import wtl
import wtlpywikibot
import pywikibot
import os
import os.path

config = wtl.load_config(config_dir="/etc/math-checker/")

if config['checktype'] == "local":
    if os.path.isdir("/opt/input/"):
        print("Running check math on files inside of input/ dir")
        site = pywikibot.Site('pool','wikitolearn')
        for dirpath, dirnames, filenames in os.walk("/opt/input/"):
            for filename in filenames:
                file_full_name = os.path.join(dirpath, filename)
                print("File: {}".format(file_full_name))
                with open(file_full_name) as f:
                    content = '\n'.join(f.readlines())
                    f.close()
                    for math in wtlpywikibot.extract_math(content):
                        print(math)
                        try:
                            wtlpywikibot.check_formula(site,math)
                        except Exception as e:
                            print(e)
    else:
        print("Missing input/ dir")

if config['checktype'] == "remote":
    site = pywikibot.Site(config['lang'],'wikitolearn')
    pages_to_check = []
    root_page = pywikibot.Page(site,config['rootpage'])
    pages_to_check.append(root_page)
    if config['includesubpages']:
        for all_page_item in site.allpages(namespace=root_page.namespace()):
            if all_page_item.title().startswith(root_page.title()) and \
                all_page_item.title() != root_page.title():
                pages_to_check.append(all_page_item)

    for page_to_check in pages_to_check:
        print("Check for {}".format(page_to_check.title()))
        for math in wtlpywikibot.extract_math(page_to_check.text):
            print("Formula:")
            print(math)
            try:
                print("Status: {}".format(wtlpywikibot.check_formula(site,math)))
            except Exception as e:
                print(e)
