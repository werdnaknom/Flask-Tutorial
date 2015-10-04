__author__ = 'Stratadon'

from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)
''' FILE UPLOADS '''
@app.route('/upload/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['the file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))