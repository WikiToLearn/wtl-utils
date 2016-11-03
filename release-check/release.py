#!/usr/bin/env python3
import requests
from pprint import pprint
import sys
import os
import os.path
import json

from pprint import pprint

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
    print(subdomain)

    response = requests.get("https://{}{}/api.php?action=query&meta=siteinfo&siprop=statistics&format=json".format(subdomain,domain))
    if 'Content-Type' in response.headers and response.headers['Content-Type']=="application/json; charset=utf-8":
        file_name = data_dir+subdomain+domain+"-siteinfo.json"
        if first_run:
            text_file = open(file_name, "wb")
            text_file.write(response.content)
            text_file.close()
        else:
            old_data = {}
            with open(file_name) as old_file:
                old_data = json.load(old_file)
                old_file.close()
            statistics = response.json()['query']['statistics']
            statistics_old = old_data['query']['statistics']

            status = True
            for label in ['activeusers','admins','articles','edits','images','jobs','pages','users']:
                partial_status = statistics[label] >= statistics_old[label]
                if not partial_status:
                    print("{}: {} = {} ({})".format(label,statistics[label],statistics_old[label],partial_status))
                status = status and partial_status
            print("\tStatus stats: {}".format(status))
            global_status = global_status and status

    response = requests.get("https://{}{}/api.php?action=query&list=recentchanges&rcprop=title%7Cids%7Csizes%7Cflags%7Cuser&rclimit=100&format=json".format(subdomain,domain))
    if 'Content-Type' in response.headers and response.headers['Content-Type']=="application/json; charset=utf-8":
        file_name = data_dir+subdomain+domain+"-changes.json"
        if first_run:
            text_file = open(file_name, "wb")
            text_file.write(response.content)
            text_file.close()
        else:
            old_data = {}
            with open(file_name) as old_file:
                old_data = json.load(old_file)
                old_file.close()

            recentchanges_new = []
            for c in response.json()['query']['recentchanges']:
                if c['user']!="Maintenance script":
                    recentchanges_new.append(c)

            recentchanges_old = []
            for c in old_data['query']['recentchanges']:
                if c['user']!="Maintenance script":
                    recentchanges_old.append(c)

            status_changed = True
            for i in range(0,min([
                                    len(recentchanges_new),
                                    len(recentchanges_old),
                                ])):
                status = True
                for key in recentchanges_new[i]:
                    val_old = None
                    val_new = None
                    if key in recentchanges_new[i]:
                        val_new = recentchanges_new[i][key]
                    if key in recentchanges_old[i]:
                        val_old = recentchanges_old[i][key]
                    status = (status and val_old==val_new)
                status_changed = status_changed and status
            print("\tStatus changes: {}".format(status_changed))
            global_status = global_status and status_changed



print("Global status: {}".format(global_status))
