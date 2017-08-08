from flask import Flask, render_template, request, url_for, redirect, flash
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
            if not user:
                error="This user does not exist. Please try again."
                flash(error)
            else:
                if password == user[0][2]:
                    return redirect(url_for('quiz'))
                else:
                    error="Wrong password. Please try again."
                    flash(error)

        return render_template("index.html")

    except Exception as e:
        error = "something went wrong"
        flash(error)

    return render_template('index.html')

@app.route('/registration/')
def registration():
    return render_template('registration.html')

@app.route('/quiz/')
def quiz():
    dirty_category = mySQL().getDataFromCustomColumn('description', 'tblcategories')
    cleaned_category = [i[0] for i in dirty_category]
    return render_template('quiz.html', tuple_category=cleaned_category)




if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    # app.debug = True
    app.run()

