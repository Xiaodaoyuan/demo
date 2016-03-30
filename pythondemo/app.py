from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
  return render_template('home.html',title='welcome',name='home')

@app.route("/app",methods=['GET'])
def login():
  return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route("/signin",methods=['POST'])
def singin():
  if request.form['username']=='admin' and request.form['password']=='111111':
    return '<h2>hello %s<h2>'% request.form['username']
  else:
    return 'Error'


if __name__=='__main__':
   app.run()
