from flask import request
from flask_restful import Resource
from models import db, Task


class TaskResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "employee_id": task.employee_id,
            }
            for task in tasks
        ], 200

    def post(self):
        data = request.get_json()
        new_task = Task(
            title=data["title"],
            description=data.get("description"),
            employee_id=data["employee_id"],
        )
        db.session.add(new_task)
        db.session.commit()
        return {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "employee_id": new_task.employee_id,
        }, 201

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data["title"]
        task.description = data.get("description")
        task.employee_id = data["employee_id"]
        db.session.commit()
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "employee_id": task.employee_id,
        }, 200

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {}, 204
