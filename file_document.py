from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot

from file_model import FileModel


class FileDocument(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._data = FileModel()
        self._fileName = ''

    @pyqtProperty('QVariant')
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @pyqtSlot('QString')
    def openFile(self, path):
        self._fileName = path
        self._data.openFile(path)

    @pyqtProperty('QString', constant=True)
    def fileName(self):
        return self._fileName
