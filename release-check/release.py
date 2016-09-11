#!/usr/bin/env python3
import requests
from pprint import pprint
import sys
import os
import os.path
import json

data_dir = "{}/data/".format(os.path.dirname(os.path.realpath(__file__)))

print(data_dir)

first_run = False
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    first_run = True

domain = ".wikitolearn.org"
subdomains = ['it', 'en', 'de', 'es', 'fr', 'pt', 'sv', 'ca', 'meta', 'pool']

global_status = True

for subdomain in subdomains:
    response = requests.get("https://{}{}/api.php?action=query&meta=siteinfo&siprop=statistics&format=json".format(subdomain,domain))
    if 'Content-Type' in response.headers and response.headers['Content-Type']=="application/json; charset=utf-8":
        print(subdomain)

        file = data_dir+subdomain+domain+".json"

        if first_run:
            text_file = open(file, "wb")
            text_file.write(response.content)
            text_file.close()
        else:
            old_data = {}
            with open(file) as old_file:
                old_data = json.load(old_file)
                old_file.close()
            statistics = response.json()['query']['statistics']
            statistics_old = old_data['query']['statistics']

            status = True
            for label in ['activeusers','admins','articles','edits','images','jobs','pages','users']:
                partial_status = statistics[label] == statistics_old[label]
                print("{}: {} = {} ({})".format(label,statistics[label],statistics_old[label],partial_status))
                status = status and partial_status
            print("Status: {}".format(status))
            global_status = global_status and status
            print()

print("Global status: {}".format(global_status))
