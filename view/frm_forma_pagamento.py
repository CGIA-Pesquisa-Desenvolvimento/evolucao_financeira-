# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forma_pagamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormaPagamento(object):
    def setupUi(self, FormaPagamento):
        FormaPagamento.setObjectName("FormaPagamento")
        FormaPagamento.resize(569, 597)
        self.label_2 = QtWidgets.QLabel(FormaPagamento)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.cbFornecedor = QtWidgets.QComboBox(FormaPagamento)
        self.cbFornecedor.setGeometry(QtCore.QRect(30, 60, 161, 22))
        self.cbFornecedor.setObjectName("cbFornecedor")
        self.label_6 = QtWidgets.QLabel(FormaPagamento)
        self.label_6.setGeometry(QtCore.QRect(30, 210, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(FormaPagamento)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pteObs = QtWidgets.QPlainTextEdit(FormaPagamento)
        self.pteObs.setGeometry(QtCore.QRect(30, 230, 511, 71))
        self.pteObs.setObjectName("pteObs")
        self.leFormaPagamento = QtWidgets.QLineEdit(FormaPagamento)
        self.leFormaPagamento.setGeometry(QtCore.QRect(30, 160, 241, 20))
        self.leFormaPagamento.setObjectName("leFormaPagamento")
        self.rbDebita = QtWidgets.QRadioButton(FormaPagamento)
        self.rbDebita.setGeometry(QtCore.QRect(330, 50, 82, 17))
        self.rbDebita.setObjectName("rbDebita")
        self.rbCredito = QtWidgets.QRadioButton(FormaPagamento)
        self.rbCredito.setGeometry(QtCore.QRect(330, 80, 101, 17))
        self.rbCredito.setObjectName("rbCredito")
        self.tbwFormaPagamento = QtWidgets.QTableWidget(FormaPagamento)
        self.tbwFormaPagamento.setGeometry(QtCore.QRect(30, 350, 511, 121))
        self.tbwFormaPagamento.setObjectName("tbwFormaPagamento")
        self.tbwFormaPagamento.setColumnCount(0)
        self.tbwFormaPagamento.setRowCount(0)
        self.pbSalvarEditar = QtWidgets.QPushButton(FormaPagamento)
        self.pbSalvarEditar.setGeometry(QtCore.QRect(40, 530, 88, 34))
        self.pbSalvarEditar.setObjectName("pbSalvarEditar")
        self.pbApagar = QtWidgets.QPushButton(FormaPagamento)
        self.pbApagar.setGeometry(QtCore.QRect(410, 530, 88, 34))
        self.pbApagar.setObjectName("pbApagar")

        self.retranslateUi(FormaPagamento)
        QtCore.QMetaObject.connectSlotsByName(FormaPagamento)

    def retranslateUi(self, FormaPagamento):
        _translate = QtCore.QCoreApplication.translate
        FormaPagamento.setWindowTitle(_translate("FormaPagamento", "Dialog"))
        self.label_2.setText(_translate("FormaPagamento", "Fornecedor"))
        self.label_6.setText(_translate("FormaPagamento", "Observa????o"))
        self.label_3.setText(_translate("FormaPagamento", "Forma de pagamento"))
        self.rbDebita.setText(_translate("FormaPagamento", "D??bito"))
        self.rbCredito.setText(_translate("FormaPagamento", "Cr??dito"))
        self.pbSalvarEditar.setText(_translate("FormaPagamento", "Salvar"))
        self.pbApagar.setText(_translate("FormaPagamento", "Apagar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormaPagamento = QtWidgets.QDialog()
    ui = Ui_FormaPagamento()
    ui.setupUi(FormaPagamento)
    FormaPagamento.show()
    sys.exit(app.exec_())
