#cs resources
import os
from flask import Flask, render_template, jsonify
from flask_assets import Bundle, Environment
from flask import request
import json

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from apiclient import discovery
from google.oauth2 import service_account

app = Flask(__name__)
#method  to communicate between javascript 
#python and html
js = Bundle('homeScript.js', output='gen/main.js')
#also connects style sheet to python (hypothetically)
#but actually might be more the case that you're better off
#putting stylesheet directly in html
css = Bundle('style.css', output='gen/mainStyle.css')
assets = Environment(app)

assets.register('main_js', js)
assets.register('mainStyle_css', css)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/paid-ops')
def paid():
  return render_template('paid-ops.html')

@app.route('/conferences')
def cons():
  return render_template('conferences.html')

@app.route('/gov-jobs')
def gov():
  return render_template('gov-jobs.html')

@app.route('/news')
def news():
  return render_template('news.html')

@app.route('/fands')
def fands():
  return render_template('fands.html')

@app.route('/learn')
def learn():
  return render_template('learn.html')

@app.route('/prep')
def prep():
  return render_template('prep.html')

@app.route('/hackathons')
def hackathons():
  return render_template('hackathons.html')

@app.route('/programs')
def programs():
  return render_template('programs.html')

@app.route('/grads')
def grads():
  return render_template('grad.html')

#only gets data from a specific sheet
@app.route('/app')
def getData():
  sheetName = request.args.get('category')
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
  creds_var = os.environ.get('CREDS', 'var not found')
  creds_file = json.loads(creds_var)
  SPREADSHEET_ID = '1ymSnsFKZGCtjU6idXxoVtWARedas7xIFcF_WcRyvkL0'
  RANGE = sheetName+ '!A2:B150'
  
  credentials = service_account.Credentials.from_service_account_info(creds_file, scopes=SCOPES)
  #builds service to access sheet
  service = build('sheets', 'v4', credentials=credentials)

  sheet_values = service.spreadsheets().values.get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
  links = sheet_values.get('values', [])

  return jsonify(links)




if __name__ == '__main__':
  app.run()