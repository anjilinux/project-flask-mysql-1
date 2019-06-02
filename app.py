from flask import Flask, request
from flask_mysqldb import MySQL
from config import mysqlHost, mysqlUser, mysqlPassword, mysqlDb

app = Flask(__name__)

app.config['MYSQL_HOST'] = mysqlHost
app.config['MYSQL_USER'] = mysqlUser
app.config['MYSQL_PASSWORD'] = mysqlPassword
app.config['MYSQL_DB'] = mysqlDb

mysql = MySQL(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    # create task
    if request.method == 'POST':
        taskName = request.args.get('taskName')
        if not taskName:
            return 'param taskName is required to create task'
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tasks(task_name) VALUES (%s)', [taskName])
        mysql.connection.commit()
        cur.close()
        return 'POST success'
    # list all tasks
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT task_name from tasks')
        results = cur.fetchall()
        return str(results)

@app.route('/<taskId>', methods=['GET', 'PATCH', 'DELETE'])
def taskById(taskId):
    # get one task
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT task_name from tasks WHERE task_id = (%s)', [taskId])
        results = cur.fetchone()
        return str(results)
    # update task
    if request.method == 'PATCH':
        taskName = request.args.get('taskName')
        if not taskName:
            return 'param taskName is required to update task'
        cur = mysql.connection.cursor()
        cur.execute('UPDATE tasks set task_name = (%s) WHERE task_id = (%s)', [taskName, taskId])
        mysql.connection.commit()
        cur.close()
        return 'updated task with id: %s' % taskId
    # delete task
    if request.method == 'DELETE':
        cur = mysql.connection.cursor()
        cur.execute('DELETE from tasks WHERE task_id = (%s)', [taskId])
        mysql.connection.commit()
        cur.close()
        return 'deleted task with id of %s' % taskId

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')