import traceback

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow
from DAL.InvoiceDAL import InvoiceDAL
from DAL.ProductDAL import ProductDAL
from model.Invoice import Invoice
from ui.BillingSystem import Ui_MainWindow
from PyQt6.QtWidgets import  QMessageBox, QTableWidgetItem
class BillingSystemExt(Ui_MainWindow):
    def __init__(self, login_window):
        self.login_window = login_window
        self.current_user = None
        self.product_dal = ProductDAL()
        self.invoice_dal = InvoiceDAL()
        self.count_row = 0
        self.chosen_product = None
        self.list_product_sell = []
        self.list_quantity = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.process_logout) #back to login_emp
        self.pushButtonAddToCart.clicked.connect(self.add_to_cart)
        self.tableWidget.itemSelectionChanged.connect(self.choose_product)
        self.pushButtonRemove.clicked.connect(self.remove_product)
        self.pushButtonClear.clicked.connect(self.clear)
        self.pushButtonTotal.clicked.connect(self.cal_total)
        self.pushButtonNew.clicked.connect(self.clear_all)
        self.pushButtonGenerate.clicked.connect(self.store_new_bill)
        self.pushButtonSearch.clicked.connect(self.search_bill)
        self.pushButtonExit.clicked.connect(self.exit_window)
    def exit_window(self):
        """Quay lại màn hình chính MainWindowExt"""
        from ui.MainWindowExt import MainWindowExt  # Import tránh lỗi vòng lặp
        self.MainWindow.close()  # Đóng cửa sổ hiện tại
        self.main_window = QMainWindow()
        self.main_ui = MainWindowExt()
        self.main_ui.setupUi(self.main_window)
        self.main_ui.showWindow()  # Dùng showWindow() thay vì show()

    def show_message(self, text, title="Thông báo"):
        """Hiển thị hộp thoại thông báo."""
        msg = QMessageBox()
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec()

    def load_bill_data(self, bill_no):
        """Load dữ liệu hóa đơn dựa vào Bill No."""
        bill_search = self.invoice_dal.get_invoice_by_id(bill_no)
        self.list_quantity.clear()
        self.list_product_sell.clear()

        if not bill_search:
            self.show_message("Cannot find your Bill? Please enter the correct Bill number ^^", "Search Error!")
            return

        self.labelBillNo.setText(bill_search.bill_no)
        self.labelCustomerName.setText(bill_search.customer_name)
        self.labelPhone.setText(bill_search.phone)
        self.labelDate.setText(bill_search.date)


        self.tableWidget.setRowCount(0)  # Xóa dữ liệu cũ trước khi hiển thị mới
        list_all_product = self.product_dal.get_all_products()

        for product_id, quantity in bill_search.list_product:
            product = self.product_dal.get_product_by_id(list_all_product, product_id)
            if not product:
                continue

            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(product.id))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(product.name))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.selling_price)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.selling_price * quantity)))

            self.list_product_sell.append(product)
            self.list_quantity.append(quantity)

    def search_bill(self):
        """Tìm kiếm hóa đơn và hiển thị dữ liệu."""
        bill_no = self.lineEditBillNo.text().strip()
        self.load_bill_data(bill_no)  # Gọi hàm load_bill_data để tránh lặp code

    def store_new_bill(self):
        try:
            customer_name = self.lineEditCustomerName.text().strip()
            contact_no = self.lineEditContactNo.text().strip()

            if not customer_name or not contact_no:
                self.show_message("Customer information cannot be left blank!", "Missing Information Error ?!")
                return

            list_invoice = self.invoice_dal.get_all_invoices()
            bill_no = f"bill{len(list_invoice) + 1}"
            date_invoice = QDate.currentDate().toString("dd/MM/yyyy")

            list_product = [[product.id, quantity] for product, quantity in zip(self.list_product_sell, self.list_quantity)]
            new_bill = Invoice(bill_no, date_invoice, customer_name, contact_no, list_product)

            self.invoice_dal.store_new_bill(new_bill)
            self.show_message("New invoice saved successfully!!!")

            # Cập nhật giao diện với thông tin hóa đơn mới
            self.labelBillNo.setText(bill_no)
            self.labelCustomerName.setText(customer_name)
            self.labelPhone.setText(contact_no)
            self.labelDate.setText(date_invoice)

            self.list_product_sell.clear()
            self.list_quantity.clear()
        except Exception as e:
            traceback.print_exc()
            self.show_message(f"Something went wrong? Please retry ^^ : {e}", "Saving Invoice Error !! ")

    def clear_all(self):
        try:
            self.clear()
            self.tableWidget.setRowCount(0)
            self.count_row = 0
            # self.list_quantity = []
            # self.list_product_sell = []
            self.list_product_sell.clear()  # Xóa danh sách sản phẩm
            self.list_quantity.clear()  # Xóa danh sách số lượng
            self.lineEditTotal.clear()
            self.lineEditRest.clear()
            self.lineEditPayment.clear()
            self.lineEditDiscount.clear()
            self.lineEditBillNo.clear()
            self.lineEditCustomerName.clear()
            self.lineEditContactNo.clear()
            self.labelCustomerName.clear()
            self.labelBillNo.clear()
            self.labelDate.clear()
            self.labelPhone.clear()
            self.lineEditCustomerName.setFocus()


        except Exception as e:
            traceback.print_exc()
            self.show_message(f"Opps, something when wrong!!Please retry ^^ : {e}", "ERROR !!!")

    def cal_total(self):
        try:
            total = 0
            payment = 0
            list_product = self.product_dal.get_all_products()

            for row in range(self.tableWidget.rowCount()):
                amount_item = self.tableWidget.item(row, 4)
                item_id = self.tableWidget.item(row, 0)
                quantity = self.tableWidget.item(row, 2)

                if amount_item and item_id and quantity:
                    total += float(amount_item.text())
                    product = self.product_dal.get_product_by_id(list_product, item_id.text())
                    if product:
                        payment += float(product.cost_price) * int(quantity.text())

            rest = total - payment
            self.lineEditTotal.setText(str(total))
            self.lineEditDiscount.setText("0")
            self.lineEditPayment.setText(str(payment))
            self.lineEditRest.setText(str(rest))
        except Exception as e:
            traceback.print_exc()
            self.show_message(f"Lỗi khi tính tổng: {e}", "Lỗi")

    def clear(self):
        self.lineEditProduct.clear()
        self.lineEditCategory.clear()
        self.lineEditSubCategory.clear()
        self.lineEditQuantity.clear()

    def index_pro(self, id):
        temp_index = 0
        if self.list_product_sell is not None:
            for i in range(len(self.list_product_sell)):
                if self.list_product_sell[i].id == id:
                    temp_index = i
                    break
        return temp_index
    def remove_product(self):
        try:
            current_row = self.tableWidget.currentRow()
            if current_row == -1:
                self.show_message("Chưa chọn sản phẩm để xóa!", "Lỗi")
                return

            product_id = self.tableWidget.item(current_row, 0).text()
            quantity = int(self.tableWidget.item(current_row, 2).text())
            need_product = self.product_dal.get_product_by_id(self.product_dal.get_all_products(), product_id)

            if need_product:
                index = next((i for i, p in enumerate(self.list_product_sell) if p.id == product_id), None)
                if index is not None:
                    self.list_product_sell.pop(index)
                    self.list_quantity.pop(index)

                self.product_dal.update_quantity_recover(quantity, need_product)

            self.tableWidget.removeRow(current_row)
            self.count_row -= 1
            self.show_message("Đã xóa sản phẩm khỏi giỏ hàng!")

        except Exception as e:
            traceback.print_exc()
            self.show_message(f"Lỗi khi xóa sản phẩm: {e}", "Lỗi")
    def choose_product(self):
        row = self.tableWidget.currentRow()
        column_id =self.tableWidget.item(row, 0)
        column_name = self.tableWidget.item(row, 1)
        quantity = self.tableWidget.item(row, 2)
        list_product = self.product_dal.get_all_products()
        chosen_product = self.product_dal.get_product_by_id(list_product, column_id.text())
        self.chosen_product = chosen_product
        self.lineEditCategory.setText(chosen_product.category)
        self.lineEditSubCategory.setText(chosen_product.sub_category)
        self.lineEditProduct.setText(column_name.text())
        self.lineEditQuantity.setText(quantity.text())
    def add_to_cart(self):
        try:
            category = self.lineEditCategory.text()
            sub_category = self.lineEditSubCategory.text()
            product_name = self.lineEditProduct.text()
            if category == "" and sub_category == "" and product_name == "":
                msg = QMessageBox()
                msg.setText("Empty !!!")
                msg.setWindowTitle("Error !!!")
                return
            else:
                quantity = int(self.lineEditQuantity.text())
                needed_product = self.product_dal.search(category, sub_category, product_name)
                self.list_product_sell.append(needed_product)
                self.list_quantity.append(quantity)
                self.tableWidget.setRowCount(self.count_row)
                self.tableWidget.insertRow(self.count_row)
                if needed_product is None:
                    msg = QMessageBox()
                    msg.setText("Error")
                    msg.setWindowTitle("Error!!!")
                    msg.exec()
                else:
                    column_id = QTableWidgetItem(needed_product.id)
                    column_name = QTableWidgetItem(needed_product.name)
                    column_quantity = QTableWidgetItem(str(quantity))
                    column_price = QTableWidgetItem(str(needed_product.selling_price))
                    column_amount = QTableWidgetItem(str(needed_product.selling_price*quantity))
                    self.tableWidget.setItem(self.count_row, 0, column_id)
                    self.tableWidget.setItem(self.count_row, 1, column_name)
                    self.tableWidget.setItem(self.count_row, 2, column_quantity)
                    self.tableWidget.setItem(self.count_row, 3, column_price)
                    self.tableWidget.setItem(self.count_row, 4, column_amount)
                    self.product_dal.update_quantity_selling(quantity, needed_product)
                    self.count_row += 1
        except:
            traceback.print_exc()
    def process_logout(self):
        self.MainWindow.close()  # Đóng cửa sổ hiện tại
        self.login_window.showWindow()  # Dùng showWindow() thay vì show()

