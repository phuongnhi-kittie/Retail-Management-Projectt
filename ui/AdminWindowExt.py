from ui.AdminWindow import Ui_mainWindow
import traceback

from PyQt6.QtWidgets import QMainWindow
from ui.EmployeeManagementExt import EmployeeManagement
from ui.InventoryManagementExt import InventoryManagement
from ui.InvoicesMainExt import InvoiceMainExt
class AdminWindowExt(Ui_mainWindow):
    def __init__(self):
        self.current_emp = None
        self.inventory_window = None
        self.emp_window = None
        self.bill_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonEmployees.clicked.connect(self.process_emp)
        self.pushButtonInventory.clicked.connect(self.process_inventory)
        self.pushButtonInvoices.clicked.connect(self.process_invoices)
        self.pushButtonLogout.clicked.connect(self.logout)
    def logout(self):
        self.MainWindow.close()
    def process_emp(self):
        EmpWindow = QMainWindow()
        self.emp_window = EmployeeManagement()
        self.emp_window.setupUi(EmpWindow)
        self.emp_window.current_user = self.current_emp
        self.emp_window.showWindow()
    def process_inventory(self):
        InventoryWindow = QMainWindow()
        self.inventory_window = InventoryManagement()
        self.inventory_window.setupUi(InventoryWindow)
        self.inventory_window.current_user = self.current_emp
        self.inventory_window.showWindow()
    def process_invoices(self):
        try:
            InvoiceWindow = QMainWindow()
            self.bill_window = InvoiceMainExt()
            self.bill_window.setupUi(InvoiceWindow)
            self.bill_window.current_user = self.current_emp
            self.bill_window.show()
        except:
            traceback.print_exc()