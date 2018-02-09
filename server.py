from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)

app.secret_key = '01189998819991197253'

@app.route('/')
def index():
  session['money']=0
  session['activity']=""
  return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def moneys():
  value= request.form['building']
  #Location + value+ time + append previous session log
  if value=='farm':
    val = random.randint(10, 20)
    session['money']+= val
    session['activity'] = "Entered the farm and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + session['activity']
  elif value=='cave':
    val = random.randint(5, 10)
    session['money']+= val
    session['activity'] = "Entered the cave and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + session['activity']
  elif value == 'house':
    val = random.randint(2, 5)
    session['money']+= val
    session['activity'] = "Entered the house and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + session['activity']
  elif value=='casino':
    val = random.randint(-50, 50)
    session['money']+= val
    session['activity'] = "Entered the casino and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + session['activity']

  return render_template("index.html", money=session['money'], activity=session['activity'])

app.run(debug=True)