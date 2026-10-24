from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
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
        self.table_prodect.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_prodect.setColumnCount(6)
        all_produits=self.recovry_all_produits()
        self.table_prodect.setRowCount(len(all_produits))
        self.table_prodect.setHorizontalHeaderLabels(["ID", "Nom", "type produit", "Categorie","Coleur", "Quantité"]) 
        for row, values in enumerate(all_produits):
           if values[5]>=values[6]:
               color=QtGui.QColor("#90EE90")
           else:
               color=QtGui.QColor("#FFC8C8")  
           for col in range(6):
                value = values[col]
                item = QtWidgets.QTableWidgetItem("" if value is None else str(value))   
                item.setBackground(color)
                self.table_prodect.setItem(row, col,item)
                self.table_prodect.resizeColumnsToContents()
        self.table_prodect.horizontalHeader().setStretchLastSection(True)
        self.table_prodect.setAlternatingRowColors(False) 
        self.table_prodect.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_prodect.customContextMenuRequested.connect(self.show_list_menu)
        self.layout_table.addWidget(self.table_prodect)     

    def form_product(self):
        self.product_window = QtWidgets.QWidget()
        self.product_window.setWindowTitle("Ajouter un produit")

        screen = QtWidgets.QApplication.primaryScreen()
        geometry = screen.availableGeometry()

        W = int(geometry.width() * 0.70)
        H = int(geometry.height() * 0.70)

        self.product_window.resize(W, H)

        self.labele_code_produit = QtWidgets.QLabel("Code du produit", self.product_window)
        self.line_edite_code = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_code.setText("#"+str(int(self.recovry_id_produit())+1))
        self.line_edite_code.setEnabled(False)  

        self.labele_choix_produit = QtWidgets.QLabel("Type de produit", self.product_window)
        self.choix_produit = QtWidgets.QComboBox(self.product_window)
        self.choix_produit.addItems(["","Matière première","Produit fini"])
        self.choix_produit.currentIndexChanged.connect(lambda: self.choice_product(H, W))

        self.label_nom_produit = QtWidgets.QLabel("Nom du produit", self.product_window)
        self.label_nom_produit.setVisible(False)  # Masquer le label au départ
        self.line_edite_nom = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_nom.setPlaceholderText("Nom du produit")
        self.line_edite_nom.setVisible(False)  # Masquer le QLineEdit au départ
        self.q_min_label = QtWidgets.QLabel("Quantité minimale", self.product_window)
        self.q_min_label.setVisible(False)  # Masquer le label au départ
        self.line_edite_q_min = QtWidgets.QLineEdit(self.product_window)
        self.line_edite_q_min.setPlaceholderText("Quantité minimale")
        self.line_edite_q_min.setVisible(False)  # Masquer le QLineEdit au départ  

        self.label_fournisseur = QtWidgets.QLabel("Fournisseur", self.product_window)  
        self.label_fournisseur.setVisible(False)  # Masquer le label au départ
        self.choix_fournisseur = QtWidgets.QComboBox(self.product_window)
        self.choix_fournisseur.setPlaceholderText("Choisir un fournisseur")
        #self.choix_fournisseur.currentTextChanged.connect(self.change_fournisseur)
        self.choix_fournisseur.setVisible(False)  # Masquer le QLineEdit au départ

        self.lable_categorie_produit = QtWidgets.QLabel("Catégorie de produit",self.product_window)
        self.lable_categorie_produit.setVisible(False)
        self.choix_categorie = QtWidgets.QComboBox(self.product_window)         
        self.choix_categorie.addItems(["","Tissu","Fil à coudre","Boton","Fermeture éclair","Doublure","Élastique","Accessoires","Emballage","Autre" ])
        self.choix_categorie.setVisible(False)

        self.lable_color_produit = QtWidgets.QLabel("Coulor de produit",self.product_window)
        self.lable_color_produit.setVisible(False)
        self.line_color_produit = QtWidgets.QLineEdit(self.product_window)
        self.line_color_produit.setPlaceholderText("Coulor")
        self.line_color_produit.setVisible(False)

        self.lable_quintite =QtWidgets.QLabel("Quintite",self.product_window)
        self.lable_quintite.setVisible(False)
        self.line_quintite = QtWidgets.QLineEdit(self.product_window)
        self.line_quintite.setVisible(False)
        
        self.lable_prix = QtWidgets.QLabel("Prix d'achat",self.product_window)
        self.lable_prix.setVisible(False)
        self.line_prix = QtWidgets.QLineEdit(self.product_window)
        self.line_prix.setPlaceholderText("DA")
        self.line_prix.setVisible(False)
        
        self.lable_date_achat = QtWidgets.QLabel("Date d'achat",self.product_window)
        self.lable_date_achat.setVisible(False)
        self.date_achat = QtWidgets.QDateEdit(self.product_window)
        self.date_achat.setDisplayFormat("dd-MM-yyyy")
        self.date_achat.setDate(QtCore.QDate.currentDate())
        self.date_achat.setVisible(False)
        

       # Code du produit
        self.labele_code_produit.setGeometry(
    int(W * 0.52), int(H * 0.05),
    int(W * 0.15), int(H * 0.08)
)
        self.line_edite_code.setGeometry(
    int(W * 0.70), int(H * 0.05),
    int(W * 0.25), int(H * 0.08)
)

# Type de produit
        self.labele_choix_produit.setGeometry(
    int(W * 0.05), int(H * 0.05),
    int(W * 0.15), int(H * 0.08)
)
        self.choix_produit.setGeometry(
    int(W * 0.22), int(H * 0.05),
    int(W * 0.25), int(H * 0.08)
)

# Nom du produit
        self.label_nom_produit.setGeometry(
    int(W * 0.05), int(H * 0.20),
    int(W * 0.15), int(H * 0.08)
)
        self.line_edite_nom.setGeometry(
    int(W * 0.22), int(H * 0.20),
    int(W * 0.25), int(H * 0.08)
)

# Quantité minimale
        self.q_min_label.setGeometry(
    int(W * 0.52), int(H * 0.20),
    int(W * 0.20), int(H * 0.08)
)
        self.line_edite_q_min.setGeometry(
    int(W * 0.70), int(H * 0.20),
    int(W * 0.23), int(H * 0.08)
)

# Fournisseur
        self.label_fournisseur.setGeometry(
    int(W * 0.05), int(H * 0.35),
    int(W * 0.15), int(H * 0.08)
)
        self.choix_fournisseur.setGeometry(
    int(W * 0.22), int(H * 0.35),
    int(W * 0.25), int(H * 0.08)
)

# Catégorie de produit
        self.lable_categorie_produit.setGeometry(
    int(W * 0.52), int(H * 0.35),
    int(W * 0.20), int(H * 0.08)
)
        self.choix_categorie.setGeometry(
    int(W * 0.72), int(H * 0.35),
    int(W * 0.23), int(H * 0.08)
)

# Couleur du produit
        self.lable_color_produit.setGeometry(
    int(W * 0.05), int(H * 0.50),
    int(W * 0.17), int(H * 0.08)
)
        self.line_color_produit.setGeometry(
    int(W * 0.22), int(H * 0.50),
    int(W * 0.15), int(H * 0.08)
)

# Quantité
        self.lable_quintite.setGeometry(
    int(W * 0.40), int(H * 0.50),
    int(W * 0.10), int(H * 0.08)
)
        self.line_quintite.setGeometry(
    int(W * 0.50), int(H * 0.50),
    int(W * 0.12), int(H * 0.08)
)

# Prix d'achat
        self.lable_prix.setGeometry(
    int(W * 0.65), int(H * 0.50),
    int(W * 0.12), int(H * 0.08)
)
        self.line_prix.setGeometry(
    int(W * 0.78), int(H * 0.50),
    int(W * 0.17), int(H * 0.08)
)
# date d'achat
        self.lable_date_achat.setGeometry(
    int(W * 0.05), int(H * 0.65),
    int(W * 0.15), int(H * 0.08)       
        )
        self.date_achat.setGeometry(
    int(W * 0.22), int(H * 0.65),
    int(W * 0.17), int(H * 0.08)            
        )
    #============bouton==============
        self.bouton_add_produit = QtWidgets.QPushButton("Ajeuter produit",self.product_window)
        self.bouton_add_produit.setIcon(QtGui.QIcon("icons/add.png"))
        self.bouton_add_produit.setIconSize(QtCore.QSize(int(H * 5.5/ 100), int(W* 5.5 / 100)))
        self.bouton_add_produit.setGeometry(
                int(W * 0.70), int(H * 0.65),
                int(W * 0.28), int(H * 0.12)
        ) 
        self.bouton_add_produit.clicked.connect(self.recovre_add_produit) 
        self.bouton_add_produit.setVisible(False)     

        self.product_window.show()
        

    def choice_product(self, H, W):
        selected_product = self.choix_produit.currentText()
        if selected_product == "Matière première":
            self.bouton_add_produit.setVisible(True)
            self.label_nom_produit.setVisible(True)  # Afficher le label
            self.line_edite_nom.setVisible(True)  # Afficher le QLineEdit
            self.q_min_label.setVisible(True)  # Afficher le label
            self.line_edite_q_min.setVisible(True)  # Afficher le QLineEdit
            self.label_fournisseur.setVisible(True)  # Afficher le label
            self.choix_fournisseur.setVisible(True)  # Afficher le QLine  
            self.change_fournisseur() 
            self.lable_categorie_produit.setVisible(True)
            self.choix_categorie.setVisible(True)
            self.lable_color_produit.setVisible(True)
            self.line_color_produit.setVisible(True)
            self.lable_quintite.setVisible(True)
            self.line_quintite.setVisible(True)
            self.lable_prix.setVisible(True)
            self.line_prix.setVisible(True)
            self.lable_date_achat.setVisible(True)
            self.date_achat.setVisible(True)


        elif selected_product == "Produit fini":
            print("Produit fini selected")
#=================function add produit,stock;achat;ligne d'achat======   
    def recovre_add_produit(self):
        id_produit = int((self.line_edite_code.text().strip()).split("#")[-1])  #produit
        nom = self.line_edite_nom.text().strip()  #produit
        type_produit = self.choix_produit.currentText() #produit
        seuil_alerte = self.line_edite_q_min.text().strip()#produit
        coleur = self.line_color_produit.text().strip() #produit
        categorie = self.choix_categorie.currentText() #produit
        texte = self.choix_fournisseur.currentText()
        id_fournisseur = int(texte.split("#")[1].split()[0]) #achat   
        quantite = self.line_quintite.text().strip() #stock
        prix_unitaire = self.line_prix.text().strip()#ligne d'achat
        date_achat = self.date_achat.date().toString("yyyy-MM-dd") #achat   
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="alilomoh24021989@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            insert = conn.cursor()
            sql_produit =("""INSERT INTO produit(id_produit,nom,type_produit,seuil_alerte,coleur,categorie)
                   VALUES (%s, %s, %s, %s, %s, %s)""")
            data_produit =(id_produit,nom,type_produit,seuil_alerte,coleur,categorie)
            insert.execute(sql_produit,data_produit)
            sql_stock =("""INSERT INTO stock(id_produit,quantite)VALUES (%s, %s)""")
            data_stock =(id_produit,quantite)
            insert.execute(sql_stock,data_stock)  
            sql_achat = ("""INSERT INTO achat(id_fournisseur,date_achat) VALUES (%s, %s)""")
            data_achat = (id_fournisseur,date_achat)
            insert.execute(sql_achat,data_achat)
            id_achat = insert.lastrowid
            sql_ligne_achat = ("""INSERT INTO ligne_achat(id_achat,id_produit,quantite,prix_unitaire) VALUES (%s, %s,%s, %s)""")
            data_ligne_achat = (id_achat,id_produit,quantite,prix_unitaire)         
            insert.execute(sql_ligne_achat,data_ligne_achat)
            conn.commit()
            QMessageBox.information(None,"Information","Le produit a été ajouté avec succès.")
            self.product_window.close()
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.clos
                   conn.close() 
#==================function recovry list of supplier==================   
    def change_fournisseur(self):
        self.choix_fournisseur.clear()
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="alilomoh24021989@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT id_fournisseur,type_fournisseur,genre_fournisseur,nom,prenom,nom_societe FROM fournisseur where etes=%s",(1,))
            reslt = cursor.fetchall()
            for i in reslt:
                if i[1]=="Personne physique":
                    choix=f"#{i[0]} - {i[2]} _ {i[5]}"
                else:
                    choix = f"#{i[0]} - {i[3]} {i[4]}"
                self.choix_fournisseur.addItem(choix)
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.clos
                   conn.close()  
#=============function recovry id_produit=============  
    def recovry_id_produit(self):
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="alilomoh24021989@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id_produit) FROM produit ")
            reslt = cursor.fetchone()
            print ("rrrr",reslt)
            if reslt[0] is None:
                return 0
            else :
                return reslt[0]
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.close()
                   conn.close() 
#-------------------function recovry produits----------------------
    def recovry_all_produits(self):
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="alilomoh24021989@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT P.id_produit,P.nom,P.type_produit,P.Categorie,P.coleur,S.quantite,P.seuil_alerte FROM produit P "\
            "JOIN stock S on P.id_produit=S.id_produit ")
            reslt = cursor.fetchall()
            return reslt 
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.close()
                   conn.close() 
#..........................function menu liste........................................
    def show_list_menu(self, pos):
        index = self.table_prodect.indexAt(pos)
        if not index.isValid():
           return
        row = index.row()
        self.table_prodect.selectRow(row)  
        menu = QtWidgets.QMenu(self.table_prodect)
        augmante = menu.addAction("Augmenté la quintité")
        modifier = menu.addAction("Modifier les informations")
        action = menu.exec_(self.table_prodect.viewport().mapToGlobal(pos))
        if action == augmante:
             self.augment()
        elif action == modifier:
           self.modify_prouit()
#=====================function augment===============================
    def augment(self):
        dialog = QtWidgets.QDialog(self.table_prodect)
        dialog.setWindowTitle("Augmenté la quintité")
        dialog.setFixedSize(300, 150)

        dialog.exec_()