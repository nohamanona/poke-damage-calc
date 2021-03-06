import cv2
import numpy as np
import pandas as pd
import wx

from capture.video_capture import VideoCapture
from capture.video_read import VideoRead
from capture.videoinput_wrapper import VideoInputWrapper
from wx_top import Mywin
from pokemon import Pokemon

from ocr.ocr import Ocr

debug = 1
mode = "video capture"#"image capture"# "video capture"
in_image_file = "D:/amarec/pic/amarec(20191228-161218).bmp"
all_poke_data = pd.read_csv("all_poke_data.csv",encoding="SHIFT-JIS")
#print(all_poke_data)

print('-------------------------start poke damage calculate---------------------------')
if mode =="video capture":
    if debug==0:
        capture = VideoCapture()
        capture.reset()
        capture.reset_tick()
        capture.set_frame_rate()
        capture.select_source(name=capture.DEV_AMAREC)
    else:
        debug_file = 'D:\\amarec\\対戦37.mp4'
        capture = cv2.VideoCapture(debug_file)
        capture.set(3, 1280)
        capture.set(4, 720)

    k=0

    #fps 
    tm = cv2.TickMeter()
    tm.start()
    count = 0
    max_count = 10
    fps = 0


    while k != 27:
        if debug==0:
            frame = capture.read_frame()
            if frame is not None:
                r=0
            else:
                r=1
        else:
            r, frame = capture.read()
            if not r:
                continue

        #fps
        if count == max_count:
            tm.stop()
            fps = max_count / tm.getTimeSec()
            tm.reset()
            tm.start()
            count = 0
        count += 1


        if frame is not None:
        #if frame is not None:
            cv2.imshow("fl", frame)
        k = cv2.waitKey(3)

        if k == ord('t'):
            img_enemy_poke = frame[30:60,970:1103,:]
            img_enemy_hp = frame[64:72,980:1245,:]
            img_my_poke = frame[625:655,5:138,:]
            img_my_hp = frame[655:663,16:281,:]
            img_enemy_hp_gray = cv2.cvtColor(img_enemy_hp, cv2.COLOR_BGR2GRAY)
            img_enemy_hp_sobel = cv2.Sobel(img_enemy_hp_gray, cv2.CV_8U,1,0,ksize=3)
            enemy_hp = (np.argmax(img_enemy_hp_sobel,axis=1)[0]+1)/img_enemy_hp_sobel.shape[1]
            print(enemy_hp)
            cv2.imshow('img_enemy_hp', img_enemy_hp)
            cv2.imshow('img_enemy_poke', img_enemy_poke)
            print(np.argmax(img_enemy_hp_sobel,axis=1))
            cv2.imwrite('img_enemy_hp_sobel.png',img_enemy_hp_sobel)
            cv2.imwrite('img_enemy_hp.png',img_enemy_hp)
            cv2.imwrite('img_enemy_poke.png',img_enemy_poke)

            ocr = Ocr()
            enemy_poke_name = ocr.ocr_image2txt(img_enemy_poke)
            print("enemy poke: ",enemy_poke_name)


elif mode == "image capture":
    if debug == 0:
        print("debug start")
    else:
        img = cv2.imread(in_image_file)
        cv2.imshow('img', img)
        cv2.waitKey(0)

        img_enemy_poke = img[30:60,970:1103,:]
        img_enemy_hp = img[63:72,980:1245,:]
        img_my_poke = img[625:655,5:138,:]
        img_my_hp = img[655:663,16:281,:]
        cv2.imshow('img_enemy_poke', img_enemy_poke)
        cv2.imshow('img_enemy_hp', img_enemy_hp)
        cv2.imshow('img_my_poke', img_my_poke)
        cv2.imshow('img_my_hp', img_my_hp)
        cv2.waitKey(0)

        img_my_hp_gray = cv2.cvtColor(img_my_hp, cv2.COLOR_BGR2GRAY)
        img_my_hp_sobel = cv2.Sobel(img_my_hp_gray, cv2.CV_8U,1,0,ksize=3)
        cv2.imshow('img_my_hp_sobel', img_my_hp_sobel)
        cv2.waitKey(0)
        #print(img_my_hp_sobel)
        cv2.imwrite('img_my_hp.png',img_my_hp)
        cv2.imwrite('img_my_hp_sobel.png',img_my_hp_sobel)
        my_hp = (np.argmax(img_my_hp_sobel,axis=1)[0]+1)/img_my_hp_sobel.shape[1]
        print(my_hp*157)



        ocr = Ocr()
        enemy_poke_name = ocr.ocr_image2txt(img_enemy_poke)
        my_poke_name = ocr.ocr_image2txt(img_my_poke)
        if my_poke_name =="ロロトム":
            my_poke_name ="ロトム"
        print("enemy poke: ",enemy_poke_name)
        print("my poke: ",my_poke_name)
        print(all_poke_data[all_poke_data["name"]==enemy_poke_name])
        print(all_poke_data[all_poke_data["name"]==my_poke_name])
        my_data=all_poke_data[all_poke_data["name"]==my_poke_name]
        print(my_data.iloc[0,1],type(my_data.iloc[0,1]))

        enemy_pokemon=Pokemon()
        enemy_pokemon.set_base_stats([my_data.iloc[0,1],my_data.iloc[0,2],my_data.iloc[0,3],my_data.iloc[0,4],my_data.iloc[0,5],my_data.iloc[0,6]])
        print(enemy_pokemon._stats_h)

        app=wx.App()
        win=Mywin(None,'Drawing test')
        win.get_my_base_stats(str(my_data.iloc[0,1]),str(my_data.iloc[0,2]),str(my_data.iloc[0,3]),str(my_data.iloc[0,4]),str(my_data.iloc[0,5]),str(my_data.iloc[0,6]))
        app.MainLoop()
        
