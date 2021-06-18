from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from model.DAO.TipoInvestimentoDAO import TipoInvestimentoDAO
from view.frm_tipo_investimento import Ui_TipoInvestimento


class TipoInvestimento(QDialog):
    def __init__(self, *args, **kwargs):
        super(TipoInvestimento, self).__init__(*args, **kwargs)
        self.ui = Ui_TipoInvestimento()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)

    def gravar(self, tipo: str, descricao: str) -> None:
          tipo_investimentoDAO = TipoInvestimentoDAO
          tipo_investimentoDAO.gravar(tipo, descricao)
          self.apagar()

    def salvar(self) -> None:
          t = self.ui.leTipoInvestimento.text()
          d = self.ui.pteDescricao.toPlainText()
          self.gravar(t, d)


    def apagar(self) -> None:
          self.ui.leTipoInvestimento.clear()
          self.ui.pteDescricao.clear()
