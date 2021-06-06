from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_cadastro_usuario import Ui_CadastroUsuario


class CadastroUsuario(QDialog):
    def __init__(self, *args, **kwargs):
        super(CadastroUsuario, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroUsuario()
        self.ui.setupUi(self)
