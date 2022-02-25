import wx

class Mywindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Graphic Interface')
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = Mywindow()
    app.MainLoop()