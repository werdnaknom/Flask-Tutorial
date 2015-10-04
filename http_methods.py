__author__ = 'Stratadon'

from flask import Flask
app = Flask(__name__)

''' OVERVIEW

HTTP knows different methods for accessing URLs. By default, a route only
answers to GET requests, but that can be changed by providing the methods
argument to the route() decorator.
'''

'''
The HTTP method (also called the 'verb') tells the server what the clients
wants to do with the requested page.
'''

#GET
'''The Browser tells teh server to just get the information stored on that page
and send it.'''
#HEAD
''' The browser tells the server to get the information, but it is only
interested in the headers, not the content of the page. An application is
supposed to handle that as if a GET request was received but to not deliver the
actual content.  In FLASK you don't have to deal with that at all, the
underlying WERKZEUG library handles that. '''
#POST
''' The browser tells the server that it wants to post some new information to
that URL and that the server must ensure the data is stored and only stored
once. This is how HTML forms usually transmit data to the server.'''
#PUT
''' Similar to POST but the server might trigger the store procedure multiple
times by overwriting the old values more than once. '''
#DELETE
''' Remove the information at the given location '''
#OPTIONS
''' Provides a quick way for a client to figure out which methods are supported
by this URL '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == '__name__':
    app.run(debug=True)