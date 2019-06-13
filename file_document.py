from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot

from interpreter.formats.win32exe import ExeFormat

from file_model import FileModel


class FileDocument(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._data = FileModel()
        self._fileName = ''
        self.structure = None

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
        self.load_structure()

    @pyqtProperty('QString', constant=True)
    def fileName(self):
        return self._fileName

    def load_structure(self):
        fmt = ExeFormat()
        self.structure = fmt.parse_file(self._fileName, to_meta=True, compact_meta=False)
        print(self.structure)
