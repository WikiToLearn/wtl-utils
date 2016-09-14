# -*- coding: utf-8 -*-
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import re
import time

config = __import__("user-config")

def get_subpages_list(prefix, site, redirects=False):
    pages = [x.title() for x in pg.PrefixingPageGenerator(prefix,
                                        site=site, includeredirects=redirects)]
    subpages = []
    for p in pages:
        if p.find("/") >=0 :
            sub = p[p.find("/"):]
            subpages.append(sub)
    return subpages

def rename_subpages_strings(prefix, site):
    subpages = get_subpages_list(prefix, site)
    result = [ prefix+ x + "|Course:"+ prefix + x for x in subpages]
    return result

def rename_subpages_dict(prefix, site):
    subpages = get_subpages_list(prefix, site)
    result = {}
    for p in subpages:
        result[p] = "Course:"+ p
    return result

def move_pages(pages, site):
    for p in pages:
        title, newtitle = p.split("|")
        page = pywikibot.Page(site, title)
        print("Moving page: {}".format(title))
        page.move(newtitle, reason="Courses moving", deleteAndMove=False, safe=True)

def fix_first_level(prefix, site):
    r = re.compile(r"\[\[(.*?)\]\]")
    pages = get_subpages_list(prefix,site)
    for p in pages:
        spl = p.split("/")
        if not len(spl)>2:
            print("Checking page: "+ prefix+"/"+spl[1])
            path = prefix +"/"+ spl[1]
            page = pywikibot.Page(site, path)
            text = page.text
            newtext = text
            for m in r.finditer(text):
                if("Course:" not in m.group(1) and "Corso:"  not in m.group(1)):
                    newtext = newtext.replace(m.group(0), "[[Course:"+m.group(1)+ "]]")
            page.text = newtext
            page.save()

def replace_urls(repl_urls, site):
    for p in repl_urls:
        page = pywikibot.Page(p, site)
        for pin in page.backlinks(followRedirects=True, namespaces="NS_COURSE", step=10, content=False):
            pass


def main(mode, prefix):
    site = pywikibot.Site()
    site.login()
    BASE_SITE = site.family.langs[config.mylang]
    site.throttle.setDelays(1, 1, True)
    print("Base URL: " + BASE_SITE)

    if mode == 'a':
        print("Getting subpages...")
        rn = rename_subpages_strings(prefix, site)
        rn.append(prefix+ "|Course:"+prefix)
        for r in rn:
            print(r)
    elif mode == "b":
        print("Fixing sections...")
        fix_first_level(prefix, site)
    elif mode == "c":
        pg = rename_subpages_dict("Course:Spazi_di_Hilbert", site)
