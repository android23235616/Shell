from flask import Flask,redirect, url_for,request,render_template,make_response,flash,session
from flask_mail import Mail,Message
import os
from werkzeug.utils import secure_filename
from fm import ContactForm
import numpy as np
from processingSql import SQL
app = Flask(__name__)

UPLOAD_FOLDER = 'C:\\xampp\\htdocs\\flask\\uploads\\.ng'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'development key'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'majumdartanmay68@gmail.com'
app.config['MAIL_PASSWORD'] = 'wart414ways466'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/contact',methods = ['GET','POST'])

def contact():
     form = ContactForm()

     if request.method == 'POST':
        if form.validate() == False:
           flash('All fields are required.')
           return render_template('contact.html', form = form)
        else:
           return render_template('success.html')
     elif request.method == 'GET':
           flash("hello")
           return render_template('contact.html', form = form)



@app.route('/sql')

def sql():
    sql = SQL()
    name = session['subject']
    query = 'SELECT * FROM main_attendance where subject=%s'
    ans = sql.ex(query,name)

    row  = [i for i in [r for r in ans]]
 #   for each in row:
#        s = s+str(each[0])+" "+str(each[1])+" "+str(each[2])+" "+str(each[3])+"<br>"

    result = {}
    for each in row:
        result["roll"]  = each[0]
        result["subject"] = each[1]
        result["period"] = each[2]
        result["attendance"] = each[3]

    return render_template('attendance_table/index.html',result = row)

@app.route('/admin')

def hello_admin():
    return "Hello Admin"

@app.route('/test')
def test():
    return "test"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s"%guest

@app.route('/user/<name>')

def check(name):
    if(name=='admin'):
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))



@app.route('/mails')

def index():
   msg = Message('Hello', sender = 'majumdartanmay68@gmail.com', recipients = ['majumdartanmay68@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@app.route('/login',methods = ['POST','GET'])

def login():
    if request.method=='POST':
        #flash('You were successfully logged in')
        sql = SQL()
        user = request.form['u']
        password = request.form['p']
        if(not (session['log'])):
           if(sql.check_login(user,password)):
                resp = make_response(render_template('templates/home.html',name=user))
                resp.set_cookie('userId', user)

                return resp
           else:
               return redirect(url_for('login2'))
    else:
        return "invalid request"


@app.route('/upload',methods = ['POST','GET'])
def upload():
    if(not(request.method=='POST')):
        return render_template("uploading/upload.html")
    elif(request.method=='POST'):
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.abspath(UPLOAD_FOLDER+filename))
        return "File Uploaded Successfully"





@app.route('/')
def login2():
     #resp = make_response(render_template('index.html'))
     #resp.set_cookie('userId',"hi")
     session['log'] = False
     checker = request.cookies.get('userId')

     if(checker is None):
         return render_template('index.html')
     else:
         session['log'] = True
         return render_template('templates/home.html',name=checker)
if __name__ == '__main__':
   app.run(debug = True,port=4996)