# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mailJNyswn.ui'
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

class Ui_Mail(object):
    def setupUi(self, Mail):
        if Mail.objectName():
            Mail.setObjectName(u"Mail")
        Mail.resize(500, 700)
        Mail.setMinimumSize(QSize(500, 700))
        Mail.setMaximumSize(QSize(500, 700))
        self.verticalLayout = QVBoxLayout(Mail)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Mail)
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
        self.label.setPixmap(QPixmap(u":/icons/asset/mail.svg"))

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
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 120, 31, 31))
        self.label_36.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_36.setPixmap(QPixmap(u":/icons/asset/user.svg"))
        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 330, 31, 31))
        self.label_37.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_37.setPixmap(QPixmap(u":/icons/asset/lock.svg"))
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 530, 441, 81))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_notification.setFont(font1)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.sender_password = QLineEdit(self.frame_4)
        self.sender_password.setObjectName(u"sender_password")
        self.sender_password.setGeometry(QRect(17, 320, 441, 51))
        self.sender_password.setMinimumSize(QSize(0, 0))
        self.sender_password.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.sender_password.setFont(font2)
        self.sender_password.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.sender_password.setEchoMode(QLineEdit.Password)
        self.sender_password.setClearButtonEnabled(True)
        self.email_subject = QLineEdit(self.frame_4)
        self.email_subject.setObjectName(u"email_subject")
        self.email_subject.setGeometry(QRect(20, 180, 441, 51))
        self.email_subject.setMinimumSize(QSize(0, 0))
        self.email_subject.setMaximumSize(QSize(16777215, 16777215))
        self.email_subject.setFont(font2)
        self.email_subject.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.email_subject.setClearButtonEnabled(True)
        self.email_sender = QLineEdit(self.frame_4)
        self.email_sender.setObjectName(u"email_sender")
        self.email_sender.setGeometry(QRect(17, 250, 441, 51))
        self.email_sender.setMinimumSize(QSize(0, 0))
        self.email_sender.setMaximumSize(QSize(16777215, 16777215))
        self.email_sender.setFont(font2)
        self.email_sender.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.email_sender.setClearButtonEnabled(True)
        self.email_from = QLineEdit(self.frame_4)
        self.email_from.setObjectName(u"email_from")
        self.email_from.setGeometry(QRect(20, 110, 441, 51))
        self.email_from.setMinimumSize(QSize(338, 0))
        self.email_from.setMaximumSize(QSize(16777215, 16777215))
        self.email_from.setFont(font2)
        self.email_from.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.email_from.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 190, 31, 31))
        self.label_38.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_38.setPixmap(QPixmap(u":/icons/asset/edit-3.svg"))
        self.label_39 = QLabel(self.frame_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 260, 31, 31))
        self.label_39.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_39.setPixmap(QPixmap(u":/icons/asset/mail.svg"))
        self.reg_email = QLineEdit(self.frame_4)
        self.reg_email.setObjectName(u"reg_email")
        self.reg_email.setGeometry(QRect(20, 40, 441, 51))
        self.reg_email.setFont(font2)
        self.reg_email.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_email.setClearButtonEnabled(True)
        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(30, 50, 31, 31))
        self.label_44.setPixmap(QPixmap(u":/icons/asset/mail.svg"))
        self.image_file_reg = QLineEdit(self.frame_4)
        self.image_file_reg.setObjectName(u"image_file_reg")
        self.image_file_reg.setGeometry(QRect(20, 390, 251, 51))
        self.image_file_reg.setFont(font2)
        self.image_file_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.image_file_reg.setClearButtonEnabled(True)
        self.btn_browse_reg = QPushButton(self.frame_4)
        self.btn_browse_reg.setObjectName(u"btn_browse_reg")
        self.btn_browse_reg.setGeometry(QRect(20, 460, 211, 51))
        self.btn_browse_reg.setFont(font2)
        self.btn_browse_reg.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse_reg.setIcon(icon)
        self.btn_browse_reg.setIconSize(QSize(30, 30))
        self.btn_browse_reg.setFlat(True)
        self.btn_send_mail = QPushButton(self.frame_4)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        self.btn_send_mail.setGeometry(QRect(250, 460, 211, 51))
        self.btn_send_mail.setFont(font2)
        self.btn_send_mail.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_mail.setIcon(icon1)
        self.btn_send_mail.setIconSize(QSize(30, 30))
        self.btn_send_mail.setFlat(True)
        self.rep_name = QLineEdit(self.frame_4)
        self.rep_name.setObjectName(u"rep_name")
        self.rep_name.setGeometry(QRect(280, 390, 181, 51))
        self.rep_name.setFont(font2)
        self.rep_name.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.rep_name.setClearButtonEnabled(True)
        self.sender_password.raise_()
        self.email_from.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_notification.raise_()
        self.email_subject.raise_()
        self.email_sender.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.reg_email.raise_()
        self.label_44.raise_()
        self.image_file_reg.raise_()
        self.btn_browse_reg.raise_()
        self.btn_send_mail.raise_()
        self.rep_name.raise_()

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Mail)

        QMetaObject.connectSlotsByName(Mail)
    # setupUi

    def retranslateUi(self, Mail):
        Mail.setWindowTitle(QCoreApplication.translate("Mail", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Mail", u"Email Application Data", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_notification.setText(QCoreApplication.translate("Mail", u"Notification", None))
        self.sender_password.setPlaceholderText(QCoreApplication.translate("Mail", u"Password", None))
        self.email_subject.setPlaceholderText(QCoreApplication.translate("Mail", u"Subject", None))
        self.email_sender.setPlaceholderText(QCoreApplication.translate("Mail", u"Email", None))
        self.email_from.setPlaceholderText(QCoreApplication.translate("Mail", u"From", None))
        self.label_38.setText("")
        self.label_39.setText("")
        self.reg_email.setPlaceholderText(QCoreApplication.translate("Mail", u"Receipient(s) ", None))
        self.label_44.setText("")
        self.image_file_reg.setPlaceholderText(QCoreApplication.translate("Mail", u"File path", None))
        self.btn_browse_reg.setText(QCoreApplication.translate("Mail", u"Browse", None))
        self.btn_send_mail.setText(QCoreApplication.translate("Mail", u"Send mail", None))
        self.rep_name.setPlaceholderText(QCoreApplication.translate("Mail", u"Receipient name", None))
    # retranslateUi

