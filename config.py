import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(".env.dev")
load_dotenv(dotenv_path, override=True)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "DATABASE_URL",
    )
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
