from PyQt6.QtWidgets import QMainWindow
from ui.login_admin import Ui_MainWindow
class login_adminExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonBack.clicked.connect(self.process_back)
    def process_back(self):
        from ui.MainWindowExt import MainWindowExt  # Import ở đây để tránh vòng lặp
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()