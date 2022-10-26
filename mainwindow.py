# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.img_dir_label.setGeometry(QtCore.QRect(40, 110, 561, 81))
        self.img_dir_label.setFrameShape(QtWidgets.QFrame.Box)
        self.img_dir_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img_dir_label.setObjectName("img_dir_label")
        self.label_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.label_dir_label.setGeometry(QtCore.QRect(40, 220, 561, 81))
        self.label_dir_label.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dir_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_dir_label.setObjectName("label_dir_label")
        self.img_dir_input_botton = QtWidgets.QToolButton(self.centralwidget)
        self.img_dir_input_botton.setGeometry(QtCore.QRect(540, 140, 37, 18))
        self.img_dir_input_botton.setObjectName("img_dir_input_botton")
        self.label_dir_input_botton = QtWidgets.QToolButton(self.centralwidget)
        self.label_dir_input_botton.setGeometry(QtCore.QRect(540, 250, 37, 18))
        self.label_dir_input_botton.setObjectName("label_dir_input_botton")
        self.do_botton = QtWidgets.QPushButton(self.centralwidget)
        self.do_botton.setGeometry(QtCore.QRect(80, 490, 131, 41))
        self.do_botton.setObjectName("do_botton")
        self.img_format_box = QtWidgets.QComboBox(self.centralwidget)
        self.img_format_box.setGeometry(QtCore.QRect(150, 340, 101, 22))
        self.img_format_box.setObjectName("img_format_box")
        self.img_format_box.addItem("")
        self.img_format_box.addItem("")
        self.img_format_box.addItem("")
        self.img_format_box.addItem("")
        self.img_format_box.addItem("")
        self.img_format_box.addItem("")
        self.img_format_label = QtWidgets.QLabel(self.centralwidget)
        self.img_format_label.setGeometry(QtCore.QRect(40, 330, 221, 41))
        self.img_format_label.setFrameShape(QtWidgets.QFrame.Box)
        self.img_format_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img_format_label.setObjectName("img_format_label")
        self.label_format_label = QtWidgets.QLabel(self.centralwidget)
        self.label_format_label.setGeometry(QtCore.QRect(370, 330, 201, 41))
        self.label_format_label.setFrameShape(QtWidgets.QFrame.Box)
        self.label_format_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_format_label.setObjectName("label_format_label")
        self.label_format_box = QtWidgets.QComboBox(self.centralwidget)
        self.label_format_box.setGeometry(QtCore.QRect(470, 340, 91, 22))
        self.label_format_box.setObjectName("label_format_box")
        self.label_format_box.addItem("")
        self.label_format_box.addItem("")
        self.save_dir_input_botton = QtWidgets.QToolButton(self.centralwidget)
        self.save_dir_input_botton.setGeometry(QtCore.QRect(540, 40, 37, 18))
        self.save_dir_input_botton.setObjectName("save_dir_input_botton")
        self.save_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.save_dir_label.setGeometry(QtCore.QRect(40, 10, 561, 81))
        self.save_dir_label.setFrameShape(QtWidgets.QFrame.Box)
        self.save_dir_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.save_dir_label.setObjectName("save_dir_label")
        self.save_dir_input_edit = QtWidgets.QLabel(self.centralwidget)
        self.save_dir_input_edit.setGeometry(QtCore.QRect(140, 40, 371, 21))
        self.save_dir_input_edit.setFrameShape(QtWidgets.QFrame.Panel)
        self.save_dir_input_edit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.save_dir_input_edit.setText("")
        self.save_dir_input_edit.setObjectName("save_dir_input_edit")
        self.img_dir_input_edit = QtWidgets.QLabel(self.centralwidget)
        self.img_dir_input_edit.setGeometry(QtCore.QRect(140, 140, 371, 21))
        self.img_dir_input_edit.setFrameShape(QtWidgets.QFrame.Panel)
        self.img_dir_input_edit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.img_dir_input_edit.setText("")
        self.img_dir_input_edit.setObjectName("img_dir_input_edit")
        self.label_dir_input_edit = QtWidgets.QLabel(self.centralwidget)
        self.label_dir_input_edit.setGeometry(QtCore.QRect(140, 250, 371, 20))
        self.label_dir_input_edit.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_dir_input_edit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_dir_input_edit.setText("")
        self.label_dir_input_edit.setObjectName("label_dir_input_edit")
        self.start_num_label = QtWidgets.QLabel(self.centralwidget)
        self.start_num_label.setGeometry(QtCore.QRect(370, 400, 201, 41))
        self.start_num_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.start_num_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.start_num_label.setObjectName("start_num_label")
        self.start_num_box = QtWidgets.QSpinBox(self.centralwidget)
        self.start_num_box.setGeometry(QtCore.QRect(480, 410, 71, 22))
        self.start_num_box.setObjectName("start_num_box")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(40, 390, 301, 51))
        self.name_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_label.setObjectName("name_label")
        self.start_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.start_name_edit.setGeometry(QtCore.QRect(150, 410, 141, 20))
        self.start_name_edit.setObjectName("start_name_edit")
        self.rename_progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.rename_progress_bar.setGeometry(QtCore.QRect(260, 500, 331, 23))
        self.rename_progress_bar.setProperty("value", 24)
        self.rename_progress_bar.setObjectName("rename_progress_bar")
        self.save_dir_label.raise_()
        self.img_format_label.raise_()
        self.img_dir_label.raise_()
        self.label_dir_label.raise_()
        self.img_dir_input_botton.raise_()
        self.label_dir_input_botton.raise_()
        self.do_botton.raise_()
        self.img_format_box.raise_()
        self.label_format_label.raise_()
        self.label_format_box.raise_()
        self.save_dir_input_botton.raise_()
        self.save_dir_input_edit.raise_()
        self.img_dir_input_edit.raise_()
        self.label_dir_input_edit.raise_()
        self.start_num_label.raise_()
        self.start_num_box.raise_()
        self.name_label.raise_()
        self.start_name_edit.raise_()
        self.rename_progress_bar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_dir_label.setText(_translate("MainWindow", "图片文件夹"))
        self.label_dir_label.setText(_translate("MainWindow", "标签文件夹"))
        self.img_dir_input_botton.setText(_translate("MainWindow", "..."))
        self.label_dir_input_botton.setText(_translate("MainWindow", "..."))
        self.do_botton.setText(_translate("MainWindow", "执行"))
        self.img_format_box.setItemText(0, _translate("MainWindow", ".jpg"))
        self.img_format_box.setItemText(1, _translate("MainWindow", ".jpeg"))
        self.img_format_box.setItemText(2, _translate("MainWindow", ".PNG"))
        self.img_format_box.setItemText(3, _translate("MainWindow", ".png"))
        self.img_format_box.setItemText(4, _translate("MainWindow", ".JPG"))
        self.img_format_box.setItemText(5, _translate("MainWindow", ".JPEG"))
        self.img_format_label.setText(_translate("MainWindow", "图片格式"))
        self.label_format_label.setText(_translate("MainWindow", "标签格式"))
        self.label_format_box.setItemText(0, _translate("MainWindow", ".txt"))
        self.label_format_box.setItemText(1, _translate("MainWindow", ".xml"))
        self.save_dir_input_botton.setText(_translate("MainWindow", "..."))
        self.save_dir_label.setText(_translate("MainWindow", "保存文件夹"))
        self.start_num_label.setText(_translate("MainWindow", "起始数字"))
        self.name_label.setText(_translate("MainWindow", "数字前标识"))
