#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from collections import OrderedDict
import json
import markdown as md


# import jinja_custom_filters as jcf

ext_config = {'markdown.extensions.toc': {},
              'markdown.extensions.attr_list': {},
              'markdown_include.include': {},
              'markdown.extensions.tables': {}}


def get_modules(value):
    print('USING GET_MODULES FILTER')
    settings_list = []
    for module in os.listdir(value):
        try:
            with open(os.path.join(value, module, 'module_settings.json'), 'r') as fp:
                settings_list.append(json.load(fp, object_pairs_hook=OrderedDict))
        except NotADirectoryError:
            pass
    return settings_list


def print_to_console(value):
    print(value)


def load_json(value):
    print('USING LOAD_JSON FILTER')
    try:
        with open(value, 'r') as fp:
            return json.load(fp, object_pairs_hook=OrderedDict)
    except TypeError:
        return value


def parse_markdown(value):
    print('USING PARSE_MARKDOWN FILTER')
    exts = []
    for key, item in ext_config.items():
        exts.append(key)
    try:
        with open(value, 'r') as fp:
            html = md.markdown(fp.read(), extensions=exts, extension_configs=ext_config)
            return html
    except FileNotFoundError:
        print(value, ' NOT FOUND')
        pass



AUTHOR = 'Georgia Stuart'
SITENAME = 'UT Dallas WeTeach_CS Collaborative'
SITEURL = ''

MODULE_ROOT = "modules/"

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'papers', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/.nojekyll': {'path': '.nojekyll'}}

INDEX_SAVE_AS = 'blog_index.html'
THEME = 'utdweteachcs_theme'
THEME_STATIC_DIR = 'static'

MARKDOWN = {'extension_configs': ext_config}

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.do']}

JINJA_FILTERS = {'get_modules': get_modules, 'load_json': load_json, 'print': print_to_console,
                 'parse_markdown': parse_markdown}

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
SOCIAL = (('Email', 'mailto:georgia.stuart@utdallas.edu', 'fa-envelope'),
          ('Facebook', 'https://www.facebook.com/utdweteachcs/', 'fa-facebook-square'),
          ('Twitter', 'https://twitter.com/utdweteachcs/', 'fa-twitter'),
          ('Instagram', 'https://www.instagram.com/utdweteachcs/', 'fa-instagram'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
