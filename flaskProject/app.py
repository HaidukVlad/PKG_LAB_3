from flask import Flask, request, render_template, send_from_directory
from PIL import Image, ImageFilter, ImageOps
import os
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'processed/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

def low_pass_filter(image):
    return image.filter(ImageFilter.BLUR)

def global_threshold(image, threshold=128):
    return image.point(lambda p: p > threshold and 255)

def niblack_threshold(image, window_size=15, k=-0.2):
    arr = np.array(image)
    mean = Image.fromarray(arr).filter(ImageFilter.BoxBlur(window_size//2))
    mean = np.array(mean)
    std_dev = np.sqrt(Image.fromarray((arr - mean)**2).filter(ImageFilter.BoxBlur(window_size//2)))
    threshold = mean + k * std_dev
    binary = arr > threshold
    return Image.fromarray((binary * 255).astype(np.uint8))

def sauvola_threshold(image, window_size=15, k=0.5, R=128):
    arr = np.array(image)
    mean = Image.fromarray(arr).filter(ImageFilter.BoxBlur(window_size//2))
    mean = np.array(mean)
    std_dev = np.sqrt(Image.fromarray((arr - mean)**2).filter(ImageFilter.BoxBlur(window_size//2)))
    threshold = mean * (1 + k * ((std_dev / R) - 1))
    binary = arr > threshold
    return Image.fromarray((binary * 255).astype(np.uint8))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = Image.open(filepath).convert('L')

            # Apply filters
            low_pass_img = low_pass_filter(image)
            low_pass_img.save(os.path.join(app.config['PROCESSED_FOLDER'], 'low_pass_' + filename))

            global_thresh_img = global_threshold(image)
            global_thresh_img.save(os.path.join(app.config['PROCESSED_FOLDER'], 'global_thresh_' + filename))

            niblack_img = niblack_threshold(image)
            niblack_img.save(os.path.join(app.config['PROCESSED_FOLDER'], 'niblack_' + filename))

            sauvola_img = sauvola_threshold(image)
            sauvola_img.save(os.path.join(app.config['PROCESSED_FOLDER'], 'sauvola_' + filename))

            return render_template('index.html', filename=filename)
    return render_template('index.html', filename=None)

@app.route('/processed/<filename>')
def send_processed_image(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)