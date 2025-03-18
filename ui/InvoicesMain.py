# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\InvoicesMain.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1518, 792)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/teddy-bear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 1531, 801))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/background.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButtonLogout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogout.setGeometry(QtCore.QRect(70, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogout.setFont(font)
        self.pushButtonLogout.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    background-color: rgb(248, 207, 239);\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff85c0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d14789;\n"
"}\n"
"\n"
"QPushButton {\n"
"    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Bóng đổ */\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/log-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 50, 611, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(247, 79, 164);\n"
"color: rgb(104, 96, 171);\n"
"font: bold 28pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 160, 501, 561))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEditBillNo = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditBillNo.setGeometry(QtCore.QRect(100, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditBillNo.setFont(font)
        self.lineEditBillNo.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditBillNo.setPlaceholderText("")
        self.lineEditBillNo.setObjectName("lineEditBillNo")
        self.pushButtonSearch = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSearch.setGeometry(QtCore.QRect(360, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    background-color: rgb(248, 207, 239);\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff85c0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d14789;\n"
"}\n"
"\n"
"QPushButton {\n"
"    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Bóng đổ */\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/search (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch.setIcon(icon2)
        self.pushButtonSearch.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButtonDeleteEmployee = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonDeleteEmployee.setGeometry(QtCore.QRect(80, 160, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDeleteEmployee.setFont(font)
        self.pushButtonDeleteEmployee.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    background-color: rgb(248, 207, 239);\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff85c0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d14789;\n"
"}\n"
"\n"
"QPushButton {\n"
"    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Bóng đổ */\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/eraser.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDeleteEmployee.setIcon(icon3)
        self.pushButtonDeleteEmployee.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDeleteEmployee.setObjectName("pushButtonDeleteEmployee")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1521, 791))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\images/background.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 50, 21, 21))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/profile.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.groupBoxBillWindow = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxBillWindow.setGeometry(QtCore.QRect(650, 190, 801, 441))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBoxBillWindow.setFont(font)
        self.groupBoxBillWindow.setObjectName("groupBoxBillWindow")
        self.labelCustomerName = QtWidgets.QLabel(parent=self.groupBoxBillWindow)
        self.labelCustomerName.setGeometry(QtCore.QRect(170, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCustomerName.setFont(font)
        self.labelCustomerName.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.labelCustomerName.setText("")
        self.labelCustomerName.setObjectName("labelCustomerName")
        self.labelBillNo = QtWidgets.QLabel(parent=self.groupBoxBillWindow)
        self.labelBillNo.setGeometry(QtCore.QRect(110, 80, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBillNo.setFont(font)
        self.labelBillNo.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.labelBillNo.setText("")
        self.labelBillNo.setObjectName("labelBillNo")
        self.labelDate = QtWidgets.QLabel(parent=self.groupBoxBillWindow)
        self.labelDate.setGeometry(QtCore.QRect(620, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.labelDate.setText("")
        self.labelDate.setObjectName("labelDate")
        self.labelPhone = QtWidgets.QLabel(parent=self.groupBoxBillWindow)
        self.labelPhone.setGeometry(QtCore.QRect(660, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPhone.setFont(font)
        self.labelPhone.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.labelPhone.setText("")
        self.labelPhone.setObjectName("labelPhone")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBoxBillWindow)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 771, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setItem(1, 0, item)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 1471, 721))
        self.label_5.setStyleSheet("border-radius: 20; background: rgb(255, 255, 255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(104, 96, 171);")
        self.label_8.setObjectName("label_8")
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
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.groupBoxBillWindow.raise_()
        self.groupBox.raise_()
        self.timelabel.raise_()
        self.label_9.raise_()
        self.pushButtonLogout.raise_()
        self.label_2.raise_()
        self.label_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Invoices"))
        self.pushButtonLogout.setText(_translate("MainWindow", "Logout"))
        self.label_2.setText(_translate("MainWindow", "Invoices"))
        self.groupBox.setTitle(_translate("MainWindow", "Menu"))
        self.label_3.setText(_translate("MainWindow", "Bill No.: "))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Bill Options"))
        self.pushButtonDeleteEmployee.setText(_translate("MainWindow", "DELETE EMPLOYEE"))
        self.groupBoxBillWindow.setTitle(_translate("MainWindow", "Invoices"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bill No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone No."))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "ADMIN"))
