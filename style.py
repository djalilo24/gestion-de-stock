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
            QLabel#title_group {
              font-size: 32px;
              font-weight: bold;
              color: #374151;
              padding: 8px 12px;
              border-radius: 6px;
            }
QPushButton#add_button {
    background-color: #B8B8FF;
    color: #374151;
    border: 1px solid #A5A5E8;
    border-radius: 8px;
    padding: 5px 14px;
    font-family: 'Sakkal Majalla';
    font-size: 22px;
    font-weight: bold;
}

QPushButton#add_button:hover {
    background-color: #A5A5F0;
    border-color: #8E8EDB;
}

QPushButton#add_button:pressed {
    background-color: #9292DE;
    padding-top: 7px;
    padding-bottom: 3px;
}

QPushButton#add_button:disabled {
    background-color: #E5E7EB;
    color: #9CA3AF;
    border-color: #D1D5DB;
}
            QGroupBox#group_menu {
                background-color: #B8B8FF; 
                border: 1px solid #0A0A0F;
                border-radius: 30px;}
            QGroupBox#main_content {
                background-color: #F0F0F5; 
                border: 1px solid #0A0A0F;
                border-radius: 30px;}
            QGroupBox#users_group {
                background-color: #B8B8FF;
                border: 1px solid #0A0A0F;
                border-radius: 30px;
                width: 100%;
                height: 100%;}   
            QlineEdit#user_line_edit {
                background-color: white;    
            border: 1px solid #B8C2CC;
            border-radius: 8px;}     
            QPushButton{
             background-color: #B8B8FF; 
             color: black;
             border: none;
             border-radius: 8px;
             padding: 8px;
             font-family: 'Sakkal Majalla';
             font-size: 38px;
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
        font-size: 25px;
        font-weight: bold;
        padding: 2px;
       }
       QCalendarWidget {
    background-color: white;
    border: 1px solid #b8c2cc;
    border-radius: 8px;
}

QCalendarWidget QToolButton {
    color: black;
    background-color: white;
    font-size: 16px;
    font-weight: bold;
    height: 30px;
}

QCalendarWidget QToolButton:hover {
    background-color: #e8eaf6;
    border-radius: 5px;
}

QCalendarWidget QSpinBox {
    font-size: 14px;
}

QCalendarWidget QAbstractItemView {
    font-size: 14px;
    selection-background-color: #6771C5;
    selection-color: white;
}
QDateEdit {
    font-size: 25px;
    padding: 6px;
}
QTableWidget {
    background-color: #FFFFFF;
    alternate-background-color: #F4F7FB;
    color: #2C3E50;
    border: 1px solid #D6DEE8;
    border-radius: 8px;
    gridline-color: #E3E8EF;
    font-size: 28px;
    selection-background-color: #D6E4F0;
    selection-color: #1A5276;
}

QTableWidget::item {
    padding: 8px;
    border: none;
}

QTableWidget::item:selected {
    background-color: #D6E4F0;
    color: #1A5276;
}

QHeaderView::section {
    background-color: #34495E;
    color: white;
    padding: 10px;
    border: none;
    border-right: 1px solid #526578;
    font-size: 30px;
    font-weight: bold;
}

QTableCornerButton::section {
    background-color: #34495E;
    border: none;
}

QScrollBar:vertical {
    background-color: #F4F7FB;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #B8C2CC;
    min-height: 25px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #7F8C8D;
}

QScrollBar:horizontal {
    background-color: #F4F7FB;
    height: 10px;
}

QScrollBar::handle:horizontal {
    background-color: #B8C2CC;
    min-width: 25px;
    border-radius: 5px;
}
    """)