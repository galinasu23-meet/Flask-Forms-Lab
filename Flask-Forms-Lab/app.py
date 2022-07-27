from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "gali"
password = "456"
facebook_friends=["Idan","Tali","Roei", "Lonia", "Tair", "Gili"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		namepsw = request.form['password']
		if username == name and password== namepsw :
			return redirect(url_for('home'))
		else :
			print ("password incorrect")
			return render_template("login.html")

@app.route('/home')
def home():  
    return render_template('home.html',friends=  facebook_friends)

@app.route('/friendsd_exists/<string :name', methods=['GET', 'POST'])
def friends_exists():
	return render_template('friends_exists.html')
	

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)