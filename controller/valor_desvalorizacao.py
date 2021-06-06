from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_valor_desvalorizacao import Ui_ValorDesvalorizacao


class ValorDesvalorizacao(QDialog):
    def __init__(self, *args, **kwargs):
        super(ValorDesvalorizacao, self).__init__(*args, **kwargs)
        self.ui = Ui_ValorDesvalorizacao()
        self.ui.setupUi(self)
