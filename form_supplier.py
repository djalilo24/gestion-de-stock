from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import traceback
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
        self.table_fournisseur.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_fournisseur.setColumnCount(5)
        all_fournisseur = self.recovry_all_fournisseur()
        self.table_fournisseur.setRowCount(len(all_fournisseur))
        self.table_fournisseur.setHorizontalHeaderLabels(["ID","Type fournisseur","Nom et Prenom", "Telephone","Nom societe"])  
        for row, values in enumerate(all_fournisseur):
           if values[5]==1:
               color=QtGui.QColor("#90EE90")
           else:
               color=QtGui.QColor("#FFC8C8")  
           for col in range(5):
                value = values[col]
                item = QtWidgets.QTableWidgetItem("" if value is None else str(value))   
                item.setBackground(color)
                self.table_fournisseur.setItem(row, col,item)
                self.table_fournisseur.resizeColumnsToContents()
        self.table_fournisseur.horizontalHeader().setStretchLastSection(True)
        self.table_fournisseur.setAlternatingRowColors(False) 
        self.table_fournisseur.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_fournisseur.customContextMenuRequested.connect(self.show_list_menu)
        self.layout_table.addWidget(self.table_fournisseur)
        #=========function form fournisseur===============
    data_fournisseur = None
    def form_fournisseur(self,data_fournisseur):
      print("data=",data_fournisseur)
      if not data_fournisseur:
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
        self.line_code_fournisseur.setText("#"+str(int(self.recovry_id_fournisseur())+1))
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
        self.lable_type_societe = QtWidgets.QLabel("Genre societé",self.fournisseur_window)
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
                int(W * 0.27), int(H * 0.30),
                int(W * 0.11), int(H * 0.08)            
        )
        self.line_nom_societe = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_nom_societe.setEnabled(False)
        self.line_nom_societe.setGeometry(
                int(W * 0.37), int(H * 0.30),
                int(W * 0.30), int(H * 0.08)            
        )

        self.lable_nom = QtWidgets.QLabel("Nom de fournisseur",self.fournisseur_window)
        self.lable_nom.setGeometry(
                int(W * 0.05), int(H * 0.45),
                int(W * 0.15), int(H * 0.08)                
        )
        self.line_nom = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_nom.setPlaceholderText("Nom de fournissseur")
        self.line_nom.setGeometry(
                int(W * 0.19), int(H * 0.45),
                int(W * 0.18), int(H * 0.08)                  
        )
        
        self.lable_prenom = QtWidgets.QLabel("Prenom de fournisseur",self.fournisseur_window)
        self.lable_prenom.setGeometry(
                int(W * 0.37), int(H * 0.45),
                int(W * 0.15), int(H * 0.08)                
        )
        self.line_prenom = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_prenom.setPlaceholderText("Prenom de fournissseur")
        self.line_prenom.setGeometry(
                int(W * 0.52), int(H * 0.45),
                int(W * 0.18), int(H * 0.08)                  
        )
        self.lable_date_naissance = QtWidgets.QLabel("Date de naissance",self.fournisseur_window)
        self.lable_date_naissance.setGeometry(
                int(W * 0.70), int(H * 0.45),
                int(W * 0.15), int(H * 0.08)                
        )  
        self.date_naissance = QtWidgets.QDateEdit(self.fournisseur_window)  
        self.date_naissance.setDate(QtCore.QDate.currentDate())   
        self.date_naissance.setGeometry(
                int(W * 0.83), int(H * 0.45),
                int(W * 0.15), int(H * 0.08)                  
        )
        self.nin_lable = QtWidgets.QLabel("Numéro identifiant nationale(NIN)",self.fournisseur_window)
        self.nin_lable.setGeometry(
                int(W * 0.05), int(H * 0.60),
                int(W * 0.25), int(H * 0.08)                 
        )
        self.line_nin = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_nin.setPlaceholderText("NIN")
        self.line_nin.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[0-9]{0,18}")))
        self.line_nin.setGeometry(
                int(W * 0.28), int(H * 0.60),
                int(W * 0.20), int(H * 0.08)  
        )
        self.lable_nif =QtWidgets.QLabel("Numéro identifiant fiscale(NIF)",self.fournisseur_window)
        self.lable_nif.setGeometry(
                int(W * 0.53), int(H * 0.60),
                int(W * 0.25), int(H * 0.08)                
        )
        self.line_nif = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_nif.setPlaceholderText("NIF")
        self.line_nif.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[0-9]{0,20}")))
        self.line_nif.setGeometry(
                int(W * 0.73), int(H * 0.60),
                int(W * 0.22), int(H * 0.08)  
        )
        self.lable_add = QtWidgets.QLabel("Address ",self.fournisseur_window)
        self.lable_add.setGeometry(
                int(W * 0.17), int(H * 0.70),
                int(W * 0.11), int(H * 0.08)
        )
        self.line_add = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_add.setPlaceholderText("address")
        self.line_add.setGeometry(
                int(W * 0.24), int(H * 0.70),
                int(W * 0.30), int(H * 0.08)
        )
        self.lable_tel = QtWidgets.QLabel("Telephone",self.fournisseur_window)
        self.lable_tel.setGeometry(
                int(W * 0.58), int(H * 0.70),
                int(W * 0.08), int(H * 0.08)               
        )
        self.line_tel = QtWidgets.QLineEdit(self.fournisseur_window)
        self.line_tel.setPlaceholderText("telephone")
        self.line_tel.setGeometry(
                int(W * 0.66), int(H * 0.70),
                int(W * 0.15), int(H * 0.08)
        )
        self.lable_etes = QtWidgets.QLabel("Etes de fournisseur")
        self.lable_etes.setGeometry(
                int(W * 0.20), int(H * 0.82),
                int(W * 0.15), int(H * 0.08)                
        )

    #============bouton==============
        self.bouton_add_fournisseur = QtWidgets.QPushButton("Ajeuter fournisseur",self.fournisseur_window)
        self.bouton_add_fournisseur.setIcon(QtGui.QIcon("icons/add.png"))
        self.bouton_add_fournisseur.setIconSize(QtCore.QSize(int(H * 5.5/ 100), int(W* 5.5 / 100)))
        self.bouton_add_fournisseur.setGeometry(
                int(W * 0.70), int(H * 0.82),
                int(W * 0.28), int(H * 0.12)
        ) 
        self.bouton_add_fournisseur.clicked.connect(self.add_fournisseur) 
        self.btn_active = QtWidgets.QPushButton("ACTIVE",self.fournisseur_window)
        self.btn_active.setObjectName("btn_active")
        self.btn_active.setCheckable(True)
        self.btn_active.setChecked(True)
        self.btn_active.setVisible(False)
        self.btn_active.setGeometry(
                int(W * 0.20), int(H * 0.82),
                int(W * 0.28), int(H * 0.12)           
        )
        self.btn_active.toggled.connect(lambda checked: self.btn_active.setText("ACTIVE" if checked else "ARRETER"))
      
        
        self.fournisseur_window.show()
#============function active societe===================
    def type_fournisseur(self):
        type_fournisseur = self.choix_type_fournisseur.currentText()
        if type_fournisseur=="Personne physique":
           self.choix_type_societe.setEnabled(True)
           self.line_nom_societe.setEnabled(True)

        else:
           self.choix_type_societe.setEnabled(False)
           self.line_nom_societe.setEnabled(False)
           self.choix_type_societe.setCurrentIndex(0)
           self.line_nom_societe.clear()
#============function add supplier in database==================
    def add_fournisseur(self):
            id_fournisseur = int((self.line_code_fournisseur.text().strip()).split("#")[-1])
            type_fournisseur = self.choix_type_fournisseur.currentText().strip()
            genre_fournisseur = self.choix_type_societe.currentText().strip()
            nom_societe = self.line_nom_societe.text().strip()
            nom = self.line_nom.text().strip()
            prenom = self.line_prenom.text().strip()
            date_naissance = self.date_naissance.date().toString("yyyy-MM-dd")
            nin = self.line_nin.text().strip()
            nif = self.line_nif.text().strip()
            adresse = self.line_add.text().strip()
            telephone = self.line_tel.text().strip()
            result = self.verify(nin,nif,date_naissance)
            if result[0]==False:
                QMessageBox.warning(self,"Erreur de validation",str(result[1]+"\n"+result[2]+"\n"+result[3]))  
            else:
                try:
                   conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="guelma24@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
                   cursor = conn.cursor()
                   sql_insert =("""INSERT INTO fournisseur(id_fournisseur,type_fournisseur,genre_fournisseur,nom_societe,nom,prenom,date_naissance,nin,nif,telephone,adresse)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""")
                   data =(id_fournisseur,type_fournisseur,genre_fournisseur,nom_societe,nom,prenom,date_naissance,nin,nif,telephone,adresse)
                   cursor.execute(sql_insert,data)
                   conn.commit()
                   QMessageBox.information(None,"Information","Le fournisseur a été ajouté avec succès.")
                except mysql.connector.Error as err:
                       QMessageBox.critical( None,"Erreur",f"Une erreur est survenue lors de l'ajout du fournisseur :\n{err}")
                finally:
                     if conn.is_connected():
                       #cursor.close()
                       conn.close()    
                                
#=============function verify value=============
    def verify(self,nin,nif,date_naissance):
        msg1="" 
        msg2=""
        msg3=""
        if nin:
           if len(nin)!=18:
              msg1="Vérifier numéro identifiant nationale(NIN)"
        if nif:      
           if len(nif) not in (12,20) :
              msg2="Vérifier numéro identifiant fiscale(NIF)"    
        if date_naissance:
             date_naissance = self.date_naissance.date()
             if date_naissance >= QDate.currentDate():
               msg3="La date de naissance est invalide"
        if msg1 or msg2 or msg3:
           return False,msg1,msg2,msg3
        else:
                return True,"","",""
#=============function recovry id_fournisseur=============  
    def recovry_id_fournisseur(self):
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="guelma24@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id_fournisseur) FROM fournisseur ")
            reslt = cursor.fetchone()
            return reslt[0] 
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.close()
                   conn.close() 
#-----------------------------------------
    def recovry_all_fournisseur(self):
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="guelma24@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT CONCAT('#', id_fournisseur),type_fournisseur,CONCAT(nom, ' ', prenom),telephone,nom_societe,ETES FROM fournisseur ")
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
        index = self.table_fournisseur.indexAt(pos)
        if not index.isValid():
           return
        row = index.row()
        self.table_fournisseur.selectRow(row)  
        menu = QtWidgets.QMenu(self.table_fournisseur)
        action_edit = menu.addAction("Modifier les informations")
        action = menu.exec_(self.table_fournisseur.viewport().mapToGlobal(pos))
        if action == action_edit:
           self.modify_op()
#..........................recovery fournisseur........................................
    def modify_op(self):       
        row_count = self.table_fournisseur.currentRow()
        id_f = (self.table_fournisseur.item(row_count, 0).text()).split("#")[-1]
        try:
            conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="guelma24@",
                     database="nakhla",
                     connection_timeout=10,
                     use_pure=True  ) 
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fournisseur where id_fournisseur=%s",(int(id_f),))
            reslt= cursor.fetchall()
            self.form_fournisseur(reslt)
        except mysql.connector.Error as err:
                QMessageBox.critical( None,"Erreur",f"Une erreur est recuperation id du fournisseur :\n{err}")
        finally:
                if conn.is_connected():
                   #cursor.close()
                   conn.close() 
#..........................update fournisseur........................................  
    def update_fournisseyr(self,reslt):
        self.line_code_fournisseur.text().strip().split("#")[-1]
        self.choix_type_fournisseur.currentText().strip()
        self.choix_type_societe.currentText().strip()
        self.line_nom_societe.text().strip()
        self.line_nom.text().strip()
        self.line_prenom.text().strip()
        self.date_naissance.date().toString("yyyy-MM-dd")
        self.line_nin.text().strip()
        self.line_nif.text().strip()
        self.line_add.text().strip()
        self.line_tel.text().strip()
        result = self.verify(nin,nif,date_naissance)  
         
            
            

           
         
           