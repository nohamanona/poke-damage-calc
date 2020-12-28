import cv2
import time
import re
import numpy as np
import pandas as pd

from ocr.ocr import Ocr
from pokemon import Pokemon

class PokeDamageEngine(object):

    def set_frame(self,frame):
        self.frame=frame

    def pause(self, pause):
        self._pause = pause

    def on_button_capture(self,e):
        print('capture')
        self.my_poke_name_img = self.input_frame[625:655,5:138,:]
        self.frame.my_poke_panel.show_name_image(self.my_poke_name_img)
        self.enemy_poke_name_img =self.input_frame[30:60,970:1103,:] # cv2.imread("G:\my documents\VScode\Python\poke-damage\img_enemy_poke.png")
        self.frame.enemy_poke_panel.show_name_image(self.enemy_poke_name_img)
        self.my_poke_hp_img = self.input_frame[655:663,16:281,:]
        self.frame.my_poke_panel.show_hp_image(self.my_poke_hp_img)
        self.enemy_poke_hp_img = self.input_frame[63:72,980:1245,:]
        self.frame.enemy_poke_panel.show_hp_image(self.enemy_poke_hp_img)

        my_poke_name_ocr = self.ocr.ocr_image2txt(self.my_poke_name_img)
        self.frame.my_poke_panel.change_poke_name(my_poke_name_ocr)
        enemy_poke_name_ocr = self.ocr.ocr_image2txt(self.enemy_poke_name_img)
        self.frame.enemy_poke_panel.change_poke_name(enemy_poke_name_ocr)

        self.my_hp_percent = self.calc_hp_percent(self.my_poke_hp_img)
        self.frame.my_poke_panel.update_hp_percent(self.my_hp_percent)
        self.enemy_hp_percent = self.calc_hp_percent(self.enemy_poke_hp_img)
        self.frame.enemy_poke_panel.update_hp_percent(self.enemy_hp_percent)

        self.my_poke_data = self.get_poke_data(my_poke_name_ocr)
        self.enemy_poke_data = self.get_poke_data(enemy_poke_name_ocr)
        print(self.my_poke_data,"len=",len(self.my_poke_data))

        if len(self.my_poke_data)>1:
            print("[my poke] select poke or recapture")
        if len(self.enemy_poke_data)>1:
            print("[enemy poke] select poke or recapture")

        self.my_pokemon.set_poke_data(self.my_poke_data)
        self.enemy_pokemon.set_poke_data(self.enemy_poke_data)
        self.frame.my_poke_panel.set_stats_list()
        self.frame.enemy_poke_panel.set_stats_list()
        self.frame.my_poke_panel.set_stats_type_image(self.my_pokemon._type1,self.my_pokemon._type2)
        self.frame.enemy_poke_panel.set_stats_type_image(self.enemy_pokemon._type1,self.enemy_pokemon._type2)

        #Combobox　初期値
        self.frame.my_poke_panel.poke_stats_name_combobox.SetStringSelection(self.my_poke_data.iloc[0,0])
        self.frame.enemy_poke_panel.poke_stats_name_combobox.SetStringSelection(self.enemy_poke_data.iloc[0,0])

        print(self.frame.my_poke_panel.nature_up_radio_box.GetStringSelection(),self.frame.my_poke_panel.nature_up_radio_box.GetSelection())

        #switch_img=cv2.imread("G:\\my documents\\VScode\\Python\\poke-damage\\amarec(20191228-161218).bmp")
        #self.frame.preview.show_switch_image(switch_img)

    def calc_hp_percent(self,hp_img):
        hp_line_nichi=[]
        for i in range(hp_img.shape[1]):
            max_rgb=max([hp_img[3,i,0],hp_img[3,i,1],hp_img[3,i,2]])
            if max_rgb > self.hp_nichi_threshold:
                hp_line_nichi.append(1)
            else:
                hp_line_nichi.append(0)
        hp_percent = np.sum(hp_line_nichi)/hp_img.shape[1]
        return hp_percent

    def get_poke_data(self,ocr_txt):
        all_poke_match_list = np.zeros(len(self.all_poke_data))
        poke_match_bool=self.all_poke_data["name"]==ocr_txt
        poke_match_bool_val = poke_match_bool.values
        if any(poke_match_bool_val):
            poke_data = self.all_poke_data[poke_match_bool]
        else:
            for i in range(len(ocr_txt)):
                poke_match_bool_one=self.all_poke_data["name"].str.contains(ocr_txt[i])
                poke_match_bool_one_val = poke_match_bool_one.values
                all_poke_match_list = all_poke_match_list + poke_match_bool_one_val.astype(np.int)
            for i in range(len(ocr_txt)-1):
                poke_match_bool_one=self.all_poke_data["name"].str.contains(ocr_txt[i]+ocr_txt[i+1])
                poke_match_bool_one_val = poke_match_bool_one.values
                all_poke_match_list = all_poke_match_list + poke_match_bool_one_val.astype(np.int)
            max_index = [i for i, x in enumerate(all_poke_match_list) if x == max(all_poke_match_list)]#np.argmax(all_poke_match_list)
            poke_data = self.all_poke_data.iloc[max_index]

        return poke_data

    def set_my_poke_nature(self,upstats,downstats):
        if upstats==downstats:
            print("Worning! upstats = downstats")
        else:
            self.my_pokemon.set_nature(upstats,downstats)
            self.frame.my_poke_panel.set_stats_list()


    def set_enemy_poke_nature(self,upstats,downstats):
        if upstats==downstats:
            print("Worning! upstats = downstats")
        else:
            self.enemy_pokemon.set_nature(upstats,downstats)
            self.frame.enemy_poke_panel.set_stats_list()


    def mypoke_combobox_event(self,e):
        name_no = self.frame.my_poke_panel.poke_stats_name_combobox.GetSelection()
        print(name_no)
        poke_data = self.all_poke_data.iloc[[name_no]]
        self.my_pokemon.set_poke_data(poke_data)
        self.frame.my_poke_panel.set_stats_list()
        self.frame.my_poke_panel.set_stats_type_image(self.my_pokemon._type1,self.my_pokemon._type2)

    def enemypoke_combobox_event(self,e):
        name_no = self.frame.enemy_poke_panel.poke_stats_name_combobox.GetSelection()
        poke_data = self.all_poke_data.iloc[[name_no]]
        self.enemy_pokemon.set_poke_data(poke_data)
        self.frame.enemy_poke_panel.set_stats_list()
        self.frame.enemy_poke_panel.set_stats_type_image(self.enemy_pokemon._type1,self.enemy_pokemon._type2)


    def main_loop(self):
        while not self._stop:
            if self._pause:
                time.sleep(0.5)
                continue

            self.input_frame = self.capture.read_frame()
            if self.input_frame is not None:
                #cv2.imshow("fl", input_frame)
                self.frame.preview.show_switch_image(self.input_frame)
            #k = cv2.waitKey(1)

    def set_capture(self, capture):
        self.capture = capture
        self.capture.reset()
        self.capture.reset_tick()
        self.capture.set_frame_rate()
        self.capture.select_source(name=capture.DEV_AMAREC)
    
    def run(self):
        print("run")
        self.main_loop()

    def __init__(self):
        self._pause = True
        self._stop = False
        self.hp_nichi_threshold=130

        self.ocr = Ocr()
        self.all_poke_data = pd.read_csv("data/all_poke_data.csv",encoding="SHIFT-JIS")

        self.my_pokemon = Pokemon()
        self.enemy_pokemon = Pokemon()