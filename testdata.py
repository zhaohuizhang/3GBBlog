#!flask/bin/python

from app import db, models, mail, app
import datetime
from flask.ext.mail import Message
from config import ADMINS

# u = models.User(nickname='john', email='john@gmail.com', role=models.ROLE_USER)
# db.session.add(u)

# u = models.User(nickname='susan', email='susan@email.com', role=models.ROLE_USER)
# db.session.add(u)
# db.session.commit()
# python -m smtpd -n -c DebuggingServer localhost:25

# users = models.User.query.all()
# print users
# for u in users:
# 	print u.id, u.nickname
# u = models.User.query.get(1)
# p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)

# db.session.add(p)
# db.session.commit()

# u = models.User.query.get(1)
# posts = u.posts.all()
# print posts

# users = models.User.query.all()
# for u in users:
# 	db.session.delete(u)
# posts = models.Post.query.all()
# for p in posts:
# 	db.session.delete(p)

# db.session.commit()

msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
msg.body = 'test  body'
msg.html = '<b> HTML </b> body'
with app.app_context():
	mail.send(msg)