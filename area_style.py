from PyQt5.QtCore import QObject, pyqtProperty, Qt, pyqtSignal


class AreaStyle(QObject):
    colorChanged = pyqtSignal()
    borderColorChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._borderWidth = 2
        self._color = Qt.transparent
        self._borderColor = Qt.black

    @pyqtProperty(int)
    def borderWidth(self):
        return self._borderWidth

    @borderWidth.setter
    def borderWidth(self, value):
        self._borderWidth = value

    @pyqtProperty('QColor', notify=colorChanged)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.colorChanged.emit()

    @pyqtProperty('QColor', notify=borderColorChanged)
    def borderColor(self):
        return self._borderColor

    @borderColor.setter
    def borderColor(self, value):
        self._borderColor = value
        self.borderColorChanged.emit()
