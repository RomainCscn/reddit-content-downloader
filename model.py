from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from collections import namedtuple

Subreddit = namedtuple('Subreddit', 'name')

class SubredditTableModel(QAbstractTableModel):
  def __init__(self, subreddits):
    super(SubredditTableModel, self).__init__()
    self.columnsTitles = ["Name"]
    self.subreddits = subreddits

  def headerData(self, section, orientation, role):
    if role == Qt.DisplayRole and orientation == Qt.Horizontal:
      return self.columnsTitles[section]
    return QVariant()

  def columnCount(self, parent):
    if parent.isValid():
      return 0
    return len(self.columnsTitles)

  def rowCount(self, parent):
    if parent.isValid():
      return 0
    return len(self.subreddits)

  def data(self, index, role):
    if role == Qt.DisplayRole and index.isValid():
      return (self.subreddits[index.row()][0])
    return QVariant()