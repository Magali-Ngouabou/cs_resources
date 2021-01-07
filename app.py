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

import asyncio
from pyppeteer import launch





loop = asyncio.get_event_loop()
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

# create environment variable when not running on Heroku
# if is_heroku not there, set var to None
is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
  creds_var = os.environ.get('CREDS', 'var not found')

else: 
  # update var
  f = open('creds.json',)
  temp = json.load(f)
  creds_var = json.dumps(temp)
  f.close()

i = 0

@app.route('/pageInfo')
def pageInfo():
  link = request.args.get('link')
  linkSplit = link.split('.')
  print(linkSplit)
  name = linkSplit[1]
  return loop.run_until_complete(pageInfoHelper(link, name))
  

async def pageInfoHelper(link, name):
    
    browser = await launch(
    handleSIGINT=False,
    handleSIGTERM=False,
    handleSIGHUP=False
)
    page = await browser.newPage()
    await page.goto(link)
    await page.screenshot({'path': name + '.png'})
    

    image = {'img': name + '.png'}
    # interact with the pafe
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    #print(dimensions)
    json = jsonify(image)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()

    return json

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

#only  gets data from a specific sheet
@app.route('/app') #specifies endpoint
def getData():
  sheetName = request.args.get('category')
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
 
  creds_file = json.loads(creds_var)
  SPREADSHEET_ID = '1ymSnsFKZGCtjU6idXxoVtWARedas7xIFcF_WcRyvkL0'
  RANGE = sheetName+ '!A2:B150'
  
  credentials = service_account.Credentials.from_service_account_info(creds_file, scopes=SCOPES)
  #builds service to access sheet
  service = build('sheets', 'v4', credentials=credentials)

  sheet_values = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
  links = sheet_values.get('values', [])

  return jsonify(links)




if __name__ == '__main__':
  app.run()