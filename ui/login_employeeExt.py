import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from DAL.UserDAL import EmployeeDAL
from ui.BillingSystemExt import BillingSystemExt
from ui.login_employee import Ui_MainWindow
class login_employeeExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.emp_dal = EmployeeDAL()
        self.billing_system_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonBack.clicked.connect(self.process_back)
        self.pushButtonLogin.clicked.connect(self.login_employee)
    def login_employee(self):
        try:
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()
            list_emp = self.emp_dal.get_all_employee()
            login_emp = None
            for emp in list_emp:
                if emp.username == username and emp.password == password and emp.designation == "Employee":
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
                    # Tạo cửa sổ bán hàng
                    self.billing_system_window = QMainWindow()
                    self.billing_ui = BillingSystemExt(self)  # Truyền login_employeeExt vào BillingSystemExt
                    self.billing_ui.setupUi(self.billing_system_window)
                    self.billing_ui.current_emp = login_emp
                    self.billing_ui.showWindow()
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
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def process_back(self):
        from ui.MainWindowExt import MainWindowExt  # Import ở đây để tránh vòng lặp
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()