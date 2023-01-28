from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class GroceryModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Creation and Setup"""
        tableModel = QSqlTableModel()
        tableModel.setTable("groceries")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select(),
        headers = ("Item", "Price", "Type", "Date")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addGrocery(self, data):
        """Adding to the database"""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteGrocery(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
# def selectDateStart(self):
    

# def selectDateEnd(self):