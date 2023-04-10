from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

import requests
import sqlite3
import sys

class Snidanki(QMainWindow):
    def __init__(win, self):
        super(Snidanki, win).__init__()

        def parsePrice(text):
            price = text.split(" ")

            self.end_price += int(price[0])
            self.end_price_field.setText(f"{self.end_price}")

        def remove_box_func(text):
            price = text.split(" ")

            self.end_price -= int(price[0])
            self.end_price_field.setText(f"{self.end_price}")


        def add_to_basket(parent, item_info):
            groupBox = QGroupBox(parent)
            groupLayout = QGridLayout(groupBox)

            groupBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))


            itemImage = QLabel(groupBox)
            itemImage.setPixmap(QPixmap(item_info[0]))
            itemImage.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))



            item_name = QLabel(groupBox, text= item_info[1])
            item_name.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

            item_ingradients = QLabel(groupBox, text= item_info[2])
            item_ingradients.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

            item_size = QLabel(groupBox, text = item_info[3])
            item_size.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

            item_price = QLabel(groupBox, text = item_info[4])
            item_price.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

            remove_btn = QPushButton(groupBox, text = "REMOVE")
            remove_btn.setStyleSheet("background: blue;")

            remove_btn.clicked.connect(lambda: remove_box_func(item_price.text()))
            remove_btn.clicked.connect(lambda: groupBox.deleteLater())


            groupLayout.addWidget(itemImage, 1, 0)
            groupLayout.addWidget(remove_btn, 2, 0)
            groupLayout.addWidget(item_name, 0, 1)
            groupLayout.addWidget(item_ingradients, 1, 1)
            groupLayout.addWidget(item_size, 2, 1)
            groupLayout.addWidget(item_price, 3, 1)



            self.scrollLayout.addWidget(groupBox)

        #------------CREATE BUTTON FUNCTION-----------------------SALAT
        def create_snidankiBox(row, column, displayed_image, label_1_text, label_2_text, label_3_text, label_price_text):
            #----- Group Box -----
            groupBox = QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum))
            groupBox.setStyleSheet("border:none; padding: 2px")
            verticalLayout = QVBoxLayout(groupBox)
            #---------------------

            conn = sqlite3.connect("C:\sushi_house\sqldb\sushi_house_database_photos.db")
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM snidanki_photos WHERE item_id == '{displayed_image + 1}'").fetchone()

            #----- Pizza Image -----
            self.snidankiImage = QLabel(groupBox)
            self.snidankiImage.setGeometry(0, 0, 180, 180)
            pmSnidankiImage = QPixmap()
            pmSnidankiImage.loadFromData(result[1])
            self.snidankiImage.setPixmap(pmSnidankiImage)


            verticalLayout.addWidget(self.snidankiImage)
            #-----------------------

            #---- Upper Text -----
            label_1 = QLabel(groupBox, text = f"{label_1_text}")
            label_1.setSizePolicy(self.textSizePolicy)
            font_1 = QFont()
            font_1.setPointSize(11)
            font_1.setBold(True)
            label_1.setFont(font_1)
            label_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeft)

            verticalLayout.addWidget(label_1)
            #------------------

            #----- Lower Text -----
            label_2 = QLabel(groupBox, text=f"{label_2_text}")
            label_2.setSizePolicy(self.textSizePolicy)
            font_2 = QFont()
            font_2.setPointSize(8)
            label_2.setFont(font_2)
            label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeft)

            verticalLayout.addWidget(label_2)
            #---------------------
            label_3 = QLabel(groupBox, text=f"{label_3_text}")
            label_3.setSizePolicy(self.textSizePolicy)
            font_3 = QFont()
            font_3.setPointSize(8)
            label_3.setFont(font_3)
            label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeft)

            verticalLayout.addWidget(label_3)


            label_price = QLabel(groupBox, text=f"{label_price_text}")
            label_price.setSizePolicy(self.textSizePolicy)
            font_price = QFont()
            font_price.setPointSize(11)
            label_price.setFont(font_price)
            label_price.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeft)

            verticalLayout.addWidget(label_price)

            #---- Hiden Push Button -----

            # hiddenPB = QPushButton(self.groupBox)

            # hiddenPB.setGeometry(0,0,220,320)
            # hiddenPB.setStyleSheet("background-color:rgba(255, 0, 0, 0.5)")
            #----------------------------

            pushButton_2 = QPushButton(groupBox, text = "Добавити в кошик")
            font_4 = QFont()
            font_4.setPointSize(10)
            pushButton_2.setFont(font_4)
            pushButton_2.setStyleSheet("background-color: #FF8F00")

            verticalLayout.addWidget(pushButton_2)


            pushButton_2.clicked.connect(lambda: add_to_basket(self, [pmSnidankiImage, label_1.text(), label_2.text(), label_3.text(), label_price.text()]))
            pushButton_2.clicked.connect(lambda: parsePrice(label_price.text()))
            pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

            self.gridLayout.addWidget(groupBox, row, column)

#---------------------------------------------------------------------
        def create_snidanki_box():
            salatCol = 0
            salatRw = 0

            for i in range(23):#23 it's pizza block count
                item_info = requests.get("http://127.0.0.1:4444/snidanki").json()
                ingradients = item_info[f"{i}"]["item_ingradients"].strip()

                if r"\n" in item_info[f"{i}"]["item_name"]:
                    item_info[f"{i}"]["item_name"] = item_info[f"{i}"]["item_name"].replace(r"\n", "\n")

                try:
                    item_info[f"{i}"]["item_ingradients"] = item_info[f"{i}"]["item_ingradients"]
                    g = item_info[f"{i}"]["item_ingradients"].replace("(", "\n").replace(")", "")

                    h = list(g)

                    h[1] = "К"
                    h[25] = ""
                    h[26] = "\n"

                    ingradients_adapted = "".join(h)
                except IndexError:
                    pass


                try:
                    if i < 9:
                        if salatCol < 4:
                            create_snidankiBox(salatRw, salatCol, i, item_info[f"{i}"]["item_name"], ingradients_adapted, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                            salatCol += 1
                        else:
                            create_snidankiBox(salatRw, salatCol, i, item_info[f"{i}"]["item_name"], ingradients_adapted, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                            salatRw += 1
                            salatCol = 0
                    else:
                        if salatCol < 4:
                            create_snidankiBox(salatRw, salatCol, i, item_info[f"{i}"]["item_name"], ingradients_adapted, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                            salatCol += 1
                        else:
                            if i == 9:
                                create_snidankiBox(salatRw, salatCol, i, item_info[f"{i}"]["item_name"], ingradients_adapted, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                                salatRw += 1
                                salatCol = 0
                            else:
                                create_snidankiBox(salatRw, salatCol, i, item_info[f"{i}"]["item_name"], ingradients_adapted, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                                salatRw += 1
                                salatCol = 0
                except:
                    import tkinter as tk
                    from tkinter import messagebox
                    print("SNIDANKI MENU ERROR")

                    root = tk.Tk()
                    root.withdraw()

                    return_answ = messagebox.showerror("ERROR!", "The program is temporarily down.\nПрограма тимчасово недоступна.")
                    if return_answ == "ok":
                        sys.exit()

                    root.destroy()


        create_snidanki_box()
