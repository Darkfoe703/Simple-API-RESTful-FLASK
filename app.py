# TODO:
#     - paginación DONE
#     - API gui y formularios
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

# # Crear base de datos si no existe
# def create_database():
#     conn = psycopg2.connect(
#         dbname="postgres",  # Conéctate a la base de datos por defecto
#         user="postgres",
#         password="vaallover15",
#         host="localhost",
#     )
#     conn.autocommit = True
#     cursor = conn.cursor()

#     # Verifica si la base de datos existe, si no la crea
#     cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'task_api_db'")
#     exists = cursor.fetchone()
#     if not exists:
#         cursor.execute(
#             sql.SQL("CREATE DATABASE {}").format(sql.Identifier("task_api_db"))
#         )
#         print("Base de datos task_api_db creada con éxito.")
#     cursor.close()
#     conn.close()

# # Llamar a la función para crear la base de datos si no existe
# create_database()

@app.route("/")
def index():
    return render_template("index.html")

api = Api(app)
api.add_resource(EmployeeResource, "/employees", "/employees/<int:employee_id>")
api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
