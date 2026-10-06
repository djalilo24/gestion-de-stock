from PyQt5 import QtCore, QtGui, QtWidgets
from style import use_style
from PyQt5.QtGui import QIcon

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
        #=================add layout=========================
        self.main_layout.addWidget(self.group_menu, 2)
        self.main_layout.addWidget(self.main_content, 8)
#=====================add button=========================
        #============bouton home============
        self.btn_home = QtWidgets.QPushButton(self.group_menu)
        self.btn_home.setObjectName("btn_home")
        self.btn_home.setText("    Accueil")
        self.btn_home.setIcon(QtGui.QIcon("icon/home.png"))
        self.btn_home.setIconSize(QtCore.QSize(int(screen_height * 4.5/ 100), int(screen_height * 4.5 / 100)))
        #===========bouton supplier ============
        self.btn_fournisseurs = QtWidgets.QPushButton(self.group_menu)
        self.btn_fournisseurs.setObjectName("btn_fournisseurs")
        self.btn_fournisseurs.setText("    Fournisseurs")
        self.btn_fournisseurs.setIcon(QtGui.QIcon("icon/supplier.png"))
        self.btn_fournisseurs.setIconSize(QtCore.QSize(int(screen_height * 5/ 100), int(screen_height * 5 / 100)))
        #========bouton selected===============
        self.menu_group = QtWidgets.QButtonGroup(MainWindow)
        self.menu_group.setExclusive(True)
        self.btn_home.setCheckable(True)
        self.btn_fournisseurs.setCheckable(True)
        self.menu_group.addButton(self.btn_home)
        self.menu_group.addButton(self.btn_fournisseurs)
        #=====================add layout menu=========================
        self.menu_layout = QtWidgets.QVBoxLayout(self.group_menu)
        self.menu_layout.setContentsMargins(10, 20, 10, 10)
        self.menu_layout.setSpacing(10)
        self.menu_layout.addWidget(self.btn_home)
        self.menu_layout.addWidget(self.btn_fournisseurs)
        self.menu_layout.addStretch()
#=====================add form=========================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    use_style(app)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())