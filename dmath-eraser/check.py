# -*- coding: utf-8 -*-
import pywikibot
import sys
import os
import re
import time

config = __import__("user-config")


def replace_dmath(page):
    if page.title().split("/")[0] == "Loreti-Teoria degli errori e Fondamenti di statistica":
        return
    '''This function make the first letter of
    filenames uppercase'''
    newtext = page.text[:]
    changed = False
    r = re.compile(r'<dmath\s*(?:type=(?P<type>.*?)\s*)?>(?P<math>.*?)</dmath>', re.DOTALL)
    for match in re.finditer(r, page.text):
        math = []
        if match.group('type'):
            t = match.group('type')
            if t.startswith('"'):
                t = t[1:]
            if t.endswith('"'):
                t= t[:-1]
            print("type: ",t)
            math.append("\\begin{"+t + "}" )
            math.append(match.group('math'))
            math.append("\\end{"+ t+"}")
        else:
            math.append(match.group('math'))
        newtext = newtext.replace(match.group(0),
                '<math display="block">'+ "".join(math) + '</math>')
        changed = True
    if changed :
        page.text = newtext
        print("\t@page "+ page.title() + " saving...")
        page.save(minor=True, botflag=True)
        global fixed
        fixed +=1


def main():
    print("Connecting to " + config.mylang + \
          " domain for the " + config.family + " family")
    site = pywikibot.Site()
    site.login()

    BASE_SITE = site.family.langs[config.mylang]
    print("Base URL: " + BASE_SITE)

    checkedPages = 0
    global fixed
    fixed = 0

    print("Checking all pages")
    for page in site.allpages(step=20):
        page_title = page.title()
        print("    @page: " + page_title + "")
        page = pywikibot.Page(site, page_title)
        replace_dmath(page)
        checkedPages+=1

    print("Checked " + str(checkedPages) + " pages")
    print("Fixed "+ str(fixed) + " pages")
