# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationacHtbm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_Registration(object):
    def setupUi(self, Registration):
        if Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(500, 700)
        Registration.setMinimumSize(QSize(500, 700))
        Registration.setMaximumSize(QSize(500, 700))
        self.verticalLayout = QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Registration)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/user-plus.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.frame_3)
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

        self.btn_maximize = QPushButton(self.frame_3)
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

        self.btn_close = QPushButton(self.frame_3)
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


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.t_firstname = QLineEdit(self.frame_4)
        self.t_firstname.setObjectName(u"t_firstname")
        self.t_firstname.setGeometry(QRect(20, 100, 441, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.t_firstname.setFont(font1)
        self.t_firstname.setTabletTracking(True)
        self.t_firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.t_firstname.setClearButtonEnabled(True)
        self.t_lastname = QLineEdit(self.frame_4)
        self.t_lastname.setObjectName(u"t_lastname")
        self.t_lastname.setGeometry(QRect(20, 240, 441, 51))
        self.t_lastname.setFont(font1)
        self.t_lastname.setTabletTracking(True)
        self.t_lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"		padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.t_lastname.setClearButtonEnabled(True)
        self.t_incharge = QLineEdit(self.frame_4)
        self.t_incharge.setObjectName(u"t_incharge")
        self.t_incharge.setGeometry(QRect(20, 380, 441, 51))
        self.t_incharge.setFont(font1)
        self.t_incharge.setTabletTracking(True)
        self.t_incharge.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"		padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.t_incharge.setClearButtonEnabled(True)
        self.btn_register = QPushButton(self.frame_4)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(20, 450, 441, 41))
        self.btn_register.setFont(font1)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 510, 441, 101))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_notification.setFont(font2)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.t_contact = QLineEdit(self.frame_4)
        self.t_contact.setObjectName(u"t_contact")
        self.t_contact.setGeometry(QRect(20, 310, 441, 51))
        self.t_contact.setFont(font1)
        self.t_contact.setTabletTracking(True)
        self.t_contact.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"		padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.t_contact.setClearButtonEnabled(True)
        self.t_middlename = QLineEdit(self.frame_4)
        self.t_middlename.setObjectName(u"t_middlename")
        self.t_middlename.setGeometry(QRect(20, 170, 441, 51))
        self.t_middlename.setFont(font1)
        self.t_middlename.setTabletTracking(True)
        self.t_middlename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.t_middlename.setClearButtonEnabled(True)
        self.label_notification_2 = QLabel(self.frame_4)
        self.label_notification_2.setObjectName(u"label_notification_2")
        self.label_notification_2.setGeometry(QRect(20, 20, 441, 41))
        self.label_notification_2.setFont(font2)
        self.label_notification_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification_2.setAlignment(Qt.AlignCenter)
        self.label_notification_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Registration", u"Registration", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.t_firstname.setPlaceholderText(QCoreApplication.translate("Registration", u"Firstname", None))
        self.t_lastname.setPlaceholderText(QCoreApplication.translate("Registration", u"Lastname", None))
        self.t_incharge.setPlaceholderText(QCoreApplication.translate("Registration", u"Incharge", None))
        self.btn_register.setText(QCoreApplication.translate("Registration", u"Register", None))
        self.label_notification.setText(QCoreApplication.translate("Registration", u"Notification", None))
        self.t_contact.setPlaceholderText(QCoreApplication.translate("Registration", u"Contact", None))
        self.t_middlename.setPlaceholderText(QCoreApplication.translate("Registration", u"Middlename", None))
        self.label_notification_2.setText(QCoreApplication.translate("Registration", u"Enter Teacher Details", None))
    # retranslateUi

