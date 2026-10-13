from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegularExpressionValidator
class Fournisseurs(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fournisseur_ui()

    def fournisseur_ui(self):
        self.group_form_fournisseur = QtWidgets.QVBoxLayout(self)
        #====================Bouton add product=========================
        self.add_fournisseur_button = QtWidgets.QPushButton("Ajouter un fournisseur")   
        self.add_fournisseur_button.setIcon(QtGui.QIcon("icons/add.png"))
        self.add_fournisseur_button.setObjectName("add_button")
        self.add_fournisseur_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_fournisseur_button.setToolTip("Ajouter un nouveau fournisseur")
        self.add_fournisseur_button.setToolTipDuration(3000)  # Durée d'aff
        self.add_fournisseur_button.setIconSize(QtCore.QSize(24, 24))
        self.add_fournisseur_button.clicked.connect(self.form_fournisseur)
        #====================title=========================
        self.title_label = QtWidgets.QLabel("Liste des Fournisseurs")       
        self.title_label.setObjectName("title_group")
        #====================add widget =========================
        self.group_box_table = QtWidgets.QGroupBox()
        self.group_form_fournisseur.addWidget(self.group_box_table)
        self.layout_table = QtWidgets.QVBoxLayout(self.group_box_table) 
        self.headre_layout = QtWidgets.QHBoxLayout()
        self.headre_layout.addWidget(self.title_label)
        self.headre_layout.addStretch()  # Ajouter un espace flexible pour pousser le bouton vers la droite
        self.headre_layout.addWidget(self.add_fournisseur_button)
        self.layout_table.addLayout(self.headre_layout)
        #====================table product=========================
        self.table_fournisseur = QtWidgets.QTableWidget()
        self.table_fournisseur.setRowCount(3)
        self.table_fournisseur.setColumnCount(5)
        self.table_fournisseur.setHorizontalHeaderLabels(["ID", "Nom", "Prix", "Quantité", "Description"])  
        data = [
           ["1", "Tissu coton", "Matière première", "150", "500"],
           ["2", "Fil à coudre", "Matière première", "80", "120"],
           ["3", "Chemise", "Produit fini", "25", "2500"]
            ]   
        for row, values in enumerate(data):
           for col, value in enumerate(values):
               self.table_fournisseur.setItem(row, col,QtWidgets.QTableWidgetItem(value))
        self.table_fournisseur.horizontalHeader().setStretchLastSection(True)
        self.table_fournisseur.setAlternatingRowColors(True) 
        self.layout_table.addWidget(self.table_fournisseur)
        #=========function form fournisseur===============
    def form_fournisseur(self):
        self.fournisseur_window = QtWidgets.QWidget()
        self.fournisseur_window.setWindowTitle("Ajouter un produit")

        screen = QtWidgets.QApplication.primaryScreen()
        geometry = screen.availableGeometry()

        W = int(geometry.width() * 0.70)
        H = int(geometry.height() * 0.70)

        self.fournisseur_window.resize(W, H)

        self.lable_code_fournisseur = QtWidgets.QLabel("Code de fournisseur",self.fournisseur_window)
        self.lable_code_fournisseur.setGeometry(
                int(W * 0.05), int(H * 0.15),
                int(W * 0.15), int(H * 0.08)
        )
        self.line_code_fournisseur = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_code_fournisseur.setEnabled(False)
        self.line_code_fournisseur.setGeometry(
                int(W * 0.20), int(H * 0.15),
                int(W * 0.15), int(H * 0.08)            
        )
        self.lable_type_fournisseur = QtWidgets.QLabel("Type de fournisseur",self.fournisseur_window)
        self.lable_type_fournisseur.setGeometry(
                int(W * 0.36), int(H * 0.15),
                int(W * 0.15), int(H * 0.08)             
        )
        self.choix_type_fournisseur = QtWidgets.QComboBox(self.fournisseur_window)
        self.choix_type_fournisseur.addItems(["","Personne morale","Personne physique"])
        self.choix_type_fournisseur.currentIndexChanged.connect(lambda :self.type_fournisseur())
        self.choix_type_fournisseur.setGeometry(
                int(W * 0.49), int(H * 0.15),
                int(W * 0.17), int(H * 0.08)           
        )
        self.lable_type_societe = QtWidgets.QLabel("Nom societé",self.fournisseur_window)
        self.lable_type_societe.setGeometry(
                int(W * 0.66), int(H * 0.15),
                int(W * 0.17), int(H * 0.08)             
        )
        self.choix_type_societe = QtWidgets.QComboBox(self.fournisseur_window)
        self.choix_type_societe.addItems(["","EURL","SARL","SPA","SNC","AUTRE"])
        self.choix_type_societe.setEnabled(False)
        self.choix_type_societe.setGeometry(
                int(W * 0.76), int(H * 0.15),
                int(W * 0.09), int(H * 0.08)          
        )
        self.lable_nom_societe = QtWidgets.QLabel("Nom societe",self.fournisseur_window)
        self.lable_nom_societe.setGeometry(
                int(W * 0.13), int(H * 0.30),
                int(W * 0.11), int(H * 0.08)            
        )
        self.line_nom_societe = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_nom_societe.setEnabled(False)
        self.line_nom_societe.setGeometry(
                int(W * 0.23), int(H * 0.30),
                int(W * 0.25), int(H * 0.08)            
        )
        self.lable_add_societe = QtWidgets.QLabel("Address societe",self.fournisseur_window)
        self.lable_add_societe.setGeometry(
                int(W * 0.49), int(H * 0.30),
                int(W * 0.11), int(H * 0.08)
        )
        self.line_add_societe = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_add_societe.setEnabled(False)
        self.line_add_societe.setGeometry(
                int(W * 0.60), int(H * 0.30),
                int(W * 0.25), int(H * 0.08)
        )



        self.fournisseur_window.show()


    def type_fournisseur(self):
        type_fournisseur = self.choix_type_fournisseur.currentText()
        if type_fournisseur=="Personne physique":
           self.choix_type_societe.setEnabled(True)
           self.line_nom_societe.setEnabled(True)
           self.line_add_societe.setEnabled(True)
        else:
           self.choix_type_societe.setEnabled(False)
           self.line_nom_societe.setEnabled(False)
           self.line_add_societe.setEnabled(False)
           self.choix_type_societe.clear()
           self.line_nom_societe.clear()
           self.line_add_societe.clear()