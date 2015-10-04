__author__ = 'Stratadon'

'''
This code creates two webpages.  The first, an Index page located at '/'.
The second, the hello world page located at '/hello'
'''
from flask import Flask #import flask class
app = Flask(__name__) #create instance of Flask class

@app.route('/') #route() decorator tells Flask what URL triggers our function
def index(): #the function is given a name which also used to generate URLs for that particular function
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

'''
Variable Rules can be used as well.
To add variable parts to a URL you can mark these special sections as
<variable_name>. Such a part is then passed as a keyword argument to your
function. Optionally a converter can be used by specifying a rule with
<converter:variable_name>.
'''

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

'''The following converters exist (like used in post_id):
    int -- accepts integers
    float -- like int but for floating point values
    path -- like default but also accepts slashes
'''

if __name__ == '__main__':
    app.run(debug=True) #runs local server with our application