from PyQt5.QtCore import pyqtProperty, QAbstractListModel, QVariant


class InterpreterModel(QAbstractListModel):
    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._offset = 0
        self._model = None

    @pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value

    @pyqtProperty('QVariant')
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def rowCount(self, parent=None, *args, **kwargs):
        return 0

    def data(self, index, role=None):
        return QVariant()
