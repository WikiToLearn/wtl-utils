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
langs = config["pywikibot"]["lang"]
user = config["pywikibot"]["user"]
passw = config["pywikibot"]["password"]


def main():
    for lang in langs:
        site = pywikibot.Site(lang, "wikitolearn")
        wtlpywikibot.login(site,user,passw)
        print("Lang: " + lang )
        ctempl = pywikibot.Page(site, "Template:CCourse")

        print(">>> CCourse fixing...")
        for p in pg.ReferringPageGenerator(ctempl,
                        followRedirects=True,withTemplateInclusion=True):
            print("> ",p.title())
            p.text = p.text.replace('{{CCourse', "{{CourseRoot")
            p.text = p.text.replace('{{SSection', "{{CourseLevelTwo")
            p.text = p.text + "\n<noinclude>[[Category:CourseRoot]]</noinclude>"
            p.save(botflag=True, minor=True, async=True)

            r = re.compile(r"{{CourseLevelTwo\|(?P<section>.*?)}}")
            for m in r.finditer(p.text):
                subp = p.title() + "/" + m.group("section")
                print(">>> SSection fixing: {}".format(subp))
                subpage = pywikibot.Page(site, subp)
                subpage.text = subpage.text + "\n<noinclude>[[Category:CourseLevelTwo]]</noinclude>"
                subpage.save(botflag=True, minor=True, async=True)


if __name__ == "__main__":
	main()
