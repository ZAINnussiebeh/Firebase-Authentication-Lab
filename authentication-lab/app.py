from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyA5sZR5sfogbGfMtdPzj9DLqZ3yrkf8KVo",
  "authDomain": "mahmoud-c35da.firebaseapp.com",
  "projectId": "mahmoud-c35da",
  "storageBucket": "mahmoud-c35da.appspot.com",
  "messagingSenderId": "392987282160",
  "appId": "1:392987282160:web:dd29473890a547e9f11035",
  "measurementId": "G-RM0WHQ74ZF",
  "databaseURL": "https://mahmoud-c35da-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
                auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   
    return render_template("signup.html")


@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)