import sys
from PySide.QtGui import *
from PySide.QtCore import *
import stringadd

class MainForm(QDialog):
    def __init__(self, string, stringlist, parent=None):
        super(MainForm, self).__init__(parent)
        self.list = stringlist
        self.stringList = QListWidget()
        self.cur = None
        '''self.stringList.addItems(self.list)'''
        for element in self.list:
            QListWidgetItem(element, self.stringList)
        buttonAdd = QPushButton('&Add')
        buttonEdit = QPushButton('&Edit')
        buttonRemove = QPushButton('&Remove')
        buttonUp = QPushButton('&Up')
        buttonDown = QPushButton('&Down')
        buttonSort = QPushButton('&Sort')
        buttonClose = QPushButton('Close')

        vLayout = QVBoxLayout()
        vLayout.addWidget(buttonAdd)
        vLayout.addWidget(buttonEdit)
        vLayout.addWidget(buttonRemove)
        vLayout.addWidget(buttonUp)
        vLayout.addWidget(buttonDown)
        vLayout.addWidget(buttonSort)
        vLayout.addWidget(buttonClose)

        grid = QGridLayout()
        grid.addWidget(self.stringList, 0,0)
        grid.addLayout(vLayout, 0, 1)
        self.setLayout(grid)

        self.connect(buttonAdd, SIGNAL('clicked()'), self.add)
        self.connect(buttonEdit, SIGNAL('clicked()'), self.edit)
        self.connect(buttonRemove, SIGNAL('clicked()'), self.remove)
        self.connect(buttonUp, SIGNAL('clicked()'), self.up)
        self.connect(buttonDown, SIGNAL('clicked()'), self.down)
        self.connect(buttonSort, SIGNAL('clicked()'), self.sort)
        self.connect(buttonClose, SIGNAL('clicked()'), self.reject)
        self.connect(self.stringList, SIGNAL('itemSelectionChanged()'), self.closeeditor)

        self.setWindowTitle('Edit %s List'%string)

    def add(self):
        dialog = stringadd.Add(self)
        if dialog.exec_():
            self.stringList.insertItem(self.stringList.currentRow(),dialog.retstring())

    def edit(self):
        self.cur = self.stringList.currentItem()
        self.stringList.openPersistentEditor(self.cur)
        self.stringList.editItem(self.cur)

    def closeeditor(self):
        self.stringList.closePersistentEditor(self.cur)

    def remove(self):
        self.stringList.removeItemWidget(self.stringList.currentItem())
        self.stringList.takeItem(self.stringList.currentRow())

    def up(self):
        new = self.stringList.currentItem()
        self.stringList.removeItemWidget(new)
        self.stringList.takeItem(self.stringList.row(new))
        self.stringList.insertItem(self.stringList.currentRow()-1,new)
        self.stringList.setCurrentItem(self.stringList.item(self.stringList.currentRow()-2))


    def down(self):
        new = self.stringList.currentItem()
        self.stringList.removeItemWidget(new)
        self.stringList.takeItem(self.stringList.row(new))
        self.stringList.insertItem(self.stringList.currentRow()+1,new)
        self.stringList.setCurrentItem(self.stringList.item(self.stringList.currentRow()+1))

    def sort(self):
        self.stringList.sortItems(Qt.AscendingOrder)



if __name__ == '__main__':
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig","Guava", "Mango", "Honeydew Melon", "Date",
             "Watermelon", "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi", "Lemon", "Nectarine", "Plum",
             "Raspberry", "Strawberry", "Orange"]
    app =QApplication(sys.argv)
    form = MainForm('Fruit', fruit)
    form.show()
    app.exec_()
