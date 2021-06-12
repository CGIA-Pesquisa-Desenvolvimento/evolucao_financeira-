import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_principal import Ui_Principal
##from controller.login import Login
from  controller.principal import Principal
# #import os
# from view.principal import Ui_Principal
# from database import conexao, criar_tabelas
#
# # class Ui_Principal():
# #     def
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     pass
#   #  principal()
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# class login(QDialog):
#     def __init__(self, *args, **kwargs):
#       #  super(principal, self).__init__(*args, **kwargs)
#       super(login, self).__init__(*args, **kwargs)
#       #  self.ui = Ui_Principal()
#       self.ui = Ui_Login()
#       self.ui.setupUi(self)

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = Principal()
    ##window = Login()
    window.show()
sys.exit(app.exec_())
