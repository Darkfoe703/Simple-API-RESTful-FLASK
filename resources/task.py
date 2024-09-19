from flask import request
from flask_restful import Resource
from models import db, Task
import json


class TaskResource(Resource):
    def get(self):
        # Pagination parameter from URL
        # First page, default 1
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get(
            "per_page", 5, type=int
        )  # Defalut 5 items per page

        # Paginated query
        paginated_tasks = Task.query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        # Crete response
        return {
            "tasks": [
                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "employee_id": task.employee_id,
                    "status": json.dumps(task.status, default=lambda x: x.name),
                }
                for task in paginated_tasks.items
            ],
            "total": paginated_tasks.total,  # Total tasks
            "page": paginated_tasks.page,  # actual page
            "per_page": paginated_tasks.per_page,
            "total_pages": paginated_tasks.pages,
            "has_next": paginated_tasks.has_next,
            "has_prev": paginated_tasks.has_prev,
        }, 200

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
            "status": json.dumps(new_task.status, default=lambda x: x.name),
        }, 201

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data["title"]
        task.description = data.get("description")
        task.employee_id = data["employee_id"]
        task.status = data["status"]
        db.session.commit()
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "employee_id": task.employee_id,
            "status": json.dumps(task.status, default=lambda x: x.name),
        }, 200

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {}, 204
