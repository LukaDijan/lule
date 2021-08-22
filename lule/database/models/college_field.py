from sqlalchemy.dialects.postgresql import UUID

from .base import db


class CollegeField(db.Model):
    __tablename__ = "college_field"

    college_id = db.Column(UUID, db.ForeignKey("colleges.id"))
    field_id = db.Column(UUID, db.ForeignKey("fields.id"))
