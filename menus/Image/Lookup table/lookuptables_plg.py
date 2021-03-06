# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:13:42 2016

@author: yxl
"""
import IPy
from imageplus import ImagePlus
from ui.canvasframe import CanvasFrame
from core.managers import ColorManager
import numpy as np
from core.engines import Free

class Plugin(Free):
    def __init__(self, key):
        self.title = key
    
    #process
    def run(self, para = None):
        
        plus = IPy.get_ips()
        if plus==None:
            img = np.ones((30,1), dtype=np.uint8) * np.arange(256, dtype=np.uint8)
            ips = ImagePlus([img])
            frame = CanvasFrame(IPy.curapp)
            frame.set_ips(ips)
            ips.lut = ColorManager.get_lut(self.title)
            frame.Show()
        elif plus.chanels!=1:
            IPy.alert('RGB image do not surport Lookup table!')
            return
        else:
            plus.lut = ColorManager.get_lut(self.title)
            plus.update = 'pix'
    
    def __call__(self):
        return self
          
plgs = [Plugin(i) for i in ColorManager.luts.keys()]
for i in range(len(plgs)):
    if plgs[i].title == 'Grays':
        plgs.insert(0, plgs.pop(i))

if __name__ == '__main__':
    print ColorManager.luts.keys()
    