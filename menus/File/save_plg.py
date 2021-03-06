# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 03:19:13 2016

@author: yxl
"""
from scipy.misc import imsave
from core.engines import Simple
import wx, IPy

class Plugin(Simple):
    title = 'Save'
    note = ['all']
    
    #parameter
    para = {'path':'./'}
    
    def show(self):
        filt = 'BMP files (*.bmp)|*.bmp|PNG files (*.png)|*.png|JPG files (*.jpg)|*.jpg|GIF files (*.gif)|*.gif'
        return IPy.getpath('save..', filt, self.para)

    #process
    def run(self, ips, img, para = None):
        imsave(para['path'], ips.get_img())

if __name__ == '__main__':
	print Plugin.title
	app = wx.App(False)
	Plugin().run()