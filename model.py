from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from collections import namedtuple
import json

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

  def saveSubsInFile(self, filename):
    with open(filename, 'w') as f:
      json.dump(self.subreddits, f)

  @staticmethod
  def createFromFile(filename):
    with open(filename, 'r') as f:
      jsonSubreddits = json.load(f)
    subreddits = [Subreddit(*jsonSubreddit) for jsonSubreddit in jsonSubreddits]
    return SubredditTableModel(subreddits)

  def addSubreddit(self, subreddit):
    subredditIndex = len(self.subreddits)
    self.beginInsertRows(QModelIndex(), subredditIndex, subredditIndex)
    self.subreddits.append(subreddit)
    self.endInsertRows()

  def deleteSubreddit(self, subredditIndex):
    self.beginRemoveRows(QModelIndex(), subredditIndex, subredditIndex)
    del self.subreddits[subredditIndex]
    self.endRemoveRows()

  def replaceSubreddit(self, subredditIndex, subreddit):
    self.subreddits[subredditIndex] = subreddit
    self.dataChanged.emit(self.createIndex(subredditIndex, 0), self.createIndex(subredditIndex, 2))