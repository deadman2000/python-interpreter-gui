from PyQt5.QtCore import QObject, pyqtSlot, QSize, pyqtProperty, pyqtSignal

# https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
# https://forum.qt.io/topic/87407/communication-between-python-and-qml
from PyQt5.QtGui import QFontMetrics, QFont, QColor


class QmlGlobal(QObject):
    hexLetterChanged = pyqtSignal()
    mainFontChanged = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        self._mainFont = QFont('Hack')
        self._mainFont.setPixelSize(16)

        # updateFontSize
        fm = QFontMetrics(self._mainFont)
        self._hexLetter = fm.size(0, ' ')

    @pyqtSlot('QVariant')
    def createStructure(self, document):
        pass

    @pyqtProperty('QSize', notify=hexLetterChanged)
    def hexLetter(self):
        return self._hexLetter

    @pyqtProperty('QFont', notify=mainFontChanged)
    def mainFont(self):
        return self._mainFont

    @pyqtSlot('QColor', float, result='QColor')
    def blendAlpha(self, color, opacity):
        return QColor(color.red(), color.green(), color.blue(), round(color.alpha() * opacity))
