from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from main import download_content

class DownloadThread(QThread):
  def __init__(self, subreddits, limit, top):
    self.subreddits = subreddits
    self.limit = limit
    self.top = top
    QThread.__init__(self)

  def __del__(self):
      self.wait()

  def run(self):
    download_content(self.subreddits, self.limit, self.top)

  def done(self):
    print('done')