import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_forma_pagamento import Ui_FormaPagamento


class FormaPagamento(QDialog):
    def __init__(self, *args, **kwargs):
        super(FormaPagamento, self).__init__(*args, **kwargs)
        self.ui = Ui_FormaPagamento()
        self.ui.setupUi(self)
        self.setWindowTitle('Cadastro: Formas de Pagamento')
        self.ui.cbFornecedor.currentIndexChanged.connect(self.texto_corrente)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)
        self.ui.tbwFormaPagamento.cellClicked.connect(self.linha_selecionada)
        self.salvar_atualizar = 1  # Flag em 0 = Atualizar, flag em 1 Gravar
        self.id = ''
        self.fornecedor_selecionado = ''
        self.categoria = ''
        self.obs = ''
        self.carrega_tabela()
        self.popula_fornecedor()

    """
        Recupera os dados referente a linha selecionada
        """

    def linha_selecionada(self, selected_row):
        id_categoria = self.ui.tbwFormaPagamento.item(selected_row, 0)  # Recupara coluna 0 da linha selecionada
        fornecedor = self.ui.tbwFormaPagamento.item(selected_row, 1)  # Recupara coluna 1 da linha selecionada

        obs_categoria = self.ui.tbwFormaPagamento.item(selected_row, 2)  # Recupara coluna 2 da linha selecionada

        self.id = id_categoria.text()
        self.categoria = categoria.text()
        self.obs = obs_categoria.text()

        self.ui.leCategoria.setText(self.categoria)
        self.ui.pteObs.setPlainText(self.obs)
        self.salvar_atualizar = 0
        self.ui.pbSalvarEditar.setText('Atualizar')

    def carrega_tabela(self) -> None:

        nRow: int = 0
        nCol: int = 0

        cabecalho = ['ID', 'Categoria', 'Observação']
        self.ui.tbwFormaPagamento.setColumnCount(len(cabecalho))
        self.ui.tbwFormaPagamento.setHorizontalHeaderLabels(cabecalho)

        try:
            conn = sqlite3.connect(
                '/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')

            cur = conn.cursor()
            cur.execute("SELECT * FROM categoria")  # TODO remover sql p/ model
            rows = cur.fetchall()

            self.ui.tbwFormaPagamento.setRowCount(len(rows))
            self.ui.tbwFormaPagamento.setAlternatingRowColors(True)
            self.ui.tbwFormaPagamento.hideColumn(0)
            self.ui.tbwFormaPagamento.setColumnWidth(1, 200)
            self.ui.tbwFormaPagamento.setColumnWidth(2, 275)

            for record in rows:
                for column in record:
                    sk = QTableWidgetItem(str(column))
                    self.ui.tbwFormaPagamento.setItem(nRow, nCol, sk)
                    nCol += 1
                nRow += 1
                nCol = 0

        except sqlite3.Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)

        conn.close()

    def limpar_campos(self):
        self.ui.leCategoria.clear()
        self.ui.pteObs.clear()
        self.salvar_atualizar = 1
        self.id = ''

    def popula_fornecedor(self) -> None:

        try:
            conn = sqlite3.connect(
                '/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')

            cur = conn.cursor()
            cur.execute("SELECT nome_fornecedor FROM fornecedor")  # TODO remover sql p/ model
            result = cur.fetchall()

            for record in result:
                self.ui.cbFornecedor.addItems(record)

        except sqlite3.Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)

        self.texto_corrente()

        conn.close()

    def texto_corrente(self):
        self.fornecedor_selecionado = self.ui.cbFornecedor.currentText()


