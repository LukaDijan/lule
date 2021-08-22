from sqlalchemy.dialects.postgresql import UUID

from .base import db


class Material(db.Model):
    __tablename__ = "materials"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    format = db.Column(db.String(), nullable=True)
    college_id = db.Column(UUID, db.ForeignKey("colleges.id"))
