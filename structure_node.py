from PyQt5.QtCore import pyqtSignal, pyqtProperty

from tree_node import TreeNode


class StructureNode(TreeNode):
    expandedChanged = pyqtSignal()

    def __init__(self, parent, block):
        TreeNode.__init__(self, parent)
        self._expanded = False

    @pyqtProperty(bool, notify=expandedChanged)
    def expanded(self):
        return self._expanded

    @expanded.setter
    def expanded(self, value):
        self._expanded = value
        self.expandedChanged.emit()
