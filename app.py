# TODO:
#     - paginación DONE
#     - Documentación  ?
# If you need create db
import psycopg2
from psycopg2 import sql

from flask import Flask, render_template
from flask_restful import Api
from models import db
from config import Config
from resources.employee import EmployeeResource
from resources.task import TaskResource
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template("index.html")
# endpoints
api = Api(app)
api.add_resource(EmployeeResource, "/employees", "/employees/<int:employee_id>")
api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
