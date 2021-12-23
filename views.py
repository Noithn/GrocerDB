import sqlite3
import pandas as pd

#This is for the UI
import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QLine, QSize
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QPushButton,
    QTableView,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox, 
    QLabel, 
    QGridLayout,
    QVBoxLayout, 
    QWidget, 
    QApplication,
    )
from model import GroceryModel
from GDB import itemSelectorSort
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
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete...")
        self.deleteButton.clicked.connect(self.deleteGrocery)
        #Calendar Select
        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateedit2 = QtWidgets.QDateEdit(calendarPopup=True)
        self.dateedit2.setDateTime(QtCore.QDateTime.currentDateTime())
        #self.clearAllButton = QPushButton("Clear All")
        #Dropdown Select
        self.cb = QComboBox()
        self.cb.addItem("All")
        self.cb.addItems(itemSelectorSort)
        self.cb.currentIndexChanged.connect(self.select)
        #Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.cb)
        layout.addWidget(self.dateedit)
        layout.addWidget(self.dateedit2)
        layout.addStretch()
        #layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """OPening Add dialog"""
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

    def select(self,i):
        """Selecting item dropdown"""
        print("Items in the list are :")
		
        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index",i,"selection changed ",self.cb.currentText())

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
        #self.keyField = QLineEdit()
        #self.keyField.setObjectName("Key")
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
        #layout.addRow("Key:", self.keyField)
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