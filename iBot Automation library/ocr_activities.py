import os
import pytesseract
from PIL import Image


def ocr_getText(filename):
    CurrentPath = os.path.dirname(__file__)
    pytesseract.pytesseract.tesseract_cmd = CurrentPath + '/tesseract/4.1.1/bin/tesseract'
    text = pytesseract.image_to_string(Image.open(filename))
    return text
