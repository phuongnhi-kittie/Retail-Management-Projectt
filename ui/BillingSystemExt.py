import traceback

from PyQt6.QtCore import QDate

from DAL.InvoiceDAL import InvoiceDAL
from DAL.ProductDAL import ProductDAL
from model.Invoice import Invoice
from ui.BillingSystem import Ui_MainWindow
from PyQt6.QtWidgets import  QMessageBox, QTableWidgetItem

class BillingSystemExt(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.product_dal = ProductDAL()
        self.count_row = 0
        self.chosen_product = None
        self.invoice_dal = InvoiceDAL()
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
        self.MainWindow.close()
    def search_bill(self):
        bill_no = self.lineEditBillNo.text()
        bill_search = self.invoice_dal.get_invoice_by_id(bill_no)
        self.list_quantity = []
        self.list_product_sell = []
        if bill_search is None:
            msg = QMessageBox()
            msg.setText("Not found")
            msg.setWindowTitle("Error!!!")
            msg.exec()
        else:
            self.labelBillNo.setText(bill_search.bill_no)
            self.labelCustomerName.setText(bill_search.customer_name)
            self.labelPhone.setText(bill_search.phone)
            self.labelDate.setText(bill_search.date)
            self.tableWidget.setRowCount(self.count_row)
            list_all_product = self.product_dal.get_all_products()
            for product in bill_search.list_product:
                product_need = self.product_dal.get_product_by_id(list_all_product,product[0])
                self.tableWidget.insertRow(self.count_row)
                column_id = QTableWidgetItem(product_need.id)
                column_name = QTableWidgetItem(product_need.name)
                column_quantity = QTableWidgetItem(str(product[1]))
                column_price = QTableWidgetItem(str(product_need.selling_price))
                column_amount = QTableWidgetItem(str(product_need.selling_price*product[1]))
                self.tableWidget.setItem(self.count_row, 0, column_id)
                self.tableWidget.setItem(self.count_row, 1, column_name)
                self.tableWidget.setItem(self.count_row, 2, column_quantity)
                self.tableWidget.setItem(self.count_row, 3, column_price)
                self.tableWidget.setItem(self.count_row, 4, column_amount)
                self.count_row += 1
                self.list_product_sell.append(product_need)
                self.list_quantity.append(product[1])
    def store_new_bill(self):
        try:
            customer_name = self.lineEditCustomerName.text()
            contact_no = self.lineEditContactNo.text()
            if customer_name == "" or contact_no == "":
                msg = QMessageBox()
                msg.setText("Empty value")
                msg.setWindowTitle("Error!!!")
                msg.exec()
                return
            list_invoice = self.invoice_dal.get_all_invoices()
            bill_no = f"bill{len(list_invoice)+1}"
            date_invoice = QDate.currentDate().toString("dd/MM/yyyy")
            list_product_sell = [product.id for product in self.list_product_sell]
            list_product = []
            for i in range(len(self.list_quantity)):
                list_product.append([list_product_sell[i], self.list_quantity[i]])
            new_bill = Invoice(bill_no=bill_no,date=date_invoice, customer_name=customer_name, phone=contact_no, list_product=list_product)
            self.invoice_dal.store_new_bill(new_bill)
            msg = QMessageBox()
            msg.setText("Create new bill successfully")
            msg.setWindowTitle("Announcement")
            msg.exec()
            self.list_product_sell = []
            self.list_quantity = []
        except:
            traceback.print_exc()
    def clear_all(self):
        try:
            self.clear()
            self.count_row = 0
            self.tableWidget.setRowCount(self.count_row)
            # self.list_quantity = []
            # self.list_product_sell = []
            self.lineEditTotal.setText("")
            self.lineEditRest.setText("")
            self.lineEditPayment.setText("")
            self.lineEditDiscount.setText("")
        except:
            traceback.print_exc()
    def cal_total(self):
        list_amount_product = []
        list_cost_product = []
        column_index = 4
        list_product = self.product_dal.get_all_products()
        for row in range(self.tableWidget.rowCount()):
            item_amount = self.tableWidget.item(row, column_index)
            list_amount_product.append(float(item_amount.text()))
            item_id = self.tableWidget.item(row, 0)
            quantity = self.tableWidget.item(row, 2)
            product_i = self.product_dal.get_product_by_id(list_product, item_id.text())
            cost_price = float(product_i.cost_price)*int(quantity.text())
            list_cost_product.append(cost_price)
        total = 0
        payment = 0
        for amount in list_amount_product:
            total += amount
        for cp in list_cost_product:
            payment += cp
        rest = total - 0 - payment
        self.lineEditTotal.setText(str(total))
        self.lineEditDiscount.setText(str(0))
        self.lineEditPayment.setText(str(payment))
        self.lineEditRest.setText(str(rest))
    def clear(self):
        try:
            self.lineEditProduct.setText("")
            self.lineEditCategory.setText("")
            self.lineEditSubCategory.setText("")
            self.lineEditQuantity.setText("")
        except:
            traceback.print_exc()
    def index_pro(self, id):
        temp_index = 0
        if self.list_product_sell != None:
            for i in range(len(self.list_product_sell)):
                if self.list_product_sell[i].id == id:
                    temp_index = i
                    break
        return temp_index
    def remove_product(self):
        try:
            list_product = self.product_dal.get_all_products()
            current_row = self.tableWidget.currentRow()
            column_id = self.chosen_product.id
            quantity = self.lineEditQuantity.text()
            need_product = self.product_dal.get_product_by_id(list_product, column_id)
            index_need_product = self.index_pro(need_product.id)
            if index_need_product != 0:
                self.list_product_sell.pop(index_need_product)
            self.list_quantity.remove(int(quantity))
            self.product_dal.update_quantity_recover(int(quantity), need_product)
            print(current_row)
            if current_row != -1:
                self.tableWidget.removeRow(current_row)
                self.count_row -= 1
                self.tableWidget.repaint()
            msg = QMessageBox()
            msg.setText("Remove successfully !!!")
            msg.setWindowTitle("Announcement")
            msg.exec()
        except:
            traceback.print_exc()

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
        self.MainWindow.close()

