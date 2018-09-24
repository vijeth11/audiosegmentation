
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template, request
from flask import jsonify
from speak import *
from werkzeug import secure_filename
from audiosegment import *

app = Flask(__name__)

@app.route('/upload')
def upload_files():
   return render_template('upload.html')

@app.route('/<query>')
def hello_world(query):
    #print(jarvis(query).replace("'","\\'"))
    return jsonify(value=jarvis(query).replace("'","\\'"))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    #print(os.path.dirname(os.path.abspath(__file__)))
    f = request.files['file']
    f.save("mysite/"+secure_filename(f.filename))
    #traindata(segment())
    return "file uploaded sucessfully"