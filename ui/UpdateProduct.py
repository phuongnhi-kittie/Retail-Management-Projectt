# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\UpdateProduct.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1631, 854)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/teddy-bear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(110, 88, 165);")
        self.label.setObjectName("label")
        self.pushButtonLogout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogout.setGeometry(QtCore.QRect(70, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogout.setFont(font)
        self.pushButtonLogout.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 207, 239);\n"
"border-radius: 20")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/log-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 50, 611, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(247, 79, 164);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 1591, 791))
        self.label_5.setStyleSheet("border-radius: 20; background: rgb(255, 255, 255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1631, 861))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/background.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 50, 21, 21))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/profile.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.timelabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.timelabel.setGeometry(QtCore.QRect(1280, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.timelabel.setFont(font)
        self.timelabel.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.timelabel.setText("")
        self.timelabel.setObjectName("timelabel")
        self.lineEditProductName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditProductName.setGeometry(QtCore.QRect(80, 260, 1451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditProductName.setFont(font)
        self.lineEditProductName.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditProductName.setPlaceholderText("")
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 320, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 440, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 560, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_9.setObjectName("label_9")
        self.lineEditCategory = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCategory.setGeometry(QtCore.QRect(80, 370, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditCategory.setFont(font)
        self.lineEditCategory.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditCategory.setPlaceholderText("")
        self.lineEditCategory.setObjectName("lineEditCategory")
        self.lineEditQuantity = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditQuantity.setGeometry(QtCore.QRect(80, 500, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditQuantity.setFont(font)
        self.lineEditQuantity.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditQuantity.setPlaceholderText("")
        self.lineEditQuantity.setObjectName("lineEditQuantity")
        self.lineEditSellingPrice = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSellingPrice.setGeometry(QtCore.QRect(80, 620, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditSellingPrice.setFont(font)
        self.lineEditSellingPrice.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditSellingPrice.setPlaceholderText("")
        self.lineEditSellingPrice.setObjectName("lineEditSellingPrice")
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(670, 720, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 207, 239);\n"
"border-radius: 20")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/backup-data.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon2)
        self.pushButtonAdd.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(840, 720, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 207, 239);\n"
"border-radius: 20")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/eraser.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClear.setIcon(icon3)
        self.pushButtonClear.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(870, 320, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(870, 440, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(870, 560, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_12.setObjectName("label_12")
        self.lineEditSubCategory = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSubCategory.setGeometry(QtCore.QRect(890, 370, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditSubCategory.setFont(font)
        self.lineEditSubCategory.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditSubCategory.setPlaceholderText("")
        self.lineEditSubCategory.setObjectName("lineEditSubCategory")
        self.lineEditCostPrice = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCostPrice.setGeometry(QtCore.QRect(890, 500, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditCostPrice.setFont(font)
        self.lineEditCostPrice.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditCostPrice.setPlaceholderText("")
        self.lineEditCostPrice.setObjectName("lineEditCostPrice")
        self.lineEditVendorPhoneNo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditVendorPhoneNo.setGeometry(QtCore.QRect(890, 620, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditVendorPhoneNo.setFont(font)
        self.lineEditVendorPhoneNo.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditVendorPhoneNo.setPlaceholderText("")
        self.lineEditVendorPhoneNo.setObjectName("lineEditVendorPhoneNo")
        self.label_6.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.pushButtonLogout.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.timelabel.raise_()
        self.lineEditProductName.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lineEditCategory.raise_()
        self.lineEditQuantity.raise_()
        self.lineEditSellingPrice.raise_()
        self.pushButtonAdd.raise_()
        self.pushButtonClear.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEditSubCategory.raise_()
        self.lineEditCostPrice.raise_()
        self.lineEditVendorPhoneNo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Product"))
        self.label.setText(_translate("MainWindow", "ADMIN"))
        self.pushButtonLogout.setText(_translate("MainWindow", "Logout"))
        self.label_2.setText(_translate("MainWindow", "Update Product"))
        self.label_3.setText(_translate("MainWindow", "Product Name:"))
        self.label_4.setText(_translate("MainWindow", "Category:"))
        self.label_8.setText(_translate("MainWindow", "Quantity:"))
        self.label_9.setText(_translate("MainWindow", "Selling Price:"))
        self.pushButtonAdd.setText(_translate("MainWindow", "UPDATE"))
        self.pushButtonClear.setText(_translate("MainWindow", "CLEAR"))
        self.label_10.setText(_translate("MainWindow", "Sub Category:"))
        self.label_11.setText(_translate("MainWindow", "Cost Price:"))
        self.label_12.setText(_translate("MainWindow", "Vendor Phone No. :"))
