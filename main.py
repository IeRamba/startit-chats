import os
from flask import Flask, json, jsonify, render_template, request
import chats
from flask_sqlalchemy import SQLAlchemy


app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class test(db.Model):
  col = db.Column(db.String(255), primary_key=True)
  col2 = db.Column(db.String(255), unique=True, nullable=False)

@app.route('/')
def index_lapa():
  return render_template('chats.html')

@app.route('/postgreSQL')
def postgreSQL():
  result = test.query.all()
  return '%r' % result

@app.route('/health')
def health_check():
  return "OK"


@app.route('/chats/lasi')
def ielasit_chatu():
  return chats.lasi()


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  chats.pieraksti_zinju(dati)

  return chats.lasi()
  

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
