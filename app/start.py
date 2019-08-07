import sys
from PyQt5.QtWidgets import QApplication
from window import MainWindowRcd

app = QApplication(sys.argv)
mainWindow = MainWindowRcd()
mainWindow.show()

rc = app.exec_()
sys.exit(rc)