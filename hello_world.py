__author__ = 'Stratadon'

from flask import Flask #import flask class
app = Flask(__name__) #create instance of Flask classs

@app.route('/') #route() decorator tells Flask what URL triggers our function

def hello_world(): #the function is given a name which also used to generate URLs for that particular function
    return 'Hello World!'

if __name__ == '__main__':
    app.run() #runs local server with our application
    #app.run(host='0.0.0.0') #tells OS to listen on all public IPs