from PyQt5 import QtCore, QtGui, QtWidgets
class Fournisseurs(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fournisseur_ui()

    def fournisseur_ui(self):
         
        self.group_form_supplier = QtWidgets.QGroupBox(self)
        self.title = QtWidgets.QLabel("Fournisseurs")
        self.nom = QtWidgets.QLineEdit()
        self.nom.setPlaceholderText("Nom du fournisseur") 
        
        self.group_form_supplier.addWidget(self.title)
        self.group_form_supplier.addWidget(self.nom)
        