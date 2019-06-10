from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot

from area_style import AreaStyle


class AddressRange(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._style = None

    @pyqtProperty(AreaStyle)
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value

    @pyqtSlot()
    def reset(self):
        pass
