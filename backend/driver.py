################################################################################
##
## BY: Asamani Redolf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

from packages.pyqt import *
from packages.system import *
from packages.driver import *
from packages.globals import *
from packages.processing import *

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())    
        #########################################################################################

        #########################################################################################
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_summary.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.summary))
        self.ui.btn_batch_job.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.batch))
        ##########################################################################################################

        ############################################################################################
        self.create_database()
        self.create_program_data_dir()
        self.program_dept = Database()
        self.ui.btn_open_database.clicked.connect(lambda: self.program_dept.show())
        self.program_dept.combo_box(self.get_tables())

        self.register = Registration()
        self.ui.btn_register.clicked.connect(lambda: self.register.show())

        self.mail = Mail()
        self.ui.btn_mail.clicked.connect(lambda: self.mail.show())
        self.ui.btn_send_mail.clicked.connect(lambda: self.mail.show())
        ############################################################################################

        ############################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_webcam)
        self.ui.btn_disconnect.clicked.connect(self.stop_webcam)
        ############################################################################################

        #############################################################################################
        self.ui.btn_search_page.clicked.connect(self.query_database_for_data)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date_on_search_page)
        ##############################################################################################
        
        #####################################################################################################
        self.ui.calendarWidget.selectionChanged.connect(self.get_date_on_search_page)
        self.ui.btn_csv.clicked.connect(self.export_data_to_csv)
        self.ui.btn_backup.clicked.connect(self.backup_database)
        #####################################################################################################

        ###############################################################################################
        self.ui.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui.contrast.valueChanged.connect(self.update_contrast)

        self.ui.brightness_value.setText(str(self.ui.brigthness.value()))
        self.ui.sharp_value.setText(str(self.ui.sharpness.value()))
        self.ui.contrast_value.setText(str(self.ui.contrast.value()))
        #################################################################################################
        self.ui.btn_scan_range.clicked.connect(self.camera_thread)
        self.ui.database_tables.addItems(self.get_tables())
        self.ui.database_summary.addItems(self.get_tables())
        self.ui.batch_table.addItems(self.get_tables())
        self.ui.btn_refresh.clicked.connect(self.refresh_tables)
        self.ui.btn_summary_load.clicked.connect(self.render_teacher_data)
        self.ui.btn_summary_save.clicked.connect(self.export_summary_data)
        self.ui.btn_summary_browse.clicked.connect(self.load_data)
        self.ui.btn_batch_browse.clicked.connect(self.load_batch_data)
        self.ui.btn_start_job.clicked.connect(self.start_insert_job)
        ##################################################################################################

    def resource_path(self,relative_path):
        path_to_img= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path_to_img
        
    def start_insert_job(self):
        path = self.ui.batch_filename.text()
        db = sqlite3.connect(os.path.abspath(self.get_path()))
        my_cursor = db.cursor()
        table = self.ui.batch_table.currentText()
        if path:
            try:
                with open(path,'r') as filename:
                    data=csv.reader(filename)
                    next(data)
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    for teacher in data:
                        time = teacher[5].split(':')
                        time_zone =time[1].split(' ')
                        time_transform = time[0]+':'+time_zone[0]+':'+'00 '+time_zone[1]
                        teacher[5] = time_transform
                        batch_hour = self.ui.batch_hour.value()
                        batch_minute = self.ui.batch_minutes.value()
                        batch_zone = self.ui.batch_time_zone.currentText()
                        if str(time[0])<=str(batch_hour) and str(time[1])<=str(batch_minute) and str(batch_zone)==str(time_zone[1]):
                            teacher.append("Early")
                        else:
                            teacher.append("Late")
                        date=str(teacher[4]).split("-")
                        transform_date = datetime.date(int(date[0]),int(date[1]),int(date[2])).strftime("%a, %b %d, %Y")
                        my_cursor.execute("INSERT INTO "+table+"(teacher_reference,teacher_name,teacher_contact,date_stamp,time_stamp,teacher_status,date_stamp_,incharge) VALUES(?,?,?,?,?,?,?,?)",
                        (teacher[0],teacher[1],teacher[2],teacher[4],teacher[5],teacher[6],transform_date,teacher[3]))
                        db.commit()
                        self.ui.batch_notification.setText("Please records are been inserted....")
                    self.ui.batch_notification.setText("Please records inserted successfully....")
                        
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! provide a file to load load from...")
            self.alert.show() 
        
    def load_batch_data(self):
        file_type = "CSV Files(*.csv)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Users\\BTC OMEN\\Documents",file_type)
        if path:
            self.ui.batch_filename.setText(path[0])
            try:
                results_list = []
                with open(path[0],'r') as filename:
                    data=csv.reader(filename)
                    next(data)
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    for teacher in data:
                        time = teacher[5].split(':')
                        time_zone =time[1].split(' ')
                        time_transform = time[0]+':'+time_zone[0]+':'+'00 '+time_zone[1]
                        teacher[5] = time_transform
                        batch_hour = self.ui.batch_hour.value()
                        batch_minute = self.ui.batch_minutes.value()
                        batch_zone = self.ui.batch_time_zone.currentText()
                        if str(time[0])<=str(batch_hour) and str(time[1])<=str(batch_minute) and str(batch_zone)==str(time_zone[1]):
                            teacher.append("Early")
                        else:
                            teacher.append("Late")
                        results_list.append(teacher)
                        self.batch_table(results_list)
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()

    def batch_table(self, details:list):
        self.ui.batch_tableWidget.setAutoScroll(True)
        self.ui.batch_tableWidget.setAutoScrollMargin(2)
        self.ui.batch_tableWidget.setTabKeyNavigation(True)
        self.ui.batch_tableWidget.setColumnWidth(0,140)
        self.ui.batch_tableWidget.setColumnWidth(1,270)
        self.ui.batch_tableWidget.setColumnWidth(2,140)
        self.ui.batch_tableWidget.setColumnWidth(3,270)
        self.ui.batch_tableWidget.setColumnWidth(4,190)
        self.ui.batch_tableWidget.setColumnWidth(5,190)
        self.ui.batch_tableWidget.setColumnWidth(6,140)
        self.ui.batch_tableWidget.setRowCount(len(details))
        self.ui.batch_tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.batch_tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[0])))
            self.ui.batch_tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            self.ui.batch_tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[2])))
            self.ui.batch_tableWidget.setItem(row_count,3,QTableWidgetItem(str(data[3])))
            self.ui.batch_tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[4])))
            self.ui.batch_tableWidget.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.ui.batch_tableWidget.setItem(row_count,6,QTableWidgetItem(str(data[6])))
            row_count = row_count+1

    def load_data(self):
        file_type = "CSV Files(*.csv)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Documents",file_type)
        if path:
            try:
                self.ui.summary_browse.setText(os.path.basename(str(path[0])))
                with open(path[0],'r') as data:
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    student_data = csv.reader(data)
                    next(student_data)
                    teacher_list = []
                    for row in student_data:
                        teacher_list.append(row)
                    if len(teacher_list):
                        self.summary_table(teacher_list)
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"))
                self.alert.show()
            return path[0]
        pass

    def export_summary_data(self):
        table=self.ui.tableWidget_summary.item(0,0)
        filename = self.ui.summary_filename.text()
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\csv_export\\'+filename+date+'.csv'
        if table and filename:
            details=self.query_summary_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Teacher Name','Teacher Contact','Anticipative Date stamp','Anticipative Time stamp','Dilatory Date stamp','Dilatory Time stamp','Early count','Late count','Total count'])
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export\nor provide filename...")
            self.alert.show()
        
    def render_teacher_data(self):
        self.summary_table(self.query_summary_data())

    def query_summary_data(self):
        self.ui.database_summary.clear()
        self.ui.database_summary.addItems(self.get_tables())
        table_name = self.ui.database_summary.currentText()
        results= self.query_database("SELECT DISTINCT teacher_reference FROM "+table_name)
        data = []
        early = []
        late = []
        transform = []
        early_data = []
        late_data = []
        for teacher_reference in range(len(results)):
            teacher_list= self.query_database("SELECT teacher_name,teacher_contact,COUNT(teacher_status) as active FROM "+table_name+" WHERE teacher_reference="+results[teacher_reference][0]+" ORDER BY teacher_name DESC")
            early_status= self.query_database("SELECT COUNT(teacher_status) as active FROM "+table_name+" WHERE teacher_reference="+results[teacher_reference][0]+" and teacher_status='Early'"+" ORDER BY teacher_name DESC")
            late_status= self.query_database("SELECT COUNT(teacher_status) as active FROM "+table_name+" WHERE teacher_reference="+results[teacher_reference][0]+" and teacher_status='Late'"+" ORDER BY teacher_name DESC")
            early_result = self.query_database("SELECT date_stamp_,time_stamp FROM "+table_name+" WHERE teacher_reference="+results[teacher_reference][0]+" ORDER BY time_stamp ASC LIMIT 1")
            late_result = self.query_database("SELECT date_stamp_,time_stamp FROM "+table_name+" WHERE teacher_reference="+results[teacher_reference][0]+" ORDER BY time_stamp DESC LIMIT 1")
            data.append(teacher_list[0])
            early.append(early_status[0])
            late.append(late_status[0])
            early_data.append(early_result[0])
            late_data.append(late_result[0])
    
        for item in data:
            transform.append([str(item[0]),str(item[1]),str(early_data[data.index(item)][0]),
                str(early_data[data.index(item)][1]),str(late_data[data.index(item)][0]),
                str(late_data[data.index(item)][1]),str(early[data.index(item)][0]),
                str(late[data.index(item)][0]),str(item[2])])
        return transform

    def summary_table(self,details:list):
        self.ui.tableWidget_summary.setAutoScroll(True)
        self.ui.tableWidget_summary.setAutoScrollMargin(2)
        self.ui.tableWidget_summary.setTabKeyNavigation(True)
        self.ui.tableWidget_summary.setColumnWidth(0,270)
        self.ui.tableWidget_summary.setColumnWidth(2,180)
        self.ui.tableWidget_summary.setColumnWidth(3,120)
        self.ui.tableWidget_summary.setColumnWidth(4,180)
        self.ui.tableWidget_summary.setColumnWidth(5,120)
        self.ui.tableWidget_summary.setColumnWidth(6,120)
        self.ui.tableWidget_summary.setColumnWidth(7,120)
        self.ui.tableWidget_summary.setColumnWidth(8,110)
        self.ui.tableWidget_summary.setRowCount(len(details))
        self.ui.tableWidget_summary.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget_summary.setItem(row_count,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_summary.setItem(row_count,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.ui.tableWidget_summary.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.ui.tableWidget_summary.setItem(row_count,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.ui.tableWidget_summary.setItem(row_count,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_summary.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.ui.tableWidget_summary.setItem(row_count,6,QtWidgets.QTableWidgetItem(str(data[6])))
            self.ui.tableWidget_summary.setItem(row_count,7,QtWidgets.QTableWidgetItem(str(data[7])))
            self.ui.tableWidget_summary.setItem(row_count,8,QtWidgets.QTableWidgetItem(str(data[8])))
            row_count = row_count+1

    def read_only_property(self):
        if self.ui.read_only_property.isChecked():
            self.ui.late_hour.setReadOnly(True)
            self.ui.late_minutes.setReadOnly(True)  
        else:
            self.ui.late_hour.setReadOnly(False)
            self.ui.late_minutes.setReadOnly(False)
       
    def refresh_tables(self):
        self.ui.database_tables.clear()
        self.ui.database_tables.addItems(self.get_tables())

    def create_database(self):
        con = sqlite3.connect(self.get_path())
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tb_attendance(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,teacher_reference TEXT,teacher_name TEXT, teacher_contact TEXT,date_stamp TEXT, time_stamp TEXT,teacher_status TEXT,date_stamp_ TEXT,incharge TEXT)")  
        con.commit()

    def get_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\database\\attendance_system.db'

    def get_tables(self):
        con = sqlite3.connect(self.get_path())
        cursor = con.cursor()
        sql = """SELECT name FROM sqlite_master WHERE type = 'table';"""
        my_cursor = cursor.execute(sql)
        my_cursor=my_cursor.fetchall()
        details = [v[0] for v in my_cursor if v[0] !='sqlite_sequence']
        return details

    def backup_history(self):
        path =Path('C:\\ProgramData\\iAttend\\data\\backup\\backup_history.txt')
        path.touch(exist_ok=True)
        file = open(path)
        time =dt.now().time().strftime('%I:%M:%S %p')
        date=dt.now().date().strftime('%a %b %d %Y')
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n{date},{time}')
            file.close()         

    def backup_database(self):
        path='C:\\ProgramData\\iAttend\\data\\backup'
        db_path = self.get_path()
        if os.path.exists(path):
            shutil.copy2(db_path,path)
            self.backup_history()
            self.alert = AlertDialog()
            self.alert.content("Database successfully backed up...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! something went wrong.....")
            self.alert.show()

    def get_dept_program(self,table:str):
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        cursor.execute("SELECT * FROM "+table)
        details = []
        cursor = cursor.fetchall()
        if cursor:
            for item in cursor:
                details.append(item[1])
            db.commit()
            return details

    def clear_camera_comboBoxes(self):
        self.ui.comboBox.clear()

    def get_active_cameras(self,camera:list):
        self.ui.comboBox.addItems(camera)
        count = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
        self.ui.scan_range_label.setText("Active camera(s): "+str(len(count)))
        self.ui.label_notification.setText("Done scanning for available cameras...")           

    def camera_thread(self):
        scan_range = self.ui.scan_range.text()
        if scan_range:
            self.clear_camera_comboBoxes()
            self.ui.scan_range_label.setText('')
            self.active = ActiveCameras(scan_range)
            self.active.start()
            self.active.cameras.connect(self.get_active_cameras)
            self.ui.label_notification.setText("Scanning for available cameras...")
        else:
            self.alert_builder("Oops! no scan range provided...")
    
    def alert(self, content:str):
        self.alert = AlertDialog()
        self.alert.content(content)
        self.alert.show()
           
    def create_program_data_dir(self):
        root_dir = 'C:\\ProgramData\\iAttend\\data'
        list =('csv_export','backup','QR_Codes','email_details','database','images')
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        for item in list:
            path = os.path.join(root_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        self.create_files()

    def create_files(self):
        details_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\detail.txt')
        details_path.touch(exist_ok=True)
        d_file = open(details_path)
        if os.path.exists(details_path):
            with open(details_path,'a+') as d_file:
                if os.path.getsize(details_path)==0:
                    d_file.write("Subject,example@gmail.mail,Sender,Password")
            d_file.close() 

        content = """
        Hello name,
                Please attached to this message is your
            attendance code. Please keep it safe as you 
            will need this everytime you would want to 
            access the facility. 
                Attend Today, Acheive Tomorrow!
                                            Thank you! """
        content_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\content.txt')
        content_path.touch(exist_ok=True)
        content_file = open(content_path)
        if os.path.exists(content_path):
            with open(content_path,'a+') as content_file:
                if os.path.getsize(content_path)==0:
                    content_file.write(content)
            content_file.close() 

        report_content = """
        Hello name,
    	        Please attached to this message is the
            report or data you requested for. Feel free 
            to contact us for our services at anytime.
                                        Thank you! """
        content_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\content_report.txt')
        content_path.touch(exist_ok=True)
        content_file = open(content_path)
        if os.path.exists(content_path):
            with open(content_path,'a+') as content_file:
                if  os.path.getsize(content_path)==0:
                    content_file.write(report_content)
            content_file.close()

    def export_data_to_csv(self):
        table=self.ui.tableWidget.item(0,0)
        filename = self.ui.filename.text()
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\csv_export\\'+filename+date+'.csv'
        if table and filename:
            details=self.query_database_for_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Reference','Name','Contact','Date_Stamp','Time_Stamp','Status'])
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export\nor provide filename...")
            self.alert.show()
        
    def query_database(self, query: str):
        db = sqlite3.connect(self.get_path())
        my_cursor = db.cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def ui_table(self, details: list):
        self.ui.tableWidget.setAutoScroll(True)
        self.ui.tableWidget.setAutoScrollMargin(2)
        self.ui.tableWidget.setTabKeyNavigation(True)
        self.ui.tableWidget.setColumnWidth(1,230)
        self.ui.tableWidget.setRowCount(len(details))
        self.ui.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[1])))
            self.ui.tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[2])))
            self.ui.tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[3])))
            self.ui.tableWidget.setItem(row_count,3,QTableWidgetItem(str(data[7])))
            self.ui.tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[5])))
            self.ui.tableWidget.setItem(row_count,5,QTableWidgetItem(str(data[6])))
            self.ui.tableWidget.setItem(row_count,6,QTableWidgetItem(str(data[8])))
            row_count = row_count+1
    
    def fetch_details_for_card_view(self):
        try:
            table = self.ui.database_tables.currentText()
            results=self.query_database("SELECT * FROM "+table+" WHERE teacher_reference="+str(self.ui.search_box.text()))
            self.ui_table(results)
            if self.ui.search_box.text():
                db_data=self.fetch_data_from_db(self.ui.search_box.text())
                if len(db_data) > 0:
                    helper = str(db_data[2]).split(" ")
                    self.ui.db_firstname.setText(helper[0])
                    self.ui.db_middlename.setText(helper[1])
                    self.ui.db_lastname.setText(helper[2])
                    self.ui.db_refrence.setText(str(db_data[1]))
                    self.ui.db_contact.setText(str(db_data[3]))
                    self.ui.status.setText(str(db_data[6]))
                    self.ui.db_incharge.setText(db_data[8]) 
                    self.ui.db_image_data.setPixmap(QPixmap.fromImage(self.resource_path(r'image.jpg')))
                    self.ui.db_image_data.setScaledContents(True)  
                else:
                    self.alert_builder("Details not found. Please enter\nyour details to register!")
                
            else:
                self.alert_builder("Oops! search field can't be empty.")
        except:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid search parameter...")
            self.alert.show()
    
    def fetch_data_from_db(self,reference):
        db = sqlite3.connect(self.get_path())
        my_cursor = db.cursor()
        table = self.ui.database_tables.currentText()
        detail =my_cursor.execute("SELECT * FROM "+table+" WHERE teacher_reference="+reference)
        detail= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
        return db_data

    def query_database_for_data(self):
        table = self.ui.database_tables.currentText()
        if self.ui.db_start_date.text():
            current_date = self.ui.db_start_date.text()
            current_date = "\'{}\'".format(current_date)
            results = self.query_database("SELECT * FROM "+table+" WHERE date_stamp ="+current_date)
            details = self.query_database("SELECT teacher_reference,teacher_name,teacher_contact,date_stamp_,time_stamp,teacher_status FROM "+table+" WHERE date_stamp ="+current_date)
            self.ui_table(results)
            return details
        elif self.ui.search_box.text():
            self.fetch_details_for_card_view()
            details=self.query_database("SELECT teacher_reference,teacher_name,teacher_contact,date_stamp_,time_stamp,teacher_status FROM "+table+" WHERE teacher_reference="+str(self.ui.search_box.text()))
            return details
        else:
            details=self.query_database("SELECT * FROM "+table)
            results=self.query_database("SELECT teacher_reference,teacher_name,teacher_contact,date_stamp_,time_stamp,teacher_status FROM "+table)
            self.ui_table(details)
            return results                        

    def get_date_on_search_page(self):
        date = self.ui.calendarWidget.selectedDate()
        self.ui.db_start_date.setText(str(date.toPython()))
   
    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
        
    def loadUi_file(self):
        self.ui.firstname.setText("Firtname")
        self.ui.middlename.setText("Middlename")
        self.ui.lastname.setText("Lastname")
        self.ui.refrence.setText("Refrence")
        self.ui.contact.setText("Contact")
        self.ui.incharge.setText("Incharge")
        self.ui.status.setText("Status")
        self.ui.image.setPixmap(u":/icons/asset/image.svg")
        self.ui.image.setScaledContents(False)
        self.ui.label_notification.setText("Notification")

    def retreive_student_details(self,data):
        data= json.loads(data)
        self.ui.firstname.setText(data['firstname'])
        self.ui.middlename.setText(data['middlename'])
        self.ui.lastname.setText(data['lastname'])
        self.ui.refrence.setText(str(data['reference']))
        self.ui.contact.setText(str(data['contact']))
        self.ui.incharge.setText(data['incharge'])
        self.ui.image.setPixmap(QPixmap.fromImage(self.resource_path(r'image.jpg')))
        self.ui.image.setScaledContents(True)
                        
    def mark_attendance_db(self):
        db = sqlite3.connect(os.path.abspath(self.get_path()))
        my_cursor = db.cursor()
        table = self.ui.database_tables.currentText()
        name = self.ui.firstname.text()+" "+self.ui.middlename.text()+" "+self.ui.lastname.text()
        hour=int(dt.now().time().strftime("%I"))
        minute=int(dt.now().time().strftime("%M"))
        type=str(dt.now().time().strftime("%p"))
        late_hour=self.ui.late_hour.value()
        late_minute=self.ui.late_minutes.value()
        
        if hour<=late_hour and minute<=late_minute and type == self.ui.time_zone.currentText():
            self.ui.status.setText("Early")
        else:
            self.ui.status.setText("Late")
            
        attendance = Attendance(
            self.ui.refrence.text(),
            name,
            self.ui.contact.text(),
            str(dt.now().date().strftime("%Y-%m-%d")),
            str(dt.now().time().strftime("%I:%M:%S %p")),
            self.ui.status.text(),
            self.ui.incharge.text(),
            str(dt.now().date().strftime("%a, %b %d, %Y")),
        )
        details = []
        date="\'{}\'".format(dt.now().date().strftime("%Y-%m-%d"))
        if self.ui.refrence.text() != "Reference" and self.ui.refrence.text() !="" :
            data=my_cursor.execute("SELECT teacher_reference,date_stamp FROM "+table+" WHERE teacher_reference="+self.ui.refrence.text()+" and date_stamp="+date)
            data=my_cursor.fetchone()
            if data:
                for detail in data:
                    details.append(detail)
                db.commit() 
            if not details:
                my_cursor.execute("INSERT INTO "+table+"(teacher_reference,teacher_name,teacher_contact,date_stamp,time_stamp,teacher_status,incharge,date_stamp_) VALUES(?,?,?,?,?,?,?,?)",
                (attendance.t_reference,attendance.t_name,attendance.t_contact,attendance.date,attendance.time_in,attendance.t_status,attendance.t_incharge,attendance.date_))
                db.commit()
            elif details:
                winsound.Beep(1000,100)
                self.show_info("Attendance taken, you can proceed!\nNext person please...")
            else:
                self.show_info("Oops! something went wrong...")
        db.close()
 
    def start_webcam(self):
        if self.ui.camera_ip.text() or self.ui.comboBox.currentText():
            ip_address = self.ui.camera_ip.text()
            system_attached_camera = self.ui.comboBox.currentText()
            self.network_capture = VideoCapture(ip_address)
            camera_id = int(system_attached_camera)
            self.system_capture = VideoCapture(camera_id)

            if ip_address:  
                if self.network_capture is None or not self.network_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(ip_address)
                
            elif system_attached_camera:       
                if self.system_capture is None or not self.system_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id) 
                        
            elif self.system_capture.isOpened() and self.network_capture.isOpened():
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id)

            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.saveTimer.timeout.connect(self.update_frame)
            self.saveTimer.start(3)
        else:
            self.show_alert = AlertDialog()
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()

    def update_frame(self):

        thickness = 2
        rect_thickness = 1
        color = (255,255,0)
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.beta = int(self.ui.brightness_value.text())
        self.apha = int(self.ui.contrast_value.text())*0.01
        self.kernel = (int(self.ui.sharp_value.text())*0.01, int(self.ui.sharp_value.text())*0.01)
       
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.ones(self.frame.shape, self.frame.dtype), 0, self.beta)
        self.read_only_property()
        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.now = dt.now()
        self.now = self.now.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.now,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        for qr_code in decode(self.result):
            qr_code_data  = qr_code.data.decode('utf-8')
            pts = np.array([qr_code.polygon], np.int)
            rect = np.array([qr_code.rect], np.int)
            pts = pts.reshape((-1, 1, 2))   
            # cv2.polylines(frame, [pts], True,color,1)
            for x,y,w,h in rect:
                w , h =x+w, y+h
                cv2.rectangle(self.result, (x,y), (w,h), color, rect_thickness)
                cv2.line(self.result,(x,y),(x+15,y),color,thickness)
                cv2.line(self.result,(x,y),(x,y+15),color,thickness)
                cv2.line(self.result,(w,y),(w-15,y),color,thickness)
                cv2.line(self.result,(w,y),(w,y+15),color,thickness)
                cv2.line(self.result,(x,h),(x+15,h),color,thickness)
                cv2.line(self.result,(x,h),(x,h-15),color,thickness)
                cv2.line(self.result,(w,h),(w-15,h),color,thickness)
                cv2.line(self.result,(w,h),(w,h-15),color,thickness)
            self.retreive_student_details(qr_code_data)
            self.mark_attendance_db()  
        self.display_feed(self.result,1)         
        
    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_view.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.camera_view.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        if self.saveTimer.isActive():
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui.camera_view.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui.camera_view.setScaledContents(False)
            self.saveTimer.stop() 
        else:
            self.show_alert.content("Oops! you have no active camera\nto disconnect from.") 
            self.show_alert.show()  

    def show_info(self, content:str):
        self.ui.label_notification.setText(content)       

    def update_brigthness(self, value):
        self.ui.brightness_value.setText(str(value))
        return value 

    def update_sharpness(self, value):
        self.ui.sharp_value.setText(str(value))
        return value

    def update_contrast(self, value):
        self.ui.contrast_value.setText(str(value))
        return value     
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()    
 
   
class Splash_screen(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_MainWindow()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop() 
            self.close() 
            self.main = MainWindow()
            self.main.show()        
        counter +=1

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Splash_screen()  
    sys.exit(application.exec_()) 