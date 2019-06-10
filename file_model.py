import math
import os
from mmap import mmap, ACCESS_READ

from PyQt5.QtCore import QAbstractListModel, Qt, QVariant, pyqtProperty, pyqtSignal


class FileModel(QAbstractListModel):
    RowSize = 16

    AddressRole = Qt.UserRole + 1
    HexRole = Qt.UserRole + 2
    TextRole = Qt.UserRole + 3

    rowsChanged = pyqtSignal()

    def __init__(self):
        QAbstractListModel.__init__(self)
        self._fileSize = 0
        self._rowCount = 0
        self._file = None
        self._mm = None

    @pyqtProperty(int, notify=rowsChanged)
    def rows(self):
        return self._rowCount

    @pyqtProperty(int, notify=rowsChanged)
    def size(self):
        return self._fileSize

    def openFile(self, path):
        self.beginResetModel()
        self._fileSize = os.path.getsize(path)
        self._rowCount = math.ceil(self._fileSize / FileModel.RowSize)
        self._file = open(path, 'rb')
        self._mm = mmap(self._file.fileno(), 0, access=ACCESS_READ)
        self.endResetModel()

        self.rowsChanged.emit()

    def rowCount(self, parent=None, *args, **kwargs):
        return self._rowCount

    def data(self, index, role=None):
        row = index.row()

        address = row * FileModel.RowSize
        size = FileModel.RowSize
        if address + size > self._fileSize:
            size = self._fileSize - address

        if role == FileModel.AddressRole:
            return "{:04X} {:04X}".format(address >> 16, address & 0xffff)

        rowData = self._mm[address:address+size]

        if role == FileModel.HexRole:
            return " ".join("{:02X}".format(v) for v in rowData)

        if role == FileModel.TextRole:
            return "".join(chr(v) if 32 <= v < 128 else '.' for v in rowData)

        return QVariant()

    def roleNames(self):
        return {
            self.AddressRole: b"address",
            self.HexRole: b"hex",
            self.TextRole: b"fileText",
        }
