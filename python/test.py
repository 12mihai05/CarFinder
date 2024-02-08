from flask import Flask, render_template, url_for, request, redirect
from flaskext.mysql import MySQL
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12050512',
    database='images'
)

mycursor = mydb.cursor()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add():
    return render_template('add.html')
def upload():
    if request.method == 'POST':
        date = request.form
        sql = "UPDATE infoid SET  NAME = %s, IMAGE = %s WHERE ID = %s"
        val=(date['NAME'], date['IMAGE'], date['ID'])
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect(url_for('index'))

@app.route("/save", methods = ['POST'])
def save():
    if request.method == 'POST':
        mycursor.execute("SELECT max(id) FROM inofid")
        myresult = mycursor.fetchall()
        idNew = myresult[0][0] + 1
        date = request.form
        val = (idNew, date['NAME'], date['IMAGES'])
        sql = "INSERT INTO infoid (ID, NAME, IMAGE) VALUES (%s, %s, %s)"
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

