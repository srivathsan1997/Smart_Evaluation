import os
import sys
import json
from bs4 import BeautifulSoup
import requests
import types
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import random
from random import randint
from apscheduler.schedulers.blocking import BlockingScheduler
import re
from datetime import datetime
import logging
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bowgmdopzdewnf:c1913ad98a2a961e370426698cab4f71b21e3ca673e14e7b43d519b5a3f90094@ec2-54-243-185-99.compute-1.amazonaws.com:5432/d3ah4pcjlgduo4'
db = SQLAlchemy(app)

class db_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(300),unique=True)
    password = db.Column(db.String(300),unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

def reguser(name,password):
    Uobj = db_User(name,password)
    db.session.add(Uobj)
    db.session.commit()
    print("checkout")



@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    #if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
     #   if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
      #      return "Verification token mismatch", 403
       # return request.args["hub.challenge"], 200

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def userregister():
    username = request.form['name']
    password = request.form['password']
    reguser(username,password)
    result = request.form
    return render_template("result.html",result = result)

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)