from PyQt6.QtWidgets import QMainWindow, QApplication
from ui.AddEmployeeExt import AddEmployeeExt
app=QApplication([])
mainwindow=QMainWindow()
myui=AddEmployeeExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()