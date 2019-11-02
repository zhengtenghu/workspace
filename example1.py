# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.example1 = QtWidgets.QDialogButtonBox(Dialog)
        self.example1.setGeometry(QtCore.QRect(-30, 240, 341, 32))
        self.example1.setOrientation(QtCore.Qt.Horizontal)
        self.example1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.example1.setObjectName("example1")

        self.retranslateUi(Dialog)
        self.example1.accepted.connect(Dialog.accept)
        self.example1.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
