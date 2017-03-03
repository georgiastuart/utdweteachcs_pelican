#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from collections import OrderedDict
import json

# import jinja_custom_filters as jcf


def get_headers(value):
    for index, pair in enumerate(value):
        value[index] = (x.strip() for x in pair.split(':'))
    return value


def load_json(value):
    print('Got here!')
    try:
        with open(value, 'r') as fp:
            return json.load(fp, object_pairs_hook=OrderedDict)
    except:
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
                                  'markdown_include.include': {},
                                  'markdown.extensions.tables': {}}}

JINJA_FILTERS = {'get_headers': get_headers, 'load_json': load_json}

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
SOCIAL = (  ('Email', 'mailto:georgia.stuart@utdallas.edu', 'fa-envelope'),
            ('Facebook', 'https://www.facebook.com/utdweteachcs/', 'fa-facebook-square'),
            ('Twitter', 'https://twitter.com/utdweteachcs/', 'fa-twitter'),
            ('Instagram', 'https://www.instagram.com/utdweteachcs/', 'fa-instagram'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False