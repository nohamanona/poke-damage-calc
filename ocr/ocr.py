import cv2
import numpy as np
from PIL import Image
import sys
import re
import pyocr
import pyocr.builders

class Ocr():
    def cv2pil(self,image_cv):
        #image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
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
        kana = re.compile('[\u3041-\u309F\u30A1-\u30FF]+')
        result_kana = ''.join(kana.findall(result))
        return result_kana

if __name__ == "__main__":
    img_enemy_poke = cv2.imread("G:\my documents\VScode\Python\poke-damage\img_enemy_poke1.png")
    img_enemy_poke2 = cv2.imread("G:\my documents\VScode\Python\poke-damage\img_enemy_poke2.png")

    def img2nichi(img):
        img_nichi = np.zeros((img.shape[0],img.shape[1]))
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                print(i,j,img.shape)
                img_min=min(img[i,j,0],img[i,j,1],img[i,j,2])
                if img_min>=126:
                    img_nichi[i,j]=255
                else:
                    img_nichi[i,j]=0
        return img_nichi

    img_nichi = img2nichi(img_enemy_poke)
    img_nichi2 = img2nichi(img_enemy_poke2)

    ocr = Ocr()
    enemy_poke_name = ocr.ocr_image2txt(img_nichi)
    enemy_poke_name2 = ocr.ocr_image2txt(img_nichi2)
    print("enemy poke: ",enemy_poke_name,enemy_poke_name2)
    cv2.imshow('img_enemy_poke', img_enemy_poke)
    cv2.imshow('img_nichi', img_nichi)
    cv2.imshow('img_nichi2', img_nichi2)
    cv2.imwrite('img_nichi.png',img_nichi)
    cv2.imwrite('img_nichi2.png',img_nichi2)
    cv2.waitKey(0)
