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

def check_subpages(pages, site):
    re_mw_link = re.compile(r"\[\[(.*?)\]\]")
    for page in pages:
        page = pywikibot.Page(page, site)
        for match in re_mw_link.finditer(page.text):
            link = match.group(1)
            if link.count("/") is not 2:
                print(link + "is malformed, abort everything")


def main(mode, prefix):
    site = pywikibot.Site()
    site.login()
    BASE_SITE = site.family.langs[config.mylang]
    site.throttle.setDelays(1, 1, True)
    print("Base URL: " + BASE_SITE)

    if mode.startswith('a'):
        print("Getting subpages...")
        subpages = rename_subpages_strings(prefix, site)
        #subpages.append(prefix+ "|Course:"+prefix)
        if mode == "au":  #output to file, hardcoded path for now, not much we need
            pageFile = open('/w2lbot/pages/' + prefix, 'w')
        for r in subpages:
            if mode == "au":
                pageFile.write(r + "\n")
            print(r)
        pageFile.write(prefix+ "|Course:"+prefix)
        if mode == "au":
            pageFile.close()

    elif mode == "b":
        print("Fixing sections...")
        fix_first_level(prefix, site)
    elif mode == "c":
        pg = rename_subpages_dict(prefix, site)
    elif mode == "check":
        pages = get_subpages_list(prefix, site)
        check_subpages(pages, site)
