from PyQt5.QtCore import QObject, pyqtProperty


class InterpreterModel(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._offset = 0
        self._model = None

    @pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value

    @pyqtProperty('QObject')
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value