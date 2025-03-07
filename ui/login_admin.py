# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\login_admin.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1679, 835)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/teddy-bear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1691, 841))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 30, 481, 781))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 90, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(103, 97, 172);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 240, 31, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/profile.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 340, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/padlock.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setGeometry(QtCore.QRect(670, 220, 371, 51))
        self.lineEditUsername.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"padding: 5px;")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(670, 330, 371, 51))
        self.lineEditPassword.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black; /* Điều chỉnh độ dày và màu của viền dưới */\n"
"padding: 5px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(640, 590, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 207, 239);\n"
"border-radius: 20")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(98, 104, 177);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(109, 109, 109);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(660, 300, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(109, 109, 109);")
        self.label_9.setObjectName("label_9")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(20, 20, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(248, 207, 239,0);\n"
"border-radius: 10\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon1)
        self.pushButtonBack.setIconSize(QtCore.QSize(50, 50))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEditUsername.raise_()
        self.label_4.raise_()
        self.lineEditPassword.raise_()
        self.label_5.raise_()
        self.pushButtonLogin.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.pushButtonBack.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Admin"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.lineEditUsername.setPlaceholderText(_translate("MainWindow", " Enter your username"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.pushButtonLogin.setText(_translate("MainWindow", "LOGIN"))
        self.label_6.setText(_translate("MainWindow", "Admin"))
        self.label_7.setText(_translate("MainWindow", "Username"))
        self.label_9.setText(_translate("MainWindow", "Password"))
        self.pushButtonBack.setText(_translate("MainWindow", "BACK"))
