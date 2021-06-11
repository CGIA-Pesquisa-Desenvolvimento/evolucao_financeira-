from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from model.DAO.CadastroUsuarioDAO import CadastroUsuarioDAO
from model.DTO.UsuarioDTO import UsuarioDTO
from view.frm_cadastro_usuario import Ui_CadastroUsuario


class CadastroUsuario(QDialog):
    def __init__(self, *args, **kwargs):
        super(CadastroUsuario, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroUsuario()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)

    def gravar(self, nome, email, senha):
        usuarioDAO = CadastroUsuarioDAO
        usuarioDAO.gravar(nome, email, senha)
        self.apagar()

    def salvar(self):
        n = self.ui.leNome.text()
        l = self.ui.leLogin.text()
        s = self.ui.leSenha.text()
        self.gravar(n, l, s)

    def apagar(self):
        self.ui.leLogin.clear()
        self.ui.leSenha.clear()
        self.ui.leNome.clear()

