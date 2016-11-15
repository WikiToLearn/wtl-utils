# Readme

## Description

This bot deletes all the pages with the indicated Prefix in the url.

## Config File

the config file has to be named `config.yaml` and has to be in `./` directory. It is 
gitignored, since it contains the user password and it strongly depends on the admin needs. There 
is a `config-template.yaml` that contains the scehme of the config file.

* `$lang` contains what domain the bot should upload the pages to, the complete list is [here](https://github.com/WikiToLearn/pywikibot/blob/master/wikitolearn_family.py)
* `$username` and `$password` contains the credentials that the bot should use to upload the pages the website,
* `$namespace` contains the namespace of the paegs that the admin wants to delete. It is `0` for "no specific template", it is "Course" for pages under the Course: template. for further info browse the [mediawiki template code reference](https://www.mediawiki.org/wiki/Manual:Namespace)
* `$prefix` : all this bot magic happens here. The admin should chose properly this parameter, since it governs this bot behaviuor. This bot wll delete every page whose link is of the form 
`$lang.$domain/$prefix*`.

`./` Contains an example, `config-example.yaml`,  to help understanding the config file. If this were `config.yaml`, it would remove all the pages whose link is 
"https://it.wikitolearn.vodka/Loreti-Teoria_degli_errori_e_Fondamenti_di_statistica/*"

## Run

`./delete-pages-prefix.sh` both build and run the docker, loading the config file dynamincally, so you have to build the container just once. 
Please note that the first time you run this it may take some time, since it has to pull the wikitolearn/pywikibot docker image

## Examples

If the file `config.yaml` is
```
pywikibot :
    lang: testen
    user: UserName
    password: UserPass
namespace: Course
prefix: Complex_Analysis_(Intermediate_Level)/Cauchy's Theorem and its Consequences
```

then the bot delete the following pages

> Lang: testen
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences
> Sleeping for 7.1 seconds, 2016-11-15 11:47:27
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/Cauchy's Theorem for a disc
> Sleeping for 9.8 seconds, 2016-11-15 11:47:34
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/Cauchy Integral Formula
> Sleeping for 9.8 seconds, 2016-11-15 11:47:44
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/Compact sets
> Sleeping for 9.8 seconds, 2016-11-15 11:47:54
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/Generalities on piecewise C^1 curves
> Sleeping for 9.7 seconds, 2016-11-15 11:48:04
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/Holomorphic functions defined by integrals
> Sleeping for 9.8 seconds, 2016-11-15 11:48:14
> Deleting page: Course:Complex Analysis (Intermediate Level)/Cauchy's Theorem and its Consequences/The Fundamental Theorem of Calculus and its converse
> Sleeping for 9.8 seconds, 2016-11-15 11:48:24

