from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from DAL.InvoiceDAL import InvoiceDAL
from ui.InvoicesMain import Ui_MainWindow
from PyQt6.QtGui import QColor
class InvoiceMainExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.invoice_dal = InvoiceDAL()
        self.billing_system_window = None  # Cửa sổ hiển thị Bill Window
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.logout)
        self.pushButtonDeleteEmployee.clicked.connect(self.delete)
        self.tableWidget.itemSelectionChanged.connect(self.choose_invoice)
        self.pushButtonExit.clicked.connect(self.exit)
        self.pushButtonSearch.clicked.connect(self.search_invoice)

    def choose_invoice(self):
        currentRow = self.tableWidget.currentRow()
        column_id = self.tableWidget.item(currentRow, 0)
        self.lineEditBillNo.setText(column_id.text())
    def delete(self):
        bill_no = self.lineEditBillNo.text().strip()
        if not bill_no:
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter a Bill No. to delete.")
            return

        success = self.invoice_dal.delete_invoice(bill_no)
        if success:
            QMessageBox.information(self.MainWindow, "Success", f"Deleted Bill No. {bill_no} successfully.")
            self.display()  # Cập nhật lại bảng
        else:
            return

    def logout(self):
        from ui.login_adminExt import login_adminExt  # Import giao diện đăng nhập
        self.MainWindow.close()  # Đóng cửa sổ hiện tại
        self.main_window = QMainWindow()
        self.main_ui = login_adminExt()
        self.main_ui.setupUi(self.main_window)
        self.main_ui.showWindow()  # Dùng showWindow() thay vì show()

    def search_invoice(self):
        bill_no = self.lineEditBillNo.text().strip()
        if not bill_no:
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter a Bill No. to search.")
            return

        found = False
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item and item.text() == bill_no:
                # Đổi màu nguyên dòng khi tìm thấy
                for col in range(self.tableWidget.columnCount()):
                    if self.tableWidget.item(row, col):
                        self.tableWidget.item(row, col).setBackground(QColor(255, 182, 193))  # Light Pink
                found = True
            else:
                # Đặt lại màu gốc nếu không phải dòng tìm thấy
                for col in range(self.tableWidget.columnCount()):
                    if self.tableWidget.item(row, col):
                        self.tableWidget.item(row, col).setBackground(QColor(255, 255, 255))  # White

        if not found:
            QMessageBox.warning(self.MainWindow, "Not Found", "Bill No. not found!")

    def display(self):
        list_invoice = self.invoice_dal.get_all_invoices()
        self.tableWidget.setRowCount(0)
        for i, invoice in enumerate(list_invoice):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(invoice.bill_no))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(invoice.date))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(invoice.customer_name))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(invoice.phone))

    def show(self):
        self.display()
        self.MainWindow.show()

    def exit(self):
        self.MainWindow.close()