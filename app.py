#cs resources
from flask import Flask, render_template
from flask_assets import Bundle, Environment
import ezsheets
from flask import request

app = Flask(__name__)
#method to communicate between javascript 
#python and html
js = Bundle('homeScript.js', output='gen/main.js')
#also connects style sheet to python (hypothetically)
#but actually might be more the case that you're better off
#putting stylesheet directly in html
css = Bundle('style.css', output='gen/mainStyle.css')
assets = Environment(app)

assets.register('main_js', js)
assets.register('mainStyle_css', css)
ss = ezsheets.Spreadsheet('1ymSnsFKZGCtjU6idXxoVtWARedas7xIFcF_WcRyvkL0')
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
  # get the sheet
  result = {}
  ss.refresh()
  ws = ss[str(sheetName)]
  #rows = ws.getRows()
  # start from below the headings
  j = 2
  while ws.getRow(j)[0] != '' or ws.getRow(j)[1] != '':
    #get the first and second values in each row
    #first representing the org, second representing the link
    result[ws.getRow(j)[0]] = ws.getRow(j)[1]

    j += 1

  return result 

# #@app.route('/app')
# def getAllData():
#   result = {}
#   #instantiate a sheet
  
#   #when the info has been updated on the sheet, update on site
#   ss.refresh()
#   sheets = ss.sheetTitles
#   #cols = ws.getColumns()
#   #headings = rows[0]
#   #i = 0

#   for s in range(1, len(sheets)): 
#     sheet = ss[s]
#     result[sheets[s]] = []
#     rows = sheet.getRows()
#     j = 2
#     while sheet.getRow(j)[0] != '' or sheet.getRow(j)[1] != '':
#       #get the first and second values in each row
#       #first representing the org, second representing the link
#       result[sheets[s]].append((sheet.getRow(j)[0], sheet.getRow(j)[1]))

#       j += 1


  # while headings[i] != '':
  #   #create a dictionary key for each header
  #   header = headings[i]
  #   result[header] = []

  #   j = 1
  #   col = ws.getColumn(i + 1)
  #   while col[j] != '':
  #     result[header].append(col[j])
  #     j+=1
  #   i += 1
  #return result



if __name__ == '__main__':
  app.run()