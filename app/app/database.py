#
#
#

from typing import Optional, Type, TypeVar

from app.extensions import db

T = TypeVar('T', bound='PKModel')

Column = db.Column
relationship = db.relationship

#
#
#
class CRUDMixin(object):
    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            db.session.commit()
        return self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit: bool = True) -> None:
        db.session.delete(self)
        if commit:
            return db.session.commit()
        return

#
#
#
class Model(CRUDMixin, db.Model):
    __abstract__ = True

#
#
#
class PKModel(Model):
    __abstract__ = True

    id = Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls: Type[T], record_id) -> Optional[T]:
        if isinstance(record_id, (int, float)):
            return cls.query.get(int(record_id))
        return None

#
#
#
def reference_col(tablename, nullable=False, pk_name="id", foreign_key_kwargs=None, column_kwargs=None):
    foreign_key_kwargs = foreign_key_kwargs or {}
    column_kwargs = column_kwargs or {}
    return Column(db.ForeignKey(column), **foreign_key_kwargs, nullable=nullable, **column_kwargs)
