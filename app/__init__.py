#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PROT, MAIL_USERNAME, MAIL_PASSWORD
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

mail = Mail(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app,os.path.join(basedir,'tmp'))

if not app.debug:
	import logging
	from logging.handlers import SMTPHandler, RotatingFileHandler
	# credentials = None
	# if MAIL_USERNAME or MAIL_PASSWORD:
	# 	credentials = (MAIL_USERNAME,MAIL_PASSWORD)
	# mail_handler = SMTPHandler((MAIL_SERVER,MAIL_PROT), 'no-reply@' + MAIL_SERVER, ADMINS[0], 'blog failure', credentials)
	# app.logger.addHandler(mail_handler)
	
	file_handler = RotatingFileHandler('tmp/blog.log','a', 1*1024*1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('blog startup')

from app import views,models