import wx
import cv2

class DamageCalcPanel(wx.Panel):
    
    def __init__(self, engine, *args, **kwargs):
        self.engine=engine
        wx.Panel.__init__(self, *args, **kwargs)
        self.panel_size = (1880, 250)