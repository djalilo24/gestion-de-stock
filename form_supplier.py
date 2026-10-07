from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegularExpressionValidator
class Fournisseurs(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fournisseur_ui()

    def fournisseur_ui(self):
        FR = QtCore.QRegularExpression("[a-zA-Z]+")
        validator_fr = QRegularExpressionValidator(FR, self)
        AR = QtCore.QRegularExpression("[ء-ي ]*")
        validator_ar = QRegularExpressionValidator(AR, self)
        self.group_form_supplier = QtWidgets.QVBoxLayout(self)
        self.title = QtWidgets.QLabel("Fournisseurs", self)
        #========nom fournisseur=========
        self.lable_nom = QtWidgets.QLabel("Nom du fournisseur", self)
        self.nom = QtWidgets.QLineEdit()
        self.nom.setPlaceholderText("Nom du fournisseur") 
        self.nom.setValidator(validator_fr)
        #========prénom fournisseur=========         
        self.lable_prenom = QtWidgets.QLabel("Prénom du fournisseur", self)
        self.prenom = QtWidgets.QLineEdit()
        self.prenom.setPlaceholderText("Prénom du fournisseur") 
        self.prenom.setValidator(validator_fr)
        
        self.group_form_supplier.addWidget(self.title)
        self.group_form_supplier.addWidget(self.lable_nom)
        self.group_form_supplier.addWidget(self.nom)
        self.group_form_supplier.addWidget(self.lable_prenom)
        self.group_form_supplier.addWidget(self.prenom)
    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        self.title.setGeometry(int(w * 0.5), int(h * 0.002), int(w * 0.2), int(h * 0.1))  
        self.lable_nom.setGeometry(int(w * 0.01), int(h * 0.07), int(w * 0.2), int(h * 0.1))
        self.nom.setGeometry(int(w * 0.147), int(h * 0.099), int(w * 0.2), int(h * 0.06))
        self.lable_prenom.setGeometry(int(w * 0.01), int(h * 0.15), int(w * 0.2), int(h * 0.1))
        self.prenom.setGeometry(int(w * 0.147), int(h * 0.179), int(w * 0.2), int(h * 0.06))
        super().resizeEvent(event)