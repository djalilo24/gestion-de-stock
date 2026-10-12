from PyQt5 import QtCore, QtGui, QtWidgets

class Product(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.product_ui()
    def product_ui(self):
        self.group_form_product = QtWidgets.QVBoxLayout(self)
        #====================Bouton add product=========================
        self.add_product_button = QtWidgets.QPushButton("Ajouter un produit")   
        self.add_product_button.setIcon(QtGui.QIcon("icons/add.png"))
        self.add_product_button.setObjectName("add_button")
        self.add_product_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_product_button.setToolTip("Ajouter un nouveau produit")
        self.add_product_button.setToolTipDuration(3000)  # Durée d'aff
        self.add_product_button.setIconSize(QtCore.QSize(24, 24))
        self.add_product_button.clicked.connect(self.form_product)
        #====================title=========================
        self.title_label = QtWidgets.QLabel("Liste des produits")       
        self.title_label.setObjectName("title_group")
        #self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        #====================add widget =========================
        self.group_box_table = QtWidgets.QGroupBox()
        self.group_form_product.addWidget(self.group_box_table)
        self.layout_table = QtWidgets.QVBoxLayout(self.group_box_table) 
        self.headre_layout = QtWidgets.QHBoxLayout()
        self.headre_layout.addWidget(self.title_label)
        self.headre_layout.addStretch()  # Ajouter un espace flexible pour pousser le bouton vers la droite
        self.headre_layout.addWidget(self.add_product_button)
        self.layout_table.addLayout(self.headre_layout)
        #====================table product=========================
        self.table_prodect = QtWidgets.QTableWidget()
        self.table_prodect.setRowCount(3)
        self.table_prodect.setColumnCount(5)
        self.table_prodect.setHorizontalHeaderLabels(["ID", "Nom", "Prix", "Quantité", "Description"])  
        data = [
           ["1", "Tissu coton", "Matière première", "150", "500"],
           ["2", "Fil à coudre", "Matière première", "80", "120"],
           ["3", "Chemise", "Produit fini", "25", "2500"]
            ]   
        for row, values in enumerate(data):
           for col, value in enumerate(values):
               self.table_prodect.setItem(row, col,QtWidgets.QTableWidgetItem(value))
        self.table_prodect.horizontalHeader().setStretchLastSection(True)
        self.table_prodect.setAlternatingRowColors(True) 
        self.layout_table.addWidget(self.table_prodect)      

    def form_product(self):
        self.product_window = QtWidgets.QWidget()
        self.product_window.setWindowTitle("Ajouter un produit")

        screen = QtWidgets.QApplication.primaryScreen()
        geometry = screen.availableGeometry()

        W = int(geometry.width() * 0.50)
        H = int(geometry.height() * 0.50)

        self.product_window.resize(W, H)

        self.labele_code_produit = QtWidgets.QLabel("Code du produit", self.product_window)
        self.labele_code_produit.setGeometry(
             int(W * 0.52), int(H * 0.05),
             int(W * 0.90), int(H * 0.10))
        self.line_edite_code = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_code.setPlaceholderText("Code du produit")
        self.line_edite_code.setGeometry(
             int(W * 0.68), int(H * 0.05),
             int(W * 0.30), int(H * 0.10))
        self.line_edite_code.setEnabled(False)  

        self.labele_choix_produit = QtWidgets.QLabel("Type de produit", self.product_window)
        self.labele_choix_produit .setGeometry(
             int(W * 0.05), int(H * 0.05),
             int(W * 0.90), int(H * 0.12))
        self.choix_produit = QtWidgets.QComboBox(self.product_window)
        self.choix_produit.setGeometry(
             int(W * 0.20), int(H * 0.05),
             int(W * 0.30), int(H * 0.10))
        self.choix_produit.addItems(["","Matière première","Produit fini"])
        self.choix_produit.currentIndexChanged.connect(lambda: self.choice_product(H, W))

        self.label_nom_produit = QtWidgets.QLabel("Nom du produit", self.product_window)
        self.label_nom_produit.setGeometry(
             int(W * 0.05), int(H * 0.20),
             int(W * 0.90), int(H * 0.10))
        self.label_nom_produit.setVisible(False)  # Masquer le label au départ
        self.line_edite_nom = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_nom.setPlaceholderText("Nom du produit")
        self.line_edite_nom.setGeometry(
             int(W * 0.20), int(H * 0.20),
             int(W * 0.30), int(H * 0.10))
        self.line_edite_nom.setVisible(False)  # Masquer le QLineEdit au départ
        self.quintite_label = QtWidgets.QLabel("Quantité minimale", self.product_window)
        self.quintite_label.setGeometry(
             int(W * 0.52), int(H * 0.20),
             int(W * 0.90), int(H * 0.10))
        self.quintite_label.setVisible(False)  # Masquer le label au départ
        self.line_edite_quantite = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_quantite.setPlaceholderText("Quantité minimale")
        self.line_edite_quantite.setGeometry(
             int(W * 0.72), int(H * 0.20),
             int(W * 0.20), int(H * 0.10))  
        self.line_edite_quantite.setVisible(False)  # Masquer le QLineEdit au départ  

        self.label_fournisseur = QtWidgets.QLabel("Fournisseur", self.product_window)
        self.label_fournisseur.setGeometry(
             int(W * 0.05), int(H * 0.35),
             int(W * 0.20), int(H * 0.10))   
        self.label_fournisseur.setVisible(False)  # Masquer le label au départ
        self.line_edite_fournisseur = QtWidgets.QComboBox(self.product_window)
        self.line_edite_fournisseur.setPlaceholderText("Fournisseur")
        self.line_edite_fournisseur.setGeometry(
             int(W * 0.20), int(H * 0.35),
             int(W * 0.30), int(H * 0.10))
        self.line_edite_fournisseur.setVisible(False)  # Masquer le QLineEdit au départ

        self.lable_categorie_produit = QtWidgets.QLabel("Catégorie de produit",self.product_window)
        self.lable_categorie_produit.setGeometry(
             int(W * 0.52), int(H * 0.35),
             int(W * 0.20), int(H * 0.10))
        self.lable_categorie_produit.setVisible(False)
        self.choix_categorie = QtWidgets.QComboBox(self.product_window)
        self.choix_categorie.setGeometry(
             int(W * 0.72), int(H * 0.35),
             int(W * 0.25), int(H * 0.10)           
        )
        self.choix_categorie.addItems(["","Tissu","Fil à coudre","Boton","Fermeture éclair","Doublure","Élastique","Accessoires","Emballage","Autre" ])
        self.choix_categorie.setVisible(False)

        self.lable_color_produit = QtWidgets.QLabel("Coulor de produit",self.product_window)
        self.lable_color_produit.setGeometry(
             int(W * 0.05), int(H * 0.50),
             int(W * 0.25), int(H * 0.10)  
        )
        self.lable_color_produit.setVisible(False)
        self.line_color_produit = QtWidgets.QLineEdit(self.product_window)
        self.line_color_produit.setPlaceholderText("Coulor")
        self.line_color_produit.setGeometry(
             int(W * 0.22), int(H * 0.50),
             int(W * 0.15), int(H * 0.10)   
        )
        self.line_color_produit.setVisible(False)

        #quentiti+prix d'acha

        

        self.product_window.show()


    def choice_product(self, H, W):
        selected_product = self.choix_produit.currentText()
        if selected_product == "Matière première":
               self.label_nom_produit.setVisible(True)  # Afficher le label
               self.line_edite_nom.setVisible(True)  # Afficher le QLineEdit
               self.quintite_label.setVisible(True)  # Afficher le label
               self.line_edite_quantite.setVisible(True)  # Afficher le QLineEdit
               self.label_fournisseur.setVisible(True)  # Afficher le label
               self.line_edite_fournisseur.setVisible(True)  # Afficher le QLine
               self.lable_categorie_produit.setVisible(True)
               self.choix_categorie.setVisible(True)
               self.lable_color_produit.setVisible(True)
               self.line_color_produit.setVisible(True)


        elif selected_product == "Produit fini":
            print("Produit fini selected")
