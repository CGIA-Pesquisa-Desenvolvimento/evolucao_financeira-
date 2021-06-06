from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from controller.principal import Principal
from view.frm_login import Ui_Login


class Login(QDialog):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pbOk.clicked.connect(self.login)
        self.ui.pbCancelar.clicked.connect(self.cancelar)


    def login(self):
        self.windown = Principal()
        self.windown.show()

    def cancelar(self):
        sys.exit()
