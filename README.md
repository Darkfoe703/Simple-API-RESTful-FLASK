# Simple API with FLASK

Is a simple API implementation with Flask and PostgreSQL database. 

    from  flask  import  Flask
    from  flask_restful  import  Api

Have 2 resources: employees and tasks, requested in JSON format

    api  =  Api(app)
    api.add_resource(EmployeeResource, "/employees", "/employees/<int:employee_id>")
    api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")
Contain the `dockerfile` and `compose.yml` to create the image and deploy the api on isolated containers.

### Settings

You can modify .env file with valid field for DB. Thats is not apropiate for production environment. Take carefully.

    FLASK_ENV=development
    FLASK_DEBUG=TRUE
    FLASK_APP=app.py
    DATABASE_URL=postgresql+psycopg2://myuser:mypass@localhost:5432/task_api_db

    DATABASE_URL_DOCK=postgresql+psycopg2://myuser:mypass@db:5432/task_api_db
    POSTGRES_USER=myuser
    POSTGRES_PASS=mypass
    POSTGRES_DB=task_api_db


## Usage
The results are paginated: 5 tasks per page by default:

    curl -X GET http://localhost:5000/tasks

If you need, can use other pagination or indicate a specific page:

    http://localhost:5000/tasks?page=1&per_page=10

Create employee:

    curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5000/employees

Create task:

    curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 1", "description": "Description of Task 1", "employee_id": 1}' http://localhost:5000/tasks
Update or modify a task:

    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "Updated description", "employee_id": 1}' http://localhost:5000/tasks/1

Delete task (or employee)

    curl -X DELETE http://localhost:5000/tasks/1

