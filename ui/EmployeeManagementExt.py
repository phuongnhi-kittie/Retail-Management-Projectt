import traceback

from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox

from DAL.UserDAL import EmployeeDAL
from model.Employee import Employee
from ui.AddEmployeeExt import AddEmployeeExt
from ui.Employeemanagement import Ui_MainWindow
from ui.UpdateEmployeeExt import UpdateEmployeeExt


class EmployeeManagement(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.emp_dal = EmployeeDAL()
        self.add_emp_window = None
        self.update_emp_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.display()
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.logout)
        self.pushButtonAddEmployee.clicked.connect(self.add_emp)
        self.pushButtonUpdateEmployee.clicked.connect(self.update_emp)
        self.pushButtonDeleteEmployee.clicked.connect(self.delete_emp)
        self.pushButtonExit.clicked.connect(self.logout)
        self.tableWidgetEmployee.itemSelectionChanged.connect(self.choose_emp)
    def choose_emp(self):
        if self.is_completed==False:
            return
        row = self.tableWidgetEmployee.currentRow()
        column_id = self.tableWidgetEmployee.item(row, 0)
        self.lineEditEmployeeID.setText(column_id.text())
    def add_emp(self):
        AddEmpWindow = QMainWindow()
        self.add_emp_window = AddEmployeeExt()
        self.add_emp_window.setupUi(AddEmpWindow)
        self.add_emp_window.showWindow()
    def update_emp(self):
        try:
            if self.is_completed == False:
                return
            row = self.tableWidgetEmployee.currentRow()
            column_id = self.tableWidgetEmployee.item(row, 0)
            column_name = self.tableWidgetEmployee.item(row, 1)
            column_phone = self.tableWidgetEmployee.item(row, 2)
            column_address = self.tableWidgetEmployee.item(row, 3)
            column_username = self.tableWidgetEmployee.item(row, 4)
            column_password = self.tableWidgetEmployee.item(row, 5)
            column_designation = self.tableWidgetEmployee.item(row, 6)
            emp_update = Employee(id = column_id.text(), name=column_name.text(), phone=column_phone.text(), address=column_address.text(), designation=column_designation.text(), username=column_username.text(), password=column_password.text())
            UpdateEmpWindow = QMainWindow()
            self.update_emp_window = UpdateEmployeeExt()
            self.update_emp_window.setupUi(UpdateEmpWindow)
            self.update_emp_window.emp_update = emp_update
            self.update_emp_window.showWindow()
        except:
            traceback.print_exc()
    def delete_emp(self):
        id = self.lineEditEmployeeID.text()
        self.emp_dal.delete_emp(id)
        msg = QMessageBox()
        msg.setText("Delete employee successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def logout(self):
        self.MainWindow.close()
    def display(self):
        self.is_completed = False
        list_emp = self.emp_dal.get_all_employee()
        self.tableWidgetEmployee.setRowCount(0)
        for i in range(len(list_emp)):
            self.tableWidgetEmployee.insertRow(i)
            emp_i = list_emp[i]
            column_id = QTableWidgetItem(emp_i.id)
            column_name = QTableWidgetItem(emp_i.name)
            column_phone = QTableWidgetItem(emp_i.phone)
            column_designation = QTableWidgetItem(emp_i.designation)
            column_address = QTableWidgetItem(emp_i.address)
            column_username = QTableWidgetItem(emp_i.username)
            column_password = QTableWidgetItem(emp_i.password)
            self.tableWidgetEmployee.setItem(i, 0, column_id)
            self.tableWidgetEmployee.setItem(i, 1, column_name)
            self.tableWidgetEmployee.setItem(i, 2, column_phone)
            self.tableWidgetEmployee.setItem(i, 3, column_address)
            self.tableWidgetEmployee.setItem(i, 4, column_username)
            self.tableWidgetEmployee.setItem(i, 5, column_password)
            self.tableWidgetEmployee.setItem(i, 6, column_designation)
        self.is_completed = True