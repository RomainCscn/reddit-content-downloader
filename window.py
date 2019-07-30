import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_window_rcd import Ui_MainWindow
from model import Subreddit, SubredditTableModel
from downloadThread import DownloadThread

class MainWindowRcd(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindowRcd, self).__init__(parent)
    self.setupUi(self)
    self.subredditTableModel = SubredditTableModel([])
    self.treeViewSubs.setModel(self.subredditTableModel)
    self.treeViewSubs.selectionModel().selectionChanged.connect(self.on_treeViewSubs_selectionChanged)

  def on_treeViewSubs_selectionChanged(self, selected, deselected):
    indexesSelection = selected.indexes()
    if len(indexesSelection) > 0:
      self.indexSelection = indexesSelection[0]
      self.indexSubSelected = self.indexSelection.row()

  @pyqtSlot()
  def on_addButton_clicked(self):
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
    top = self.topComboBox.currentText().lower()
    subreddits = list(map(lambda s : s.name, self.subredditTableModel.subreddits))
    self.download_thread = DownloadThread(subreddits, limit, top)
    self.download_thread.content_downloaded.connect(self.onContentDownloaded)
    self.downloadButton.setEnabled(False)
    self.cancelButton.setEnabled(True)
    self.progressBar.setMaximum(len(subreddits) * limit)
    self.download_thread.finished.connect(self.download_finished)
    self.download_thread.start()

  def onContentDownloaded(self, content_index):
    self.progressBar.setValue(content_index)

  @pyqtSlot()
  def on_cancelButton_clicked(self):
    self.progressBar.setValue(0)
    self.download_thread.terminate()

  def download_finished(self):
    self.cancelButton.setEnabled(False)
    self.downloadButton.setEnabled(True)
    self.progressBar.setValue(0)