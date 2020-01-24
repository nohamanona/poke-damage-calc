import wx

class Mywin(wx.Frame):
    def __init__(self,parent,title):
        super(Mywin,self).__init__(parent,title=title,size=(500,300))
        self.name="けつばん"
        self.h="0"
        self.a="0"
        self.b="0"
        self.c="0"
        self.d="0"
        self.s="0"
        # self.panel = wx.Panel(self,wx.ID_ANY)
        root_panel = wx.Panel(self, wx.ID_ANY)
        base_stats_header_panel = BaseStatsHeaderPanel(root_panel)
        name_text_panel = NamePanel(root_panel)
        name_text_panel.get_name(self.name)
        ability_up_radio_box_panel = AbilityUpRadioBoxPanel(root_panel)
        self.base_stats_panel = BaseStatsPanel(root_panel)
        self.base_stats_panel.get_base_stats(self.h,self.a,self.b,self.c,self.d,self.s)
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(name_text_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(ability_up_radio_box_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(base_stats_header_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(self.base_stats_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)
        #self.InitializeComponents()
        self.Centre()
        self.Show(True)

    def get_my_base_stats(self,h,a,b,c,d,s):
        self.h=h
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.s=s
        self.base_stats_panel.get_base_stats(self.h,self.a,self.b,self.c,self.d,self.s)
    
    def InitUI(self):
        #self.CreateStatusBar()
        #self.panel = wx.Panel(self,wx.ID_ANY)
        #self.panel.SetBackgroundColour('#FFFFFF')
        #self.InitCompo()
        self.button_aray=('なし','H','A','B','C','D','S')
        self.radio_box = wx.RadioBox(self.panel,wx.ID_ANY,label="とくせい上昇",choices=self.button_aray,style=wx.RA_HORIZONTAL)
        self.panel.Bind(wx.EVT_RADIOBOX,self.selected_radio_text)
        #self.Centre()
        #self.Show(True)
    
    def OnPaint(self,e):
        dc = wx.PaintDC(self.panel)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()
        pen=wx.Pen(wx.Colour(0,0,255))
        dc.SetPen(pen)
        dc.DrawRectangle(380,15,90,60)
    
    def InitCompo(self):
        name="a"
        self.companel = wx.Panel(self.panel,wx.ID_ANY,pos=(0,100),size=(300,100))
        self.companel.SetBackgroundColour('#0000FF')
        button1 = wx.Button(self.companel, -1, "Button 1")
        button2 = wx.Button(self.companel, -1, "Button 2")
        # self.text1 = wx.StaticText(self.companel,wx.ID_ANY,"表示test",style=wx.EXPAND)
        # self.text2 = wx.StaticText(self.companel,wx.ID_ANY,self.name,style=wx.EXPAND)
        # self.text3 = wx.StaticText(self.companel,wx.ID_ANY,"",style=wx.ALIGN_CENTER)
        # self.text4 = wx.StaticText(self.companel,wx.ID_ANY,"",style=wx.ALIGN_CENTER)
        # self.text5 = wx.StaticText(self.companel,wx.ID_ANY,"",style=wx.ALIGN_CENTER)
        # self.text6 = wx.StaticText(self.companel,wx.ID_ANY,"",style=wx.ALIGN_CENTER)
        # self.text11 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)
        # self.text12 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)
        # self.text13 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)
        # self.text14 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)
        # self.text15 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)
        # self.text16 = wx.StaticText(self.companel,wx.ID_ANY,self.h,style=wx.ALIGN_CENTER)

        # sizer = wx.FlexGridSizer(rows=2,cols=3,gap=(0,0))
        # sizer.Add(self.text1,flag=wx.EXPAND)
        # sizer.Add(self.text2,flag=wx.EXPAND)
        # sizer.Add(self.text3,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text4,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text5,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text6,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text11,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text12,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text13,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text14,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text15,flag=wx.ALIGN_CENTER)
        # sizer.Add(self.text16,flag=wx.ALIGN_CENTER)
        sizer = wx.FlexGridSizer(rows=2,cols=3,gap=(0,0))
        sizer.Add(button1, flag=wx.EXPAND)
        sizer.Add(button2, flag=wx.EXPAND)
        # sizer.AddGrowableCol(0,1)
        # sizer.AddGrowableCol(1,1)
        # sizer.AddGrowableCol(2,1)
        # sizer.AddGrowableCol(3,1)
        # sizer.AddGrowableCol(4,1)
        # sizer.AddGrowableCol(5,1)
        self.companel.SetSizer(sizer)

class BaseStatsHeaderPanel(wx.Panel):
    """
    a
    """
  
    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
  
        button_collection = ('H', 'A', 'B', 'C','D', 'S')
  
        layout = wx.GridSizer(1, 6, 3, 3)
          
        for i in button_collection:
            layout.Add(wx.StaticText(self, wx.ID_ANY, i, size=(30,25)), 1, flag=wx.ALIGN_CENTER)
  
        self.SetSizer(layout)

    def InitializeComponents(self):
        mainPanel = wx.Panel(self,wx.ID_ANY)
        button1 = wx.Button(mainPanel, -1, "Button 1")
        button2 = wx.Button(mainPanel, -1, "Button 2")
        button3 = wx.Button(mainPanel, -1, "Button 3")
        button4 = wx.Button(mainPanel, -1, "Button 4")
        button5 = wx.Button(mainPanel, -1, "Button 5")
        button6 = wx.Button(mainPanel, -1, "Button 6")

        # Create a sizer.
        sizer = wx.FlexGridSizer(rows=2,cols=3,gap=(0,0))
        sizer.Add(button1, flag=wx.EXPAND)
        sizer.Add(button2, flag=wx.EXPAND)
        sizer.Add(button3, flag=wx.EXPAND)
        sizer.Add(button4, flag=wx.EXPAND)
        sizer.Add(button5, flag=wx.EXPAND)
        sizer.Add(button6, flag=wx.EXPAND)
        mainPanel.SetSizer(sizer)
    
    def selected_radio_text(self,e):
        str_in = self.radio_box.GetStringSelection()
        wx.StaticText.SetLabel(self.text1,str_in)

    def set_status(self,name=None,h=0,a=0,b=0,c=0,d=0,s=0):
        #to change static input
        self.name = name
        self.h=h
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.s=s

class BaseStatsPanel(wx.Panel):
    """
    a
    """
  
    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)

        self._h="0"
        self._a="0"
        self._b="0"
        self._c="0"
        self._d="0"
        self._s="0"

        button_collection = (self._h, self._a, self._b, self._c, self._d, self._s)
  
        layout = wx.GridSizer(1, 6, 3, 3)
          
        for i in button_collection:
            layout.Add(wx.StaticText(self, wx.ID_ANY, i, size=(30,25)), 1, flag=wx.ALIGN_CENTER)
  
        self.SetSizer(layout)

    def get_base_stats(self,h,a,b,c,d,s):
        self._h=h
        self._a=a
        self._b=b
        self._c=c
        self._d=d
        self._s=s


class NamePanel(wx.Panel):
    """
    画面上部に表示されるテキスト部分
    """
  
    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
        
        self._name = "None"

        name_text = wx.StaticText(self, wx.ID_ANY,self._name)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(name_text, 1)
        self.SetSizer(layout)

    def get_name(self,name):
        self._name=name

class AbilityUpRadioBoxPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        button_aray=('なし','H','A','B','C','D','S')
        self._radio_box = wx.RadioBox(self,wx.ID_ANY,label="とくせい上昇",choices=button_aray,style=wx.RA_HORIZONTAL)
        self._text1 = wx.StaticText(self,wx.ID_ANY,"None",style=wx.EXPAND)
        self.Bind(wx.EVT_RADIOBOX,self.selected_radio_text)

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self._radio_box, 1)
        layout.Add(self._text1, 1)
        self.SetSizer(layout)

    def selected_radio_text(self,e):
        strin=self._radio_box.GetStringSelection()
        wx.StaticText.SetLabel(self._text1,strin)


if __name__ == "__main__":
    app=wx.App()
    Mywin(None,'Drawing test')
    app.MainLoop()