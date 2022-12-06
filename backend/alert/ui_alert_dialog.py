# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert_dialogYKFbEn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide2.QtGui import (QFont,
    QPixmap)
from PySide2.QtWidgets import *

import asset_rc

class Ui_AlertDialog(object):
    def setupUi(self, AlertDialog):
        if AlertDialog.objectName():
            AlertDialog.setObjectName(u"AlertDialog")
        AlertDialog.resize(512, 233)
        self.verticalLayout = QVBoxLayout(AlertDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AlertDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"    background-color: rgb(45, 45, 45);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.title_frame = QFrame(self.frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 40))
        self.title_frame.setMaximumSize(QSize(16777215, 40))
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.title_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.title_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.title_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.title_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.title_frame)

        self.content_frame = QFrame(self.frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setPixmap(QPixmap(u":/icons/asset/alert-triangle.svg"))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.content = QLabel(self.content_frame)
        self.content.setObjectName(u"content")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.content.setFont(font)
        self.content.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.content_frame)

        self.btn_frame = QFrame(self.frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setMinimumSize(QSize(0, 60))
        self.btn_frame.setMaximumSize(QSize(16777215, 60))
        self.btn_frame.setFrameShape(QFrame.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.btn_close_alert = QPushButton(self.btn_frame)
        self.btn_close_alert.setObjectName(u"btn_close_alert")
        self.btn_close_alert.setGeometry(QRect(330, 20, 131, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_close_alert.setFont(font1)
        self.btn_close_alert.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);	\n"
"	border:2px solid rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_close_alert.setIconSize(QSize(30, 30))
        self.btn_close_alert.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_frame)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AlertDialog)

        QMetaObject.connectSlotsByName(AlertDialog)
    # setupUi

    def retranslateUi(self, AlertDialog):
        AlertDialog.setWindowTitle(QCoreApplication.translate("AlertDialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.label_3.setText("")
        self.content.setText(QCoreApplication.translate("AlertDialog", u" Something went wrong", None))
        self.btn_close_alert.setText(QCoreApplication.translate("AlertDialog", u"Ok", None))
    # retranslateUi

