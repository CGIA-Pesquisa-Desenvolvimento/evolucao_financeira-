# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.pbCancelar = QtWidgets.QPushButton(Login)
        self.pbCancelar.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbOk = QtWidgets.QPushButton(Login)
        self.pbOk.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.pbOk.setObjectName("pbOk")
        self.leLogin = QtWidgets.QLineEdit(Login)
        self.leLogin.setGeometry(QtCore.QRect(132, 50, 221, 20))
        self.leLogin.setObjectName("leLogin")
        self.leSenha = QtWidgets.QLineEdit(Login)
        self.leSenha.setGeometry(QtCore.QRect(130, 120, 221, 20))
        self.leSenha.setObjectName("leSenha")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.pbCancelar.setText(_translate("Login", "Cancelar"))
        self.pbOk.setText(_translate("Login", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())