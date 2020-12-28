import wx
import cv2
import numpy as np
import pandas as pd

from engine import PokeDamageEngine
from gui import PokeDamageGUI
from capture.video_capture import VideoCapture
from capture.video_read import VideoRead
from capture.videoinput_wrapper import VideoInputWrapper

def Poke_damage_gui_main ():
    print("poke damage GUI start")

    application = wx.App()
    input_plugin = VideoCapture()

    engine = PokeDamageEngine()
    engine.set_capture(input_plugin)

    gui = PokeDamageGUI(engine)
    engine.set_frame(gui)
    gui.run()
    application.MainLoop()

if __name__ == '__main__':
    Poke_damage_gui_main()