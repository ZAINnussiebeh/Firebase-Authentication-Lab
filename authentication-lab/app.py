
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

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

tweet = {"input's _name"}
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        print("hey")
        email = request.form['email']
        password = request.form['password']
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))

    else:
        return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    error = ""
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        login_session['user']= auth.create_user_with_email_and_password(email, password)
        user={'email':resquest.form['email'],
        'password':resquest.form['password'],
        'fullname':resquest.form['fullname'],
        'username':resquest.form['username'],
        'bio':resquest.form['bio']}
        db.child("Users").child(login_session['user']['localId'])


        return redirect(url_for('signin'))
       
    return render_template("signup.html")


#@app.route('/signout')
#def signout():
    #ogin_session['user'] = None
    #auth.current_user = None
    #return redirect(url_for('signin'))



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    error:""
    if request.method=='POST':
        tweet={'title':request.form["title"],
        'text':request.form['text'],
        'uid': login_session['user']['localId']}
        db.child("tweets").push(tweet)
        return redirect(url_for("tweett"))
    else:
        return render_template("add_tweet.html")

@app.route('/all_tweet', methods=['GET', 'POST'])
def tweett():
    tweets = db.child("tweets").get().val()
    return render_template("tweets.html" , tweets = tweets)
    



if __name__ == '__main__':
    app.run(debug=True)