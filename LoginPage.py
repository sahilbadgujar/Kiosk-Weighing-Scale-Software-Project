from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from config.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from config.database import con
import os
from PyQt5.QtCore import Qt
import sys
import config.database as cu 


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        #LoginWindow.setWindowFlags(Qt.FramelessWindowHint)
        LoginWindow.setAttribute(Qt.WA_DeleteOnClose)
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        LoginWindow.setMinimumSize(QtCore.QSize(SCREEN_WIDTH, SCREEN_HEIGHT))
        LoginWindow.setMaximumSize(QtCore.QSize(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LineEdit_Label_1_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_Label_1_Username.setGeometry(QtCore.QRect(440, 240, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LineEdit_Label_1_Username.setFont(font)
        self.LineEdit_Label_1_Username.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(192, 191, 188)"
        )

        self.Label_Username = QtWidgets.QLabel(self.centralwidget)
        self.Label_Username.setGeometry(QtCore.QRect(440, 291, 411, 15))
        
        self.LineEdit_Label_1_Username.setObjectName("LineEdit_Label_1_Value_4")
        self.LineEdit_Label_1_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_Label_1_Password.setGeometry(QtCore.QRect(440, 325 , 411, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LineEdit_Label_1_Password.setFont(font)
        self.LineEdit_Label_1_Password.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(192, 191, 188)"
        )
        self.LineEdit_Label_1_Password.setObjectName("LineEdit_Label_1_Value")

        self.Label_Password = QtWidgets.QLabel(self.centralwidget)
        self.Label_Password.setGeometry(QtCore.QRect(440, 376, 411, 15))
        
        self.Visibility_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Visibility_Button.setGeometry(QtCore.QRect(800,325,50,50))
        self.Visibility_Button.setCheckable(True)
        self.Visibility_Button.setStyleSheet("border:none;" "background-color:transparent;" "hover{" "background-color:lightgrey;" "}")
        eye_path = os.path.join(os.path.dirname(__file__), "config", "Images", "eye_off.png")
        self.Visibility_Button.setIcon(QtGui.QIcon(eye_path))
        self.Visibility_Button.clicked.connect(self.toggle_visibility_button)
        self.Visibility_Button.setIconSize(QtCore.QSize(50, 50))
    

        #self.LineEdit_Label_1_Value_2 = QtWidgets.QLineEdit(self.centralwidget)
        #self.LineEdit_Label_1_Value_2.setGeometry(QtCore.QRect(440, 340, 411, 31))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        #self.LineEdit_Label_1_Value_2.setFont(font)
        #self.LineEdit_Label_1_Value_2.setStyleSheet(
        #   "color: rgb(0, 0, 0);\n" "background-color: rgb(192, 191, 188)"
        #)
        #self.LineEdit_Label_1_Value_2.setObjectName("LineEdit_Label_1_Value_2")

        # self.LineEdit_Label_1_Value_3 = QtWidgets.QLineEdit(self.centralwidget)
        # self.LineEdit_Label_1_Value_3.setGeometry(QtCore.QRect(440, 380, 411, 31))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.LineEdit_Label_1_Value_3.setFont(font)
        # self.LineEdit_Label_1_Value_3.setStyleSheet(
        #     "color: rgb(0, 0, 0);\n" "background-color: rgb(192, 191, 188)"
        # )
        # self.LineEdit_Label_1_Value_3.setObjectName("LineEdit_Label_1_Value_3")

        self.bShutdown = QtWidgets.QPushButton(self.centralwidget)
        self.bShutdown.setGeometry(QtCore.QRect(720, 460, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bShutdown.setFont(font)
        self.bShutdown.setStyleSheet(
            "background-color: rgb(255, 85, 0);\n"
            "border-style: outset;\n"
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: black;\n"
            "padding: 4px;"
        )
        self.bShutdown.clicked.connect(self.shutDown)
        self.bShutdown.setFlat(False)
        self.bShutdown.setObjectName("bShutdown")

        self.ButtonMainPage = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMainPage.setGeometry(QtCore.QRect(440, 460, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonMainPage.setFont(font)
        self.ButtonMainPage.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n"
            "border-style: outset;\n"
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: black;\n"
            "padding: 4px;"
        )
        self.ButtonMainPage.setFlat(False)
        self.ButtonMainPage.setObjectName("ButtonMainPage")

        self.ButtonMenu_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMenu_5.setGeometry(QtCore.QRect(580, 460, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonMenu_5.setFont(font)
        self.ButtonMenu_5.setStyleSheet(
            "background-color: rgb(255, 255, 0);\n"
            "border-style: outset;\n"
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: black;\n"
            "padding: 4px;"
        )
        self.ButtonMenu_5.setFlat(False)
        self.ButtonMenu_5.setObjectName("ButtonMenu_5")
        
        self.ButtonMenu_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMenu_6.setGeometry(QtCore.QRect(760, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonMenu_6.setFont(font)
        self.ButtonMenu_6.setStyleSheet(
            "background-color: rgb(170, 255, 255);\n"
            "border-style: outset;\n"
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: black;\n"
            "padding: 4px;"
        )
        self.ButtonMenu_6.setFlat(False)
        self.ButtonMenu_6.setObjectName("ButtonMenu_6")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        #self.LineEdit_Label_1_Value_2.setText(_translate("LoginWindow", "BALANCE123"))
        #self.LineEdit_Label_1_Value_2.setPlaceholderText(
        #   _translate("LoginWindow", "Enter Product Name")
        #)
        # self.LineEdit_Label_1_Value_3.setText(_translate("LoginWindow", "BALANCE123"))
        # self.LineEdit_Label_1_Value_3.setPlaceholderText(
        #     _translate("LoginWindow", "Enter Product Name")
        # )

        #username
        self.LineEdit_Label_1_Username.setText(
            _translate("LoginWindow", "")
        )
        self.LineEdit_Label_1_Username.setPlaceholderText(
            _translate("LoginWindow", "Enter Username")
        )
        username_regex = QtCore.QRegularExpression("^[a-zA-Z0-9]{5,}$")
        username_validator = QtGui.QRegularExpressionValidator(username_regex,self.LineEdit_Label_1_Username)
        self.LineEdit_Label_1_Username.setValidator(username_validator)
        #password
        self.LineEdit_Label_1_Password.setText(
            _translate("LoginWindow", "")
        )
        self.LineEdit_Label_1_Password.setPlaceholderText(
            _translate("LoginWindow", "Enter Password")
        )
        self.LineEdit_Label_1_Password.setEchoMode(QLineEdit.Password)
        password_regex = QtCore.QRegularExpression("^[a-zA-Z0-9@#$%^&*!.,+-]{5,}$")
        password_validator = QtGui.QRegularExpressionValidator(password_regex,self.LineEdit_Label_1_Password)
        self.LineEdit_Label_1_Password.setValidator(password_validator)


        self.bShutdown.setText(_translate("LoginWindow", "Shutdown"))
        self.ButtonMainPage.setText(_translate("LoginWindow", "Main page"))
        self.ButtonMenu_5.setText(_translate("LoginWindow", "Reboot"))
        
        self.ButtonMenu_6.setText(_translate("LoginWindow", "Login"))
        #if self.LineEdit_Label_1_Password.text():
        #self.ButtonMenu_6.clicked.connect(self.gotoscreen)
        #else:
        #   self.LineEdit_Label_1_Password.setToolTip("Password field is empty!")
  
    def validate(self):
        username_text=self.LineEdit_Label_1_Username.text()
        password_text=self.LineEdit_Label_1_Password.text()
        if self.LineEdit_Label_1_Username.hasAcceptableInput() and self.LineEdit_Label_1_Password.hasAcceptableInput():
            cur=con.cursor()
            q1="select password from user where username=%s"
            cur.execute(q1,(username_text,))
            data=cur.fetchone()
            if data==None:
                self.Label_Username.setText("No user found")
                self.Label_Username.setStyleSheet("color : red")
                font=QtGui.QFont()
                font.setBold(True)
                self.Label_Username.setFont(font)
            elif data[0] == password_text:
                self.Label_Username.setText("")
                self.Label_Password.setText("")
                self.LineEdit_Label_1_Username.clear()
                self.LineEdit_Label_1_Password.clear()
                q2="insert into session(username,status) values (%s, 'active')"
                cur.execute(q2,(username_text,))
                con.commit()
                cur.close()
                cu.current_user=username_text
                return True
            else:
                self.Label_Password.setText("Incorrect Password")
                self.Label_Password.setStyleSheet("color : red")
                font=QtGui.QFont()
                font.setBold(True)
                self.Label_Password.setFont(font)
        else:
            if not username_text:
                self.Label_Username.setText("*required")
                self.Label_Username.setStyleSheet("color : red")
                font=QtGui.QFont()
                font.setBold(True)
                self.Label_Username.setFont(font)
            else:
                self.Label_Username.setText("")
            if not password_text:
                self.Label_Password.setText("*required")
                font=QtGui.QFont()
                font.setBold(True)
                self.Label_Password.setFont(font)
                self.Label_Password.setStyleSheet("color : red")
            else:
                self.Label_Password.setText("")
            if username_text and password_text:
                if not self.LineEdit_Label_1_Username.hasAcceptableInput() and username_text:
                    self.Label_Username.setText("*Invalid Username")
                    self.Label_Username.setStyleSheet("color : red")
                    font=QtGui.QFont()
                    font.setBold(True)
                    self.Label_Username.setFont(font)
                else:
                    self.Label_Username.setText("")
                if not self.LineEdit_Label_1_Password.hasAcceptableInput() and password_text:
                    self.Label_Password.setText("*Invalid Password")
                    self.Label_Password.setStyleSheet("color : red")
                    font=QtGui.QFont()
                    font.setBold(True)
                    self.Label_Password.setFont(font)
                else:
                    self.Label_Password.setText("")
                    
                    
    def toggle_visibility_button(self):
        if self.Visibility_Button.isChecked():
            self.LineEdit_Label_1_Password.setEchoMode(QLineEdit.Normal)
            eye_path= os.path.join(os.path.dirname(__file__), "config", "Images", "eye.png")
            self.Visibility_Button.setIcon(QtGui.QIcon(eye_path))
        else:
            self.LineEdit_Label_1_Password.setEchoMode(QLineEdit.Password)
            eye_path= os.path.join(os.path.dirname(__file__), "config", "Images", "eye_off.png")
            self.Visibility_Button.setIcon(QtGui.QIcon(eye_path))

      
    def shutDown(self):
          sys.exit()             

'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())'''
