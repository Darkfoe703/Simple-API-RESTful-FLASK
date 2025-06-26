from flask import render_template, send_from_directory
from flask_restful import Api
from auth.auth import Register, Login, MeResource #LogoutResource
from resources.user import UserResource
from resources.employee import EmployeeResource
from resources.task import TaskResource

def register_routes(app):
    api = Api(app)

    # v1 prefix
    api_prefix = "/api/v1"

    # Auth
    api.add_resource(Register, f"{api_prefix}/register")
    api.add_resource(Login, f"{api_prefix}/login")
    api.add_resource(MeResource, f"{api_prefix}/me")
    # api.add_resource(LogoutResource, f"{api_prefix}/logout")

    # API Resources
    api.add_resource(UserResource, f"{api_prefix}/users", f"{api_prefix}/users/<int:user_id>")
    api.add_resource(EmployeeResource, f"{api_prefix}/employees", f"{api_prefix}/employees/<int:employee_id>")
    api.add_resource(TaskResource, f"{api_prefix}/tasks", f"{api_prefix}/tasks/<int:task_id>")

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route('/swagger-dark.css')
    def swagger_dark_css():
        return send_from_directory('static/css', 'swagger-dark.css')
