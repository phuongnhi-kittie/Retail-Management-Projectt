from PyQt6.QtWidgets import QMessageBox

from DAL.ProductDAL import ProductDAL
from model.Product import Product
from ui.AddProduct import Ui_MainWindow
class AddProductExt(Ui_MainWindow):
    def __init__(self):
        self.product_dal = ProductDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonAdd.clicked.connect(self.add_new_product)
        self.pushButtonClear.clicked.connect(self.clear)
        self.pushButtonLogout.clicked.connect(self.logout)
    def clear(self):
        self.lineEditProductName.setText("")
        self.lineEditCategory.setText("")
        self.lineEditSubCategory.setText("")
        self.lineEditQuantity.setText("")
        self.lineEditCostPrice.setText("")
        self.lineEditSellingPrice.setText("")
        self.lineEditVendorPhoneNo.setText("")
    def add_new_product(self):
        id_product = f"prod{len(self.product_dal.get_all_products()) + 1}"
        name = self.lineEditProductName.text()
        category = self.lineEditCategory.text()
        sub_category = self.lineEditSubCategory.text()
        quantity = int(self.lineEditQuantity.text())
        cost_price = float(self.lineEditCostPrice.text())
        selling_price = float(self.lineEditSellingPrice.text())
        vendor_phone = self.lineEditVendorPhoneNo.text()
        new_product = Product(id=id_product, name=name, category=category, sub_category=sub_category, quantity=quantity, cost_price=cost_price, selling_price=selling_price, vendor_phone=vendor_phone)
        self.product_dal.store_new_product(new_product)
        msg = QMessageBox()
        msg.setText("Add new product successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def logout(self):
        self.MainWindow.close()