from ui.BillingSystem import Ui_MainWindow
from ui.login_employeeExt import login_employeeExt
from PyQt6.QtWidgets import QMainWindow

class BillingSystemExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.conncet(self.process_logout) #back to login_emp
    def process_logout(self):
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = login_employeeExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
