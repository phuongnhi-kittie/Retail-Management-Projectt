from PyQt6.QtWidgets import QMessageBox

from DAL.UserDAL import EmployeeDAL
from model.Employee import Employee
from ui.AddEmployee import Ui_MainWindow
class AddEmployeeExt(Ui_MainWindow):
    def __init__(self):
        self.emp_dal = EmployeeDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonAdd.clicked.connect(self.add_new_emp)
        self.pushButtonClear.clicked.connect(self.clear)
        self.pushButtonLogout.clicked.connect(self.logout)
    def add_new_emp(self):
        id = f"emp{len(self.emp_dal.get_all_employee()) + 1}"
        name = self.lineEditEmployeeName.text()
        phone = self.lineEditContactNo.text()
        designation = self.comboBoxDesignation.currentText()
        address = self.lineEditAdress.text()
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        new_emp = Employee(id=id, name=name, phone=phone, designation=designation, address=address, username=username, password=password)
        self.emp_dal.store_new_employee(new_emp)
        msg = QMessageBox()
        msg.setText("Add new employee successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def clear(self):
        self.lineEditEmployeeName.setText("")
        self.lineEditContactNo.setText("")
        self.lineEditAdress.setText("")
        self.lineEditUserName.setText("")
        self.lineEditPassword.setText("")
    def logout(self):
        self.MainWindow.close()