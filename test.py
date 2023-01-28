from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.dateEdit = QDateEdit(self)
        self.lbl = QLabel()
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)

        layout = QGridLayout()
        layout.addWidget(self.dateEdit)
        layout.addWidget(self.lbl)
        self.setLayout(layout)


        self.dateEdit.dateChanged.connect(self.onDateChanged)

    def onDateChanged(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.month(),qDate.day(), qDate.year()))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())