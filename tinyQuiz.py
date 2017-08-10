from flask import Flask, render_template, request, url_for, redirect, flash, session
from dbClass import mySQL
from flask_hashing import Hashing
# from passlib.hash import sha256_crypt #need to change the password system to use this instead
from functools import wraps #neccesary to have "login required" pages protected against access
import gc #garbage collection to make sure stuff is cleaned up after mySQL stuff. Has mem leaks

app = Flask(__name__)
hashing = Hashing(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("you need to login first")
            return redirect(url_for('index'))
    return wrap

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            password = hashing.hash_value(attempted_password, salt='6825')

            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)


            if not user:
                error="This user does not exist. Please try again."
                flash(error)
            else:
                if password == user[0][2]:
                    session['logged_in'] = True
                    session['username'] = attempted_username
                    session['uid'] = user[0][0]
                    return redirect(url_for('quiz'))
                else:
                    error="Wrong password. Please try again."
                    flash(error)

        gc.collect()
        return render_template("index.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    return render_template('index.html')

@app.route('/registration/', methods=['GET','POST'])
def registration():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password1 = request.form['password1']
            attempted_password2 = request.form['password2']
            password = hashing.hash_value(attempted_password1, salt='6825')

            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)
            if attempted_username == '':
                error = "Please enter a username"
                flash(error)
            else:
                if user != []:
                    error = "This username is taken. Please choose another."
                    flash(error)
                else:
                    if attempted_password1 == '':
                        error = "Please enter a password"
                        flash(error)
                    else:
                        if attempted_password1 != attempted_password2:
                            error = "Passwords do not match."
                            flash(error)
                        else:
                            session['logged_in'] = True
                            session['username'] = attempted_username
                            session['uid'] = user[0][0]
                            error = "you have successfully registered."
                            flash(error)
                            mySQL().setLoginDataToDatabase('tblusers', attempted_username, password)
                            return redirect(url_for('quiz'))
        gc.collect()
        return render_template("registration.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    return render_template('registration.html.html')

@app.route('/quiz/')
@login_required
def quiz():
    print(session['logged_in'])
    print(session['username'])
    print(session['uid'])
    dirty_category = mySQL().getDataFromCustomColumn('description', 'tblcategories')
    cleaned_category = [i[0] for i in dirty_category]
    return render_template('quiz.html', tuple_category=cleaned_category)

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", e=e)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()

