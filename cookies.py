__author__ = 'Stratadon'

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

#Reading Cookies
@app.route('/')
def index():
    username = request.cookies.get("username")
    '''
    use cookies.get(key) instead of cookies[key] to not get a KeyError if the
    cookie is missing
    '''

#Storing Cookies
@app.route('/')
def index():
    #this code won't work
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'the username')
    return resp


if __name__ == "__main__":
    app.run(debug=True)