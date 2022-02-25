import PyQt5.QtWidgets as qtw
from front import Mywindow
import sys

app = qtw.QApplication(sys.argv)
mw = Mywindow()
mw.create_window()

app.exec_()
