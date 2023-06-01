from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
#code for connection
#MySQL Hostname
app.config['MYSQL_HOST'] = 'localhost'
#MySQL username
app.config['MYSQL_USER'] = 'root'
#MySQL password here in my case password is null so i left empty
app.config['MYSQL_PASSWORD'] = 'Python@ng123'
#Database name In my case database name is projectreporting
app.config['MYSQL_DB'] = 'flask_html'

mysql = MySQL(app)
@app.route('/')
@app.route('/flask_html',methods=['GET','POST'])
def flask_html():
    #creating variable for connection
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #executing query
    cursor.execute("select * from fetch_mysql")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to projectlist.html with all records from MySQL which are stored in variable data
    return render_template("index.html",data=data)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
