from flask import Flask, render_template, request, url_for, redirect, flash, session
from dbClass import mySQL
from flask_hashing import Hashing

app = Flask(__name__)
hashing = Hashing(app)

@app.route('/', methods=['GET','POST'])
def index():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            password = hashing.hash_value(attempted_password, salt='6825')

            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)
            # session['uid'] = user[0][0]

            if not user:
                error="This user dSoes not exist. Please try again."
                flash(error)
            else:
                if password == user[0][2]:
                    return redirect(url_for('quiz'))
                else:
                    error="Wrong password. Please try again."
                    flash(error)

        return render_template("index.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    return render_template('index.html')

@app.route('/registration/')
def registration():
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password1 = request.form['password1']
            attempted_password2 = request.form['password2']
            password = hashing.hash_value(attempted_password1, salt='6825')

            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)
            print("attempted username: " + attempted_username)
            # print("value of user list: " + str(user))
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
                            error = "you have successfully registered."
                            flash(error)
                            mySQL().setLoginDataToDatabase('tblusers', attempted_username, password)
                            return redirect(url_for('quiz'))

        return render_template("registration.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    return render_template('registration.html.html')

@app.route('/quiz/')
def quiz():
    dirty_category = mySQL().getDataFromCustomColumn('description', 'tblcategories')
    cleaned_category = [i[0] for i in dirty_category]
    return render_template('quiz.html', tuple_category=cleaned_category)


















@app.errorhandler(403)
def forbidden():
    return render_template("403.html")
@app.errorhandler(404)
def page_not_found():
    return render_template("404.html")
@app.errorhandler(405)
def method_not_found():
    return render_template("405.html")
@app.errorhandler(500)
def method_not_found():
    return render_template("500.html")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    # app.debug = True
    app.run()

