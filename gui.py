import wx
import threading

from panel import PreviewPanel
from poke_panel import PokePanel
from damage_calc_panel import DamageCalcPanel


class PokeDamageGUI(object):
    def __init__(self,engine):
        self.engine=engine
        self.frame = wx.Frame(None, wx.ID_ANY, "Poke Damage GUI")#, size=(1880, 720))

        self.layout = wx.BoxSizer(wx.HORIZONTAL)
        self.preview = PreviewPanel(self.frame, size=(1280, 720))
        self.my_poke_panel = PokePanel(self.engine, 0, self.frame, size=(300,720))
        self.enemy_poke_panel = PokePanel(self.engine, 1, self.frame, size=(300,720))
        self.damage_calc_panel = DamageCalcPanel(self.engine, self.frame, size=(1880,250))
        self.layout.Add(self.my_poke_panel)#, flag=wx.EXPAND)
        self.layout.Add(self.preview)#, flag=wx.EXPAND)
        self.layout.Add(self.enemy_poke_panel)#, flag=wx.EXPAND)
        self.layout_v = wx.BoxSizer(wx.VERTICAL)
        self.layout_v.Add(self.layout)
        self.layout_v.Add(self.damage_calc_panel)
        self.frame.SetSizer(self.layout_v)
        self.layout_v.Fit(self.frame)

    def engine_thread_func(self):
        print('Poke Damage GUI thread started')
        self.engine.pause(False)
        self.engine.run()
        print('Poke Damage GUI thread terminated')

    def run(self):
        self.engine_thread = threading.Thread(target=self.engine_thread_func)
        self.engine_thread.daemon = True
        self.engine_thread.start()

        self.frame.Show()
