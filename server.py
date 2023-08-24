from flask import Flask, render_template, session, redirect, request

import random

app = Flask(__name__)

app.secret_key="guess_number_game"

@app.route('/') 
def index():
    if "guess_num" not in session:
        session['guess_num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if "count" not in session:
        session['count']=1
    else:
        session['count'] += 1
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/insert_name',methods=['POST'])
def process():
    session['name'] = request.form['name']
    return redirect('/leaderboard')

@app.route('/leaderboard')
def success():
    return render_template('leaderboard.html')

if __name__=="__main__":
    app.run(debug=True)