__author__ = 'Stratadon'

'''
The run() method is nice to start a local development server, but you would
have to restart it manually after each change to your code. That is not very
nice and Flask can do better. If you enable debug support the server will
reload itself on code changes, and it will also provide you with a helpful
debugger if things go wrong.
'''

from flask import Flask #import flask class
app = Flask(__name__) #create instance of Flask class

@app.route('/') #route() decorator tells Flask what URL triggers our function

def hello_world(): #the function is given a name which also used to generate URLs for that particular function
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)