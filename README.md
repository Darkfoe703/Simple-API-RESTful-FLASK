# Simple API with FLASK

Is a simple API implementation with Flask. 

    from  flask  import  Flask
    from  flask_restful  import  Api

Has 2 resources: employees and tasks, requested in JSON format

    api  =  Api(app)
    api.add_resource(EmployeeResource, "/employees", "/employees/<int:employee_id>")
    api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")
## Usage
Create employee:

    curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5000/employees

Create task:

    curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 1", "description": "Description of Task 1", "employee_id": 1}' http://localhost:5000/tasks
Update or modify a task:

    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "Updated description", "employee_id": 1}' http://localhost:5000/tasks/1