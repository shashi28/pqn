from PySide.QtCore import *
from PySide.QtGui import *


class Add(QDialog):
    def __init__(self, parent=None):
        super(Add, self).__init__(parent)

        addLabel = QLabel('Add Fruit')
        self.addEdit = QLineEdit()
        addLabel.setBuddy(self.addEdit)
        addButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        vlayout = QVBoxLayout()
        vlayout.addWidget(addLabel)
        vlayout.addWidget(self.addEdit)
        vlayout.addWidget(addButtonBox)
        self.setLayout(vlayout)

        self.connect(addButtonBox,SIGNAL('accepted()'),self.accept)
        self.connect(addButtonBox,SIGNAL('rejected()'),self.reject)

    def retstring(self):
        return self.addEdit.text()
