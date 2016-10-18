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
