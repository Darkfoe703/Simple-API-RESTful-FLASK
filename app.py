from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources.employee import EmployeeResource
from resources.task import TaskResource

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

api = Api(app)
api.add_resource(EmployeeResource, "/employees")
api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
