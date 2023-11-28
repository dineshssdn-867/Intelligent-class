from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import pickle
from process_frames import allowed_file, process_video_emotion


app = Flask(__name__)
EMOTION_UPLOAD_FOLDER = 'emotion_uploads'
app.config['EMOTION_UPLOAD_FOLDER'] = EMOTION_UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('course.html')

@app.route('/check_emotion_analysis')
def check_emotion_analysis():
    return render_template('project.html')

@app.route('/emotion_analysis', methods=["POST"])
def emotion_analysis():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        output_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4')
        process_video_emotion(filename, output_filename)

        return redirect(url_for('home'))

    return redirect(request.url)

@app.route('/check_anomalous_analysis')
def check_anomalous_analysis():
    return render_template('project.html')

@app.route('/anomalous_analysis', methods=["POST"])
def anomalous_analysis():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        output_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4')
        process_video_emotion(filename, output_filename)

        return redirect(url_for('home'))

    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)