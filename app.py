from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import mysqlHost, mysqlUser, mysqlPassword, mysqlDb

app = Flask(__name__)

app.config['MYSQL_HOST'] = mysqlHost
app.config['MYSQL_USER'] = mysqlUser
app.config['MYSQL_PASSWORD'] = mysqlPassword
app.config['MYSQL_DB'] = mysqlDb

mysql = MySQL(app)
    
@app.route('/', methods=['GET')
def index():
    return 'this is an api'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')