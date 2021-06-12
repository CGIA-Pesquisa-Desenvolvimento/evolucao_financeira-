from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from model.DTO.FornecedorDTO import FornecedorDTO
from model.DAO.FornecedorDAO import FornecedorDAO

from view.frm_fornecedor import Ui_Fornecedor


class Fornecedor(QDialog):
    def __init__(self, *args, **kwargs):
        super(Fornecedor, self).__init__(*args, **kwargs)
        self.ui = Ui_Fornecedor()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)

    def gravar(self, nome, instituicao, descricao):
        fornecedorDAO = FornecedorDAO
        fornecedorDAO.gravar(nome, instituicao, descricao)
        self.apagar()

    def salvar(self):
        n = self.ui.leFornecedor.text()
        if self.ui.cbinstituicaoBancaria.isChecked():
            i = 1
        else:
            i = 0
        d = self.ui.pteDescricao.toPlainText()
        self.gravar(n, i, d)

    def apagar(self):
        self.ui.leFornecedor.clear()
        self.ui.cbinstituicaoBancaria.setChecked(False)
        self.ui.pteDescricao.clear()


