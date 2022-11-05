#
#
#

from celery import Celery
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf import CSRFProtect

celery = Celery()
login_manager = LoginManager()
migrate = Migrate()
db = SQLAlchemy()
flask_static_digest = FlaskStaticDigest()
csrf_protect = CSRFProtect()
