import wx
import cv2

class PreviewPanel(wx.Panel):

    def show_switch_image(self,img):
        img_size=(1280,720)
        img_resize = cv2.resize(img, img_size)
        img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
        bmp = wx.Bitmap.FromBuffer(img_size[0], img_size[1], img_rgb)
        dc = wx.ClientDC(self.preview_panel)
        dc.DrawBitmap(bmp, 0, 0)

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.preview_size = (1280, 720)
        # Preview image.
        self.preview_panel = wx.Panel(self, wx.ID_ANY, size=self.preview_size)
        self.preview_panel.SetBackgroundColour('#0000FF')

        self.top_sizer = wx.BoxSizer(wx.VERTICAL)
        self.top_sizer.Add(self.preview_panel)
        self.SetSizer(self.top_sizer)