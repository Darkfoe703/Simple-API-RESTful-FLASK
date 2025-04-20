from flask import render_template
from flask_restful import Api
from auth.auth import Register, Login, MeResource #LogoutResource
from resources.user import UserResource
from resources.employee import EmployeeResource
from resources.task import TaskResource

def register_routes(app):
    api = Api(app)

    # Auth
    api.add_resource(Register, "/register")
    api.add_resource(Login, "/login")
    api.add_resource(MeResource, "/me")
    # api.add_resource(LogoutResource, "/logout")

    # API Resources
    api.add_resource(UserResource, "/users", "/users/<int:user_id>")
    api.add_resource(EmployeeResource, "/employees", "/employees/<int:employee_id>")
    api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")

    @app.route("/")
    def index():
        return render_template("index.html")
