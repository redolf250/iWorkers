# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboard.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1520, 1000)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setGeometry(QRect(0, 0, 1541, 1000))
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 1000))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 6, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.other_fields)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(5, 0))
        self.logo.setMaximumSize(QSize(60, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.options)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.options)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")

        self.horizontalLayout_19.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(100, 0))
        self.controls_frame.setMaximumSize(QSize(100, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(40, 20, 16, 16))
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
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(10, 20, 16, 16))
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
        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 16, 16))
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

        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(70, 0))
        self.menu_frame.setMaximumSize(QSize(80, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 3)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(False)
        self.btn_home.setFlat(True)

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(40, 40))
        self.btn_search.setCheckable(True)
        self.btn_search.setFlat(True)

        self.verticalLayout.addWidget(self.btn_search)

        self.btn_register = QPushButton(self.frame)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(0, 70))
        self.btn_register.setMaximumSize(QSize(16777215, 70))
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon2)
        self.btn_register.setIconSize(QSize(40, 40))
        self.btn_register.setCheckable(True)
        self.btn_register.setFlat(True)

        self.verticalLayout.addWidget(self.btn_register)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.btn_help = QPushButton(self.menu_frame)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 70))
        self.btn_help.setMaximumSize(QSize(16777215, 70))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"    padding-left:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon3)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_help)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 390))
        self.info_frame.setMaximumSize(QSize(16777215, 390))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 261, 281))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 80, 191, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.firstname.setFont(font3)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(290, 140, 191, 41))
        self.middlename.setFont(font3)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 200, 191, 41))
        self.lastname.setFont(font3)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(290, 20, 191, 41))
        self.refrence.setFont(font3)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.contact = QLabel(self.info_frame)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(290, 260, 191, 41))
        self.contact.setFont(font3)
        self.contact.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.contact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.incharge = QLabel(self.info_frame)
        self.incharge.setObjectName(u"incharge")
        self.incharge.setGeometry(QRect(20, 320, 261, 41))
        self.incharge.setFont(font3)
        self.incharge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.incharge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 0, 481, 381))
        self.image_2.setFont(font2)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.status = QLabel(self.info_frame)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(290, 320, 191, 41))
        self.status.setFont(font3)
        self.status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.middlename.raise_()
        self.lastname.raise_()
        self.refrence.raise_()
        self.contact.raise_()
        self.incharge.raise_()
        self.status.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 530))
        self.frame_3.setMaximumSize(QSize(16777215, 530))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 440, 481, 91))
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.camera_ip = QLineEdit(self.frame_3)
        self.camera_ip.setObjectName(u"camera_ip")
        self.camera_ip.setGeometry(QRect(20, 300, 461, 51))
        font4 = QFont()
        font4.setPointSize(10)
        self.camera_ip.setFont(font4)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_ip.setClearButtonEnabled(True)
        self.btn_connect_detect = QPushButton(self.frame_3)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(20, 370, 131, 41))
        self.btn_connect_detect.setFont(font4)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_detect.setIcon(icon4)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, 310, 41, 31))
        self.label_27.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(160, 370, 141, 41))
        self.btn_disconnect.setFont(font4)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon5)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 370, 171, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.firstname_23 = QLabel(self.frame_3)
        self.firstname_23.setObjectName(u"firstname_23")
        self.firstname_23.setGeometry(QRect(10, 260, 481, 171))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.firstname_23.setFont(font5)
        self.firstname_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_24 = QLabel(self.frame_3)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(10, 190, 481, 61))
        self.firstname_24.setFont(font5)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(260, 200, 221, 41))
        self.btn_clear_label.setFont(font4)
        self.btn_clear_label.setStyleSheet(u"QPushButton{\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon6)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_open_database = QPushButton(self.frame_3)
        self.btn_open_database.setObjectName(u"btn_open_database")
        self.btn_open_database.setGeometry(QRect(20, 200, 221, 41))
        self.btn_open_database.setFont(font4)
        self.btn_open_database.setStyleSheet(u"QPushButton{\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_database.setIcon(icon7)
        self.btn_open_database.setIconSize(QSize(30, 30))
        self.btn_open_database.setFlat(True)
        self.firstname_25 = QLabel(self.frame_3)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 120, 481, 61))
        self.firstname_25.setFont(font5)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.database_tables = QComboBox(self.frame_3)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(30, 130, 291, 38))
        self.database_tables.setMinimumSize(QSize(0, 38))
        self.database_tables.setMaximumSize(QSize(16777215, 38))
        self.database_tables.setFont(font4)
        self.database_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables.setFrame(False)
        self.btn_refresh = QPushButton(self.frame_3)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(340, 130, 131, 41))
        self.btn_refresh.setFont(font4)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon8)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.firstname_26 = QLabel(self.frame_3)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 0, 481, 101))
        self.firstname_26.setFont(font5)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.status_2 = QLabel(self.frame_3)
        self.status_2.setObjectName(u"status_2")
        self.status_2.setGeometry(QRect(10, 10, 111, 21))
        self.status_2.setFont(font3)
        self.status_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"\n"
"}")
        self.status_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.late_hour = QSpinBox(self.frame_3)
        self.late_hour.setObjectName(u"late_hour")
        self.late_hour.setGeometry(QRect(130, 50, 81, 41))
        font6 = QFont()
        font6.setPointSize(14)
        self.late_hour.setFont(font6)
        self.late_hour.setStyleSheet(u"QSpinBox{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.late_hour.setReadOnly(False)
        self.late_hour.setMaximum(12)
        self.late_hour.setValue(8)
        self.late_minutes = QSpinBox(self.frame_3)
        self.late_minutes.setObjectName(u"late_minutes")
        self.late_minutes.setGeometry(QRect(400, 50, 81, 41))
        self.late_minutes.setFont(font6)
        self.late_minutes.setStyleSheet(u"QSpinBox{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.late_minutes.setReadOnly(False)
        self.late_minutes.setMaximum(59)
        self.late_minutes.setValue(30)
        self.contact_2 = QLabel(self.frame_3)
        self.contact_2.setObjectName(u"contact_2")
        self.contact_2.setGeometry(QRect(20, 50, 101, 41))
        self.contact_2.setFont(font3)
        self.contact_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_2.setAlignment(Qt.AlignCenter)
        self.contact_3 = QLabel(self.frame_3)
        self.contact_3.setObjectName(u"contact_3")
        self.contact_3.setGeometry(QRect(280, 50, 111, 41))
        self.contact_3.setFont(font3)
        self.contact_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_3.setAlignment(Qt.AlignCenter)
        self.contact_4 = QLabel(self.frame_3)
        self.contact_4.setObjectName(u"contact_4")
        self.contact_4.setGeometry(QRect(230, 50, 31, 41))
        font7 = QFont()
        font7.setFamilies([u"MS Shell Dlg 2"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.contact_4.setFont(font7)
        self.contact_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_4.setAlignment(Qt.AlignCenter)
        self.read_only_property = QRadioButton(self.frame_3)
        self.read_only_property.setObjectName(u"read_only_property")
        self.read_only_property.setGeometry(QRect(310, 10, 171, 20))
        self.read_only_property.setFont(font4)
        self.read_only_property.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.read_only_property.setChecked(True)
        self.firstname_23.raise_()
        self.label_notification.raise_()
        self.camera_ip.raise_()
        self.btn_connect_detect.raise_()
        self.label_27.raise_()
        self.btn_disconnect.raise_()
        self.comboBox.raise_()
        self.firstname_24.raise_()
        self.btn_clear_label.raise_()
        self.btn_open_database.raise_()
        self.firstname_25.raise_()
        self.database_tables.raise_()
        self.btn_refresh.raise_()
        self.firstname_26.raise_()
        self.status_2.raise_()
        self.late_hour.raise_()
        self.late_minutes.raise_()
        self.contact_2.raise_()
        self.contact_3.raise_()
        self.contact_4.raise_()
        self.read_only_property.raise_()

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 700))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 700))
        self.camera_frame.setMaximumSize(QSize(16777215, 700))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font2)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_view.setAlignment(Qt.AlignCenter)
        self.camera_view.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(20)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 3)

        self.brightness_value = QLabel(self.frame_4)
        self.brightness_value.setObjectName(u"brightness_value")
        self.brightness_value.setMinimumSize(QSize(50, 0))
        self.brightness_value.setMaximumSize(QSize(50, 16777215))
        self.brightness_value.setFont(font5)
        self.brightness_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_value, 4, 2, 1, 1)

        self.brightness_label = QLabel(self.frame_4)
        self.brightness_label.setObjectName(u"brightness_label")
        self.brightness_label.setFont(font5)
        self.brightness_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_label, 4, 0, 1, 1)

        self.brigthness = QSlider(self.frame_4)
        self.brigthness.setObjectName(u"brigthness")
        self.brigthness.setMaximum(100)
        self.brigthness.setValue(30)
        self.brigthness.setSliderPosition(30)
        self.brigthness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.brigthness, 4, 1, 1, 1)

        self.sharpness = QSlider(self.frame_4)
        self.sharpness.setObjectName(u"sharpness")
        self.sharpness.setMaximum(100)
        self.sharpness.setValue(50)
        self.sharpness.setSliderPosition(50)
        self.sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sharpness, 5, 1, 1, 1)

        self.sharp_label = QLabel(self.frame_4)
        self.sharp_label.setObjectName(u"sharp_label")
        self.sharp_label.setFont(font5)
        self.sharp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_label, 5, 0, 1, 1)

        self.sharp_value = QLabel(self.frame_4)
        self.sharp_value.setObjectName(u"sharp_value")
        self.sharp_value.setMinimumSize(QSize(50, 0))
        self.sharp_value.setMaximumSize(QSize(50, 16777215))
        self.sharp_value.setFont(font5)
        self.sharp_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_value, 5, 2, 1, 1)

        self.contrast = QSlider(self.frame_4)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setStyleSheet(u"QSlider:groove:horizontal{\n"
"	margin:2px;\n"
"	height:1px;\n"
"}\n"
"")
        self.contrast.setMaximum(100)
        self.contrast.setValue(60)
        self.contrast.setSliderPosition(60)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.contrast, 6, 1, 1, 1)

        self.contrast_label = QLabel(self.frame_4)
        self.contrast_label.setObjectName(u"contrast_label")
        self.contrast_label.setFont(font5)
        self.contrast_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.contrast_label, 6, 0, 1, 1)

        self.contrast_value = QLabel(self.frame_4)
        self.contrast_value.setObjectName(u"contrast_value")
        self.contrast_value.setMinimumSize(QSize(50, 0))
        self.contrast_value.setMaximumSize(QSize(50, 16777215))
        self.contrast_value.setFont(font5)
        self.contrast_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.contrast_value, 6, 2, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 20, 150, 20))
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.scan_range_label = QLabel(self.frame_5)
        self.scan_range_label.setObjectName(u"scan_range_label")
        self.scan_range_label.setGeometry(QRect(20, 160, 431, 51))
        self.scan_range_label.setFont(font3)
        self.scan_range_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:45px;\n"
"\n"
"}")
        self.scan_range_label.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 170, 31, 31))
        self.label_42.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_42.setPixmap(QPixmap(u":/icons/asset/camera.svg"))
        self.btn_scan_range = QPushButton(self.frame_5)
        self.btn_scan_range.setObjectName(u"btn_scan_range")
        self.btn_scan_range.setGeometry(QRect(300, 80, 151, 51))
        self.btn_scan_range.setFont(font4)
        self.btn_scan_range.setStyleSheet(u"QPushButton{\n"
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
        self.btn_scan_range.setIcon(icon1)
        self.btn_scan_range.setIconSize(QSize(30, 30))
        self.btn_scan_range.setFlat(True)
        self.scan_range = QLineEdit(self.frame_5)
        self.scan_range.setObjectName(u"scan_range")
        self.scan_range.setGeometry(QRect(20, 80, 271, 51))
        self.scan_range.setFont(font4)
        self.scan_range.setStyleSheet(u"QLineEdit{\n"
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
        self.scan_range.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_frame_2 = QFrame(self.search)
        self.left_frame_2.setObjectName(u"left_frame_2")
        self.left_frame_2.setMinimumSize(QSize(500, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 500))
        self.top.setMaximumSize(QSize(500, 500))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 130, 261, 281))
        self.db_image_data.setFont(font2)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.db_image_data.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(290, 310, 191, 41))
        self.db_lastname.setFont(font3)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(290, 250, 191, 41))
        self.db_middlename.setFont(font3)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(290, 190, 191, 41))
        self.db_firstname.setFont(font3)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_contact = QLabel(self.top)
        self.db_contact.setObjectName(u"db_contact")
        self.db_contact.setGeometry(QRect(290, 370, 191, 41))
        self.db_contact.setFont(font3)
        self.db_contact.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_contact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_incharge = QLabel(self.top)
        self.db_incharge.setObjectName(u"db_incharge")
        self.db_incharge.setGeometry(QRect(20, 430, 261, 41))
        self.db_incharge.setFont(font3)
        self.db_incharge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_incharge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_incharge.setWordWrap(True)
        self.search_box = QLineEdit(self.top)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(20, 30, 321, 41))
        self.search_box.setFont(font4)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
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
        self.search_box.setClearButtonEnabled(True)
        self.btn_search_page = QPushButton(self.top)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(350, 30, 131, 41))
        self.btn_search_page.setFont(font4)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
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
        self.btn_search_page.setIcon(icon1)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_29 = QLabel(self.top)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 481, 81))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(11)
        font9.setBold(True)
        self.label_29.setFont(font9)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3 = QLabel(self.top)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setGeometry(QRect(10, 110, 481, 381))
        self.image_3.setFont(font2)
        self.image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_3.setAlignment(Qt.AlignCenter)
        self.db_status = QLabel(self.top)
        self.db_status.setObjectName(u"db_status")
        self.db_status.setGeometry(QRect(290, 430, 191, 41))
        self.db_status.setFont(font3)
        self.db_status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_status.setWordWrap(True)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(290, 130, 191, 41))
        self.db_refrence.setFont(font3)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3.raise_()
        self.label_29.raise_()
        self.db_image_data.raise_()
        self.db_lastname.raise_()
        self.db_middlename.raise_()
        self.db_firstname.raise_()
        self.db_contact.raise_()
        self.db_incharge.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()
        self.db_status.raise_()
        self.db_refrence.raise_()

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 450))
        self.bottom.setMaximumSize(QSize(16777215, 450))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.frame_6 = QFrame(self.bottom)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 190, 461, 240))
        self.frame_6.setMinimumSize(QSize(0, 240))
        self.frame_6.setMaximumSize(QSize(16777215, 240))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)

        self.verticalLayout_12.addWidget(self.calendarWidget)

        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(20, 130, 171, 51))
        self.db_start_date.setFont(font4)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_start_date.setInputMethodHints(Qt.ImhPreferNumbers)
        self.db_start_date.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.bottom)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 140, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 110, 481, 331))
        self.label_30.setMinimumSize(QSize(0, 300))
        self.label_30.setFont(font9)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_csv = QPushButton(self.bottom)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setGeometry(QRect(20, 30, 201, 41))
        self.btn_csv.setFont(font4)
        self.btn_csv.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_csv.setIcon(icon9)
        self.btn_csv.setIconSize(QSize(30, 30))
        self.btn_csv.setFlat(True)
        self.label_40 = QLabel(self.bottom)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 10, 481, 81))
        self.label_40.setFont(font9)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filename = QLineEdit(self.bottom)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(200, 130, 281, 51))
        self.filename.setFont(font4)
        self.filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.filename.setInputMethodHints(Qt.ImhPreferNumbers)
        self.filename.setClearButtonEnabled(True)
        self.btn_backup = QPushButton(self.bottom)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setGeometry(QRect(280, 30, 201, 41))
        self.btn_backup.setFont(font4)
        self.btn_backup.setStyleSheet(u"QPushButton{\n"
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
        self.btn_backup.setIcon(icon7)
        self.btn_backup.setIconSize(QSize(30, 30))
        self.btn_backup.setFlat(True)
        self.label_40.raise_()
        self.label_30.raise_()
        self.frame_6.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.btn_csv.raise_()
        self.filename.raise_()
        self.btn_backup.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.NoFrame)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 9, 12)
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_5.addWidget(self.rigth_frame)

        self.stackedWidget.addWidget(self.search)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)

        dashboard.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("dashboard", u"iAttend", None))
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_search.setText("")
        self.btn_register.setText("")
        self.btn_help.setText("")
        self.image.setText("")
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.contact.setText(QCoreApplication.translate("dashboard", u"Contact", None))
        self.incharge.setText(QCoreApplication.translate("dashboard", u"Incharge", None))
        self.image_2.setText("")
        self.status.setText(QCoreApplication.translate("dashboard", u"Status", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.label_27.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Entry camera", None))
        self.firstname_24.setText("")
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_open_database.setText(QCoreApplication.translate("dashboard", u"Create table", None))
        self.firstname_25.setText("")
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        self.firstname_26.setText("")
        self.status_2.setText(QCoreApplication.translate("dashboard", u"Status check", None))
        self.contact_2.setText(QCoreApplication.translate("dashboard", u"Hour(s)", None))
        self.contact_3.setText(QCoreApplication.translate("dashboard", u"Minute(s)", None))
        self.contact_4.setText(QCoreApplication.translate("dashboard", u":", None))
        self.read_only_property.setText(QCoreApplication.translate("dashboard", u"Read Only Property", None))
        self.camera_view.setText("")
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Image Enhancement", None))
        self.brightness_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.brightness_label.setText(QCoreApplication.translate("dashboard", u"Brigthness", None))
        self.sharp_label.setText(QCoreApplication.translate("dashboard", u"Sharpness", None))
        self.sharp_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.contrast_label.setText(QCoreApplication.translate("dashboard", u"Contrast", None))
        self.contrast_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Camera Scan", None))
        self.scan_range_label.setText("")
        self.label_42.setText("")
        self.btn_scan_range.setText(QCoreApplication.translate("dashboard", u"Scan", None))
        self.scan_range.setPlaceholderText(QCoreApplication.translate("dashboard", u"Scan range ?", None))
        self.db_image_data.setText("")
        self.db_lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_contact.setText(QCoreApplication.translate("dashboard", u"Contact", None))
        self.db_incharge.setText(QCoreApplication.translate("dashboard", u"Incharge", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_29.setText("")
        self.image_3.setText("")
        self.db_status.setText(QCoreApplication.translate("dashboard", u"Status", None))
        self.db_refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.db_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.label_25.setText("")
        self.label_30.setText("")
        self.btn_csv.setText(QCoreApplication.translate("dashboard", u"Save Data", None))
        self.label_40.setText("")
        self.filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename?", None))
        self.btn_backup.setText(QCoreApplication.translate("dashboard", u"Backup", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Contact", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Date Stamp", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Time Stamp", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Status", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Incharge", None));
    # retranslateUi

