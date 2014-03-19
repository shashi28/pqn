from PySide.QtCore import *
from PySide.QtGui import *


class Edit(QDialog):
    def __init__(self, string, parent=None):
        super(Edit, self).__init__(parent)

        eLabel = QLabel('Edit Fruit %s'%string)
        self.eEdit = QLineEdit()
        eLabel.setBuddy(self.eEdit)
        eButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        vlayout = QVBoxLayout()
        vlayout.eWidget(eLabel)
        vlayout.eWidget(self.eEdit)
        vlayout.eWidget(eButtonBox)
        self.setLayout(vlayout)

        self.connect(eButtonBox,SIGNAL('accepted()'),self.accept)
        self.connect(eButtonBox,SIGNAL('rejected()'),self.reject)

    def retstring(self):
        return self.eEdit.text()
