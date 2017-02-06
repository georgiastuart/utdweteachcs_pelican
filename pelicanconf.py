#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import jinja_custom_filters as jcf
import ast


def str_to_dict(value):
    for index, pair in enumerate(value):
        value[index] = (x.strip() for x in pair.split(':'))
    return value

AUTHOR = 'Georgia Stuart'
SITENAME = 'UT Dallas WeTeach_CS'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

INDEX_SAVE_AS = 'blog_index.html'
THEME = 'utdweteachcs_theme'
THEME_STATIC_DIR = 'static'

MARKDOWN = {'extension_configs': {'markdown.extensions.toc': {},
                                  'markdown.extensions.attr_list': {},
                                  'markdown_include.include': {}}}

JINJA_FILTERS = {'str2dict': str_to_dict}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False