from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot

from file_model import FileModel


class FileDocument(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._data = FileModel()

    @pyqtProperty('QObject')
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @pyqtSlot('QString')
    def openFile(self, path):
        print('openFile', path)
