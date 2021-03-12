from flask import render_template, redirect, url_for, flash,request,current_app,Flask
from __init__ import  app




#home
@app.route('/')
def home():    
    return render_template('index.html')

#adminlogin
@app.route('/adminlogin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/check_admin',methods=['GET','POST'])
def check_admin():
	if request.method=='GET':
		return "Please go back to the admin login page and fill the credentials"
	else:
		uname = request.form['uname']
		password = request.form['pass']
		if uname == 'rojee' and password=='bmw':
			return"success login"

	return password

#customer
@app.route('/customerlogin')
def customer_login():
    return render_template('customer_login.html')




