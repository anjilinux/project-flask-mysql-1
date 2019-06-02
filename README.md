# flask-mysql-docker-api
Python/Flask tasks API using a Docker container and remotely hosted MySQL database.

### Project Setup
```
docker-compose up --build
```

### Methods
**Get (all) Tasks**
- GET: http://localhost:5000

**Create Task**
- POST: http://localhost:5000/?taskName=[TASK_NAME]

**Get Task**
- GET: http://localhost:5000/[TASK_ID]

**Update Task**
- PATCH: http://localhost:5000/[TASK_ID]?taskName=[TASK_NAME]

**Delete Task**
- DELETE: http://localhost:5000/[TASK_ID]
