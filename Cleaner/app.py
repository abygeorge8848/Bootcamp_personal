from flask import Flask, render_template, request
import psycopg2

def create_app():
	app = Flask(__name__)
	app.config.from_mapping(
	DATABASE = "signIn"
	)
	
@app.route("/signup", methods=["GET", "POST"])
def signup():
	render_template('signup.html')
	
	
@app.route("/login")
def login():
	render_template('login.html')
	

@app.route("/signedIn", method=["POST"])
def getSignIn():
	name = request.form['sName']
	email = request.form['sEmail']
	password = request.form['sPassword']
	dbconn = db.get_db()
	cursor = dbconn.cursor()
	cursor.execute("INSERT INTO SignIn (name, email, password) VALUES (name, email, password)")
	dbconn.commit()
	render_template('submit.html')

def getLogIn():
	email = request.form['lEmail']
	password = request.form['lPassword']
	
	#I can set up an if condition here where it will ask for the email and password with partial matching from our database and if it is equal, it will render a template that will log them in
	#And if there is no such email and password, the else condition will be triggered and it will render a template saying 
	

if __name__ = "__main__":
	app.run()
	
	
	

