import os
from flask import Flask ,render_template , redirect ,url_for, request



global auth
auth=""


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	global auth
        	auth="yes"
        	return redirect('/home')
        	print(auth)
    return render_template('login.html', error=error)





@app.route('/home')


def hello():
	if auth=="yes" :

		
		

		data={1:"hello world"}

		return render_template("home.html",data=data)


@app.route('/logout') 
def logo():
	global auth
	auth="no"
	return redirect('/')
	


if __name__ == '__main__':
    app.run(debug=True)

