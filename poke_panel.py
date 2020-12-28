import wx
import cv2

class PokePanel(wx.Panel):

    def create_poke_name_panel(self):
        self.poke_name_panel =wx.Panel(self.poke_panel, wx.ID_ANY,size=(300,40)) 
        self.poke_name_panel.SetBackgroundColour('#FF0000')

        self.poke_name_txt_panel =wx.Panel(self.poke_name_panel, wx.ID_ANY,pos=(0,10), size=(160,30)) 
        self.poke_name_txt_panel.SetBackgroundColour('#FFFF00')

        self.wx_name = wx.StaticText(self.poke_name_txt_panel,wx.ID_ANY,"けつばん",style=wx.EXPAND)
        self.font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.wx_name.SetFont(self.font)

        self.create_poke_name_img_panel()


    def create_poke_name_img_panel(self):
        self.poke_name_img_panel=wx.Panel(self.poke_name_panel, wx.ID_ANY,pos=(160,10), size=(140,30)) 
        self.poke_name_img_panel.SetBackgroundColour('#AF0000')

    def create_poke_hp_panel(self):
        self.poke_hp_panel = wx.Panel(self.poke_panel, wx.ID_ANY,size=(300,60)) 
        self.poke_hp_panel.SetBackgroundColour('#005F00')
        
        self.poke_hp_img_panel = wx.Panel(self.poke_hp_panel, wx.ID_ANY,pos=(5,12), size=(270,8)) 
        self.poke_hp_img_panel.SetBackgroundColour('#00FF00')

        self.poke_hp_text_panel = wx.Panel(self.poke_hp_panel, wx.ID_ANY,pos=(0,30), size=(300,30))
        self.poke_hp_text_panel.SetBackgroundColour('#00AF00')

        self.poke_hp_text_percent_panel = wx.Panel(self.poke_hp_text_panel, wx.ID_ANY,pos=(20,0), size=(80,30))
        self.poke_hp_text_percent_panel.SetBackgroundColour('#5FAF00')

        self.wx_hp_percent = wx.StaticText(self.poke_hp_text_percent_panel,wx.ID_ANY,"00.00%",style=wx.EXPAND)
        self.font_hp = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.wx_hp_percent.SetFont(self.font_hp)

    def show_name_image(self,img):
        name_img_size=(140,30)
        img_resize = cv2.resize(img, name_img_size)
        img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
        bmp = wx.Bitmap.FromBuffer(name_img_size[0], name_img_size[1], img_rgb)
        dc = wx.ClientDC(self.poke_name_img_panel)
        dc.DrawBitmap(bmp, 0, 0)

    def show_hp_image(self,img):
        hp_img_size=(270,8)
        img_resize = cv2.resize(img, hp_img_size)
        img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
        bmp = wx.Bitmap.FromBuffer(hp_img_size[0], hp_img_size[1], img_rgb)
        dc = wx.ClientDC(self.poke_hp_img_panel)
        dc.DrawBitmap(bmp, 0, 0)

    def change_poke_name(self,name):
        self.name=name
        wx.StaticText.SetLabel(self.wx_name,self.name)


    def update_hp_percent(self,hp_percent):
        hp_percent_str = '{:.2f}'.format(hp_percent*100)+"%"
        wx.StaticText.SetLabel(self.wx_hp_percent,hp_percent_str)

    def create_button_panel(self):
        panel = self.poke_panel
        self.button_capture = wx.Button(panel, wx.ID_ANY, 'Capture')

        self.buttons_layout = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons_layout.Add(self.button_capture)

        self.button_capture.Bind(wx.EVT_BUTTON, self.engine.on_button_capture)

    def create_radiobox_panel(self):
        self.radio_box_panel = wx.Panel(self.poke_panel, wx.ID_ANY,size=(300,110)) 
        self.radio_box_panel.SetBackgroundColour('#AFAFFF')
        button_aray=('なし','A','B','C','D','S')
        self.nature_up_radio_box_panel = wx.Panel(self.radio_box_panel, wx.ID_ANY,size=(300,55),pos=(0,0)) 
        self.nature_up_radio_box = wx.RadioBox(self.nature_up_radio_box_panel,wx.ID_ANY,label="せいかく上昇",choices=button_aray,style=wx.RA_HORIZONTAL)
        self.nature_down_radio_box_panel = wx.Panel(self.radio_box_panel, wx.ID_ANY,size=(300,55),pos=(0,55)) 
        self.nature_down_radio_box = wx.RadioBox(self.nature_down_radio_box_panel,wx.ID_ANY,label="せいかく下降",choices=button_aray,style=wx.RA_HORIZONTAL)

        self.nature_up_radio_box.Bind(wx.EVT_RADIOBOX,self.selected_radio_box)
        self.nature_down_radio_box.Bind(wx.EVT_RADIOBOX,self.selected_radio_box)

    def selected_radio_box(self,e):
        print(self.nature_up_radio_box.GetSelection())
        if self.side:
            self.engine.set_enemy_poke_nature(self.nature_up_radio_box.GetSelection(),self.nature_down_radio_box.GetSelection())
        else:
            self.engine.set_my_poke_nature(self.nature_up_radio_box.GetSelection(),self.nature_down_radio_box.GetSelection())

    def create_stats_poke_name_type_panel(self):
        self.poke_stats_name_type_panel = wx.Panel(self.poke_panel, wx.ID_ANY,size=(300,30))
        self.poke_stats_name_panel =  wx.Panel(self.poke_stats_name_type_panel, wx.ID_ANY,size=(200,30), pos=(0,0))
        self.element_array = self.engine.all_poke_data["name"].values.tolist()
        print(self.element_array)
        self.poke_stats_name_combobox = wx.ComboBox(self.poke_stats_name_panel, wx.ID_ANY, choices=self.element_array , style=wx.CB_DROPDOWN)
        self.poke_stats_name_combobox.SetSelection(0)

        if self.side:
            self.poke_stats_name_combobox.Bind(wx.EVT_COMBOBOX, self.engine.enemypoke_combobox_event)
        else:
            self.poke_stats_name_combobox.Bind(wx.EVT_COMBOBOX, self.engine.mypoke_combobox_event)

        self.create_stats_type_panel()

    def create_stats_panel(self):
        caption = ("","HP","A","B","C","D","S")

        self.poke_stats_panel = wx.Panel(self.poke_panel, wx.ID_ANY,size=(300,170)) 
        self.poke_stats_panel.SetBackgroundColour('#5F005F')
        self.poke_stats_list = wx.ListCtrl(self.poke_stats_panel, wx.ID_ANY, size=(300,170),pos=(0,0),style = wx.LC_REPORT | wx.LC_HRULES)
        
        for c,v in enumerate(caption):
            self.poke_stats_list.InsertColumn(c,v,width=42)
        #self.poke_stats_list.InsertColumn(0,"test")
        self.poke_stats_list.InsertItem(0,"個体")#str(self.engine.my_pokemon._stats[0]))
        self.poke_stats_list.InsertItem(1,"最高")
        self.poke_stats_list.InsertItem(2,"準")
        self.poke_stats_list.InsertItem(3,"無振")
        self.poke_stats_list.InsertItem(4,"下降")
        self.poke_stats_list.InsertItem(5,"最低")
        self.poke_stats_list.InsertItem(6,"選択")

    def create_stats_type_panel(self):
        self.poke_type_panel1 = wx.Panel(self.poke_stats_name_type_panel, wx.ID_ANY,size=(48,21), pos=(180,0)) 
        self.poke_type_panel1.SetBackgroundColour('#FF005F')
        self.poke_type_panel2 = wx.Panel(self.poke_stats_name_type_panel, wx.ID_ANY,size=(48,21), pos=(230,0)) 
        self.poke_type_panel2.SetBackgroundColour('#FF005F')

    def set_stats_type_image(self,type1,type2):
        img_size=(48,21)
        img1 = self.type_str2img(type1)#self.img_nomal
        if img1 is not None:
            img_resize = cv2.resize(img1, img_size)
            img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
            bmp = wx.Bitmap.FromBuffer(img_size[0], img_size[1], img_rgb)
            dc = wx.ClientDC(self.poke_type_panel1)
            dc.DrawBitmap(bmp, 0, 0)
        img2 = self.type_str2img(type2)#self.img_nomal
        if img2 is not None:
            img_resize2 = cv2.resize(img2, img_size)
            img_rgb2 = cv2.cvtColor(img_resize2, cv2.COLOR_BGR2RGB)
            bmp2 = wx.Bitmap.FromBuffer(img_size[0], img_size[1], img_rgb2)
            dc2 = wx.ClientDC(self.poke_type_panel2)
            dc2.DrawBitmap(bmp2, 0, 0)
        else:
            dc2 = wx.ClientDC(self.poke_type_panel2)
            dc2.Clear()

    def type_str2img(self,type_str):
        if type_str == "ノーマル":
            img = self.img_nomal
        elif type_str == "かくとう":
            img = self.img_kakutou
        elif type_str == "ひこう":
            img = self.img_hikou
        elif type_str == "どく":
            img = self.img_doku
        elif type_str == "じめん":
            img = self.img_jimen
        elif type_str == "いわ":
            img = self.img_iwa
        elif type_str == "むし":
            img = self.img_mushi
        elif type_str == "ゴースト":
            img = self.img_goast
        elif type_str == "はがね":
            img = self.img_hagane
        elif type_str == "ほのお":
            img = self.img_honoo
        elif type_str == "みず":
            img = self.img_mizu
        elif type_str == "くさ":
            img = self.img_kusa
        elif type_str == "でんき":
            img = self.img_dennki
        elif type_str == "エスパー":
            img = self.img_esper
        elif type_str == "こおり":
            img = self.img_koori
        elif type_str == "ドラゴン":
            img = self.img_dragon
        elif type_str == "あく":
            img = self.img_aku
        elif type_str == "フェアリー":
            img = self.img_fairy
        else:
            img = None
        return img



    def set_stats_list(self):
        if self.side:
            for col in range(1,len(self.engine.enemy_pokemon._base_stats)+1):
                    self.poke_stats_list.SetItem(0,col,str(self.engine.enemy_pokemon._base_stats[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats_max)+1):
                    self.poke_stats_list.SetItem(1,col,str(self.engine.enemy_pokemon._stats_max[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats_jyun)+1):
                    self.poke_stats_list.SetItem(2,col,str(self.engine.enemy_pokemon._stats_jyun[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats_mufuri)+1):
                    self.poke_stats_list.SetItem(3,col,str(self.engine.enemy_pokemon._stats_mufuri[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats_kakou)+1):
                    self.poke_stats_list.SetItem(4,col,str(self.engine.enemy_pokemon._stats_kakou[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats_min)+1):
                    self.poke_stats_list.SetItem(5,col,str(self.engine.enemy_pokemon._stats_min[col-1]))
            for col in range(1,len(self.engine.enemy_pokemon._stats)+1):
                    self.poke_stats_list.SetItem(6,col,str(self.engine.enemy_pokemon._stats[col-1]))
        else:
            for col in range(1,len(self.engine.my_pokemon._base_stats)+1):
                    self.poke_stats_list.SetItem(0,col,str(self.engine.my_pokemon._base_stats[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats_max)+1):
                    self.poke_stats_list.SetItem(1,col,str(self.engine.my_pokemon._stats_max[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats_jyun)+1):
                    self.poke_stats_list.SetItem(2,col,str(self.engine.my_pokemon._stats_jyun[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats_mufuri)+1):
                    self.poke_stats_list.SetItem(3,col,str(self.engine.my_pokemon._stats_mufuri[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats_kakou)+1):
                    self.poke_stats_list.SetItem(4,col,str(self.engine.my_pokemon._stats_kakou[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats_min)+1):
                    self.poke_stats_list.SetItem(5,col,str(self.engine.my_pokemon._stats_min[col-1]))
            for col in range(1,len(self.engine.my_pokemon._stats)+1):
                    self.poke_stats_list.SetItem(6,col,str(self.engine.my_pokemon._stats[col-1]))

    def set_engine(self,engine):
        self.engine=engine

    def __init__(self, engine, side, *args, **kwargs):
        self.engine=engine
        self.side = side
        wx.Panel.__init__(self, *args, **kwargs)
        self.panel_size = (300, 720)
        # Preview image.
        self.poke_panel = wx.Panel(self, wx.ID_ANY,size=self.panel_size)
        #self.preview_panel.SetBackgroundColour('#000000')

        self.create_poke_name_panel()
        self.create_poke_hp_panel()
        self.create_button_panel()
        self.create_radiobox_panel()
        self.create_stats_poke_name_type_panel()
        self.create_stats_panel()

        self.poke_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.poke_panel_sizer.Add(self.poke_name_panel)
        self.poke_panel_sizer.Add(self.poke_hp_panel)
        self.poke_panel_sizer.Add(self.radio_box_panel)
        self.poke_panel_sizer.Add(self.poke_stats_name_type_panel)
        self.poke_panel_sizer.Add(self.poke_stats_panel)
        self.poke_panel_sizer.Add(self.buttons_layout)
        self.SetSizer(self.poke_panel_sizer)

        gif_nomal = cv2.VideoCapture("data\\type_img\\n0.gif")
        gif_kakutou = cv2.VideoCapture("data\\type_img\\n1.gif")
        gif_hikou = cv2.VideoCapture("data\\type_img\\n2.gif")
        gif_doku = cv2.VideoCapture("data\\type_img\\n3.gif")
        gif_jimen = cv2.VideoCapture("data\\type_img\\n4.gif")
        gif_iwa = cv2.VideoCapture("data\\type_img\\n5.gif")
        gif_mushi = cv2.VideoCapture("data\\type_img\\n6.gif")
        gif_goast = cv2.VideoCapture("data\\type_img\\n7.gif")
        gif_hagane = cv2.VideoCapture("data\\type_img\\n8.gif")
        gif_honoo = cv2.VideoCapture("data\\type_img\\n9.gif")
        gif_mizu = cv2.VideoCapture("data\\type_img\\n10.gif")
        gif_kusa = cv2.VideoCapture("data\\type_img\\n11.gif")
        gif_dennki = cv2.VideoCapture("data\\type_img\\n12.gif")
        gif_esper = cv2.VideoCapture("data\\type_img\\n13.gif")
        gif_koori = cv2.VideoCapture("data\\type_img\\n14.gif")
        gif_dragon = cv2.VideoCapture("data\\type_img\\n15.gif")
        gif_aku = cv2.VideoCapture("data\\type_img\\n16.gif")
        gif_fairy = cv2.VideoCapture("data\\type_img\\n17.gif")
        _, self.img_nomal = gif_nomal.read()
        _, self.img_kakutou = gif_kakutou.read()
        _, self.img_hikou = gif_hikou.read()
        _, self.img_doku = gif_doku.read()
        _, self.img_jimen = gif_jimen.read()
        _, self.img_iwa = gif_iwa.read()
        _, self.img_mushi = gif_mushi.read()
        _, self.img_goast = gif_goast.read()
        _, self.img_hagane = gif_hagane.read()
        _, self.img_honoo = gif_honoo.read()
        _, self.img_mizu = gif_mizu.read()
        _, self.img_kusa = gif_kusa.read()
        _, self.img_dennki = gif_dennki.read()
        _, self.img_esper = gif_esper.read()
        _, self.img_koori = gif_koori.read()
        _, self.img_dragon = gif_dragon.read()
        _, self.img_aku = gif_aku.read()
        _, self.img_fairy = gif_fairy.read()
        #self.set_stats_type_image("ノーマル","a")
        #cv2.imshow('img_my_hp_sobel', self.img_nomal)
        #cv2.waitKey(0)