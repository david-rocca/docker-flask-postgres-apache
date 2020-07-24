#Config Stuff here
DEBUG = False
THREADS_PER_PAGE = 2

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI='postgresql://postgres:changeme@db:5432/databasename'