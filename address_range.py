from PyQt5.QtCore import QObject, pyqtProperty

from area_style import AreaStyle


class AddressRange(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._style = None

    @pyqtProperty(AreaStyle)
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value
