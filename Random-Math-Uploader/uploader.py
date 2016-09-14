#!/usr/bin/python
# -*- coding: utf-8  -*-
from __future__ import absolute_import, unicode_literals

__version__ = '$Id$'
#

import codecs
import os
import re

from warnings import warn

import pywikibot

from pywikibot import config, Bot
from pywikibot.exceptions import ArgumentDeprecationWarning

import random

def generatePage():
    tokens = ["+","-","\\lor","\\land","\\alpha","\\diamond","\\cup","\\cap","\\int","\\sum _{|x_ i - E(x)| \\geq \\epsilon }","\\mu _4 = E \\left\\{  \\bigl [ x - E(x) \\bigr ]^4 \\right\\}"];
    page = ""

    for x in range(0,10): #quante pag
        page += "\nxxxx\n"
        page += ("'''" + str(random.choice(range(1, 100000))) + "'''\n")
        for i in range(0,50): #quante righe
            line = "<dmath> " 
            for j in range(0,15): #quanti token per riga
                line += random.choice(tokens)
                line += " "
                line += str(random.choice(range(1, 100)))
            line += "</dmath>"    
            page += line
            page += "\n"
        page += "\nyyyy\n"
    return page

class NoTitle(Exception):

    """No title found."""

    def __init__(self, offset):
        """Constructor."""
        self.offset = offset


class PageFromFileRobot(Bot):

    """
    Responsible for writing pages to the wiki.

    Titles and contents are given by a PageFromFileReader.

    """

    def __init__(self, reader, **kwargs):
        """Constructor."""
        self.availableOptions.update({
            'always': True,
            'force': False,
            'append': None,
            'summary': None,
            'minor': False,
            'autosummary': False,
            'nocontent': '',
            'redirect': True,
            'showdiff': False,
        })

        super(PageFromFileRobot, self).__init__(**kwargs)
        self.availableOptions.update(
            {'always': False if self.getOption('showdiff') else True})
        self.reader = reader

    def run(self):
        """Start file processing and upload content."""
        for title, contents in self.reader.run():
            self.save(title, contents)

    def save(self, title, contents):
        """Upload page content."""
        mysite = pywikibot.Site()

        page = pywikibot.Page(mysite, title)
        self.current_page = page

        if self.getOption('summary'):
            comment = self.getOption('summary')
        else:
            comment = ""

        comment_top = ""
        comment_bottom = ""
        comment_force = "%s *** %s ***" % (
            comment, "")

        # Remove trailing newlines (cause troubles when creating redirects)
        contents = re.sub('^[\r\n]*', '', contents)

        if page.exists():
            if not self.getOption('redirect') and page.isRedirectPage():
                pywikibot.output(u"Page %s is redirect, skipping!" % title)
                return
            pagecontents = page.get(get_redirect=True)
            nocontent = self.getOption('nocontent')
            if nocontent and (
                    nocontent in pagecontents or
                    nocontent.lower() in pagecontents):
                pywikibot.output('Page has %s so it is skipped' % nocontent)
                return
            if self.getOption('append'):
                separator = self.getOption('append')[1]
                if separator == r'\n':
                    separator = '\n'
                if self.getOption('append')[0] == 'top':
                    above, below = contents, pagecontents
                    comment = comment_top
                else:
                    above, below = pagecontents, contents
                    comment = comment_bottom
                pywikibot.output('Page {0} already exists, appending on {1}!'.format(
                                 title, self.getOption('append')[0]))
                contents = above + separator + below
            elif self.getOption('force'):
                pywikibot.output(u"Page %s already exists, ***overwriting!"
                                 % title)
                comment = comment_force
            else:
                pywikibot.output(u"Page %s already exists, not adding!" % title)
                return
        else:
            if self.getOption('autosummary'):
                comment = ''
                config.default_edit_summary = ''

        self.userPut(page, page.text, contents,
                     summary=comment,
                     minor=self.getOption('minor'),
                     show_diff=self.getOption('showdiff'),
                     ignore_save_related_errors=True)


class PageFromFileReader(object):

    """
    Responsible for reading the file.

    The run() method yields a (title, contents) tuple for each found page.

    """

    def __init__(self, filename, pageStartMarker, pageEndMarker,
                 titleStartMarker, titleEndMarker, include, notitle):
        """Constructor.

        Check if self.file name exists. If not, ask for a new filename.
        User can quit.

        """
        self.filename = filename
        self.pageStartMarker = pageStartMarker
        self.pageEndMarker = pageEndMarker
        self.titleStartMarker = titleStartMarker
        self.titleEndMarker = titleEndMarker
        self.include = include
        self.notitle = notitle

    def run(self):
        """Read file and yield page title and content."""
        #pywikibot.output('\n\nReading \'%s\'...' % self.filename)
        try:
            text = generatePage()

        except IOError as err:
            pywikibot.output(str(err))
            raise IOError

        position = 0
        length = 0
        while True:
            try:
                length, title, contents = self.findpage(text[position:])
            except AttributeError:
                if not length:
                    pywikibot.output(u'\nStart or end marker not found.')
                else:
                    pywikibot.output(u'End of file.')
                break
            except NoTitle as err:
                pywikibot.output(u'\nNo title found - skipping a page.')
                position += err.offset
                continue

            position += length
            yield title, contents

    def findpage(self, text):
        """Find page to work on."""
        pageR = re.compile(re.escape(self.pageStartMarker) + "(.*?)" +
                           re.escape(self.pageEndMarker), re.DOTALL)
        titleR = re.compile(re.escape(self.titleStartMarker) + "(.*?)" +
                            re.escape(self.titleEndMarker))

        location = pageR.search(text)
        if self.include:
            contents = location.group()
        else:
            contents = location.group(1)
        try:
            title = titleR.search(contents).group(1)
            if self.notitle:
                # Remove title (to allow creation of redirects)
                contents = titleR.sub('', contents, count=1)
        except AttributeError:
            raise NoTitle(location.end())
        else:
            return location.end(), title, contents


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: list of unicode
    """
    # Adapt these to the file you are using. 'pageStartMarker' and
    # 'pageEndMarker' are the beginning and end of each entry. Take text that
    # should be included and does not occur elsewhere in the text.

    # TODO: make config variables for these.
    filename = "dict.txt"
    pageStartMarker = "{{-start-}}"
    pageEndMarker = "{{-stop-}}"
    titleStartMarker = u"'''"
    titleEndMarker = u"'''"
    options = {}
    include = False
    notitle = False

    for arg in pywikibot.handle_args(args):
        if arg.startswith('-start:'):
            pageStartMarker = arg[7:]
            warn('-start param (text that marks the beginning) of a page has been '
                 'deprecated in favor of begin; make sure to use the updated param.',
                 ArgumentDeprecationWarning)
        elif arg.startswith('-begin:'):
            pageStartMarker = arg[len('-begin:'):]
        elif arg.startswith("-end:"):
            pageEndMarker = arg[5:]
        elif arg.startswith("-file:"):
            filename = arg[6:]
        elif arg == "-include":
            include = True
        elif arg.startswith('-appendbottom'):
            options['append'] = ('bottom', arg[len('-appendbottom:'):])
        elif arg.startswith('-appendtop'):
            options['append'] = ('top', arg[len('-appendtop:'):])
        elif arg == "-force":
            options['force'] = True
        elif arg == "-safe":
            options['force'] = False
            options['append'] = None
        elif arg == "-noredirect":
            options['redirect'] = False
        elif arg == '-notitle':
            notitle = True
        elif arg == '-minor':
            options['minor'] = True
        elif arg.startswith('-nocontent:'):
            options['nocontent'] = arg[11:]
        elif arg.startswith("-titlestart:"):
            titleStartMarker = arg[12:]
        elif arg.startswith("-titleend:"):
            titleEndMarker = arg[10:]
        elif arg.startswith("-summary:"):
            options['summary'] = arg[9:]
        elif arg == '-autosummary':
            options['autosummary'] = True
        elif arg == '-showdiff':
            options['showdiff'] = True
        else:
            pywikibot.output(u"Disregarding unknown argument %s." % arg)

    """failed_filename = False
    while not os.path.isfile(filename):
        pywikibot.output('\nFile \'%s\' does not exist. ' % filename)
        _input = pywikibot.input(
            'Please enter the file name [q to quit]:')
        if _input == 'q':
            failed_filename = True
            break
        else:
            filename = _input

    # show help text from the top of this file if reader failed
    # or User quit.
    if failed_filename:
        pywikibot.bot.suggest_help(missing_parameters=['-file'])
        return False
    else:"""
    reader = PageFromFileReader(filename, pageStartMarker, pageEndMarker,
                                titleStartMarker, titleEndMarker, include,
                                notitle)
    bot = PageFromFileRobot(reader, **options)
    bot.run()

if __name__ == "__main__":
    main()