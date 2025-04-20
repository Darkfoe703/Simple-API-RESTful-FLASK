from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .employee import Employee
from .task import Task
from .user import User