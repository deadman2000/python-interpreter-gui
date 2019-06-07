from PyQt5.QtCore import QObject, pyqtProperty


class FileDocument(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._data = None

    @pyqtProperty('QObject')
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
