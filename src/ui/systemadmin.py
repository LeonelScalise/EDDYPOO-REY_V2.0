# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/systemadmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Systemadmin(object):
    def setupUi(self, Systemadmin):
        Systemadmin.setObjectName("Systemadmin")
        Systemadmin.resize(920, 604)
        self.centralwidget = QtWidgets.QWidget(Systemadmin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.gridLayout_2.addWidget(self.label_info, 2, 0, 1, 1)
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.gridLayout_2.addWidget(self.btn_logout, 4, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        Systemadmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Systemadmin)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Systemadmin)

    def retranslateUi(self, Systemadmin):
        _translate = QtCore.QCoreApplication.translate
        Systemadmin.setWindowTitle(_translate("Systemadmin", "MainWindow"))
        self.label_info.setText(_translate("Systemadmin", "Logeado como ..."))
        self.btn_logout.setText(_translate("Systemadmin", "Cerrar Sesión"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Systemadmin", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Systemadmin", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Systemadmin = QtWidgets.QMainWindow()
    ui = Ui_Systemadmin()
    ui.setupUi(Systemadmin)
    Systemadmin.show()
    sys.exit(app.exec_())
