from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_principal import Ui_Principal
from controller.fornecedores import Fornecedor
from controller.categoria import Categoria
from controller.cadastro_usuario import CadastroUsuario
from controller.tipo_investimentos import TipoInvestimento
from controller.investimentos import Investimentos
from controller.forma_pagamento import FormaPagamento
from controller.receitas_despesas import ReceitasDespesas
from controller.valor_desvalorizacao import ValorDesvalorizacao


class Principal(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Principal, self).__init__(*args, **kwargs)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.ui.actionFornecedor.triggered.connect(self.add)
        self.ui.actionCategoria.triggered.connect(self.add_categoria)
        self.ui.actionUsuario.triggered.connect(self.add_cadastro_usuario)
        self.ui.actionTipo_de_Investimento.triggered.connect(self.add_tipo_investimento)
        self.ui.actionInvestimentos.triggered.connect(self.add_investimento)
        self.ui.actionForma_de_Pagamento.triggered.connect(self.add_forma_pagamento)
        self.ui.actionReceitas_Despesas.triggered.connect(self.add_receita_despesa)
        self.ui.actionDevalorizacaoMonetaria.triggered.connect(self.add_valor_desvalorizacao)

    def add(self) -> None:
        add = Fornecedor()
        add.exec_()

    def add_categoria(self):
        add_categoria = Categoria()
        add_categoria.exec_()

    def add_cadastro_usuario(self):
        add_cadastro_usuario = CadastroUsuario()
        add_cadastro_usuario.exec_()

    def add_tipo_investimento(self):
        add_tipo_investimento = TipoInvestimento()
        add_tipo_investimento.exec_()

    def add_investimento(self):
        add_investimento = Investimentos()
        add_investimento.exec_()

    def add_forma_pagamento(self):
        add_forma_pagamento = FormaPagamento()
        add_forma_pagamento.exec_()

    def add_receita_despesa(self):
        add_receita_despesa = ReceitasDespesas()
        add_receita_despesa.exec_()

    def add_valor_desvalorizacao(self):
        add_valor_desvalorizacao = ValorDesvalorizacao()
        add_valor_desvalorizacao.exec_()


# from PyQt5 import uic, QtWidgets
# #from view import fornecedor
# import view
#
#
# def abre_fornecedor():
#     view.fornecedor()
#
#
#
#
# app = QtWidgets.QApplication([])
# tela_principal = uic.loadUi('frm_principal.ui')
# #tela_fornecedores = uic.loadUi('frm_fornecedores.ui')
# #tela.actionFornecedor.clicked.connect(abre_fornecedor)
# tela_principal.btnTeste.clicked.connect(abre_fornecedor)
#
# tela_principal.show()
# app.exec()
