import json
import sqlite3
import os
import random
from werkzeug.utils import secure_filename
from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for

#Staging functions/variables for later
connection = sqlite3.connect('users.db')
print('Database connected')
crsr = connection.cursor()

def get_row():
    data = crsr.execute('SELECT id FROM accounts')
    counter = 0
    for row in data:
        counter += 1
    fin_count = counter + 1
    return fin_count

def authenticate(uname, pw, token):
    if token == user_token:
        data = crsr.execute('SELECT username, password FROM accounts')
        for row in data:
            if uname == row[0]:
                if pw == row[1]:
                    return redirect(url_for('render_prof', username = username))
                else:
                    return render_template('login.html', error = 'Incorrect username or password')
    else:
        return render_template('login.html', error = 'Token not recognized')

def create_acct(name, uname, email, password):
    id_index = get_rows()
    sql_query = f'INSERT INTO accounts(id, name, uname, email, pw) VALUES ({id_index}, {name}, {uname}, {email}, {password})'
    crsr.execute(sql_query)
    return redirect(url_for(render_prof), username = uname)
    
#Ref App and  conditions
app = Flask(__name__)

#Index page and path
@app.route('/')
def index():
    return render_template('index.html')
    
#login screen and path
@app.route('/login')
def login_page():
    return render_template('login.html')
    
#login POST request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_token = random.ranint(0,10000)
    authenticate(username, password, user_token)
            
#Profile screens and path
@app.route('/profiles/<username>')
def render_prof(username):
    return render_template('profile.html', username = username)
    
#File screen and path
@app.route('/files')
def file_screen():
    return render_template('files.html')
    
#File handler
@app.route('/files', methods = ['GET', 'POST'])
def file_handler():
    if request.method == 'POST':
        file = request.files['file']
        if file == '':
            return render_template('files.html', really = "You didn't pick a file!")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            file_list.append(filename)
            clean_file_list(file_list)
            return render_template('files.html', really = "Your file has been uploaded! You made need to refresh to see changes.", py_dir = file_list)
        else:
            clean_file_list(file_list)
            return render_template('files.html', really = "There was a problem uploading the file, please try again.", py_dir = file_list)
            
#Call to start service 1st param is hosts to serve set to 0.0.0.0 if serving to everybody 2nd is port param
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80)
