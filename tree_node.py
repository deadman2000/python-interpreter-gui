from PyQt5.QtCore import QAbstractListModel, pyqtProperty, pyqtSignal, Qt, QVariant, QModelIndex, pyqtSlot


class TreeNode(QAbstractListModel):
    NodeRole = Qt.UserRole + 1

    textChanged = pyqtSignal()
    iconChanged = pyqtSignal()
    countChanged = pyqtSignal()

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._text = ''
        self._icon = ''
        self._nodes = []

    @pyqtProperty('QString', notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.textChanged.emit()

    @pyqtProperty('QString', notify=iconChanged)
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.iconChanged.emit()

    @pyqtProperty(int, notify=countChanged)
    def count(self):
        return len(self._nodes)

    @pyqtProperty('QObject')
    def parentNode(self):
        return self.parent()

    def roleNames(self):
        return { self.NodeRole: b"node" }

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._nodes)

    def data(self, index, role=None):
        row = index.row()

        if role == TreeNode.NodeRole:
            return QVariant(self._nodes[row])

        return QVariant()

    def indexOf(self, node):
        return self._nodes.index(node)

    @pyqtSlot()
    def update(self):
        for n in self._nodes:
            n.update()

    @pyqtSlot('QObject')
    def append(self, node):
        self.insert(len(self._nodes), node)

    @pyqtSlot(int, 'QObject')
    def insert(self, index, node):
        print('insert', node.parentNode()) # TODO Check it
        if node.parentNode() is not None:
            node.remove()
        node.setParent(self)

        self.beginInsertRows(QModelIndex(), index, index)
        self._nodes.append(node)
        self.endInsertRows()

        self.countChanged.emit()

    @pyqtSlot()
    def remove(self):
        self.parentNode().removeChild(self)

    @pyqtSlot('QObject')
    def removeChild(self, node):
        node.setParent(None)
        i = self._nodes.index(node)

        self.beginRemoveRows(QModelIndex(), i, i)
        del self._nodes[i]
        self.endRemoveRows()

        self.countChanged.emit()

    @pyqtSlot('QObject')
    def moveBefore(self, target):
        self.remove()
        i = target.parentNode().indexOf(target)
        target.parentNode().insert(i, self)

    @pyqtSlot('QObject')
    def moveAfter(self, target):
        self.remove()
        i = target.parentNode().indexOf(target)
        target.parentNode().insert(i + 1, self)

    @pyqtSlot('QObject', result=bool)
    def canAppend(self, node):
        return True
