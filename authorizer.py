import subprocess
import os
from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for

app = Flask(__name__)
#Start screen with app to call
@app.route('/')
def index():
    file_list = os.listdir('C:/Web Server/Uploads')
    return render_template('virtual_app.html', app_data = file_list)
#Call functions given under specific format
@app.route('/', methods = ['GET', 'POST'])
def app_handler():
    if request.method == 'POST':
        app = request.form['app_name']
        if app.find('.py' or 'py'):
            cmd_str = ('py ' + app)
        elif app.find('.exe' or 'exe'):
            cmd_str = app
        elif app.find('.msi' or 'msi'):
            cmd_str = app
        else:
            return 'This file type is not yet supported'
        os.system(r'cd C:\Web Server\Uploads && ' + cmd_str)
        return render_template('virtual_app.html', app_data = 'Virtual Development Tabs are under development')
#PLEASE DON'T CHANGE PORT UNTIL YOU CHANGE THE HTML PAGE virtual_app.html!!!!!!!!!!!
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4500)