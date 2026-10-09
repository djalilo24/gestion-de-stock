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
        self.product_label = QtWidgets.QLabel("Nouveau produit", self.product_window)
        self.product_label.setGeometry(
             int(W * 0.05), int(H * 0.05),
             int(W * 0.90), int(H * 0.12))
        self.line_edite_nom = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_nom.setPlaceholderText("Nom du produit")
        self.line_edite_nom.setGeometry(
             int(W * 0.010), int(H * 0.25),
             int(W * 0.30), int(H * 0.10))
        self.product_window.show()