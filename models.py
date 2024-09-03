from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class StatusEnum(Enum):
    UNASSIGNED = "Unassigned"
    ASSIGNED = "Assigned"
    PENDING = "Pending"
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship("Task", backref="employee", lazy=True)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.name"), nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default=StatusEnum.UNASSIGNED)
