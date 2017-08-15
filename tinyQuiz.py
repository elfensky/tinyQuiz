from flask import Flask, render_template, request, url_for, redirect, flash, session
from dbClass import mySQL
from flask_hashing import Hashing
import random
from functools import wraps #neccesary to have "login required" pages protected against access
import gc #garbage collection to make sure stuff is cleaned up after mySQL stuff. Has mem leaks
import time

app = Flask(__name__)
hashing = Hashing(app)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print()

# ----- GENERAL PAGES ----- #
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("you need to login first")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    # session.clear()
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            password = hashing.hash_value(attempted_password, salt='6825')

            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)

            if not user:
                error="This user dSoes not exist. Please try again."
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
        return render_template("login.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    # return render_template('login.html')

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
                            error = "you have successfully registered."
                            flash(error)
                            mySQL().setLoginDataToDatabase('tblusers', attempted_username, password)
                            session['logged_in'] = True
                            session['username'] = attempted_username
                            user = mySQL().getDataFromCustomRow('tblusers', 'username', attempted_username)
                            session['uid'] = str(user[0][0])
                            return redirect(url_for('quiz'))
        gc.collect()
        return render_template("registration.html")

    except Exception as e:
        error = "something went wrong: "
        flash(error + str(e))

    # return render_template('registration.html')

@app.route("/logout/")
@login_required
def logout():
    session.clear() #on logout, cleal session cookies
    # flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('index'))

@app.route("/settings/", methods=['GET','POST'])
@login_required
def settings():
    try:
        if request.method == "POST":
            attempted_password_old = hashing.hash_value(request.form['password_old'], salt='6825')
            attempted_password1 = request.form['password1']
            attempted_password2 = request.form['password2']
            current_password = mySQL().getCustomQuery('SELECT password FROM tblusers WHERE IDuser='+str(session['uid']))

            if attempted_password_old == '' or attempted_password1 == '' or attempted_password2 == '':
                flash("Please completely fill out the form.")
            else:
                if attempted_password1 != attempted_password2:
                    flash('New passwords do not match.')
                    # return render_template('settings.html', username=session['username'])
                else:
                    if attempted_password_old == current_password[0][0]:
                        flash('Your password has been changed.')
                        new_password = hashing.hash_value(attempted_password1, salt='6825')
                        mySQL().setCustomQuery('UPDATE tblusers SET password="'+str(new_password)+'" WHERE IDuser='+str(session['uid']))
                        # print('UPDATE tblusers SET password="'+str(new_password)+'" WHERE IDuser='+str(session['uid']))
                        # return render_template('settings.html', username=session['username'])
                    else:
                        flash('Old password does not match.')
                        # return render_template('settings.html', username=session['username'])

        gc.collect()
        return render_template('settings.html', username=session['username'])

    except Exception as e:
        flash(str(e))

# ------- GAME -------- #
scores = ['0','0','0','0','0']
trivia_clean_question = ['0']
trivia_clean_types = ['0','0','0','0']
trivia_clean_answers = ['0','0','0','0']
trivia_clean_trivia = ['0']

@app.route('/quiz/')
@login_required
def quiz():
    dirty_category = mySQL().getDataFromCustomColumn('description', 'tblcategories')
    cleaned_category = [i[0] for i in dirty_category]
    return render_template('quiz.html', tuple_category=cleaned_category, username=session['username'])

@app.route('/quiz/<category>/<int:id>/')
@login_required
def category(category, id):
    # -----------conditional returns----------- #
    if id == 5:
        correct = scores.count(1)
        wrong = scores.count(0)
        mySQL().setGameDataToDatabase('tblgames', session['uid'], session['cid'], correct)
        return render_template('scores.html', correct=correct, wrong=wrong, username=session['username'])

    else:
        session['cid'] = mySQL().getCustomQuery("SELECT IDcategory FROM tblcategories WHERE description = '" + str(category) + "'")[0][0]
        # -----------questions----------- #
        questions = list(mySQL().getQuestionsByCategory(category))  # get question from db
        # shuffled_questions = random.sample(questions, len(questions)) ##since I randomize on every call, I can't use this cuz I might get the same question twice.
        clean_question = questions[id][1]  # get the question of the current page
        session['qid'] = questions[id][0]

        # -----------answers----------- #
        dirty_answers = []  # empty dict dirty answers
        for x in range(0, 4):
            dirty_answers.append(questions[id][2 + x])  # put the complete answers in it.
        shuffled_answers = random.sample(dirty_answers, len(dirty_answers))  # shuffle their position in dict
        clean_answers = [i.split(',')[0] for i in shuffled_answers]  # split into "before the ","
        clean_types = [i.split(',')[1] for i in shuffled_answers]  # split into after the ","

        # -----------global lists for trivia pages----------- #
        trivia_clean_question[0] = clean_question
        trivia_clean_trivia[0] = questions[id][6]
        for x in range(0, 4):
            trivia_clean_answers[x] = clean_answers[x]
            trivia_clean_types[x] = clean_types[x]
        # -----------statistics----------- #
        stat1 = mySQL().getCustomQuery("SELECT answer FROM db_quiz.tblscores WHERE IDquestion = " + str(session['qid']))
        cleaned_test = []
        for i in range(0, len(stat1)):
            cleaned_test.append(stat1[i][0])
        percentage_dirty = str(100.0 / len(stat1) * cleaned_test.count(1))
        session['percentage'] = percentage_dirty.split('.', 1)[0]
        # -----------return quiz----------- #
        return render_template('questions.html',
                                     category=category,
                                     id=id,
                                     clean_question=clean_question,
                                     clean_types=clean_types,
                                     clean_answers=clean_answers,
                                     username=session['username'],
                                     percentage=session['percentage'])

@app.route('/quiz/<category>/<int:id>/<type>/')
@login_required
def trivia(category, id, type):
    if id < 5:
        if type == 'True':
            scores[id] = 1  # add one to show you got a question correctly
            mySQL().setScoreDataToDatabase('tblscores', session['uid'], session['cid'], session['qid'], '1', time.strftime('%Y-%m-%d %H:%M:%S'))
            return render_template('trivia_true.html',
                                         category=category,
                                         id=id,
                                         clean_question=trivia_clean_question,
                                         clean_answers=trivia_clean_answers,
                                         clean_types=trivia_clean_types,
                                         trivia_clean_trivia=trivia_clean_trivia,
                                         username=session['username'],
                                         percentage=session['percentage'])
        else:
            scores[id] = 0  # add zero to show you failed to answer correctly
            mySQL().setScoreDataToDatabase('tblscores', session['uid'], session['cid'], session['qid'], '0',time.strftime('%Y-%m-%d %H:%M:%S'))
            return render_template('trivia_false.html',
                                         category=category,
                                         id=id,
                                         clean_question=trivia_clean_question,
                                         clean_answers=trivia_clean_answers,
                                         clean_types=trivia_clean_types,
                                         trivia_clean_trivia=trivia_clean_trivia,
                                         username=session['username'],
                                         percentage=session['percentage'])
    else:
        correct = scores.count(1)
        wrong = scores.count(0)
        return render_template('scores.html', correct=correct, wrong=wrong,username=session['username'])

# ----------- STATISTICS ----------- #
@app.route("/dashboard/")
@login_required
def dashboard():
    # --- section 1 >> total games played by user ---#
    played_games = mySQL().getCustomQuery('SELECT COUNT(*) FROM db_quiz.tblgames WHERE IDuser = '+str(session['uid']))
    played_games_wins = mySQL().getCustomQuery('SELECT COUNT(*) FROM db_quiz.tblgames WHERE IDuser = '+str(session['uid'])+' AND correct >= 3')
    while len(played_games) < 1:
        played_games.append([0, 0])
    while len(played_games_wins) < 1:
        played_games_wins.append([0, 0])
    # --- section 2 >> total points earned --- #
    points = mySQL().getCustomQuery('SELECT SUM(correct) FROM db_quiz.tblgames WHERE IDuser = ' + str(session['uid']))
    if points[0][0] == None:
        points = [[0, 0]]
    totalpoints = mySQL().getCustomQuery('SELECT COUNT(correct) FROM db_quiz.tblgames WHERE IDuser = ' + str(session['uid']))[0][0] * 5
    # --- section 2 >> total points earned --- #
    #somthing
    # --- section 4 >> most played category ---#
    category_id = mySQL().getCustomQuery('SELECT IDcategory , COUNT(IDcategory) AS MOST_FREQUENT FROM tblgames WHERE IDuser = '+str(session['uid'])+' GROUP BY IDcategory ORDER BY COUNT(IDcategory) DESC LIMIT 1')
    while len(category_id) < 4:
        category_id.append([0, 0])
    category_times = mySQL().getCustomQuery('SELECT IDcategory , COUNT(IDcategory) AS MOST_FREQUENT FROM tblgames WHERE IDuser = '+str(session['uid'])+' GROUP BY IDcategory ORDER BY IDcategory')
    while len(category_times) < 4:
        category_times.append([0, 0])
    category = mySQL().getCustomQuery('SELECT description FROM tblcategories WHERE IDcategory = ' + str(category_id[0][0]))
    if not category:
        category_fixed = 'not available'
    else:
        category_fixed = category[0][0]
    return render_template('dashboard.html',
                           username=session['username'],
                           played_games=played_games[0][0],
                           played_games_wins=played_games_wins[0][0],
                           category_max_played=category_id,
                           category_times_played=category_times,
                           category=category_fixed,
                           points=points[0][0],
                           totalpoints=totalpoints)

@app.route("/statistics/")
@login_required
def statistics():
    # --- section 1 >> question most frequently answered wrong ---#
    wrong_answer = mySQL().getCustomQuery('SELECT IDquestion, COUNT(IDquestion) AS MOST_FREQUENT FROM tblscores WHERE answer = 0 GROUP BY IDquestion ORDER BY COUNT(IDquestion) DESC LIMIT 1')
    wrong_question = mySQL().getCustomQuery('SELECT * FROM tblquestions WHERE IDquestion =' + str(wrong_answer[0][0]))
    wrong_category = mySQL().getCustomQuery('SELECT description FROM tblcategories WHERE IDcategory =' + str(wrong_question[0][7]))
    # --- section 2 >> total points earned on server ---#
    points = mySQL().getCustomQuery('SELECT SUM(correct) FROM db_quiz.tblgames')
    totalpoints = mySQL().getCustomQuery('SELECT COUNT(correct) FROM db_quiz.tblgames')[0][0] * 5
    # --- section 3 >> total games played on server ---#
    played_games = mySQL().getCustomQuery('SELECT COUNT(*) FROM db_quiz.tblgames')
    played_games_wins = mySQL().getCustomQuery('SELECT COUNT(*) FROM db_quiz.tblgames WHERE correct >= 3')
    # --- section 4 >> most played category ---#
    category_id = mySQL().getCustomQuery('SELECT IDcategory , COUNT(IDcategory) AS MOST_FREQUENT FROM tblgames GROUP BY IDcategory ORDER BY COUNT(IDcategory) DESC LIMIT 1')
    category_times = mySQL().getCustomQuery('SELECT IDcategory , COUNT(IDcategory) AS MOST_FREQUENT FROM tblgames GROUP BY IDcategory ORDER BY IDcategory')
    category = mySQL().getCustomQuery('SELECT description FROM tblcategories WHERE IDcategory = ' + str(category_id[0][0]))

    return render_template('statistics.html',
                           username=session['username'],
                           wrong_question=wrong_question[0][1],
                           wrong_category=wrong_category[0][0],
                           points=points[0][0],
                           totalpoints=totalpoints,
                           played_games=played_games[0][0],
                           played_games_wins=played_games_wins[0][0],
                           category_max_played=category_id,
                           category_times_played=category_times,
                           category=category[0][0])


#------ ERRORS ------#
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html", e=e)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)
@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html", e=e)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", e=e)

# RUN
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(threaded=True) #better performance, multiple clients

