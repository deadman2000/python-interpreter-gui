from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal

from area_style import AreaStyle


class AddressRange(QObject):
    changed = pyqtSignal()

    def __init__(self, parent=None, begin=-1, end=-1):
        QObject.__init__(self, parent)
        self._begin = begin
        self._end = end
        self._style = None
        self._isSet = False
        self._visible = True
        self._selected = False
        self._shadow = False
        self._name = ''
        self.is_block = False

    @pyqtProperty(int, notify=changed)
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
        self.update_isset()
        self.changed.emit()

    @pyqtProperty(int, notify=changed)
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
        self.update_isset()
        self.changed.emit()

    @pyqtProperty(bool, notify=changed)
    def isSet(self):
        return self._isSet

    @pyqtProperty(int, notify=changed)
    def size(self):
        if not self._isSet:
            return 0
        return self._end - self._begin + 1

    @pyqtProperty(AreaStyle, notify=changed)
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value
        self.unselect()

    @pyqtProperty(bool, notify=changed)
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
        self.changed.emit()

    @pyqtProperty(bool, notify=changed)
    def selected(self):
        return self._selected

    @pyqtProperty(bool, notify=changed)
    def shadow(self):
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        self._shadow = value
        self.changed.emit()

    @pyqtProperty(bool, notify=changed)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.changed.emit()

    @pyqtSlot()
    def reset(self):
        self._begin = -1
        self._end = -1
        self.update_isset()
        self.changed.emit()

    @pyqtSlot()
    def select(self):
        self._selected = True
        self.changed.emit()

    @pyqtSlot()
    def unselect(self):
        self._selected = False
        self.changed.emit()

    def update_isset(self):
        self._isSet = self._begin != -1 and self._end != -1

    @pyqtSlot(int, result=bool)
    def contains(self, address):
        return self._begin <= address <= self._end
