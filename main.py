# -*- coding:utf-8 -*-
import os
import sys

import wx

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='pip安装工具', size=(479, 324),name='frame',style=541072384)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.window_name_lable = wx.StaticText(self.启动窗口,size=(271, 36),pos=(82, 11),label='pip安装工具',name='window_name_lable',style=2321)
        window_name_lable_字体 = wx.Font(15,74,90,400,False,'Microsoft YaHei UI',28)
        self.window_name_lable.SetFont(window_name_lable_字体)
        self.组合框2 = wx.ComboBox(self.启动窗口,value='',pos=(105, 55),name='comboBox',choices=['豆瓣源', '清华源', '阿里云', '中科大', '山东理工大学', '华中理工大学', ''],style=16)
        self.组合框2.SetSize((113, 21))
        self.标签2 = wx.StaticText(self.启动窗口,size=(89, 25),pos=(19, 55),label='安装镜像源：',name='staticText',style=2321)
        self.分组单选框2 = wx.RadioBox(self.启动窗口,size=(182, 60),pos=(268, 55),label='选择地区',choices=['国内源', '国外源(普通)'],majorDimension=0,name='radioBox',style=4)
        self.分组单选框2.Bind(wx.EVT_RADIOBOX,self.分组单选框2_选项被单击)
        self.标签3 = wx.StaticText(self.启动窗口,size=(420, 18),pos=(25, 124),label='想要安装的python库，存在多个，用空格隔开,镜像源选择指的是国内的',name='staticText',style=2321)
        self.ku = wx.TextCtrl(self.启动窗口,size=(441, 83),pos=(14, 147),value='',name='ku',style=1073741856)
        self.pip_install_start = wx.Button(self.启动窗口,size=(75, 33),pos=(36, 236),label='开始',name='button')
        self.pip_install_start.SetForegroundColour((255, 0, 0, 255))
        self.pip_install_start.Bind(wx.EVT_BUTTON,self.pip_install_start_按钮被单击)
        self.pip_close = wx.Button(self.启动窗口,size=(75, 33),pos=(297, 236),label='关闭',name='pip_close')
        self.pip_close.Bind(wx.EVT_BUTTON,self.pip_close_按钮被单击)


    def 分组单选框2_选项被单击(self,event):
        print('分组单选框2,选项被单击')


    def pip_install_start_按钮被单击(self,event):
        #print('pip_install_start,按钮被单击')
        pip_yuan = self.组合框2.GetSelection()
        pip_yuan += 1
        pip_diqu = self.分组单选框2.GetSelection()
        pip_install_name = self.ku.GetValue()
        #print(pip_yuan)
        #print(pip_diqu)
        print(pip_install_name)
        pip_yuan_int = int(pip_yuan)
        pip_diqu_int = int(pip_diqu)
        if pip_diqu_int == 0:
            print('国内源')
            if pip_yuan_int == -1:
                wx.MessageBox("请选择一个镜像源！", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
            if pip_yuan_int == 1:#豆瓣源
                wx.MessageBox("准备安装，豆瓣源，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i https://pypi.douban.com/simple/')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)

            if pip_yuan_int == 2:#清华源
                wx.MessageBox("准备安装，清华源，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i https://pypi.tuna.tsinghua.edu.cn/simple')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)

            if pip_yuan_int == 3:#阿里云
                wx.MessageBox("准备安装，阿里云，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i http://mirrors.aliyun.com/pypi/simple/')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)

            if pip_yuan_int == 4:#中科大
                wx.MessageBox("准备安装，中科大，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i https://pypi.mirrors.ustc.edu.cn/simple/')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)

            if pip_yuan_int == 5:#山东理工大学
                wx.MessageBox("准备安装，山东理工大学，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i http://pypi.sdutlinux.org/')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)

            if pip_yuan_int == 6:#华中理工大学
                wx.MessageBox("准备安装，华中理工大学，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
                os.system('python -m pip install '+pip_install_name+' -i http://pypi.hustunique.com/')
                wx.MessageBox("安装完成", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
            #else:
                #print('失败')

        if pip_diqu_int == 2:
            wx.MessageBox("准备安装，国外源，按“ok”开始，请查看控制台。如果报错，请查看是否输入有误或pip工具出错。国内使用尽量选国内，网速更快。", "pip安装工具", wx.OK | wx.ICON_INFORMATION)
            os.system('python -m pip install '+pip_install_name)
            wx.MessageBox("安装成功", "pip安装工具", wx.OK | wx.ICON_INFORMATION)



    def pip_close_按钮被单击(self,event):
        sys.exit()

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
