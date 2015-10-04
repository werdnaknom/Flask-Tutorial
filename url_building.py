__author__ = 'Stratadon'

from flask import Flask, url_for
app = Flask(__name__)

'''
To build a URL to a specific function you can use the url_for() function. It
accepts the name of the function as first argument and a number of keyword
arguments, each corresponding to the variable part of the URL rule. Unknown
variable parts are appended to the URL as query parameters.
'''

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    #test_request_context tells Flask to behave as though it is handling a
    #request, even though we are interacting with it though a python shell
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username = 'John Doe')

if __name__ == '__main__':
    #with all the route functions returning "pass" this app will fail
    #this shows the ability to build URLs instead of hardcoding them in
    '''
    Build URLs to:
    1) change URLs in 1 go, without having to change URLs all over the place
    2) URL building will handle escaping of special characters and unicode data
    transparently
    3) if the app is placed outside the URL root, url_for() will handle that
    properly
    '''
    app.run(debug=True)
