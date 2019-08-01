import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from ui_main_window_rcd import Ui_MainWindow
from model import Subreddit, SubredditTableModel
from settings_window import SettingsWindow
from downloadThread import DownloadThread

class MainWindowRcd(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindowRcd, self).__init__(parent)
    self.setupUi(self)
    self.subs_not_found = []
    self.subredditTableModel = SubredditTableModel([])
    self.treeViewSubs.setModel(self.subredditTableModel)
    self.treeViewSubs.selectionModel().selectionChanged.connect(self.on_treeViewSubs_selectionChanged)

  def on_treeViewSubs_selectionChanged(self, selected, deselected):
    indexesSelection = selected.indexes()
    if len(indexesSelection) > 0:
      self.indexSelection = indexesSelection[0]
      self.indexSubSelected = self.indexSelection.row()

  @pyqtSlot()
  def on_menuActionSettings_triggered(self):
    settingsWindow = SettingsWindow(self)
    settingsWindow.show()

  @pyqtSlot()
  def on_addButton_clicked(self):
    if len(self.subredditName.text()) == 0:
      QMessageBox.critical(self, "No subreddit", "Please enter a subreddit.", QMessageBox.Ok)
      return
    subreddit = Subreddit(name = self.subredditName.text())
    self.subredditTableModel.addSubreddit(subreddit)
    self.subredditName.setText('')
  
  @pyqtSlot()
  def on_deleteButton_clicked(self):
    selectionModel = self.treeViewSubs.selectionModel()
    indexes = selectionModel.selectedRows()
    if len(indexes) > 0:
      subIndex = indexes[0].row()
      self.subredditTableModel.deleteSubreddit(subIndex)
  
  @pyqtSlot()
  def on_downloadButton_clicked(self):
    limit = self.limitSpinBox.value()
    if self.topComboBox.currentText().lower() == 'all time':
      top = 'all'
    else:
      top = self.topComboBox.currentText().lower()
    subreddits = list(map(lambda s : s.name, self.subredditTableModel.subreddits))
    if len(subreddits) == 0:
      QMessageBox.critical(self, "No subreddits", "You didn't enter any subreddits.", QMessageBox.Ok)
      return
    self.download_thread = DownloadThread(subreddits, limit, top)
    self.download_thread.content_downloaded.connect(self.on_content_downloaded)
    self.download_thread.sub_not_found.connect(self.on_sub_not_found)
    self.download_thread.config_error.connect(self.on_config_error)
    self.download_thread.download_completed.connect(self.download_completed)
    self.downloadButton.setEnabled(False)
    self.cancelButton.setEnabled(True)
    self.progressBar.setMaximum(len(subreddits) * limit)
    self.download_thread.finished.connect(self.download_finished)
    self.download_thread.start()

  @pyqtSlot()
  def on_cancelButton_clicked(self):
    self.progressBar.setValue(0)
    self.download_thread.terminate()

  def on_content_downloaded(self, content_index):
    self.progressBar.setValue(content_index)

  def download_finished(self):
    self.subs_not_found = []
    self.cancelButton.setEnabled(False)
    self.downloadButton.setEnabled(True)
    self.progressBar.setValue(0)
  
  def download_completed(self):
    QMessageBox.information(self, "Done!", "Done downloading content!")

  def on_sub_not_found(self, subreddit):
    self.subs_not_found.append(subreddit)
    self.download_info.setText(f"{'Subreddits' if len(self.subs_not_found) > 1 else 'Subreddit'} {' '.join(list(map(lambda s : 'r/' + s, self.subs_not_found)))} not found")

  def on_config_error(self):
    QMessageBox.critical(self, "Config error", "Oops, an error occured. Please check your configuration values.", QMessageBox.Ok)
