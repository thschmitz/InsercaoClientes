# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmbanco.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 551)
        Dialog.setMaximumSize(QtCore.QSize(848, 553))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(570, 510, 171, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 280, 731, 221))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(180)
        self.linePesquisa = QtWidgets.QLineEdit(Dialog)
        self.linePesquisa.setGeometry(QtCore.QRect(110, 244, 191, 31))
        self.linePesquisa.setObjectName("linePesquisa")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 731, 223))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 250, 67, 17))
        self.label.setObjectName("label")
        self.btnProcurar = QtWidgets.QPushButton(Dialog)
        self.btnProcurar.setGeometry(QtCore.QRect(310, 244, 91, 31))
        self.btnProcurar.setObjectName("btnProcurar")
        self.btnEditar = QtWidgets.QPushButton(Dialog)
        self.btnEditar.setGeometry(QtCore.QRect(20, 510, 91, 31))
        self.btnEditar.setObjectName("btnEditar")
        self.btnExcluir = QtWidgets.QPushButton(Dialog)
        self.btnExcluir.setGeometry(QtCore.QRect(120, 510, 91, 31))
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnAtualizar = QtWidgets.QPushButton(Dialog)
        self.btnAtualizar.setGeometry(QtCore.QRect(650, 240, 91, 31))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.btnPlanos = QtWidgets.QPushButton(Dialog)
        self.btnPlanos.setGeometry(QtCore.QRect(340, 510, 91, 31))
        self.btnPlanos.setObjectName("btnPlanos")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nome"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Endereco"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Telefone"))
        self.label.setText(_translate("Dialog", "Pesquisa"))
        self.btnProcurar.setText(_translate("Dialog", "Procurar"))
        self.btnEditar.setText(_translate("Dialog", "Editar"))
        self.btnExcluir.setText(_translate("Dialog", "Excluir"))
        self.btnAtualizar.setText(_translate("Dialog", "Atualizar"))
        self.btnPlanos.setText(_translate("Dialog", "Planos"))
