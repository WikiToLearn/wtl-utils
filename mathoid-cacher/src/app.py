# -*- coding: utf-8 -*-
import wtlpywikibot
import pywikibot
import pywikibot.pagegenerators as pg
import sys
import os
import yaml
import re
import time
import requests


stream = open('config.yaml', 'r')
config = yaml.load(stream, Loader=yaml.Loader)
lang = os.environ.get('PYWIKIBOT_LANG')
user = config["pywikibot"]["user"]
passw = config["pywikibot"]["password"]


current_page = ''
n_page = 0

def check_page(page,lang):
    r = re.compile('<\s*math\s*(type=\s*"?block"?)?\s*>(?P<math>.*?)</math>', re.DOTALL)
    for m in r.finditer(page.text):
        math = m.group("math")
        request_formula(math,lang)

def request_formula(tex,lang):
    url_check = 'http://restbase.wikitolearn.org/'+\
            lang + '.wikitolearn.org/v1/media/math/check/tex'
    header= {'Accept':'application/json',
             'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'q': tex}
    r = requests.post(url_check, data=payload, headers = header)
    if r.status_code == 200:
        print(n_page, ") ", current_page,": ", tex)
        loc = r.headers['x-resource-location']
        url_render = 'http://restbase.wikitolearn.org/'+\
                lang + '.wikitolearn.org/v1/media/math/render/'
        header_render1= {'Accept':'image/svg+xml',
                 'Content-Type': 'application/x-www-form-urlencoded'}
        header_render2= {'Accept':'image/mathml+xml',
                 'Content-Type': 'application/x-www-form-urlencoded'}
        r_svg = requests.get(url_render+"svg/"+loc, headers = header_render1)
        r_mathml = requests.get(url_render+"mml/"+loc, headers = header_render2)
        print("\t\tRendering svg: " ,r_svg.status_code)
        print("\t\tRendering mml: " ,r_mathml.status_code)
    else:
        print("\t\tPage rendering error: ", r.status_code)


def main():
    site = pywikibot.Site(lang, "wikitolearn")
    wtlpywikibot.login(site,user,passw)
    print("Lang: " + lang )

    checkedPages = 0
    print("Checking all pages")
    for page in pg.AllpagesPageGenerator(site=site, step=30,namespace=2800):
        global current_page
        current_page =  page.title()
        print("\n@page: " + current_page + "")
        check_page(page,lang)
        checkedPages+=1
        global n_page
        n_page+=1
    print("Checked " + str(checkedPages) + " pages")


if __name__ == "__main__":
	main()
