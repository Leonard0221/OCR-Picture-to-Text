# OCR (Optical Character Recognition)

This project aims to develop an Optical Character Recognition (OCR) system to recognize text from images and convert it into real text.

## Project Description

The OCR system uses image processing techniques and machine learning algorithms to identify and extract text characters from images. The goal is to accurately recognize the text present in the provided image(s) and output the corresponding real text.

## Project Structure

The project folder contains the following file:

- `ocr.py`: Python script containing the OCR system implementation.

## Sample Image

A sample image (`01.jpg`) is provided in the project folder to test the OCR system.

## Getting Started

1. Clone the repository to your local machine using the following command:

2. Ensure you have Python installed on your system.

3. Install the required Python dependencies:
   ```
   pip install pytesseract pillow
   ```

4. Run the OCR system on the sample image:
   ```
   python ocr.py 01.jpg
   ```

## Usage

The OCR system can be used to recognize text from any image with clear text characters. To use the OCR system on your own images, simply provide the path to the image as an argument when running the `ocr.py` script:
```
python ocr.py path/to/your/image.jpg
```

The OCR system will then process the image and display the recognized text.
