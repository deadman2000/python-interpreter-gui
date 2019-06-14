from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal
from PyQt5.QtQml import QQmlListProperty

from interpreter.formats.win32exe import ExeFormat

from address_range import AddressRange
from file_model import FileModel
from structure_node import StructureNode


class FileDocument(QObject):
    structureChanged = pyqtSignal()
    sectionsChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._data = FileModel()
        self._fileName = ''
        self._structure = None
        self._meta = None
        self._sections = []

    @pyqtProperty('QVariant')
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @pyqtProperty(QQmlListProperty, notify=sectionsChanged)
    def sections(self):
        return QQmlListProperty(AddressRange, self, self._sections)

    @pyqtSlot('QString')
    def openFile(self, path):
        self._fileName = path
        self._data.openFile(path)
        self.load_structure()

    @pyqtProperty('QString', constant=True)
    def fileName(self):
        return self._fileName

    @pyqtProperty(StructureNode, notify=structureChanged)
    def structure(self):
        return self._structure

    def load_structure(self):
        fmt = ExeFormat()
        self._meta = fmt.parse_file(self._fileName, to_meta=True, compact_meta=False)
        self.create_structure(self._meta)

    def create_structure(self, meta):
        self._structure = StructureNode(None, value=meta, sections=self._sections)
        self.structureChanged.emit()
        self.sectionsChanged.emit()
