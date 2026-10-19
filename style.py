def use_style(app):
           app.setStyleSheet("""
            QWidget {
                background-color: #E4E8F2;
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
        font-size: 30px;
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
    background-color: #e0e0d1;
    gridline-color: #999;
    font-size: 30px;
    font-family: 'Sakkal Majalla';
    border: 2px solid #d1d9e6;
    border-radius: 10px;
}

QTableWidget::item {
    padding: 6px;
}

QTableWidget::item:selected {
    background-color: #1e90ff;
    color: white;
}

QTableView {
    background-color: #e0e0d1;
}

QTableView::item {
    padding: 6px;
}

QHeaderView::section {
    background-color: #E6FFE6;
    color: black;
    font-size: 28px;
    font-weight: bold;
    padding: 6px;
    border: none;
    border-right: 2px solid #999999;   /* خط فاصل عمودي */
    border-bottom: 2px solid #999999;  /* خط فاصل أفقي */
}
    QComboBox {
        background-color: white;
        color: #2C3E50;
        border: 1px solid #B8C2CC;
        border-radius: 8px;
        padding: 6px 10px;
        min-height: 28px;
        font-family: "Sakkal Majalla";
        font-size: 28px;
    }

    QComboBox:hover {
        border: 1px solid #3498DB;
    }

    QComboBox:focus {
        border: 1px solid #2980B9;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #D5DDE5;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }

    QComboBox QAbstractItemView {
        background-color: white;
        color: #2C3E50;
        selection-background-color: #D6EAF8;
        selection-color: #154360;
        border: 1px solid #B8C2CC;
        outline: 0;
    }
        QDateEdit {
        background-color: white;
        color: #2C3E50;
        border: 1px solid #B8C2CC;
        border-radius: 8px;
        padding: 6px;
        font-size: 38px;
        min-height: 25px;
    }

    QDateEdit:hover {
        border: 1px solid #3498DB;
    }

    QDateEdit:focus {
        border: 1px solid #2980B9;
    }

    QDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left: 1px solid #B8C2CC;
    }
        QPushButton#btn_active {
        background-color: #27AE60;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-size: 24px;
    }

    QPushButton#btn_active:checked {
        background-color: #27F542;
    }

    QPushButton#btn_active:!checked {
        background-color: #E74C3C;
    }
    QMenu {
    background-color: #FFFFFF;
    color: #2C3E50;
    border: 1px solid #DCE3EB;
    border-radius: 8px;
    padding: 5px;
    font-family: 'Sakkal Majalla';
    font-size: 20px;
}

QMenu::item {
    padding: 8px 25px;
    background-color: transparent;
    border-radius: 5px;
}

QMenu::item:selected {
    background-color: #3498DB;
    color: #FFFFFF;
}

QMenu::item:disabled {
    color: #BDC3C7;
}

QMenu::separator {
    height: 1px;
    background-color: #E5EAF0;
    margin: 5px 8px;
}
    """)