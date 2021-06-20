import sqlite3

from model.DTO.FornecedorDTO import FornecedorDTO
from model.DAO.FornecedorDAO import FornecedorDAO

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from view.frm_fornecedor import Ui_Fornecedor


class Fornecedor(QDialog):
    def __init__(self, *args, **kwargs):
        super(Fornecedor, self).__init__(*args, **kwargs)
        self.ui = Ui_Fornecedor()
        self.ui.setupUi(self)
        self.ui.pbSalvarEditar.clicked.connect(self.salvar)
        self.ui.pbApagar.clicked.connect(self.apagar)
        self.ui.tbwFornecedor.cellClicked.connect(self.linha_selecionada)
        self.salvar_atualizar = 1 #Flag em 0 = Atualizar, flag em 1 Gravar
        self.id = ''
        self.instituicao_bancaria = 0 #Referente a bancos, corretoras e afins. Flag em 0 = não, flag em 1 = sim
        self.fornecedor = ''
        self.descricao = ''
        self.carrega_tabela()

    """
    Recupera os ados referente a linha selecionada
    """
    def linha_selecionada(self, selected_row):
        id_fornecedor = self.ui.tbwFornecedor.item(selected_row, 0) #Recupara coluna 0 da linha selecionada
        fornecedor = self.ui.tbwFornecedor.item(selected_row, 1) #Recupara coluna 1 da linha selecionada
        inst_bancaria = self.ui.tbwFornecedor.item(selected_row, 2) #Recupara coluna 2 da linha selecionada
        descricao_fornecedor = self.ui.tbwFornecedor.item(selected_row, 3) #Recupara coluna 3 da linha selecionada

        self.id  = id_fornecedor.text()
        self.fornecedor = fornecedor.text()
        self.instituicao_bancaria = inst_bancaria.text()
        self.descricao = descricao_fornecedor.text()

        self.ui.leFornecedor.setText(self.fornecedor)
        if self.instituicao_bancaria == 'SIM':
            self.ui.cbinstituicaoBancaria.setChecked(True)
        else:
            self.ui.cbinstituicaoBancaria.setChecked(False)
        self.ui.pteDescricao.setPlainText(self.descricao)
        self.salvar_atualizar = 0
        self.ui.pbSalvarEditar.setText('Atualizar')

    def gravar(self, fornecedor: str, inst_bancaria: str, descricao: str) -> None:
        fornecedorDAO = FornecedorDAO
        fornecedorDAO.gravar(fornecedor, inst_bancaria, descricao)
        self.limpar_campos()

    def atualizar(self):
        fornecedorDAO = FornecedorDAO
        id = self.id
        fornecedor = self.ui.leFornecedor.text()
        if self.ui.cbinstituicaoBancaria.isChecked():
            ibancaria = 'SIM'
        else:
            ibancaria = 'NÂO'
        obs = self.ui.pteDescricao.toPlainText()
        fornecedorDAO.atualizar(id, fornecedor, ibancaria, obs) #TODO Implementar limpar campos
        self.limpar_campos()
        self.carrega_tabela()

    def salvar(self) -> None:
        fornecedor = self.ui.leFornecedor.text()
        if self.ui.cbinstituicaoBancaria.isChecked():
            ibancaria = 'SIM'
        else:
            ibancaria = 'NÂO'
        obs = self.ui.pteDescricao.toPlainText()
        self.gravar(fornecedor, ibancaria, obs)
        self.carrega_tabela()

    def apagar(self) -> None:
        fornecedorDAO = FornecedorDAO
        id = self.id
        fornecedorDAO.apagar(id)
        self.ui.leFornecedor.clear()
        self.ui.cbinstituicaoBancaria.setChecked(False)
        self.ui.pteDescricao.clear()
        self.carrega_tabela()
        self.ui.pbSalvarEditar.setText('Salvar')

    def carrega_tabela(self) -> None:

        nRow: int = 0
        nCol: int = 0

        cabecalho = ['ID', 'Fornecedor', ' Inst. Bancária', 'Descrição']
        self.ui.tbwFornecedor.setColumnCount(len(cabecalho))
        self.ui.tbwFornecedor.setHorizontalHeaderLabels(cabecalho)

        try:
            conn = sqlite3.connect(
                '/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')

            cur = conn.cursor()
            cur.execute("SELECT * FROM fornecedor") #TODO remover sql p/ model
            rows = cur.fetchall()

            self.ui.tbwFornecedor.setRowCount(len(rows))
            self.ui.tbwFornecedor.setAlternatingRowColors(True)
            self.ui.tbwFornecedor.hideColumn(0)
            self.ui.tbwFornecedor.setColumnWidth(1, 200)
            self.ui.tbwFornecedor.setColumnWidth(2, 100)
            self.ui.tbwFornecedor.setColumnWidth(3, 200)

            for record in rows:
                for column in record:
                    sk = QTableWidgetItem(str(column))
                    self.ui.tbwFornecedor.setItem(nRow, nCol, sk)
                    nCol += 1
                nRow += 1
                nCol = 0

        except sqlite3.Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)

        conn.close()

    def limpar_campos(self):
        self.ui.leFornecedor.clear()
        self.ui.cbinstituicaoBancaria.setChecked(False)
        self.ui.pteDescricao.clear()
        self.salvar_atualizar = 1
        self.id = ''

