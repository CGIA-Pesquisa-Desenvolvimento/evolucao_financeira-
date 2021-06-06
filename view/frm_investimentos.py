# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'investimentos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Investimentos(object):
    def setupUi(self, Investimentos):
        Investimentos.setObjectName("Investimentos")
        Investimentos.resize(544, 584)
        self.label_2 = QtWidgets.QLabel(Investimentos)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.label_2.setObjectName("label_2")
        self.cbAporteInicial = QtWidgets.QCheckBox(Investimentos)
        self.cbAporteInicial.setGeometry(QtCore.QRect(270, 300, 91, 17))
        self.cbAporteInicial.setObjectName("cbAporteInicial")
        self.pteObs = QtWidgets.QPlainTextEdit(Investimentos)
        self.pteObs.setGeometry(QtCore.QRect(30, 450, 481, 71))
        self.pteObs.setObjectName("pteObs")
        self.rbRendaVariavel = QtWidgets.QRadioButton(Investimentos)
        self.rbRendaVariavel.setGeometry(QtCore.QRect(270, 150, 101, 17))
        self.rbRendaVariavel.setObjectName("rbRendaVariavel")
        self.leValorCotas = QtWidgets.QLineEdit(Investimentos)
        self.leValorCotas.setGeometry(QtCore.QRect(30, 300, 113, 20))
        self.leValorCotas.setObjectName("leValorCotas")
        self.cbFornecedor = QtWidgets.QComboBox(Investimentos)
        self.cbFornecedor.setGeometry(QtCore.QRect(30, 30, 161, 22))
        self.cbFornecedor.setObjectName("cbFornecedor")
        self.rbRendaFixa = QtWidgets.QRadioButton(Investimentos)
        self.rbRendaFixa.setGeometry(QtCore.QRect(270, 120, 82, 17))
        self.rbRendaFixa.setObjectName("rbRendaFixa")
        self.label = QtWidgets.QLabel(Investimentos)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Investimentos)
        self.label_6.setGeometry(QtCore.QRect(30, 430, 101, 16))
        self.label_6.setObjectName("label_6")
        self.leNumeroCotas = QtWidgets.QLineEdit(Investimentos)
        self.leNumeroCotas.setGeometry(QtCore.QRect(30, 230, 113, 20))
        self.leNumeroCotas.setObjectName("leNumeroCotas")
        self.label_5 = QtWidgets.QLabel(Investimentos)
        self.label_5.setGeometry(QtCore.QRect(30, 350, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Investimentos)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Investimentos)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 101, 16))
        self.label_4.setObjectName("label_4")
        self.cbTipoInvestimento = QtWidgets.QComboBox(Investimentos)
        self.cbTipoInvestimento.setGeometry(QtCore.QRect(30, 130, 161, 22))
        self.cbTipoInvestimento.setObjectName("cbTipoInvestimento")
        self.dteDataAporte = QtWidgets.QDateEdit(Investimentos)
        self.dteDataAporte.setGeometry(QtCore.QRect(30, 370, 110, 22))
        self.dteDataAporte.setObjectName("dteDataAporte")

        self.retranslateUi(Investimentos)
        QtCore.QMetaObject.connectSlotsByName(Investimentos)

    def retranslateUi(self, Investimentos):
        _translate = QtCore.QCoreApplication.translate
        Investimentos.setWindowTitle(_translate("Investimentos", "Dialog"))
        self.label_2.setText(_translate("Investimentos", "Produto Financeiro"))
        self.cbAporteInicial.setText(_translate("Investimentos", "Aporte Inicial"))
        self.rbRendaVariavel.setText(_translate("Investimentos", "Renda variável"))
        self.rbRendaFixa.setText(_translate("Investimentos", "Renda Fixa"))
        self.label.setText(_translate("Investimentos", "Fornecedor"))
        self.label_6.setText(_translate("Investimentos", "Observação"))
        self.label_5.setText(_translate("Investimentos", "Data"))
        self.label_3.setText(_translate("Investimentos", "Número de cotas"))
        self.label_4.setText(_translate("Investimentos", "Valor Cota"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Investimentos = QtWidgets.QDialog()
    ui = Ui_Investimentos()
    ui.setupUi(Investimentos)
    Investimentos.show()
    sys.exit(app.exec_())
