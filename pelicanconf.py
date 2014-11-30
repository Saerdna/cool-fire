#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saerdna'
SITENAME = u'cool-fire'
#SITEURL = 'http://saerdna.github.io/'

USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Shanghai'
#NUM_FULL_ARTICLES = 100
DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
#THEME = 'bootstrap2'
RELATIVE_URLS = True


ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'posts/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}.html'

DISQUS_SITENAME = 'coolfire'
GOOGLE_ANALYTICS = 'UA-43474657-1'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('http://weibo.com/saerdna13', 'Weibo'),
        ('https://plus.google.com/105858506209398295278', 'Google plus'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
