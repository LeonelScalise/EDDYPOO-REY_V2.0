# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 462)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_alu = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_alu.sizePolicy().hasHeightForWidth())
        self.btn_alu.setSizePolicy(sizePolicy)
        self.btn_alu.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_alu.setFont(font)
        self.btn_alu.setObjectName("btn_alu")
        self.gridLayout.addWidget(self.btn_alu, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_admin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_admin.sizePolicy().hasHeightForWidth())
        self.btn_admin.setSizePolicy(sizePolicy)
        self.btn_admin.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_admin.setFont(font)
        self.btn_admin.setObjectName("btn_admin")
        self.gridLayout.addWidget(self.btn_admin, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_salir.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_salir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_salir.setDefault(False)
        self.btn_salir.setFlat(False)
        self.btn_salir.setObjectName("btn_salir")
        self.gridLayout.addWidget(self.btn_salir, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_profe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profe.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_profe.setFont(font)
        self.btn_profe.setObjectName("btn_profe")
        self.gridLayout.addWidget(self.btn_profe, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_2.setObjectName("actionLoad_2")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSet_size = QtWidgets.QAction(MainWindow)
        self.actionSet_size.setObjectName("actionSet_size")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eddypoo-rey"))
        self.btn_alu.setText(_translate("MainWindow", "Alumno"))
        self.btn_admin.setText(_translate("MainWindow", "Administrativo"))
        self.btn_salir.setText(_translate("MainWindow", "Salir"))
        self.btn_profe.setText(_translate("MainWindow", "Profesor"))
        self.label.setText(_translate("MainWindow", "MENU PRINCIPAL"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad_2.setText(_translate("MainWindow", "Load..."))
        self.actionSave_2.setText(_translate("MainWindow", "Save..."))
        self.actionSet_size.setText(_translate("MainWindow", "Set size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())