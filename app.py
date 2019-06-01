from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import mysqlHost, mysqlUser, mysqlPassword, mysqlDb

app = Flask(__name__)

app.config['MYSQL_HOST'] = mysqlHost
app.config['MYSQL_USER'] = mysqlUser
app.config['MYSQL_PASSWORD'] = mysqlPassword
app.config['MYSQL_DB'] = mysqlDb

mysql = MySQL(app)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        taskName = details['tname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks(task_name) VALUES (%s)", [taskName])
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')