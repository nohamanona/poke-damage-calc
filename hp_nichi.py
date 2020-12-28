import cv2
import numpy as np
img = cv2.imread("G:\my documents\VScode\Python\poke-damage\img_my_hp.png")
cv2.imshow('img',img)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',img_gray)
#maximg = max(img)
#minimg = min(img)
print(img_gray.max(0),img_gray.min(0))
print(img_gray)
print(img.size)
a=[10,11,12]
enemy_hp_line=[]
enemy_hp_line_nichi=[]
thr = 130
tmp=0
for i in range(img.shape[1]):
    print(img[3,i,2],max([img[3,i,0],img[3,i,1],img[3,i,2]]))
    max_rgb=max([img[3,i,0],img[3,i,1],img[3,i,2]])
    enemy_hp_line.append(max_rgb)
    if max_rgb > thr:
        enemy_hp_line_nichi.append(1)
    else:
        enemy_hp_line_nichi.append(0)
    
print(enemy_hp_line,enemy_hp_line_nichi)
print(np.sum(enemy_hp_line_nichi),157*np.sum(enemy_hp_line_nichi)/img.shape[1])
cv2.waitKey(0)
