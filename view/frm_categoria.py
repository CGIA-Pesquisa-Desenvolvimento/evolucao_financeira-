# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoria.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Categoria(object):
    def setupUi(self, Categoria):
        Categoria.setObjectName("Categoria")
        Categoria.resize(587, 370)
        self.label_2 = QtWidgets.QLabel(Categoria)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.leCategoria = QtWidgets.QLineEdit(Categoria)
        self.leCategoria.setGeometry(QtCore.QRect(30, 30, 500, 20))
        self.leCategoria.setObjectName("leCategoria")
        self.pbSalvarEditar = QtWidgets.QPushButton(Categoria)
        self.pbSalvarEditar.setGeometry(QtCore.QRect(80, 260, 81, 31))
        self.pbSalvarEditar.setObjectName("pbSalvarEditar")
        self.pbApagar = QtWidgets.QPushButton(Categoria)
        self.pbApagar.setGeometry(QtCore.QRect(370, 260, 81, 31))
        self.pbApagar.setObjectName("pbApagar")
        self.label = QtWidgets.QLabel(Categoria)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.label.setObjectName("label")
        self.pteObs = QtWidgets.QPlainTextEdit(Categoria)
        self.pteObs.setGeometry(QtCore.QRect(30, 130, 511, 87))
        self.pteObs.setObjectName("pteObs")

        self.retranslateUi(Categoria)
        QtCore.QMetaObject.connectSlotsByName(Categoria)

    def retranslateUi(self, Categoria):
        _translate = QtCore.QCoreApplication.translate
        Categoria.setWindowTitle(_translate("Categoria", "Dialog"))
        self.label_2.setText(_translate("Categoria", "Observação"))
        self.pbSalvarEditar.setText(_translate("Categoria", "Salvar"))
        self.pbApagar.setText(_translate("Categoria", "Apagar"))
        self.label.setText(_translate("Categoria", "Categoria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Categoria = QtWidgets.QDialog()
    ui = Ui_Categoria()
    ui.setupUi(Categoria)
    Categoria.show()
    sys.exit(app.exec_())
