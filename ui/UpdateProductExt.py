from PyQt6.QtWidgets import QMessageBox
from sympy.integrals.meijerint_doc import category

from DAL.ProductDAL import ProductDAL
from model.Product import Product
from ui.UpdateProduct import Ui_MainWindow
class UpdateProductExt(Ui_MainWindow):
    def __init__(self):
        self.product_update = None
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
        self.pushButtonAdd.clicked.connect(self.update_product)
        self.pushButtonClear.clicked.connect(self.clear)
    def clear(self):
        self.lineEditProductName.setText("")
        self.lineEditCategory.setText("")
        self.lineEditSubCategory.setText("")
        self.lineEditQuantity.setText("")
        self.lineEditCostPrice.setText("")
        self.lineEditSellingPrice.setText("")
        self.lineEditVendorPhoneNo.setText("")
    def logout(self):
        self.MainWindow.close()
    def update_product(self):
        id = self.product_update.id
        name = self.lineEditProductName.text()
        category = self.lineEditCategory.text()
        sub_category = self.lineEditSubCategory.text()
        quantity = int(self.lineEditQuantity.text())
        cost_price = float(self.lineEditCostPrice.text())
        selling_price = float(self.lineEditSellingPrice.text())
        vendor_no = self.lineEditVendorPhoneNo.text()
        update_product = Product(id = id, name = name, category= category, sub_category=sub_category, quantity= quantity, cost_price = cost_price, selling_price=selling_price, vendor_phone=vendor_no)
        self.product_dal.update_new_product(update_product)
        msg = QMessageBox()
        msg.setText("Update product successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def display(self):
        self.lineEditProductName.setText(str(self.product_update.name))
        self.lineEditCategory.setText(self.product_update.category)
        self.lineEditSubCategory.setText(self.product_update.sub_category)
        self.lineEditQuantity.setText(str(self.product_update.quantity))
        self.lineEditCostPrice.setText(str(self.product_update.cost_price))
        self.lineEditSellingPrice.setText(str(self.product_update.selling_price))
        self.lineEditVendorPhoneNo.setText(str(self.product_update.vendor_phone))