# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\AddEmployee.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1633, 854)
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
        self.lineEditEmployeeName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmployeeName.setGeometry(QtCore.QRect(80, 260, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditEmployeeName.setFont(font)
        self.lineEditEmployeeName.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditEmployeeName.setPlaceholderText("")
        self.lineEditEmployeeName.setObjectName("lineEditEmployeeName")
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
        self.label_8.setGeometry(QtCore.QRect(70, 440, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_8.setObjectName("label_8")
        self.lineEditContactNo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditContactNo.setGeometry(QtCore.QRect(80, 370, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditContactNo.setFont(font)
        self.lineEditContactNo.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditContactNo.setPlaceholderText("")
        self.lineEditContactNo.setObjectName("lineEditContactNo")
        self.lineEditCCCDNo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCCCDNo.setGeometry(QtCore.QRect(80, 500, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditCCCDNo.setFont(font)
        self.lineEditCCCDNo.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditCCCDNo.setPlaceholderText("")
        self.lineEditCCCDNo.setObjectName("lineEditCCCDNo")
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(670, 690, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 207, 239);\n"
"border-radius: 20")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/add (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon2)
        self.pushButtonAdd.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(850, 690, 131, 41))
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
        self.label_12.setGeometry(QtCore.QRect(870, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.label_12.setObjectName("label_12")
        self.lineEditAdress = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditAdress.setGeometry(QtCore.QRect(890, 370, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditAdress.setFont(font)
        self.lineEditAdress.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditAdress.setPlaceholderText("")
        self.lineEditAdress.setObjectName("lineEditAdress")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(890, 500, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("border: none;\n"
"border-bottom: 2px solid grey; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"border-color: rgb(211, 211, 211);\n"
"padding: 5px;")
        self.lineEditPassword.setPlaceholderText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.comboBoxDesignation = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxDesignation.setGeometry(QtCore.QRect(880, 251, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxDesignation.setFont(font)
        self.comboBoxDesignation.setStyleSheet("color: rgb(72, 72, 72);\n"
"")
        self.comboBoxDesignation.setObjectName("comboBoxDesignation")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/profile.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.comboBoxDesignation.addItem(icon4, "")
        self.comboBoxDesignation.addItem(icon4, "")
        self.comboBoxDesignation.addItem(icon4, "")
        self.comboBoxDesignation.addItem(icon4, "")
        self.label_6.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.pushButtonLogout.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.timelabel.raise_()
        self.lineEditEmployeeName.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.lineEditContactNo.raise_()
        self.lineEditCCCDNo.raise_()
        self.pushButtonAdd.raise_()
        self.pushButtonClear.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEditAdress.raise_()
        self.lineEditPassword.raise_()
        self.comboBoxDesignation.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Employee"))
        self.label.setText(_translate("MainWindow", "ADMIN"))
        self.pushButtonLogout.setText(_translate("MainWindow", "Logout"))
        self.label_2.setText(_translate("MainWindow", "Add Employee"))
        self.label_3.setText(_translate("MainWindow", "Employee Name:"))
        self.label_4.setText(_translate("MainWindow", "Contact No. :"))
        self.label_8.setText(_translate("MainWindow", "Personal Identification No. :"))
        self.pushButtonAdd.setText(_translate("MainWindow", "ADD"))
        self.pushButtonClear.setText(_translate("MainWindow", "CLEAR"))
        self.label_10.setText(_translate("MainWindow", "Adress:"))
        self.label_11.setText(_translate("MainWindow", "Password:"))
        self.label_12.setText(_translate("MainWindow", "Designation:"))
        self.comboBoxDesignation.setItemText(0, _translate("MainWindow", "Store Manager"))
        self.comboBoxDesignation.setItemText(1, _translate("MainWindow", "Accountant"))
        self.comboBoxDesignation.setItemText(2, _translate("MainWindow", "System Administrator (IT Manager)"))
        self.comboBoxDesignation.setItemText(3, _translate("MainWindow", "Employee"))
