from PyQt5 import QtWidgets
from LoginPage import Ui_LoginWindow
from MainPage import Ui_MainWindow
from Settings import Ui_SettingsWindow
from PyQt5.QtCore import QDate
import config.database as ch

class Controller:
    def __init__(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        #self.LoginWindow = QtWidgets.QMainWindow()
        self.MainWindow = QtWidgets.QMainWindow()
        self.SettingsWindow = QtWidgets.QMainWindow()
        
        # self.uiLogin = Ui_LoginWindow()
        # self.uiLogin.setupUi(self.LoginWindow)
        # self.uiLogin.ButtonMenu_6.clicked.connect(self.loggedin)
        # self.uiLogin.ButtonMainPage.clicked.connect(self.showMainWindow)

        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.MainWindow)
        
        self.uisetting = Ui_SettingsWindow()
        self.uisetting.setupUi(self.SettingsWindow)
        self.uisetting.pblogout.clicked.connect(self.loggedout)
        
    def loggedin(self):
        if self.uiLogin.validate():
            self.uiLogin.ButtonMenu_6.clicked.connect(self.showMainWindow)
            self.showMainWindow()
            
    def loggedout(self):
        if self.uisetting.sessionLogOut():
            # self.uiLogin.LineEdit_Label_1_Username.clear()
            # self.uiLogin.LineEdit_Label_1_Password.clear()
            self.uisetting.pblogout.clicked.connect(self.showLoginWindow)
            self.showLoginWindow()
        
    def showLoginWindow(self):
        self.MainWindow.close()
        self.SettingsWindow.close()
        self.LoginWindow = QtWidgets.QMainWindow()
        self.uiLogin = Ui_LoginWindow()
        self.uiLogin.setupUi(self.LoginWindow)
        self.uiLogin.ButtonMenu_6.clicked.connect(self.loggedin)
        self.uiLogin.ButtonMainPage.clicked.connect(self.showMainWindow)
        self.LoginWindow.show()
        
        
    def showMainWindow(self):
        if self.LoginWindow:
            self.LoginWindow.close()
            self.LoginWindow=None
        self.SettingsWindow.close()
        self.MainWindow.show()
        self.uiMain.ButtonMenu.clicked.connect(self.showSettingsWindow)
        self.uiMain.ButtonPLU.clicked.connect(self.showSettingsWindow)
       # self.uisetting.tabWidget.setCurrentWidget(self.uisetting.tab_2)
        
        
    def showSettingsWindow(self):
        #self.LoginWindow.close()
        self.MainWindow.close()
        self.SettingsWindow.show()
        if self.uiMain.ButtonPLU.isChecked():
            self.uisetting.product_code.setText(self.uiMain.product_code.currentText())
            self.uisetting.showpludetails()
            self.uiMain.ButtonPLU.setChecked(False)
        if self.uiMain.ButtonMenu.isChecked():
            self.uisetting.newProduct()
            self.uiMain.ButtonMenu.setChecked(False)
        self.uisetting.tab11exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab21exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab22exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab31exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab41exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab51exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab61exit.clicked.connect(self.showMainWindow)
        self.uisetting.tab71exit.clicked.connect(self.showMainWindow)
        

    def globalupdate(self):
        ch.pluflag=1
        
    def run(self):
        self.showLoginWindow()
        self.app.exec_()
        
        
if __name__ == "__main__":
    controller = Controller()
    controller.run()