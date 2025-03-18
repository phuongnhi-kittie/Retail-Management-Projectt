import traceback

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from DAL.ProductDAL import ProductDAL

from model.Product import Product
from ui.AddProductExt import AddProductExt
from ui.InventoryManagement import Ui_MainWindow
from ui.UpdateProductExt import UpdateProductExt


class InventoryManagement(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.add_product_window = None
        self.update_product_window = None
        self.product_dal = ProductDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.display()
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogout.clicked.connect(self.logout)
        self.pushButtonExit.clicked.connect(self.logout)
        self.pushButtonAddProduct.clicked.connect(self.add_product)
        self.pushButtonUpdateProduct.clicked.connect(self.update_product)
        self.pushButtonDeleteProduct.clicked.connect(self.delete_product)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.choose_product)
    def choose_product(self):
        if self.is_completed==False:
            return
        row = self.tableWidgetProduct.currentRow()
        column_id = self.tableWidgetProduct.item(row, 0)
        self.lineEditProductID.setText(column_id.text())
    def delete_product(self):
        id_delete = self.lineEditProductID.text()
        self.product_dal.delete_product(id_delete)
        msg = QMessageBox()
        msg.setText("Delete successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def display(self):
        self.is_completed = False
        list_product = self.product_dal.get_all_products()
        self.tableWidgetProduct.setRowCount(0)
        for i in range(len(list_product)):
            self.tableWidgetProduct.insertRow(i)
            product_i = list_product[i]
            column_id = QTableWidgetItem(product_i.id)
            column_name = QTableWidgetItem(product_i.name)
            column_category = QTableWidgetItem(product_i.category)
            column_sub_category = QTableWidgetItem(product_i.sub_category)
            column_quantity = QTableWidgetItem(str(product_i.quantity))
            column_cost_price = QTableWidgetItem(str(product_i.cost_price))
            column_selling_price = QTableWidgetItem(str(product_i.selling_price))
            column_vendor_phone = QTableWidgetItem(str(product_i.vendor_phone))
            self.tableWidgetProduct.setItem(i, 0, column_id)
            self.tableWidgetProduct.setItem(i, 1, column_name)
            self.tableWidgetProduct.setItem(i, 2, column_category)
            self.tableWidgetProduct.setItem(i, 3, column_sub_category)
            self.tableWidgetProduct.setItem(i, 4, column_quantity)
            self.tableWidgetProduct.setItem(i, 5, column_selling_price)
            self.tableWidgetProduct.setItem(i, 6, column_cost_price)
            self.tableWidgetProduct.setItem(i, 7, column_vendor_phone)
        self.is_completed = True
    def add_product(self):
        try:
            AddProductWindow = QMainWindow()
            self.add_product_window = AddProductExt()
            self.add_product_window.setupUi(AddProductWindow)
            self.add_product_window.showWindow()
        except:
            traceback.print_exc()
    def update_product(self):
        try:
            if self.is_completed == False:
                return
            row = self.tableWidgetProduct.currentRow()
            column_id = self.tableWidgetProduct.item(row, 0)
            column_name = self.tableWidgetProduct.item(row, 1)
            column_category = self.tableWidgetProduct.item(row, 2)
            column_sub_category = self.tableWidgetProduct.item(row, 3)
            column_quantity = self.tableWidgetProduct.item(row, 4)
            column_selling_price = self.tableWidgetProduct.item(row, 5)
            column_cost_price = self.tableWidgetProduct.item(row, 6)
            column_vendor_phone = self.tableWidgetProduct.item(row, 7)
            UpdateEmpWindow = QMainWindow()
            product_update = Product(id=column_id.text(), name=column_name.text(), category=column_category.text(), sub_category=column_sub_category.text(), quantity=column_quantity.text(), cost_price=column_cost_price.text(), selling_price=column_selling_price.text(), vendor_phone=column_vendor_phone.text())
            self.update_product_window = UpdateProductExt()
            self.update_product_window.setupUi(UpdateEmpWindow)
            self.update_product_window.product_update = product_update
            self.update_product_window.showWindow()
        except:
            traceback.print_exc()
    def logout(self):
        self.MainWindow.close()