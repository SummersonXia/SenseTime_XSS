# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SenseTime_UI_child_log_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Child_log_analysis(object):
    def setupUi(self, Child_log_analysis):
        Child_log_analysis.setObjectName("Child_log_analysis")
        Child_log_analysis.resize(401, 305)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Child_log_analysis.sizePolicy().hasHeightForWidth())
        Child_log_analysis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Child_log_analysis.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Child_log_analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton_gt_csv = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_gt_csv.setObjectName("toolButton_gt_csv")
        self.horizontalLayout.addWidget(self.toolButton_gt_csv)
        self.lineEdit_gt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gt.setObjectName("lineEdit_gt")
        self.horizontalLayout.addWidget(self.lineEdit_gt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.toolButton_log_folder = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_log_folder.setObjectName("toolButton_log_folder")
        self.horizontalLayout_2.addWidget(self.toolButton_log_folder)
        self.lineEdit_log_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_log_folder.setObjectName("lineEdit_log_folder")
        self.horizontalLayout_2.addWidget(self.lineEdit_log_folder)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.toolButton_result_csv = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_result_csv.setObjectName("toolButton_result_csv")
        self.horizontalLayout_3.addWidget(self.toolButton_result_csv)
        self.lineEdit_result = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.horizontalLayout_3.addWidget(self.lineEdit_result)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_log_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log_analysis.setObjectName("pushButton_log_analysis")
        self.verticalLayout_2.addWidget(self.pushButton_log_analysis)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        Child_log_analysis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Child_log_analysis)
        self.statusbar.setObjectName("statusbar")
        Child_log_analysis.setStatusBar(self.statusbar)

        self.retranslateUi(Child_log_analysis)
        QtCore.QMetaObject.connectSlotsByName(Child_log_analysis)

    def retranslateUi(self, Child_log_analysis):
        _translate = QtCore.QCoreApplication.translate
        Child_log_analysis.setWindowTitle(_translate("Child_log_analysis", "MainWindow"))
        self.label.setText(_translate("Child_log_analysis", "GT文件"))
        self.toolButton_gt_csv.setText(_translate("Child_log_analysis", "..."))
        self.label_2.setText(_translate("Child_log_analysis", "log文件夹"))
        self.toolButton_log_folder.setText(_translate("Child_log_analysis", "..."))
        self.label_3.setText(_translate("Child_log_analysis", "结果文件"))
        self.toolButton_result_csv.setText(_translate("Child_log_analysis", "..."))
        self.pushButton_log_analysis.setText(_translate("Child_log_analysis", "分析"))