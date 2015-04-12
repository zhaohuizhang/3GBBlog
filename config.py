#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

# whoosh base
WHOOSH_BASE = os.path.join(basedir,'search.db')
MAX_SEARCH_RESULTS = 50

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PROT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'zhaohuizhang90@gmail.com'
MAIL_PASSWORD = 'zhang1990'

# administrator list
ADMINS = ['zhaohuizhang90@gmail.com']

# pagination
POSTS_PER_PAGE = 3

CSRF_ENABLED = True
SECRET_KEY = 'hello world!'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]