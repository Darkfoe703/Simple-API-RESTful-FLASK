# TODO:
#   - paginación DONE
#   - Add JWT access DONE
#   - __init__.detección automática de modelos ??
#   - Documentación  ?
# If you need create db

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from routes import register_routes


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

register_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
