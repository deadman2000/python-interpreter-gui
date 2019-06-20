from PyQt5.QtCore import pyqtProperty, QAbstractListModel, QVariant, pyqtSignal, Qt

from file_model import FileModel


class InterpreterModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    ValueRole = Qt.UserRole + 2

    modelChanged = pyqtSignal()
    offsetChanged = pyqtSignal()

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._offset = 0
        self._model = None
        self._interpreters = []

    @pyqtProperty(int, notify=offsetChanged)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self.beginResetModel()
        self._offset = value
        self.offsetChanged.emit()
        self.endResetModel()

    @pyqtProperty(FileModel, notify=modelChanged)
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self.beginResetModel()
        self._model = value
        self.modelChanged.emit()
        self.endResetModel()

    def roleNames(self):
        return {
            self.NameRole: b"name",
            self.ValueRole: b"value",
        }

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._interpreters)

    def data(self, index, role=None):
        row = index.row()

        if role == self.NameRole:
            return self._interpreters[row].name

        if role == self.ValueRole:
            if self._model is None:
                return QVariant()
            return self._interpreters[row].toString(self._model, self._offset)

        return QVariant()
