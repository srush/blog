#!/usr/bin/env python
# -*- coding: utf-8 -*- #


MARKUP = ('md', 'html')

from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid]

IGNORE_FILES = [".ipynb_checkpoints"]

AUTHOR = 'Sasha Rush'
SITENAME = 'Sasha Rush'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Theme
THEME = 'MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2020
MINIMALXY_CURRENT_YEAR = 2020 #date.today().year

# Author
AUTHOR_INTRO = u'Sasha Rush. Professor at Cornell Tech and researcher at Hugging Face. This blog collects some of my sporadic literate coding projects. All notebooks are available at https://github.com/srush/blog/'
AUTHOR_DESCRIPTION = u'Sasha Rush. Professor at Cornell Tech and researcher at Hugging Face. This blog collects some of my sporadic literate coding projects. All notebooks are available at https://github.com/srush/blog/'
AUTHOR_AVATAR = 'https://avatars0.githubusercontent.com/u/35882?s=460&v=4'
AUTHOR_WEB = 'http://rush-nlp.com'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'blog-rush-nlp-com'

# Social
SOCIAL = (
    ('twitter', 'http://twitter.com/srush_nlp'),
    ('github', 'https://github.com/srush'),
    ('linkedin', 'https://www.linkedin.com/in/sasha-rush-a69b6917/'),
)

# Menu
MENUITEMS = (
#    ('Categories', '/' + CATEGORIES_SAVE_AS),
#    ('Archive', '/' + ARCHIVES_SAVE_AS),
)
