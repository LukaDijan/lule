from sqlalchemy.dialects.postgresql import UUID

from .base import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    surname = db.Column(db.String(), nullable=True)
    college_id = db.Column(UUID, db.ForeignKey("colleges.id"))
