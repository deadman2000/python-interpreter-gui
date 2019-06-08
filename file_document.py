from PyQt5.QtCore import QObject, pyqtProperty


class FileDocument(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._data = None

    @pyqtProperty('QObject')
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
