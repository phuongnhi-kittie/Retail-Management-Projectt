# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\AdminWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1542, 775)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/teddy-bear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("border-radius: 10;")
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1531, 771))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/mainbackground.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 1441, 701))
        self.label_2.setStyleSheet("background-color: rgba(248, 201, 205,0.5);\n"
"border-radius: 50")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 120, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: bold 40pt \"Imprint MT Shadow\";")
        self.label_3.setObjectName("label_3")
        self.pushButtonInventory = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonInventory.setGeometry(QtCore.QRect(190, 340, 271, 231))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonInventory.setFont(font)
        self.pushButtonInventory.setStyleSheet("QPushButton {\n"
"    font:  20PT\"Imprint MT Shadow\";\n"
"    color: rgb(255, 210, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(251, 211, 204);\n"
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
        self.pushButtonInventory.setText("")
        self.pushButtonInventory.setObjectName("pushButtonInventory")
        self.pushButtonEmployees = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonEmployees.setGeometry(QtCore.QRect(630, 340, 271, 231))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonEmployees.setFont(font)
        self.pushButtonEmployees.setStyleSheet("QPushButton {\n"
"    font:  20PT\"Imprint MT Shadow\";\n"
"    color: rgb(255, 210, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(251, 211, 204);\n"
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
        self.pushButtonEmployees.setText("")
        self.pushButtonEmployees.setObjectName("pushButtonEmployees")
        self.pushButtonInvoices = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonInvoices.setGeometry(QtCore.QRect(1070, 340, 271, 231))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonInvoices.setFont(font)
        self.pushButtonInvoices.setStyleSheet("QPushButton {\n"
"    font:  20PT\"Imprint MT Shadow\";\n"
"    color: rgb(255, 210, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(251, 211, 204);\n"
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
        self.pushButtonInvoices.setText("")
        self.pushButtonInvoices.setObjectName("pushButtonInvoices")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 490, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 490, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1150, 490, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 400, 91, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/inventory.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 400, 91, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/multiple-users-silhouette.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1170, 380, 91, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/bill.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(99, 103, 176);")
        self.label_10.setObjectName("label_10")
        self.pushButtonLogout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogout.setGeometry(QtCore.QRect(140, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogout.setFont(font)
        self.pushButtonLogout.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 210, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(251, 211, 204);\n"
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
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(150, 70, 21, 21))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/profile.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Admin Mode"))
        self.label_3.setText(_translate("mainWindow", "ADMIN MODE"))
        self.label_6.setText(_translate("mainWindow", "Inventories"))
        self.label_7.setText(_translate("mainWindow", "Employees"))
        self.label_8.setText(_translate("mainWindow", "Invoices"))
        self.label_10.setText(_translate("mainWindow", "ADMIN"))
        self.pushButtonLogout.setText(_translate("mainWindow", "Logout"))
