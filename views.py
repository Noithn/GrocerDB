import sqlite3
import pandas as pd

#This is for the UI
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from soupsieve import select
from model import GroceryModel
from GDB import itemSelectorSort, graphing
selected_item = []
endDate = []
startDate = []
class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Groceries")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.GroceryModel = GroceryModel()
        self.setupUI()
    
    def setupUI(self):
        """Main Window GUI"""
        #Table view
        self.table = QTableView()
        self.table.setModel(self.GroceryModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        self.fileButton = QPushButton("Import Grocery File")
        ###self.addButton.clicked.connect(self.addFile)
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete...")
        self.deleteButton.clicked.connect(self.deleteGrocery)
        self.goButton = QPushButton("Show Graph")
        self.goButton.clicked.connect(lambda: graphing(selected_item, startDate, endDate))
        #Show Graph button call.
        # self.goButton.clicked.connect(self.showGraph)
        #Calendar Start
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.onSelectStart)
        #self.dateEdit.dateChanged.connect(QtWidgets.QDateEdit.lineEdit(lambda: dateStart))
        #self.dateEdit.dateChanged.connect(l)
        #self.qDate = self.dateEdit.setDateTime(QtCore.QDateTime.)
        #print(self.qDate)
        #self.dateEdit.dateChanged.connect(lambda: print(self.dateEdit.setDateTime(QtCore.QDateTime.)))
        #Calendar End
        self.dateEdit2 = QDateEdit(self)
        self.dateEdit2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit2.setCalendarPopup(True)
        self.dateEdit2.dateChanged.connect(self.onSelectEnd)
        #self.clearAllButton = QPushButton("Clear All")
        #Dropdown Select
        self.cb = QComboBox()
        self.cb.addItem("All")
        self.cb.addItems(itemSelectorSort)
        self.cb.currentTextChanged.connect(self.selectedItem)
        #Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.fileButton)
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.cb)
        layout.addWidget(self.dateEdit)
        layout.addWidget(self.dateEdit2)
        layout.addWidget(self.goButton)
        layout.addStretch()
        #layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
    
    def openAddDialog(self):
        """Opening Add dialog"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.GroceryModel.addGrocery(dialog.data)
            self.table.resizeColumnsToContents()
    def deleteGrocery(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        messageBox = QMessageBox.warning(
            self,
            "Achtung",
            "Do you want to delete this item?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if messageBox == QMessageBox.Ok:
            self.GroceryModel.deleteGrocery(row)

    #Item Selection
    def selectedItem(self,itemSelected):
        # """Selecting item dropdown"""
        selected_item.clear()
        itemSelected = self.cb.currentText()
        selected_item.append(itemSelected)
        #print(str(selected_item).replace("'", ''))
        return(str(selected_item[0]).replace("'", ''))

    #Start Date Selection
    def onSelectStart(self, Date):
        startDate.clear()
        startDateSelect = '{0}/{1}/{2}'.format(Date.year(), Date.month(), Date.day())
        startDate.append(startDateSelect)
        print(str(startDate[0]))
        return(startDate[0])

    #End Date Selection
    def onSelectEnd(self, Date):
        endDate.clear()
        endDateSelect = '{0}/{1}/{2}'.format(Date.year(), Date.month(), Date.day())
        endDate.append(endDateSelect)
        print(str(endDate[0]))
        return(endDate)
class AddDialog(QDialog):
    """Adding Groceries"""
    def __init__(self, parent=None):
        """Initializing"""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Groceries")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setupUI()
    
    def setupUI(self):
        """Dialog GUI"""
        #Line edits
        self.itemField = QLineEdit()
        self.itemField.setObjectName("Item")
        self.priceField = QLineEdit()
        self.priceField.setObjectName("Price")
        self.typeField = QLineEdit()
        self.typeField.setObjectName("Type")
        self.dateField = QLineEdit()
        self.dateField.setObjectName("Date")
        #Layout of fields
        layout = QFormLayout()
        layout.addRow("Item:", self.itemField)
        layout.addRow("Price:", self.priceField)
        layout.addRow("Type:", self.typeField)
        layout.addRow("Date:", self.dateField)
        self.layout.addLayout(layout)
        #Add buttons to the dialog
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
    def accept(self):
        """Accepting data through input"""
        self.data = []
        for field in (self.itemField, self.priceField, self.typeField, self.dateField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error",
                    f"You must provide the item's {field.objectName()}",
                )
                self.data = None
                return
            self.data.append(field.text())

        if not self.data:
            return
        super().accept()