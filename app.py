# importing dependencies
from prediction import runVideo
import glob
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


app = Flask(__name__)
app.secret_key = "detectform"

ALLOWED_EXTENSIONS = {'mp4'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

BASE_DIR = os.getcwd()
dir = os.path.join(BASE_DIR, "uploads")

for root, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(dir, file)
        os.remove(path)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cardetails', methods=['POST'])
def upload_file():
    global videoPath
    videoPath = "E:/Internship/CV/test2.jpeg"
        # uploaded_file.save(videoPath)

    vehInfo = runVideo(videoPath)
    print(vehInfo)

    carDesc = vehInfo["CarMake"]["CurrentTextValue"]
    return render_template("details.html", carDesc=carDesc,  vehInfo=vehInfo)
if __name__ == "__main__":
    app.run(debug=True)