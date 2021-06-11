from model.DTO.CategoriaDTO import CategoriaDTO
from model.DAO.CategoriaDAO import CategoriaDAO

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_categoria import Ui_Categoria


class Categoria(QDialog):
    def __init__(self, *args, **kwargs):
        super(Categoria, self).__init__(*args, **kwargs)
        self.ui = Ui_Categoria()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)

    def gravar(self, cat, obs):
        categoriaDAO = CategoriaDAO
        categoriaDAO.Gravar(cat, obs)
        self.apagar()

    def salvar(self):
        c = self.ui.leCategoria.text()
        o = self.ui.pteObs.toPlainText()
        self.gravar(c, o)

    def apagar(self):
        self.ui.leCategoria.clear()
        self.ui.pteObs.clear()


