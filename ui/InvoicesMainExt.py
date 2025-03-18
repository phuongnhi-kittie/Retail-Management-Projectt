from PyQt6.QtWidgets import QTableWidgetItem

from DAL.InvoiceDAL import InvoiceDAL
from ui.InvoicesMain import Ui_MainWindow


class InvoiceMainExt(Ui_MainWindow):
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.logout)
        self.pushButtonDeleteEmployee.clicked.connect(self.delete)
        self.tableWidget.itemSelectionChanged.connect(self.choose_invoice)
    def choose_invoice(self):
        currentRow = self.tableWidget.currentRow()
        column_id = self.tableWidget.item(currentRow, 0)
        self.lineEditBillNo.setText(column_id.text())
    def delete(self):
        bill_no = self.lineEditBillNo.text()
        self.invoice_dal.delete_invoice(bill_no)
    def logout(self):
        self.MainWindow.close()
    def display(self):
        self.is_completed = True
        list_invoice = self.invoice_dal.get_all_invoices()
        self.tableWidget.setRowCount(0)
        for i in range(len(list_invoice)):
            invoice_i = list_invoice[i]
            self.tableWidget.insertRow(i)
            column_billno = QTableWidgetItem(invoice_i.bill_no)
            column_date = QTableWidgetItem(invoice_i.date)
            column_customer_name = QTableWidgetItem(invoice_i.customer_name)
            column_phone = QTableWidgetItem(invoice_i.phone)
            self.tableWidget.setItem(i, 0, column_billno)
            self.tableWidget.setItem(i, 1, column_date)
            self.tableWidget.setItem(i, 2, column_customer_name)
            self.tableWidget.setItem(i, 3, column_phone)
    def show(self):
        self.display()
        self.MainWindow.show()
