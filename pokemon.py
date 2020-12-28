import numpy as np
import math
class Pokemon(object):
    def __init__(self):
        self._name="けつばん"
        self._lv=50
        self._base_stats_h=0
        self._base_stats_a=0
        self._base_stats_b=0
        self._base_stats_c=0
        self._base_stats_d=0
        self._base_stats_s=0
        self._base_stats = [0,0,0,0,0,0]
        self._type1="None"
        self._type2="None"
        self._individual_value=[31,31,31,31,31,31]
        self._individual_value_max=[31,31,31,31,31,31]
        self._individual_value_min=[0,0,0,0,0,0]
        self._effort_value=[0,0,0,0,0,0]
        self._effort_value_max=[255,255,255,255,255,255]
        self._effort_value_min=[0,0,0,0,0,0]
        self._stats_h=0
        self._stats=[0,0,0,0,0,0]
        self._nature=[1,1,1,1,1]
        self._nature_max=[1.1,1.1,1.1,1.1,1.1]
        self._nature_none=[1,1,1,1,1]
        self._nature_min=[0.9,0.9,0.9,0.9,0.9]
        self._stats_max =[0,0,0,0,0,0]
        self._stats_jyun =[0,0,0,0,0,0]
        self._stats_mufuri =[0,0,0,0,0,0]
        self._stats_kakou =[0,0,0,0,0,0]
        self._stats_min =[0,0,0,0,0,0]
        self.now_hp=0
        self.hp_percent=100

        self._thr=130

    def hp_img2float(self,img):
        enemy_hp_line_nichi=[]
        for i in range(img.shape[1]):
            max_rgb=max([img[3,i,0],img[3,i,1],img[3,i,2]])
            if max_rgb > self._thr:
                enemy_hp_line_nichi.append(1)
            else:
                enemy_hp_line_nichi.append(0)
        return np.sum(enemy_hp_line_nichi)/img.shape[1]

    def set_now_hp(self,img):
        self.hp_percent= self.hp_img2float(img)
        self._now_hp = self._stats_h * self.hp_percent

    def set_base_stats(self,stats):
        self._base_stats_h = stats[0]
        self._base_stats_a = stats[1]
        self._base_stats_b = stats[2]
        self._base_stats_c = stats[3]
        self._base_stats_d = stats[4]
        self._base_stats_s = stats[5]
        self.calc_stats()

    def set_poke_data(self,poke_data):
        self._name = poke_data.iloc[0,0]
        self._base_stats[0] = poke_data.iloc[0,1]
        self._base_stats[1] = poke_data.iloc[0,2]
        self._base_stats[2] = poke_data.iloc[0,3]
        self._base_stats[3] = poke_data.iloc[0,4]
        self._base_stats[4] = poke_data.iloc[0,5]
        self._base_stats[5] = poke_data.iloc[0,6]
        self._type1 = poke_data.iloc[0,7]
        self._type2 = poke_data.iloc[0,8]

        self.calc_stats_all()

        print(self._name,self._stats_h)
        print(self._base_stats)
        print("stats",self._stats,self._nature)
        print(self._stats_max)
        print(self._stats_jyun)
        print(self._stats_mufuri)
        print(self._stats_kakou)
        print(self._stats_min)

    def calc_stats(self):
        self._stats[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value[0] + self._effort_value[0]/4) * self._lv /100  + self._lv +10)
        self.calc_stats_abcds()

    def calc_stats_abcds(self):
        for i in range(1,6):
            self._stats[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value[i] + self._effort_value[0]/4) * self._lv /100 +5) * self._nature[i-1])

    def calc_stats_all(self):
        self.calc_stats()
        #calc max
        self._stats_max[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value_max[0] + self._effort_value_max[0]/4) * self._lv /100  + self._lv +10)
        for i in range(1,6):
            self._stats_max[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value_max[i] + self._effort_value_max[0]/4) * self._lv /100 +5) * self._nature_max[i-1])
        #calc jyunn 個体値努力値最大、性格補正なし
        self._stats_jyun[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value_max[0] + self._effort_value_max[0]/4) * self._lv /100  + self._lv +10)
        for i in range(1,6):
            self._stats_jyun[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value_max[i] + self._effort_value_max[0]/4) * self._lv /100 +5) * self._nature_none[i-1])
        #calc mufuri 個体値最大、努力値０、性格補正なし
        self._stats_mufuri[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value_max[0] + self._effort_value_min[0]/4) * self._lv /100  + self._lv +10)
        for i in range(1,6):
            self._stats_mufuri[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value_max[i] + self._effort_value_min[0]/4) * self._lv /100 +5) * self._nature_none[i-1])
        #calc kakou 個体値最大、努力値０、性格補正0.9
        self._stats_kakou[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value_max[0] + self._effort_value_min[0]/4) * self._lv /100  + self._lv +10)
        for i in range(1,6):
            self._stats_kakou[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value_max[i] + self._effort_value_min[0]/4) * self._lv /100 +5) * self._nature_min[i-1])
        #calc min 個体値０、努力値０、性格補正0.9
        self._stats_min[0] = math.floor(math.floor(self._base_stats[0] *2 + self._individual_value_min[0] + self._effort_value_min[0]/4) * self._lv /100  + self._lv +10)
        for i in range(1,6):
            self._stats_min[i] = math.floor(math.floor(math.floor(self._base_stats[i]*2 + self._individual_value_min[i] + self._effort_value_min[0]/4) * self._lv /100 +5) * self._nature_min[i-1])

    def set_nature(self,upstats,downstats):
        self._nature=[1,1,1,1,1]
        if upstats!=0:self._nature[upstats-1] = 1.1
        if downstats!=0:self._nature[downstats-1] = 0.9
        self.calc_stats_abcds()
        print(self._nature)