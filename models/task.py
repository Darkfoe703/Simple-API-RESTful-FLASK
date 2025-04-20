from . import db
from enum import Enum

class StatusEnum(Enum):
    UNASSIGNED = "Unassigned"
    ASSIGNED = "Assigned"
    PENDING = "Pending"
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(
        db.Enum(StatusEnum), nullable=False, default=StatusEnum.UNASSIGNED
    )
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
