# TODO:
#   - pagination DONE
#   - Add JWT access DONE
#   - Add versions  DONE
#   - __init__.detección automática de modelos ??
#   - Documentación  <--
#   - Token: limits and protection
#   - CI/CD

# If you need create db
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from routes import register_routes
from flasgger import Swagger
import os, yaml
from os.path import join, dirname

app = Flask(__name__)
app.config.from_object(Config)

with open(join(dirname(__file__), "docs/swagger_config.yml"), "r") as f:
    swagger_config = yaml.safe_load(f)
with open(join(dirname(__file__), "docs/swagger_template.yml"), "r") as f:
    swagger_template = yaml.safe_load(f)

swagger = Swagger(app, config=swagger_config, template=swagger_template)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

register_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
