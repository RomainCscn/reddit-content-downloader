import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_window_rcd import Ui_MainWindow
from model import Subreddit, SubredditTableModel

class MainWindowRcd(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindowRcd, self).__init__(parent)
    self.setupUi(self)
    subredditsTest = [Subreddit("Tinder"), Subreddit("test")]
    self.subredditTableModel = SubredditTableModel(subredditsTest)
    self.treeViewSubs.setModel(self.subredditTableModel)
    self.treeViewSubs.selectionModel().selectionChanged.connect(self.on_treeViewSubs_selectionChanged)

  def on_treeViewSubs_selectionChanged(self, selected, deselected):
    indexesSelection = selected.indexes()
    if len(indexesSelection) > 0:
      self.indexSelection = indexesSelection[0]
      self.indexSubSelected = self.indexSelection.row()