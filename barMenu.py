from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


import requests
import sqlite3
import sys


class Bar(QMainWindow):
    def __init__(win, self):
        super(Bar, win).__init__()

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

            groupBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))


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

#------------CREATE BUTTON FUNCTION-----------------------BAR

        def create_barBox(row, column, displayed_image : str, label_1_text, label_2_text, label_3_text, label_price_text):
            #----- Group Box -----
            groupBox = QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum))
            groupBox.setStyleSheet("border:none; padding: 2px")
            verticalLayout = QVBoxLayout(groupBox)
            #---------------------

            conn = sqlite3.connect("C:\sushi_house\sqldb\sushi_house_database_photos.db")
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM bar_photos WHERE item_id == '{displayed_image + 1}'").fetchone()


            #----- Pizza Image -----
            self.barImage = QLabel(groupBox)
            self.barImage.setGeometry(0, 0, 180, 180)
            pmBarImage = QPixmap()
            pmBarImage.loadFromData(result[1])
            self.barImage.setPixmap(pmBarImage)


            verticalLayout.addWidget(self.barImage)
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
            #----------------------


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


            pushButton_2.clicked.connect(lambda: add_to_basket(self, [pmBarImage, label_1.text(), label_2.text(), label_3.text(), label_price.text()]))
            pushButton_2.clicked.connect(lambda: parsePrice(label_price.text()))
            pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

            self.gridLayout.addWidget(groupBox, row, column)

        #---------------------------------------------------------------------

        def create_bar_box():

            barCol = 0
            barRw = 0

            #----INGREDIENTS----
            for i in range(131): #131 it's bar block count

                item_info = requests.get("http://127.0.0.1:4444/bar").json()
                ingradients = item_info[f"{i}"]["item_ingradients"].strip()


                if r"\n" in item_info[f"{i}"]["item_name"]:
                    item_info[f"{i}"]["item_name"] = item_info[f"{i}"]["item_name"].replace(r"\n", "\n")

                string = item_info[f"{i}"]["item_ingradients"].strip()
                di = string.split(",")
                if len(di) == 1:
                    di.extend(["\n" * 8])
                if len(di) == 2:
                    di.extend(["\n" * 7])
                if len(di) == 3:
                    di.extend(["\n" * 6])
                if len(di) == 4:
                    di.extend(["\n" * 5])
                if len(di) == 5:
                    di.extend(["\n" * 4])
                if len(di) == 6:
                    di.extend(["\n" * 3])
                if len(di) == 7:
                    di.extend(["\n" * 2])
                if len(di) == 8:
                    di.extend(["\n"])

                tempPizzaIngredientList = []


                for el in di:
                    # if i != "\n":
                    new = "● " + el.strip().capitalize() + "\n"
                    tempPizzaIngredientList.append(new)

                pizzaIngredientsList = []

                for j in tempPizzaIngredientList:
                    if j == "● \n":
                        let = j.replace("● ", "")
                        pizzaIngredientsList.append(let)
                    else:
                        pizzaIngredientsList.append(j)

                norm = "".join(pizzaIngredientsList)

                try:
                    if barCol < 4:
                        create_barBox(barRw, barCol, i, item_info[f"{i}"]["item_name"], norm, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                        barCol += 1
                    else:
                        create_barBox(barRw, barCol, i, item_info[f"{i}"]["item_name"], norm, item_info[f"{i}"]["item_size"], item_info[f"{i}"]["item_price"])
                        barRw += 1
                        barCol = 0
                except:
                    import tkinter as tk
                    from tkinter import messagebox
                    print("BAR MENU ERROR")

                    root = tk.Tk()
                    root.withdraw()

                    return_answ = messagebox.showerror("ERROR!", "The program is temporarily down.\nПрограма тимчасово недоступна.")
                    if return_answ == "ok":
                        sys.exit()

                    root.destroy()

        create_bar_box()
