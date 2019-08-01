from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog
from ui_settings_window import Ui_Dialog

settings = QSettings('Romain Cascino', 'Reddit Content Downloader')

class SettingsWindow(QDialog, Ui_Dialog):
  def __init__(self, parent=None):
    super(SettingsWindow, self).__init__(parent)
    self.setupUi(self)
    self.client_id.setText(settings.value('client_id', type=str))
    self.client_secret.setText(settings.value('client_secret', type=str))
    self.user_agent.setText(settings.value('user_agent', type=str))

  def accept(self):
    settings.setValue('client_id', self.client_id.text())
    settings.setValue('client_secret', self.client_secret.text())
    settings.setValue('user_agent', self.user_agent.text())
    self.hide()
  
  def reject(self):
    self.hide()