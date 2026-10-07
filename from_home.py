from PyQt5 import QtCore, QtGui, QtWidgets
class Home(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.home_ui()

    def home_ui(self):
         
        self.group_form_supplier = QtWidgets.QVBoxLayout(self)
        self.title = QtWidgets.QLabel("Welcome to the Home Page")
        self.group_form_supplier.addWidget(self.title)