# Readme

## Description

This bot deletes all the pages with the indicated Prefix in the url.

## Config File

the config file has to be named `config.yaml` and has to be in `./src/` directory. It is 
gitignored, since it contains the user password and it strongly depends on the admin needs. There 
is a `config-template.yaml` that contains the scehme of the config file.

* `$lang` contains what domain the bot should upload the pages to, the complete list is [here](https://github.com/WikiToLearn/pywikibot/blob/master/wikitolearn_family.py)
* `$username` and `$password` contains the credentials that the bot should use to upload the pages the website,
* `$namespace` contains the namespace of the paegs that the admin wants to delete. It is `0` for "no specific template"
* `$prefix` : all this bot magic happens here. The admin should chose properly this parameter, since it governs this bot behaviuor. This bot wll delete every page whose link is of the form 
`$lang.$domain/$prefix*`

`./src` Contains an example, `config-example.yaml`,  to help understanding the config file. If this were `config.yaml`, it would remove all the pages whose link is 
"https://it.wikitolearn.vodka/Loreti-Teoria_degli_errori_e_Fondamenti_di_statistica/*"

## Build

You need a working docker engine to run this bot

Build the docekr image

	docker build -t wikitolearn/delete-pages-prefix .

The first time you run this it may take some time, since it has to pull the wikitolearn/pywikibot docker image

## Run

run the script with

	docker run -ti --rm wikitolearn/delete-pages-prefix
