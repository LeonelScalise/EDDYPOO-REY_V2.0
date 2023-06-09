# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/systemalu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Systemalu(object):
    def setupUi(self, Systemalu):
        Systemalu.setObjectName("Systemalu")
        Systemalu.resize(1090, 600)
        self.centralwidget = QtWidgets.QWidget(Systemalu)
        self.centralwidget.setMinimumSize(QtCore.QSize(1090, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_logout_alu = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_logout_alu.setFont(font)
        self.btn_logout_alu.setObjectName("btn_logout_alu")
        self.gridLayout.addWidget(self.btn_logout_alu, 2, 0, 1, 1)
        self.label_info_usuario_log = QtWidgets.QLabel(self.centralwidget)
        self.label_info_usuario_log.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_info_usuario_log.setFont(font)
        self.label_info_usuario_log.setText("")
        self.label_info_usuario_log.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_info_usuario_log.setObjectName("label_info_usuario_log")
        self.gridLayout.addWidget(self.label_info_usuario_log, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_menu_modif = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu_modif.sizePolicy().hasHeightForWidth())
        self.frame_menu_modif.setSizePolicy(sizePolicy)
        self.frame_menu_modif.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_menu_modif.setMaximumSize(QtCore.QSize(190, 16777215))
        self.frame_menu_modif.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu_modif.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu_modif.setObjectName("frame_menu_modif")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_menu_modif)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_inscr_mat_alu = QtWidgets.QPushButton(self.frame_menu_modif)
        self.btn_inscr_mat_alu.setObjectName("btn_inscr_mat_alu")
        self.verticalLayout_5.addWidget(self.btn_inscr_mat_alu)
        self.btn_desinscr_mat_alu = QtWidgets.QPushButton(self.frame_menu_modif)
        self.btn_desinscr_mat_alu.setObjectName("btn_desinscr_mat_alu")
        self.verticalLayout_5.addWidget(self.btn_desinscr_mat_alu)
        self.btn_iniciar_tramite_alu = QtWidgets.QPushButton(self.frame_menu_modif)
        self.btn_iniciar_tramite_alu.setObjectName("btn_iniciar_tramite_alu")
        self.verticalLayout_5.addWidget(self.btn_iniciar_tramite_alu)
        self.btn_modif_pass_alu = QtWidgets.QPushButton(self.frame_menu_modif)
        self.btn_modif_pass_alu.setObjectName("btn_modif_pass_alu")
        self.verticalLayout_5.addWidget(self.btn_modif_pass_alu)
        self.btn_stats_academicas = QtWidgets.QPushButton(self.frame_menu_modif)
        self.btn_stats_academicas.setObjectName("btn_stats_academicas")
        self.verticalLayout_5.addWidget(self.btn_stats_academicas)
        self.gridLayout_2.addWidget(self.frame_menu_modif, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_inscr_mat = QtWidgets.QWidget()
        self.page_inscr_mat.setObjectName("page_inscr_mat")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_inscr_mat)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_inscr_mat = QtWidgets.QPushButton(self.page_inscr_mat)
        self.btn_inscr_mat.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.btn_inscr_mat.setFont(font)
        self.btn_inscr_mat.setObjectName("btn_inscr_mat")
        self.gridLayout_4.addWidget(self.btn_inscr_mat, 2, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.page_inscr_mat)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.gridLayout_4.addWidget(self.label_51, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.page_inscr_mat)
        self.frame_5.setMinimumSize(QtCore.QSize(330, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.tW_inscr_mat = QtWidgets.QTableWidget(self.frame_5)
        self.tW_inscr_mat.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tW_inscr_mat.setObjectName("tW_inscr_mat")
        self.tW_inscr_mat.setColumnCount(3)
        self.tW_inscr_mat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tW_inscr_mat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_inscr_mat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_inscr_mat.setHorizontalHeaderItem(2, item)
        self.gridLayout_23.addWidget(self.tW_inscr_mat, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_23.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 1, 2, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.page_inscr_mat)
        self.frame_6.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.cb_inscrip_mat_comi = QtWidgets.QComboBox(self.frame_6)
        self.cb_inscrip_mat_comi.setObjectName("cb_inscrip_mat_comi")
        self.gridLayout_24.addWidget(self.cb_inscrip_mat_comi, 1, 1, 1, 1)
        self.label_info_dni_en_6 = QtWidgets.QLabel(self.frame_6)
        self.label_info_dni_en_6.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_info_dni_en_6.setFont(font)
        self.label_info_dni_en_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_dni_en_6.setObjectName("label_info_dni_en_6")
        self.gridLayout_24.addWidget(self.label_info_dni_en_6, 1, 0, 1, 1)
        self.label_info_nombre_en_6 = QtWidgets.QLabel(self.frame_6)
        self.label_info_nombre_en_6.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_info_nombre_en_6.setFont(font)
        self.label_info_nombre_en_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_nombre_en_6.setObjectName("label_info_nombre_en_6")
        self.gridLayout_24.addWidget(self.label_info_nombre_en_6, 0, 0, 1, 1)
        self.cb_inscrip_mat = QtWidgets.QComboBox(self.frame_6)
        self.cb_inscrip_mat.setObjectName("cb_inscrip_mat")
        self.gridLayout_24.addWidget(self.cb_inscrip_mat, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 2)
        self.label_informe_inscr_mat = QtWidgets.QLabel(self.page_inscr_mat)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_informe_inscr_mat.setFont(font)
        self.label_informe_inscr_mat.setText("")
        self.label_informe_inscr_mat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_informe_inscr_mat.setObjectName("label_informe_inscr_mat")
        self.gridLayout_4.addWidget(self.label_informe_inscr_mat, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_inscr_mat)
        self.page_desinscr_mat = QtWidgets.QWidget()
        self.page_desinscr_mat.setObjectName("page_desinscr_mat")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_desinscr_mat)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_52 = QtWidgets.QLabel(self.page_desinscr_mat)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.gridLayout_5.addWidget(self.label_52, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.page_desinscr_mat)
        self.frame_8.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_info_dni_en_7 = QtWidgets.QLabel(self.frame_8)
        self.label_info_dni_en_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_info_dni_en_7.setFont(font)
        self.label_info_dni_en_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_dni_en_7.setObjectName("label_info_dni_en_7")
        self.gridLayout_26.addWidget(self.label_info_dni_en_7, 1, 0, 1, 1)
        self.label_info_nombre_en_7 = QtWidgets.QLabel(self.frame_8)
        self.label_info_nombre_en_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_info_nombre_en_7.setFont(font)
        self.label_info_nombre_en_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_nombre_en_7.setObjectName("label_info_nombre_en_7")
        self.gridLayout_26.addWidget(self.label_info_nombre_en_7, 0, 0, 1, 1)
        self.lv_desinscr_alu_mat_en_curso = QtWidgets.QListView(self.frame_8)
        self.lv_desinscr_alu_mat_en_curso.setMaximumSize(QtCore.QSize(16777215, 200))
        self.lv_desinscr_alu_mat_en_curso.setObjectName("lv_desinscr_alu_mat_en_curso")
        self.gridLayout_26.addWidget(self.lv_desinscr_alu_mat_en_curso, 0, 1, 1, 1)
        self.label_desinscr_mat_cod_com = QtWidgets.QLabel(self.frame_8)
        self.label_desinscr_mat_cod_com.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_desinscr_mat_cod_com.setText("")
        self.label_desinscr_mat_cod_com.setObjectName("label_desinscr_mat_cod_com")
        self.gridLayout_26.addWidget(self.label_desinscr_mat_cod_com, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_8, 1, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.page_desinscr_mat)
        self.frame_7.setMinimumSize(QtCore.QSize(330, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.tabla_desinscr_mat = QtWidgets.QTableWidget(self.frame_7)
        self.tabla_desinscr_mat.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabla_desinscr_mat.setObjectName("tabla_desinscr_mat")
        self.tabla_desinscr_mat.setColumnCount(3)
        self.tabla_desinscr_mat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabla_desinscr_mat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_desinscr_mat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_desinscr_mat.setHorizontalHeaderItem(2, item)
        self.gridLayout_25.addWidget(self.tabla_desinscr_mat, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_25.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_7, 1, 1, 1, 1)
        self.label_informe_desinscr_mat = QtWidgets.QLabel(self.page_desinscr_mat)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_informe_desinscr_mat.setFont(font)
        self.label_informe_desinscr_mat.setText("")
        self.label_informe_desinscr_mat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_informe_desinscr_mat.setObjectName("label_informe_desinscr_mat")
        self.gridLayout_5.addWidget(self.label_informe_desinscr_mat, 2, 0, 1, 1)
        self.btn_desinscr_mat = QtWidgets.QPushButton(self.page_desinscr_mat)
        self.btn_desinscr_mat.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.btn_desinscr_mat.setFont(font)
        self.btn_desinscr_mat.setObjectName("btn_desinscr_mat")
        self.gridLayout_5.addWidget(self.btn_desinscr_mat, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_desinscr_mat)
        self.page_iniciar_tramite_alu = QtWidgets.QWidget()
        self.page_iniciar_tramite_alu.setObjectName("page_iniciar_tramite_alu")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_iniciar_tramite_alu)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_ini_tram_alu_estado_en = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_estado_en.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_ini_tram_alu_estado_en.setFont(font)
        self.label_ini_tram_alu_estado_en.setText("")
        self.label_ini_tram_alu_estado_en.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ini_tram_alu_estado_en.setObjectName("label_ini_tram_alu_estado_en")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_estado_en, 5, 1, 1, 1)
        self.label_info_ult_tramite_alu = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_info_ult_tramite_alu.setEnabled(True)
        self.label_info_ult_tramite_alu.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        self.label_info_ult_tramite_alu.setFont(font)
        self.label_info_ult_tramite_alu.setText("")
        self.label_info_ult_tramite_alu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_info_ult_tramite_alu.setObjectName("label_info_ult_tramite_alu")
        self.gridLayout_6.addWidget(self.label_info_ult_tramite_alu, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 5, 3, 1, 1)
        self.label_ini_tram_alu_asig = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_asig.setText("")
        self.label_ini_tram_alu_asig.setObjectName("label_ini_tram_alu_asig")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_asig, 4, 2, 1, 1)
        self.label_ini_tram_alu_fini_en = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_fini_en.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_ini_tram_alu_fini_en.setFont(font)
        self.label_ini_tram_alu_fini_en.setText("")
        self.label_ini_tram_alu_fini_en.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ini_tram_alu_fini_en.setObjectName("label_ini_tram_alu_fini_en")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_fini_en, 3, 1, 1, 1)
        self.label_informe_ini_tram_alu = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_informe_ini_tram_alu.setFont(font)
        self.label_informe_ini_tram_alu.setText("")
        self.label_informe_ini_tram_alu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_informe_ini_tram_alu.setObjectName("label_informe_ini_tram_alu")
        self.gridLayout_6.addWidget(self.label_informe_ini_tram_alu, 6, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(273, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 4, 3, 1, 1)
        self.btn_ini_tram_alu = QtWidgets.QPushButton(self.page_iniciar_tramite_alu)
        self.btn_ini_tram_alu.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.btn_ini_tram_alu.setFont(font)
        self.btn_ini_tram_alu.setObjectName("btn_ini_tram_alu")
        self.gridLayout_6.addWidget(self.btn_ini_tram_alu, 6, 3, 1, 1)
        self.label_error_ini_tram_alu = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_error_ini_tram_alu.setStyleSheet("color:red;")
        self.label_error_ini_tram_alu.setText("")
        self.label_error_ini_tram_alu.setObjectName("label_error_ini_tram_alu")
        self.gridLayout_6.addWidget(self.label_error_ini_tram_alu, 1, 3, 1, 1)
        self.label_ini_tram_alu_fini = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_fini.setText("")
        self.label_ini_tram_alu_fini.setObjectName("label_ini_tram_alu_fini")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_fini, 3, 2, 1, 1)
        self.input_motivo_tramite_alu = QtWidgets.QTextEdit(self.page_iniciar_tramite_alu)
        self.input_motivo_tramite_alu.setMaximumSize(QtCore.QSize(16777215, 150))
        self.input_motivo_tramite_alu.setObjectName("input_motivo_tramite_alu")
        self.gridLayout_6.addWidget(self.input_motivo_tramite_alu, 0, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_6.addWidget(self.label_42, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_6.addWidget(self.label_41, 0, 1, 1, 1)
        self.label_ini_tram_alu_estado = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_estado.setText("")
        self.label_ini_tram_alu_estado.setObjectName("label_ini_tram_alu_estado")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_estado, 5, 2, 1, 1)
        self.label_ini_tram_alu_asig_en = QtWidgets.QLabel(self.page_iniciar_tramite_alu)
        self.label_ini_tram_alu_asig_en.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_ini_tram_alu_asig_en.setFont(font)
        self.label_ini_tram_alu_asig_en.setText("")
        self.label_ini_tram_alu_asig_en.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ini_tram_alu_asig_en.setObjectName("label_ini_tram_alu_asig_en")
        self.gridLayout_6.addWidget(self.label_ini_tram_alu_asig_en, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_iniciar_tramite_alu)
        self.page_modif_pass_alu = QtWidgets.QWidget()
        self.page_modif_pass_alu.setObjectName("page_modif_pass_alu")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_modif_pass_alu)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_57 = QtWidgets.QLabel(self.page_modif_pass_alu)
        self.label_57.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout_7.addWidget(self.label_57, 0, 0, 1, 2)
        self.frame_13 = QtWidgets.QFrame(self.page_modif_pass_alu)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_34.setContentsMargins(-1, -1, 40, -1)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.input_modif_pass_actual_alu = QtWidgets.QLineEdit(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_modif_pass_actual_alu.sizePolicy().hasHeightForWidth())
        self.input_modif_pass_actual_alu.setSizePolicy(sizePolicy)
        self.input_modif_pass_actual_alu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.input_modif_pass_actual_alu.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_modif_pass_actual_alu.setObjectName("input_modif_pass_actual_alu")
        self.gridLayout_34.addWidget(self.input_modif_pass_actual_alu, 0, 1, 1, 1)
        self.label_error_new_pass_alu = QtWidgets.QLabel(self.frame_13)
        self.label_error_new_pass_alu.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_error_new_pass_alu.setText("")
        self.label_error_new_pass_alu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_error_new_pass_alu.setObjectName("label_error_new_pass_alu")
        self.gridLayout_34.addWidget(self.label_error_new_pass_alu, 2, 1, 1, 1)
        self.input_new_pass_alu = QtWidgets.QLineEdit(self.frame_13)
        self.input_new_pass_alu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.input_new_pass_alu.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_new_pass_alu.setObjectName("input_new_pass_alu")
        self.gridLayout_34.addWidget(self.input_new_pass_alu, 1, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_34.addWidget(self.label_49, 1, 0, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.gridLayout_34.addWidget(self.label_56, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_13, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(158, 269, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 1, 1, 1, 2)
        self.label_informe_modif_pass_alu = QtWidgets.QLabel(self.page_modif_pass_alu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_informe_modif_pass_alu.setFont(font)
        self.label_informe_modif_pass_alu.setText("")
        self.label_informe_modif_pass_alu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_informe_modif_pass_alu.setObjectName("label_informe_modif_pass_alu")
        self.gridLayout_7.addWidget(self.label_informe_modif_pass_alu, 2, 0, 1, 1)
        self.btn_cambiar_pass_alu = QtWidgets.QPushButton(self.page_modif_pass_alu)
        self.btn_cambiar_pass_alu.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.btn_cambiar_pass_alu.setFont(font)
        self.btn_cambiar_pass_alu.setObjectName("btn_cambiar_pass_alu")
        self.gridLayout_7.addWidget(self.btn_cambiar_pass_alu, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_modif_pass_alu)
        self.page_stats_academicas = QtWidgets.QWidget()
        self.page_stats_academicas.setObjectName("page_stats_academicas")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_stats_academicas)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tW_mat_aprobadas = QtWidgets.QTableWidget(self.page_stats_academicas)
        self.tW_mat_aprobadas.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.tW_mat_aprobadas.setFont(font)
        self.tW_mat_aprobadas.setObjectName("tW_mat_aprobadas")
        self.tW_mat_aprobadas.setColumnCount(2)
        self.tW_mat_aprobadas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tW_mat_aprobadas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_mat_aprobadas.setHorizontalHeaderItem(1, item)
        self.gridLayout_8.addWidget(self.tW_mat_aprobadas, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_stats_academicas)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_stats_academicas)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 5)
        self.frame_3 = QtWidgets.QFrame(self.page_stats_academicas)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_promedio_alu = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.label_promedio_alu.setFont(font)
        self.label_promedio_alu.setText("")
        self.label_promedio_alu.setObjectName("label_promedio_alu")
        self.gridLayout_9.addWidget(self.label_promedio_alu, 2, 1, 1, 1)
        self.label_cred_aprobados_alu = QtWidgets.QLabel(self.frame_3)
        self.label_cred_aprobados_alu.setText("")
        self.label_cred_aprobados_alu.setObjectName("label_cred_aprobados_alu")
        self.gridLayout_9.addWidget(self.label_cred_aprobados_alu, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 2, 2, 1, 2)
        self.stackedWidget.addWidget(self.page_stats_academicas)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Systemalu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Systemalu)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Systemalu)

    def retranslateUi(self, Systemalu):
        _translate = QtCore.QCoreApplication.translate
        Systemalu.setWindowTitle(_translate("Systemalu", "MainWindow"))
        self.btn_logout_alu.setText(_translate("Systemalu", "Cerrar sesión"))
        self.btn_inscr_mat_alu.setText(_translate("Systemalu", "Inscripción a materia"))
        self.btn_desinscr_mat_alu.setText(_translate("Systemalu", "Desinscripción a materia"))
        self.btn_iniciar_tramite_alu.setText(_translate("Systemalu", "Iniciar trámite"))
        self.btn_modif_pass_alu.setText(_translate("Systemalu", "Cambiar contraseña"))
        self.btn_stats_academicas.setText(_translate("Systemalu", "Estadísticas académicas"))
        self.btn_inscr_mat.setText(_translate("Systemalu", "Inscribir a materia"))
        self.label_51.setText(_translate("Systemalu", "INSCRIPCION A MATERIA"))
        item = self.tW_inscr_mat.horizontalHeaderItem(0)
        item.setText(_translate("Systemalu", "Dia"))
        item = self.tW_inscr_mat.horizontalHeaderItem(1)
        item.setText(_translate("Systemalu", "Inicio"))
        item = self.tW_inscr_mat.horizontalHeaderItem(2)
        item.setText(_translate("Systemalu", "Fin"))
        self.label.setText(_translate("Systemalu", "Información de la comisión"))
        self.label_info_dni_en_6.setText(_translate("Systemalu", "Seleccione una comision:"))
        self.label_info_nombre_en_6.setText(_translate("Systemalu", "Seleccione una materia:"))
        self.label_52.setText(_translate("Systemalu", "DESINSCRIPCION A MATERIA"))
        self.label_info_dni_en_7.setText(_translate("Systemalu", "Cod. Comision inscripta:"))
        self.label_info_nombre_en_7.setText(_translate("Systemalu", "Seleccione una materia:"))
        item = self.tabla_desinscr_mat.horizontalHeaderItem(0)
        item.setText(_translate("Systemalu", "Dia"))
        item = self.tabla_desinscr_mat.horizontalHeaderItem(1)
        item.setText(_translate("Systemalu", "Inicio"))
        item = self.tabla_desinscr_mat.horizontalHeaderItem(2)
        item.setText(_translate("Systemalu", "Fin"))
        self.label_2.setText(_translate("Systemalu", "Información de la comisión"))
        self.btn_desinscr_mat.setText(_translate("Systemalu", "Desinscribir a materia"))
        self.btn_ini_tram_alu.setText(_translate("Systemalu", "Iniciar trámite"))
        self.label_42.setText(_translate("Systemalu", "INICIAR TRAMITE"))
        self.label_41.setText(_translate("Systemalu", "Ingrese motivo del trámite:"))
        self.label_57.setText(_translate("Systemalu", "CAMBIAR CONTRASEÑA"))
        self.label_49.setText(_translate("Systemalu", "Nueva contraseña:"))
        self.label_56.setText(_translate("Systemalu", "Ingrese su contraseña actual:"))
        self.btn_cambiar_pass_alu.setText(_translate("Systemalu", "Cambiar contraseña"))
        item = self.tW_mat_aprobadas.horizontalHeaderItem(0)
        item.setText(_translate("Systemalu", "Materia"))
        item = self.tW_mat_aprobadas.horizontalHeaderItem(1)
        item.setText(_translate("Systemalu", "Final"))
        self.label_4.setText(_translate("Systemalu", "Materias aprobadas"))
        self.label_3.setText(_translate("Systemalu", "ESTADISTICAS ACADEMICAS"))
        self.label_5.setText(_translate("Systemalu", "Promedio de la carrera:"))
        self.label_6.setText(_translate("Systemalu", "Créditos aprobados:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Systemalu = QtWidgets.QMainWindow()
    ui = Ui_Systemalu()
    ui.setupUi(Systemalu)
    Systemalu.show()
    sys.exit(app.exec_())
