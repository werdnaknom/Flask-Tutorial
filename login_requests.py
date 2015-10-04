__author__ = 'Stratadon'

from flask import Flask, request, render_template

app = Flask(__name__)

''' THE REQUEST OBJECT '''
@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form('username'))
        else:
            error = "Invalid username/Password"
    #the code below is executed if the request method was GET or the
    #credentials were invalid
    return render_template('login.html', error=error)



''' FILE UPLOADS '''
@app.route('/upload/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['the file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

