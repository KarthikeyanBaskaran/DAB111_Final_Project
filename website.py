from flask import Flask, render_template
import pathlib
import sqlite3

app = Flask(__name__)

base_path = pathlib.Path().cwd()
dbname = "AppDB.db"
file_path = base_path/dbname

print(file_path)

@app.route("/")
def index():
    return render_template("Homepage.html")


@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path) # create a connection to the database
    cursor = con.cursor()
    Apps = cursor.execute("SELECT * FROM Apps").fetchall()# create a cursor
    con.close()
    return render_template("Data_2.html", apps = Apps)

if __name__ =="__main__":
    app.run(debug=True)