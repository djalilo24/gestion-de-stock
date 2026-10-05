def use_style(app):
           app.setStyleSheet("""
            QWidget {
                background-color: #3E6DEDC;
                font-family: 'Sakkal Majalla';
            }
            

            QGroupBox {
               background-color: white;
               border: 1px solid #b8c2cc;
               border-radius: 10px;
               margin-top: 15px;
               padding: 10px;
               font-size: 22px;
               font-weight: bold;
             }

            QGroupBox::title {
              subcontrol-origin: margin;
              subcontrol-position: top center;
            }
            QGroupBox#group_menu {
                background-color: #6771C5; 
                border: 1px solid #0A0A0F;
                border-radius: 30px;}
            QGroupBox#main_content {
                background-color: #F0F0F5; 
                border: 1px solid #0A0A0F;
                border-radius: 30px;}
            QPushButton{
             background-color: #6771C5;
             color: black;
             border: none;
             border-radius: 8px;
             padding: 8px;
             font-family: 'Sakkal Majalla';
             font-size: 58px;
            font-weight: bold;
            }

           QPushButton:hover {
            color: white;
            }

    """)