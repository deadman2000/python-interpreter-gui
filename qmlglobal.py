from PyQt5.QtCore import QObject, pyqtSlot

# https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
# https://forum.qt.io/topic/87407/communication-between-python-and-qml


class QmlGlobal(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot()
    def test(self):
        print('test...')
