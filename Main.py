from PyQt5 import QtCore, QtGui, QtWidgets
from style import use_style
from PyQt5.QtGui import QIcon
from form_supplier import Fournisseurs
from product import Product
from from_home import Home
from PyQt5.QtWidgets import QWidget
import mysql.connector
import traceback
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Gestion de Stock")
#================taille screen============================
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        #===========pocentge========
        percentage = 85
        window_width = int(screen_width * percentage / 100)
        window_height = int(screen_height * percentage / 100)
        MainWindow.resize(window_width, window_height)

        #===========centre screen======
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        MainWindow.move(x, y)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
#==========layout pricipale====================
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        #=================group menu=========================
        self.group_menu = QtWidgets.QGroupBox()
        self.group_menu.setObjectName("group_menu")
        self.group_menu.setTitle("MENU")
        #=====================group content=========================
        self.main_content = QtWidgets.QGroupBox()
        self.main_content.setObjectName("main_content")
        # ================= pages =========================
        self.pages = QtWidgets.QStackedWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.main_content)
        self.content_layout.setContentsMargins(10, 10, 10, 10)
        self.content_layout.addWidget(self.pages) 
        #=================add layout=========================
        self.main_layout.addWidget(self.group_menu, 2)
        self.main_layout.addWidget(self.main_content, 8)
#=====================add button=========================
        #============group box users============
        self.users_group = QtWidgets.QGroupBox()
        self.users_group.setObjectName("users_group")
        self.users_group.setTitle("Utilisateurs")
        self.user_line_edit = QtWidgets.QLineEdit(self.users_group)
        self.user_line_edit.setObjectName("user_line_edit")
        self.mop_pass = QtWidgets.QLineEdit(self.users_group)
        self.mop_pass.setObjectName("mop_pass")
        self.mop_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        w_goupUser = self.users_group.width()
        h_goupUser = self.users_group.height()
        self.user_line_edit.setGeometry(int(w_goupUser * 0.02), int(h_goupUser * 0.2), int(w_goupUser * 0.2), int(h_goupUser * 0.3))
        self.mop_pass.setGeometry(int(w_goupUser * 0.1), int(h_goupUser * 0.6), int(w_goupUser * 0.8), int(h_goupUser * 0.3))
        #============bouton home============
        self.btn_home = QtWidgets.QPushButton(self.group_menu)
        self.btn_home.setText(" Tableau de bord")
        self.btn_home.setIcon(QtGui.QIcon("icons/research.png"))
        self.btn_home.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        self.btn_home.clicked.connect(self.home_button_clicked)
        #============bouton product============
        self.btn_product = QtWidgets.QPushButton(self.group_menu)
        self.btn_product.setText(" Produits")
        self.btn_product.setIcon(QtGui.QIcon("icons/products.png"))
        self.btn_product.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        self.btn_product.clicked.connect(self.product_button_clicked)
        #============bouton depot============
        self.btn_depot = QtWidgets.QPushButton(self.group_menu)
        self.btn_depot.setText(" Dépôt")
        self.btn_depot.setIcon(QtGui.QIcon("icons/depot.png"))
        self.btn_depot.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        #============bouton stock============
        self.btn_stock = QtWidgets.QPushButton(self.group_menu)
        self.btn_stock.setText(" Stock")
        self.btn_stock.setIcon(QtGui.QIcon("icons/in-stock.png"))
        self.btn_stock.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        #============bouton achat============
        self.btn_achat = QtWidgets.QPushButton(self.group_menu)
        self.btn_achat.setText(" Achat")
        self.btn_achat.setIcon(QtGui.QIcon("icons/achat.png"))
        self.btn_achat.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        #============bouton prodection============
        self.btn_production = QtWidgets.QPushButton(self.group_menu)
        self.btn_production.setText(" Production")
        self.btn_production.setIcon(QtGui.QIcon("icons/production.png"))
        self.btn_production.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        #===========bouton supplier ============
        self.btn_fournisseurs = QtWidgets.QPushButton(self.group_menu)
        self.btn_fournisseurs.setText(" Fournisseurs")
        self.btn_fournisseurs.setIcon(QtGui.QIcon("icons/team.png"))
        self.btn_fournisseurs.setIconSize(QtCore.QSize(int(screen_height * 5/ 100), int(screen_height * 5 / 100)))
        self.btn_fournisseurs.clicked.connect(self.supplier_button_clicked)
        #========bouton selected===============
        self.menu_group = QtWidgets.QButtonGroup(MainWindow)
        self.menu_group.setExclusive(True)
        self.btn_home.setCheckable(True)
        self.btn_product.setCheckable(True)
        self.btn_depot.setCheckable(True)
        self.btn_stock.setCheckable(True)
        self.btn_achat.setCheckable(True)
        self.btn_production.setCheckable(True)
        self.btn_fournisseurs.setCheckable(True)
        self.menu_group.addButton(self.btn_home)
        self.menu_group.addButton(self.btn_achat)
        self.menu_group.addButton(self.btn_product)
        self.menu_group.addButton(self.btn_depot)   
        self.menu_group.addButton(self.btn_stock)    
        self.menu_group.addButton(self.btn_production)
        self.menu_group.addButton(self.btn_fournisseurs)
        #=====================add layout menu=========================
        self.menu_layout = QtWidgets.QVBoxLayout(self.group_menu)
        self.menu_layout.setContentsMargins(10, 20, 10, 10)
        self.menu_layout.setSpacing(10)
        self.menu_layout.addWidget(self.users_group)
        self.menu_layout.addWidget(self.btn_home)
        self.menu_layout.addWidget(self.btn_product)
        self.menu_layout.addWidget(self.btn_depot)
        self.menu_layout.addWidget(self.btn_stock)
        self.menu_layout.addWidget(self.btn_achat)
        self.menu_layout.addWidget(self.btn_production)
        self.menu_layout.addWidget(self.btn_fournisseurs)
        self.menu_layout.addStretch()
#=====================Functions Boutons=========================  
    #bouton home==========      
    def home_button_clicked(self):
        home_page = Home()
        self.pages.addWidget(home_page)
        self.pages.setCurrentWidget(home_page)
    #bouton fournisseur==========      
    def supplier_button_clicked(self):
        fournisseur_page = Fournisseurs()
        self.pages.addWidget(fournisseur_page)
        self.pages.setCurrentWidget(fournisseur_page)
        #bouton product==========
    def product_button_clicked(self):
        product_page = Product()
        self.pages.addWidget(product_page)
        self.pages.setCurrentWidget(product_page)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    use_style(app)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())