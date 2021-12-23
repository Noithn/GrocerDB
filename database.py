""" Database Connection """
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
#Item,Price,Type,Date

def _createGroceryTable():
    #Creating Grocery table
    createTableQuery = QSqlQuery()
    return createTableQuery.exec (
        """
            CREATE TABLE IF NOT EXISTS groceries (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                item VARCHAR(50) NOT NULL,
                price INT,
                type VARCHAR(50) NOT NULL,
                date VARCHAR(50)
            )
        """
    )

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning (
            None,
            "Groceries",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
#    _createGroceryTable()
    return True