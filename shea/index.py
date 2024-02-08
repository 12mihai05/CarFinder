from flask import Flask, render_template, url_for, request, Response, redirect
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12050512',
    database='masini'
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/addcar",methods=['POST'])
def addcar():
    if request.method == 'POST':
        mycursor.execute("SELECT max(id) FROM car")
        myresult = mycursor.fetchall()
        idNew = myresult[0][0] + 1
        date = request.form
        val = (idNew, date['name'], date['model'], date['year'], date['cp'], date['price'])
        sql = "INSERT INTO car (id,name,model,year,cp,price) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, val)
        mydb.commit()
    return redirect(url_for('add'))

@app.route("/searchcar")
def searchcar():
    return render_template('search.html')

@app.route('/search',methods=['POST'])
def search():
    if request.method=='POST':
        date=request.form
        if date['name'] !='':
            mycursor.execute("SELECT * FROM masini.car WHERE name like %s",('%'+date['name']+'%',))
            myresult=mycursor.fetchall()
            return render_template('search.html',search=myresult)
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
