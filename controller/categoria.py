import sqlite3

from model.DTO.CategoriaDTO import CategoriaDTO
from model.DAO.CategoriaDAO import CategoriaDAO

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTreeWidgetItem
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
        self.ui.tbwCategoria.cellClicked.connect(self.linha_selecionada)
        self.salvar_atualizar = 1
        self.id = ''
        self.categoria = ''
        self.obs = ''
        self.carrega_tabela()

    def linha_selecionada(self, row1):
        v0 = self.ui.tbwCategoria.item(row1, 0)
        v1 = self.ui.tbwCategoria.item(row1, 1)
        v2 = self.ui.tbwCategoria.item(row1, 2)

        self.id  = v0.text()
        self.categoria = v1.text()
        self.obs = v2.text()
        print(self.ui)
        print(self.categoria)
        print(self.obs)

        self.ui.leCategoria.setText(self.categoria)
        self.ui.pteObs.setPlainText(self.obs)
        self.salvar_atualizar = 0
        self.ui.pbSalvarEditar.setText('Atualizar')

    def gravar(self, cat: str, obs: str) -> None:
        categoriaDAO = CategoriaDAO
        categoriaDAO.Gravar(cat, obs)
        self.limpar_campos()

    def atualizar(self):
        categoriaDAO = CategoriaDAO
        id = self.id
        cat = self.ui.leCategoria.text()
        obs = self.ui.pteObs.toPlainText()
        categoriaDAO.Atualizar(id, cat, obs) #TODO Implementar limpar campos
        self.limpar_campos()

    def salvar(self) -> None:
        c = self.ui.leCategoria.text()
        o = self.ui.pteObs.toPlainText()
        if self.salvar_atualizar:
            self.gravar(c, o)
            self.carrega_tabela()
        else:
            self.atualizar()
            self.carrega_tabela()

    def apagar(self) -> None:
        categoriaDAO = CategoriaDAO
        id = self.id
        categoriaDAO.Apagar(id)
        self.ui.leCategoria.clear()
        self.ui.pteObs.clear()
        self.carrega_tabela()
        self.ui.pbSalvarEditar.setText('Salvar')

    def carrega_tabela(self) -> None:

        nRow: int = 0
        nCol: int = 0

        cabecalho = ['ID', 'Categoria', 'Observação']
        self.ui.tbwCategoria.setColumnCount(len(cabecalho))
        self.ui.tbwCategoria.setHorizontalHeaderLabels(cabecalho)

        try:
            conn = sqlite3.connect(
                '/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')

            cur = conn.cursor()
            cur.execute("SELECT * FROM categoria")
            rows = cur.fetchall()

            self.ui.tbwCategoria.setRowCount(len(rows))
            self.ui.tbwCategoria.setAlternatingRowColors(True)
            self.ui.tbwCategoria.hideColumn(0)
            self.ui.tbwCategoria.setColumnWidth(1, 200)
            self.ui.tbwCategoria.setColumnWidth(2, 275)
           # self.ui.tbwCategoria.setSizePolicy(1)

            for record in rows:
                for column in record:
                    sk = QTableWidgetItem(str(column))
                    self.ui.tbwCategoria.setItem(nRow, nCol, sk)
                    nCol += 1
                nRow += 1
                nCol = 0
            # v0 = self.ui.tbwCategoria.item(0, 0)
            # v1 = self.ui.tbwCategoria.item(0, 1)
            # v2 = self.ui.tbwCategoria.item(0, 2)
            # s = self.ui.tbwCategoria.selectedItems()
            #
            # v00 = v0.text()
            # v11 = v1.text()
            # v22 = v2.text()
            # self.ui.leCategoria.setText(v11)
            # self.ui.pteObs.setPlainText(v22)
        except sqlite3.Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)

        conn.close()

    def limpar_campos(self):
        self.ui.leCategoria.clear()
        self.ui.pteObs.clear()
        self.salvar_atualizar = 1
        self.id = ''






