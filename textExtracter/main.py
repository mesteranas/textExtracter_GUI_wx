import sys
from custome_errors import *
sys.excepthook=my_excepthook
import urlfinder
import xFind

import wx
import settings,gui,guiTools
settings.language.init_translation()
class main(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,title=settings.app.name + _(" version ") + str(settings.app.version))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        self.activeFile = None
        open = wx.Button(panel , -1, "&open text file", pos=(10,235), size=(100,30))
        open.Bind(wx.EVT_BUTTON, self.onOpen)

        wx.StaticText(panel , -1, "text")
        self.re= wx.TextCtrl(panel , -1,style=wx.TE_MULTILINE+wx.HSCROLL)
        gitre = wx.Button(panel,-1,"&get result",pos=(335,30),size=(35,35))
        gitre.Bind(wx.EVT_BUTTON,self.onAdd)
        gitre.SetDefault()
        wx.StaticText(panel , -1, "links")
        self.links = wx.ListBox(panel, -1,)
        wx.StaticText(panel , -1, "Text between quotation marks")
        self.text = wx.ListBox(panel, -1,)
        wx.StaticText(panel , -1, "Text between ( and )")
        self.text1 = wx.ListBox(panel, -1,)
        wx.StaticText(panel , -1, "Text between [ and ]")
        self.text2 = wx.ListBox(panel, -1,)
        wx.StaticText(panel , -1, "Text between { and }")
        self.text3 = wx.ListBox(panel, -1,)
        wx.StaticText(panel , -1, "Text between < and >")
        self.text4 = wx.ListBox(panel, -1,)



        clos = wx.Button(panel , -1, "&back")
        clos.Bind(wx.EVT_BUTTON, self.onback)
        self.settings=wx.Button(panel,-1,_("settings"))
        self.Bind(wx.EVT_BUTTON,lambda event:settings.settings(self).Show(),self.settings)
        sizer.Add(self.settings)
        panel.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE,self.CloseEvent)
        mb=wx.MenuBar()
        help=wx.Menu()
        cus=wx.Menu()
        telegram=cus.Append(-1,"telegram")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/mesteranasm"),telegram)
        telegramChannel=cus.Append(-1,_("telegram channel"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/tprogrammers"),telegramChannel)
        github=cus.Append(-1,"github")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://Github.com/mesteranas"),github)
        x=cus.Append(-1,"X")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://x.com/mesteranasm"),x)
        email=cus.Append(-1,_("email"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.sendEmail("anasformohammed@gmail.com",settings.settings_handler.appName,"hello"),email)
        help.AppendSubMenu(cus,_("contect us"))
        projetGithub=help.Append(-1,_("visit project on github"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://github.com/mesteranas/{}_gui_wx".format(settings.settings_handler.appName)),projetGithub)
        donate=help.Append(-1,_("donate"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"),donate)
        about=help.Append(-1,_("about"))
        self.Bind(wx.EVT_MENU,lambda event:wx.MessageBox(_("{} version: {} description: {} developer: {}").format(settings.app.name,settings.app.version,settings.app.description,settings.app.creater),_("about")),about)
        mb.Append(help,_("help"))
        self.SetMenuBar(mb)
    def CloseEvent(self,event):
        if settings.settings_handler.get("g","exitdialog")=="True":
            guiTools.ExitDialog(self).Show()
        else:
            wx.Exit()
    def onOpen(self, event):
        openDialog = wx.FileDialog(self, "open")
        result = openDialog.ShowModal()
        if result == wx.ID_CANCEL:
            return

        path = openDialog.Path
        filename = openDialog.Filename
        file = open(path, "r", encoding="utf-8")
        self.re.Value = file.read()
        file.close()

    def onAdd(self,event):
        self.links.Set(urlfinder.find_urls(self.re.Value))
        self.text.Set(xFind.xFind(self.re.Value, '"', '"'))
        self.text1.Set(xFind.xFind(self.re.Value, '(', ')'))
        self.text2.Set(xFind.xFind(self.re.Value, '[', ']'))
        self.text3.Set(xFind.xFind(self.re.Value, '{', '}'))
        self.text4.Set(xFind.xFind(self.re.Value, '<', '>'))
    def onback(self, event):
        self.Close()


app=wx.App()
w=main()
w.Show()
app.MainLoop()