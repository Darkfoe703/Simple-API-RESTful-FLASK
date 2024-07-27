from flask import request
from flask_restful import Resource
from models import db, Employee


class EmployeeResource(Resource):
    def get(self):
        employees = Employee.query.all()
        return [{"id": emp.id, "name": emp.name} for emp in employees], 200

    def post(self):
        data = request.get_json()
        new_employee = Employee(name=data["name"])
        db.session.add(new_employee)
        db.session.commit()
        return {"id": new_employee.id, "name": new_employee.name}, 201
