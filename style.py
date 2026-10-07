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
            QPushButton:checked {
            background-color: #d6e4f0;
            color: #1a5276;
            font-weight: bold;
            border-radius: 8px;
        }
      QLineEdit {
        background-color: white;
        border: 1px solid #B8C2CC;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 18px;
        color: #333333;
       }

        QLineEdit:focus {
        border: 2px solid #3E6DEC;
        }

        QLineEdit:hover {
        border: 1px solid #3E6DEC;
        }

       QLineEdit::placeholder {
        color: #999999;
        }
        QLabel {
        background-color: transparent;
        color: #333333;
        font-family: "Sakkal Majalla";
        font-size: 20px;
        font-weight: bold;
        padding: 2px;
       }
    """)