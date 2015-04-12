#!flask/bin/python

from migrate.versioning import api
from config import SQLALCHMEY_DATABASE_URI, SQLALCHMEY_MIGRATE_REPO

v = api.db_version(SQLALCHMEY_DATABASE_URI,SQLALCHMEY_MIGRATE_REPO)
api.downgrade(SQLALCHMEY_DATABASE_URI,SQLALCHMEY_MIGRATE_REPO,v-1)

print 'Current database version: ' + str(api.db_version(SQLALCHMEY_DATABASE_URI,SQLALCHMEY_MIGRATE_REPO))