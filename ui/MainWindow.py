# Form implementation generated from reading ui file 'D:\Retail-Management-Project\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1471, 753)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/teddy-bear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("border-radius: 10;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1471, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Retail-Management-Project\\ui\\../images/mainbackground.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1471, 751))
        self.label_2.setStyleSheet("background-color: rgba(248, 201, 205,0.5);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 160, 431, 101))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButtonAdmin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdmin.setGeometry(QtCore.QRect(410, 320, 251, 221))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonAdmin.setFont(font)
        self.pushButtonAdmin.setStyleSheet("QPushButton {\n"
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
        self.pushButtonAdmin.setText("")
        self.pushButtonAdmin.setObjectName("pushButtonAdmin")
        self.pushButtonEmployee = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonEmployee.setGeometry(QtCore.QRect(810, 320, 261, 221))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonEmployee.setFont(font)
        self.pushButtonEmployee.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Imprint MT Shadow\";\n"
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
        self.pushButtonEmployee.setText("")
        self.pushButtonEmployee.setObjectName("pushButtonEmployee")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 360, 91, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(900, 360, 71, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Phuong Nhi/Downloads/user (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(860, 450, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "LOG IN AS ? "))
        self.label_6.setText(_translate("MainWindow", "ADMIN"))
        self.label_7.setText(_translate("MainWindow", "EMPLOYEE"))
