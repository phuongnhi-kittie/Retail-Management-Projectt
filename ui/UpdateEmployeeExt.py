from PyQt6.QtWidgets import QMessageBox

from DAL.UserDAL import EmployeeDAL
from model.Employee import Employee
from ui.UpdateEmployee import Ui_MainWindow
class UpdateEmployeeExt(Ui_MainWindow):
    def __init__(self):
        self.emp_update = None
        self.emp_dal = EmployeeDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.display()
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.logout)
        self.pushButtonAdd.clicked.connect(self.update_employee)
        self.pushButtonClear.clicked.connect(self.clear)
    def clear(self):
        self.lineEditEmployeeName.setText("")
        self.lineEditContactNo.setText("")
        self.lineEditAdress.setText("")
        self.lineEditUserName.setText("")
        self.lineEditPassword.setText("")
    def update_employee(self):
        id = self.emp_update.id
        name = self.lineEditEmployeeName.text()
        phone = self.lineEditContactNo.text()
        designation = self.comboBoxDesignation.currentText()
        address = self.lineEditAdress.text()
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        update_emp = Employee(id=id, name=name, phone=phone, designation=designation, address=address, username=username, password=password)
        self.emp_dal.update_new_employee(update_emp)
        msg = QMessageBox()
        msg.setText("Update employee successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def logout(self):
        self.MainWindow.close()
    def display(self):
        self.lineEditEmployeeName.setText(self.emp_update.name)
        self.lineEditContactNo.setText(self.emp_update.phone)
        self.lineEditUserName.setText(self.emp_update.username)
        self.lineEditPassword.setText(self.emp_update.password)
        self.lineEditAdress.setText(self.emp_update.address)
        self.comboBoxDesignation.setCurrentText(self.emp_update.designation)