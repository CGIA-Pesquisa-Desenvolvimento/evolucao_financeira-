# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receita_despesa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReceitaDespesa(object):
    def setupUi(self, ReceitaDespesa):
        ReceitaDespesa.setObjectName("ReceitaDespesa")
        ReceitaDespesa.resize(601, 424)
        self.cbUsuario = QtWidgets.QComboBox(ReceitaDespesa)
        self.cbUsuario.setGeometry(QtCore.QRect(40, 30, 281, 22))
        self.cbUsuario.setObjectName("cbUsuario")
        self.rbReceita = QtWidgets.QRadioButton(ReceitaDespesa)
        self.rbReceita.setGeometry(QtCore.QRect(430, 70, 82, 17))
        self.rbReceita.setObjectName("rbReceita")
        self.rbDespesa = QtWidgets.QRadioButton(ReceitaDespesa)
        self.rbDespesa.setGeometry(QtCore.QRect(430, 30, 82, 17))
        self.rbDespesa.setObjectName("rbDespesa")
        self.leProdutoServico = QtWidgets.QLineEdit(ReceitaDespesa)
        self.leProdutoServico.setGeometry(QtCore.QRect(40, 110, 551, 20))
        self.leProdutoServico.setObjectName("leProdutoServico")
        self.cbCategoria = QtWidgets.QComboBox(ReceitaDespesa)
        self.cbCategoria.setGeometry(QtCore.QRect(40, 160, 281, 22))
        self.cbCategoria.setObjectName("cbCategoria")
        self.cbFornecedor = QtWidgets.QComboBox(ReceitaDespesa)
        self.cbFornecedor.setGeometry(QtCore.QRect(40, 210, 281, 22))
        self.cbFornecedor.setObjectName("cbFornecedor")
        self.leValor = QtWidgets.QLineEdit(ReceitaDespesa)
        self.leValor.setGeometry(QtCore.QRect(40, 270, 181, 20))
        self.leValor.setObjectName("leValor")
        self.leData = QtWidgets.QLineEdit(ReceitaDespesa)
        self.leData.setGeometry(QtCore.QRect(280, 270, 91, 20))
        self.leData.setObjectName("leData")
        self.cbOrcamento = QtWidgets.QCheckBox(ReceitaDespesa)
        self.cbOrcamento.setGeometry(QtCore.QRect(50, 320, 70, 17))
        self.cbOrcamento.setObjectName("cbOrcamento")
        self.leFrequencia = QtWidgets.QLineEdit(ReceitaDespesa)
        self.leFrequencia.setGeometry(QtCore.QRect(160, 350, 91, 20))
        self.leFrequencia.setObjectName("leFrequencia")
        self.cbRecursivo = QtWidgets.QCheckBox(ReceitaDespesa)
        self.cbRecursivo.setGeometry(QtCore.QRect(50, 350, 70, 17))
        self.cbRecursivo.setObjectName("cbRecursivo")
        self.ptObs = QtWidgets.QPlainTextEdit(ReceitaDespesa)
        self.ptObs.setGeometry(QtCore.QRect(390, 270, 201, 151))
        self.ptObs.setObjectName("ptObs")

        self.retranslateUi(ReceitaDespesa)
        QtCore.QMetaObject.connectSlotsByName(ReceitaDespesa)

    def retranslateUi(self, ReceitaDespesa):
        _translate = QtCore.QCoreApplication.translate
        ReceitaDespesa.setWindowTitle(_translate("ReceitaDespesa", "Dialog"))
        self.rbReceita.setText(_translate("ReceitaDespesa", "Receita"))
        self.rbDespesa.setText(_translate("ReceitaDespesa", "Despesa"))
        self.cbOrcamento.setText(_translate("ReceitaDespesa", "Recursivo"))
        self.cbRecursivo.setText(_translate("ReceitaDespesa", "Recursivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReceitaDespesa = QtWidgets.QDialog()
    ui = Ui_ReceitaDespesa()
    ui.setupUi(ReceitaDespesa)
    ReceitaDespesa.show()
    sys.exit(app.exec_())