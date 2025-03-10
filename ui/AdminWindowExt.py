from ui.AdminWindow import Ui_mainWindow
class AdminWindowExt(Ui_mainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonEmployees.clicked.connect(self.process_emp)
        self.pushButtonInventory.clicked.connect(self.process_inventory)
        self.pushButtonInvoices.clicked.conncet(self.process_invoices)
    def process_emp(self):
        pass
    def process_inventory(self):
        pass
    def process_invoices(self):
        pass