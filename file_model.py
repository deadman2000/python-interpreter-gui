from PyQt5.QtCore import QAbstractListModel


class FileModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)

    def rowCount(self, parent=None, *args, **kwargs):
        return 10

    def data(self, QModelIndex, role=None):
        return b'1234567890'