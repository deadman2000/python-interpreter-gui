from PyQt5.QtCore import QObject, pyqtSlot, QSize, pyqtProperty, pyqtSignal

# https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
# https://forum.qt.io/topic/87407/communication-between-python-and-qml
from PyQt5.QtGui import QFontMetrics, QFont, QColor

from file_document import FileDocument
from structure_node import StructureNode


class QmlGlobal(QObject):
    fontChanged = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        self._rowHeight = 32
        self._mainFont = QFont('Hack')
        self._mainFont.setPixelSize(16)

        # updateFontSize
        fm = QFontMetrics(self._mainFont)
        self._hexLetter = fm.size(0, ' ')

    @pyqtProperty(int, notify=fontChanged)
    def rowHeight(self):
        return self._rowHeight

    @pyqtSlot('QVariant')
    def createStructure(self, document: FileDocument):
        if document.structure:
            return StructureNode(None, document.structure)

    @pyqtProperty('QSize', notify=fontChanged)
    def hexLetter(self):
        return self._hexLetter

    @pyqtProperty('QFont', notify=fontChanged)
    def mainFont(self):
        return self._mainFont

    @pyqtSlot('QColor', float, result='QColor')
    def blendAlpha(self, color, opacity):
        return QColor(color.red(), color.green(), color.blue(), round(color.alpha() * opacity))
