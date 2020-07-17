import os
import pytesseract
from PIL import Image
import re

class OCR:
    def __init__(self, path):
        self.path = path

    def ocr_getText(self, filePath):
        pytesseract.pytesseract.tesseract_cmd = self.path
        text = pytesseract.image_to_string(Image.open(filePath))
        return text


