from PyQt5.QtCore import QObject, pyqtProperty, Qt


class AreaStyle(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._borderWidth = 2
        self._color = Qt.transparent
        self._borderColor = Qt.black

    @pyqtProperty(int)
    def borderWidth(self):
        return self._borderWidth

    @borderWidth.setter
    def borderWidth(self, value):
        self._borderWidth = value


    @pyqtProperty('QColor')
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


    @pyqtProperty('QColor')
    def borderColor(self):
        return self._borderColor

    @borderColor.setter
    def borderColor(self, value):
        self._borderColor = value
