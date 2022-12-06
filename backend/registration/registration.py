import json
import math
import qrcode
import numpy as np
from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
from model.teacher import Registration_
from registration.ui_registration import Ui_Registration

class Registration(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_registration = Ui_Registration()
        self.ui_registration.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_registration.btn_close.clicked.connect(self.close)
        self.ui_registration.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_registration.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_registration.frame.setGraphicsEffect(self.shadow)

        self.ui_registration.btn_register.clicked.connect(self.generate_code)

    def generate_code(self):
        details = self.get_field_text()
        reference=math.floor(np.random.random(1)*10000000)
        register = Registration_(
            t_reference=str(reference),
            t_firstname=details[0],
            t_middlename=details[1],
            t_lastname=details[2],
            t_contact=details[3],
            t_incharge=details[4]
        )
        if register.t_firstname !=""  and register.t_lastname !=""  and register.t_contact !="" :
            teacher ={
            "reference":register.t_reference,
            "firstname":register.t_firstname,
            "middlename":register.t_middlename,
            "lastname":register.t_lastname,
            "contact":register.t_contact,
            "incharge":register.t_incharge
            }
            teacher_json=self.convert_to_json(teacher)
            image = qrcode.make(teacher_json)
            image.save('C:\\ProgramData\\iteachers\\data\\QR_Codes\\'+register.t_firstname+"_"+register.t_lastname+"_"+register.t_reference+".png")
            self.ui_registration.label_notification.setText("Hey! you have successfully registered...")
            print(teacher_json)
        else:
            self.ui_registration.label_notification.setText("Oops! provide valid registration details...")
     

    def convert_to_json(self, teacher:Registration_):
        to_json = json.dumps(teacher)
        return to_json
        
    def get_field_text(self):
        t_firstname=self.ui_registration.t_firstname.text()
        t_middlename=self.ui_registration.t_middlename.text()
        t_lastname=self.ui_registration.t_lastname.text()
        t_contact=self.ui_registration.t_contact.text()
        t_incharge=self.ui_registration.t_incharge.text() 
        return t_firstname,t_middlename,t_lastname,t_contact,t_incharge
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    
