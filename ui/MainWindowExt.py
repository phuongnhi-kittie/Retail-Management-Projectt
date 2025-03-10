from ui.login_adminExt  import login_adminExt
from ui.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from ui.login_employeeExt import login_employeeExt
class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonAdmin.clicked.connect(self.admin)
        self.pushButtonEmployee.clicked.connect(self.employee)

    def admin(self):
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = login_adminExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def employee(self):
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = login_employeeExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()



