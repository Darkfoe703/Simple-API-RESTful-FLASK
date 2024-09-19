import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:pass1234@localhost:5432/task_api_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
