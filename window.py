import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_window_rcd import Ui_MainWindow
from model import Subreddit, SubredditTableModel

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