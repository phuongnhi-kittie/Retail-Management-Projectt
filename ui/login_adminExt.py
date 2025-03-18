import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from DAL.UserDAL import EmployeeDAL
from ui.AdminWindowExt import AdminWindowExt
from ui.login_admin import Ui_MainWindow
class login_adminExt(Ui_MainWindow):
    def __init__(self):
        self.emp_dal = EmployeeDAL()
        self.admin_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonBack.clicked.connect(self.process_back)
        self.pushButtonLogin.clicked.connect(self.login_admin)
    def login_admin(self):
        try:
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()
            list_emp = self.emp_dal.get_all_employee()
            login_emp = None
            for emp in list_emp:
                if emp.username == username and emp.password == password and (emp.designation == "System Administrator (IT Manager)" or emp.designation == "Accountant" or emp.designation == "Store Manager"):
                    login_emp = emp
                    break
            if login_emp != None:
                msg = QMessageBox()
                msg.setWindowTitle("Announcement")
                msg.setText("Login successfully")
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                button = msg.exec()
                if button == QMessageBox.StandardButton.Ok:
                    AdminWindow = QMainWindow()
                    self.admin_window = AdminWindowExt()
                    self.admin_window.setupUi(AdminWindow)
                    self.admin_window.current_emp = login_emp
                    self.admin_window.showWindow()
                    self.MainWindow.close()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Login failed")
                    msg.exec()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Login failed")
                msg.exec()
        except:
            traceback.print_exc()
    def process_back(self):
        from ui.MainWindowExt import MainWindowExt  # Import ở đây để tránh vòng lặp
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()