# Image Processing with Flask and Pillow

This project is a simple web application for processing images using the Flask framework and the Pillow library. It applies various filters and adaptive thresholding techniques to uploaded images.

## Features

- **Low Pass Filter**: Blurs the image to reduce noise.
- **Global Thresholding**: Converts the image to a binary image using a fixed threshold.
- **Niblack Thresholding**: Applies adaptive thresholding based on local mean and standard deviation.
- **Sauvola Thresholding**: An improved adaptive thresholding method that normalizes the local standard deviation.

## Prerequisites

- Python 3.x
- Required Python libraries: Flask, Pillow, NumPy

## Installation

1. Clone the repository:
   ``` bash
   git clone https://github.com/HaidukVlad/PKG_LAB_3.git
   ```
2. Navigate to the project directory:
  ``` bash
  cd image-processing-flask
  ```
3. Install the required dependencies:
  ``` bash
  pip install -r requirements.txt
  ```

## Usage

1. Run the Flask application:
  ``` bash
  python app.py
  ```
2. Open your web browser and go to http://127.0.0.1:5000/.
3. Upload an image file to apply the processing techniques. The processed images will be displayed on the same page.

## Directory Structure

- app.py: Main Flask application file.
- static/uploads/: Directory for storing uploaded images.
- processed/: Directory for storing processed images.
- templates/index.html: HTML file for the web interface.

## Code Overview

- Image Filters:
  - low_pass_filter: Applies a blur effect to the image.
  - global_threshold: Converts the image to binary using a fixed threshold.
  - niblack_threshold: Applies Niblack adaptive thresholding.
  - sauvola_threshold: Applies Sauvola adaptive thresholding.
- Flask Routes:
  - /: Main page for uploading and viewing images.
  - /processed/<filename>: Serves the processed images.
 
## Contributing

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

This project uses the Flask framework and the Pillow library for image processing.

### Instructions

- Replace `https://github.com/HaidukVlad/PKG_LAB_3.git` with your actual repository link.
- Save this content in a file named `README.md` in the root directory of your project.
- You can also add any additional information or sections as needed.
