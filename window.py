import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_window_rcd import Ui_MainWindow

class MainWindowRcd(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindowRcd, self).__init__(parent)
    self.setupUi(self)
