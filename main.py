# -*- coding: utf-8 -*-
# gdb/main.py

"""Groceries DB application."""
import sys
from PyQt5.QtWidgets import QApplication
from database import createConnection
from views import Window

def main():
    app = QApplication(sys.argv)
    if not createConnection("groceries.sqlite"):
        sys.ext(1)
    win = Window()
    win.show()
    sys.exit(app.exec())