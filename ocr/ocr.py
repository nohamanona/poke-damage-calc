import cv2
import numpy as np
from PIL import Image
import sys
import re
import pyocr
import pyocr.builders

class Ocr():
    def cv2pil(self,image_cv):
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_cv)
        image_pil = image_pil.convert('RGB')
        return image_pil

    def ocr_image2txt(self,cimg):
        image_pil = self.cv2pil(cimg)
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        tool = tools[0]
        txt = tool.image_to_string(image_pil, lang="script/Japanese", builder=pyocr.builders.TextBuilder(tesseract_layout=6))
        result = re.sub('([あ-んア-ン一-龥ー])\s+((?=[あ-んア-ン一-龥ー]))',r'\1\2', txt)
        return result