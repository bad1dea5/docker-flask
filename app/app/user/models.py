#
#
#

import datetime

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from app.database import Column, PKModel, db, reference_col, relationship
from app.utilities.password import check_password, generate_password

#
#
#
class User(UserMixin, PKModel):
    __tablename__ = 'users'

    username = Column(db.String(92), unique=True, nullable=False)
    _password = Column('password', db.LargeBinary(200), nullable=True)
    timestamp = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password(value)

    def check_password(self, value):
        return check_password(self._password, value)

    def __repr__(self):
        return f'<User({self.username!r})>'
