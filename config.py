import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://postgres:vaallover15@localhost:5432/task_api"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
