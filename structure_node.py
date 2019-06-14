from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot
from PyQt5.QtGui import QColor

from address_range import AddressRange
from area_style import AreaStyle
from tree_node import TreeNode

PALETTE = [
    QColor(0xF44336),
    QColor(0xE91E63),
    QColor(0x9C27B0),
    QColor(0x673AB7),
    QColor(0x3F51B5),
    QColor(0x2196F3),
    QColor(0x03A9F4),
    QColor(0x00BCD4),
    QColor(0x009688),
    QColor(0x4CAF50),
    QColor(0x8BC34A),
    QColor(0xCDDC39),
    QColor(0xFFEB3B),
    QColor(0xFFC107),
    QColor(0xFF9800),
    QColor(0xFF5722),
    QColor(0x795548)
]

NEXT_COLOR_IND = 0


def get_next_color():
    global NEXT_COLOR_IND
    c = NEXT_COLOR_IND
    NEXT_COLOR_IND = (NEXT_COLOR_IND + 1) % len(PALETTE)
    return PALETTE[c]


class StructureNode(TreeNode):
    expandedChanged = pyqtSignal()

    def __init__(self, parent, offset=0, size=0, type=0, value=None, name=None, sections=None):
        TreeNode.__init__(self, parent)
        self._expanded = False
        self._value = value

        self._range = AddressRange(self, offset, offset + size - 1)
        self._range.update_isset()

        c = get_next_color()
        bgr = QColor(c)
        bgr.setAlpha(25)
        self._range.style = AreaStyle(color=bgr, borderColor=c, borderWidth=2)

        self._range.is_block = True

        if sections is not None:
            sections.append(self._range)

        if isinstance(value, dict):
            self._text = name
            for k in value:
                self._nodes.append(StructureNode(self, name=k, **value[k], sections=sections))
        else:
            self.text = '{}: <b>{}</b>'.format(name, value)

        if parent is None:
            self._expanded = True
            self.show()

    @pyqtProperty(bool, notify=expandedChanged)
    def expanded(self):
        return self._expanded

    @expanded.setter
    def expanded(self, value):
        self._expanded = value
        self.show()
        self.expandedChanged.emit()

    def show(self):
        if self._expanded and len(self._nodes) > 0:
            self._range.visible = False
            for n in self._nodes:
                n.show()
        else:
            self._range.visible = True
            for n in self._nodes:
                n.hide()

    def hide(self):
        self._range.visible = False
        for n in self._nodes:
            n.hide()

    @pyqtProperty(AddressRange)
    def range(self):
        return self._range

    @pyqtSlot()
    def select(self):
        self._range.select()

        for n in self._nodes:
            n.select()

    @pyqtSlot()
    def unselect(self):
        self._range.unselect()

        for n in self._nodes:
            n.unselect()

    @pyqtSlot(int)
    def getByAddress(self, address):
        if self._range.isSet:
            if not self._range.visible or not self._range.contains(address):
                return None

        if self._expanded:
            for n in self._nodes:
                r = n.getByAddress(address)
                if n is not None:
                    return r

        if self._range.isSet:
            return self._range

        return None
