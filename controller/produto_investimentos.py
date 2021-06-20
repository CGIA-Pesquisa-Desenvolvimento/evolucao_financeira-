import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from model.DAO.ProdutoInvestimentoDAO import ProdutoInvestimentoDAO
from view.frm_produto_investimento import Ui_ProdutoInvestimento


class ProdutoInvestimento(QDialog):
    def __init__(self, *args, **kwargs):
        super(ProdutoInvestimento, self).__init__(*args, **kwargs)
        self.ui = Ui_ProdutoInvestimento()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)
        self.ui.tbwProdutoInvestimento.cellClicked.connect(self.linha_selecionada)
        self.salvar_atualizar = 1  # Flag em 0 = Atualizar, flag em 1 Gravar
        self.id = ''
        self.produto = ''
        self.descricao = ''
        self.carrega_tabela()

    """
        Recupera os dados referente a linha selecionada
        """

    def linha_selecionada(self, selected_row):
        id_produto = self.ui.tbwProdutoInvestimento.item(selected_row, 0)  # Recupara coluna 0 da linha selecionada
        produto = self.ui.tbwProdutoInvestimento.item(selected_row, 1)  # Recupara coluna 1 da linha selecionada
        obs_categoria = self.ui.tbwProdutoInvestimento.item(selected_row, 2)  # Recupara coluna 2 da linha selecionada

        self.id = id_produto.text()
        self.produto = produto.text()
        self.descricao = obs_categoria.text()

        self.ui.leTipoInvestimento.setText(self.produto)
        self.ui.pteDescricao.setPlainText(self.descricao)
        self.salvar_atualizar = 0
        self.ui.pbSalvarEditar.setText('Atualizar')

    def gravar(self, produto: str, descricao: str) -> None:
          produto_investimentoDAO = ProdutoInvestimentoDAO
          produto_investimentoDAO.gravar(produto, descricao)
          self.limpar_campos()
          self.carrega_tabela()

    def salvar(self) -> None:
        produto = self.ui.leTipoInvestimento.text()
        descricao = self.ui.pteDescricao.toPlainText()
        if self.salvar_atualizar:
            self.gravar(produto, descricao)
            self.carrega_tabela()
        else:
            self.atualizar()
            self.carrega_tabela()

    def atualizar(self):
        produto_investimentoDAO = ProdutoInvestimentoDAO
        id = self.id
        produto = self.ui.leTipoInvestimento.text()
        descricao = self.ui.pteDescricao.toPlainText()
        produto_investimentoDAO.atualizar(produto, descricao, id) #TODO Implementar limpar campos
        self.carrega_tabela()
        self.limpar_campos()

    def apagar(self) -> None:
        produto_investimentoDAO = ProdutoInvestimentoDAO
        id = self.id
        produto_investimentoDAO.apagar(id)
        self.ui.leTipoInvestimento.clear()
        self.ui.pteDescricao.clear()
        self.carrega_tabela()
        self.ui.pbSalvarEditar.setText('Salvar')

    def carrega_tabela(self) -> None:

        nRow: int = 0
        nCol: int = 0

        cabecalho = ['ID', 'Categoria', 'Observação']
        self.ui.tbwProdutoInvestimento.setColumnCount(len(cabecalho))
        self.ui.tbwProdutoInvestimento.setHorizontalHeaderLabels(cabecalho)

        try:
            conn = sqlite3.connect(
                '/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')

            cur = conn.cursor()
            cur.execute("SELECT * FROM produto_investimento")  # TODO remover sql p/ model
            rows = cur.fetchall()

            self.ui.tbwProdutoInvestimento.setRowCount(len(rows))
            self.ui.tbwProdutoInvestimento.setAlternatingRowColors(True)
            self.ui.tbwProdutoInvestimento.hideColumn(0)
            self.ui.tbwProdutoInvestimento.setColumnWidth(1, 200)
            self.ui.tbwProdutoInvestimento.setColumnWidth(2, 275)

            for record in rows:
                for column in record:
                    sk = QTableWidgetItem(str(column))
                    self.ui.tbwProdutoInvestimento.setItem(nRow, nCol, sk)
                    nCol += 1
                nRow += 1
                nCol = 0

        except sqlite3.Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)

        conn.close()

    def limpar_campos(self):
        self.ui.leTipoInvestimento.clear()
        self.ui.pteDescricao.clear()
        self.salvar_atualizar = 1
        self.id = ''
