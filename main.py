from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import asyncio
import sys

import os
import re
import threading
import warnings
import requests
import random
import string

from pizzaMenu import Pizza
from snidankiMenu import Snidanki
from euroMenu import Euro
from barMenu import Bar
from sushiMenu import Sushi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        def send_order(children, end_price, contacts, address):
            children.pop(0)

            contacts_s = "Контактні дані: " + str(contacts) + " \n" + "Адреса: " + str(address)
            requests.get(f"https://api.telegram.org/bot5861561979:AAH1FzUipKsAiatgjmqZ7ybJFx1KKdINg7o/sendMessage?chat_id=1375279061&text={contacts_s}")

            for order in children:
                box = order.children()

                order_item_name = box[2].text().strip()
                order_item_ingradients = box[3].text().strip()
                order_item_size = box[4].text().strip()
                order_item_price = box[5].text().strip()


                all_order = "Назва: " + order_item_name + "\n\n" + "Розмір: " + order_item_size + "\n\n" + "Ціна: " + order_item_price
                requests.get(f"https://api.telegram.org/bot5861561979:AAH1FzUipKsAiatgjmqZ7ybJFx1KKdINg7o/sendMessage?chat_id=1375279061&text={all_order}")

            en_price = "Загальна сума: " + str(end_price) + " грн"
            requests.get(f"https://api.telegram.org/bot5861561979:AAH1FzUipKsAiatgjmqZ7ybJFx1KKdINg7o/sendMessage?chat_id=1375279061&text={en_price}")



        self.setGeometry(300, 200, 1280, 720)
        self.setFixedSize(1280, 730)
        self.setWindowTitle("Sushi House")

        self.textFont = QFont("Futura Md BT", 12)
        self.textFont.setBold(True)

        self.textSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.fixedSizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(0,0,1280,730)

        self.test_button_to_basket = QPushButton(self, text = "BASKET")
        self.test_button_to_basket.setGeometry(67, 45, 175, 70)
        self.test_button_to_basket.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))


#----------------- PIXMAP ELEMENTS FOR RIGHT MENU------
        list0 = [QPixmap("images\Menu\pizzaImageDis.png"), QPixmap("images\Menu\salatImageDis.png"),
                        QPixmap("images\Menu\cakeImageDis.png"),QPixmap("images\Menu\drinksImageDis.png"),
                        QPixmap("images\Menu\sushiImageDis.png")]

        list1 = [QPixmap("images\Menu\pizzaImageEn.png"), QPixmap("images\Menu\salatImageDis.png"),
                        QPixmap("images\Menu\cakeImageDis.png"),QPixmap("images\Menu\drinksImageDis.png"),
                        QPixmap("images\Menu\sushiImageDis.png")]

        list2 = [QPixmap("images\Menu\pizzaImageDis.png"), QPixmap("images\Menu\salatImageEn.png"),
                        QPixmap("images\Menu\cakeImageDis.png"),QPixmap("images\Menu\drinksImageDis.png"),
                        QPixmap("images\Menu\sushiImageDis.png")]

        list3 = [QPixmap("images\Menu\pizzaImageDis.png"), QPixmap("images\Menu\salatImageDis.png"),
                        QPixmap("images\Menu\cakeImageEn.png"),QPixmap("images\Menu\drinksImageDis.png"),
                        QPixmap("images\Menu\sushiImageDis.png")]

        list4 = [QPixmap("images\Menu\pizzaImageDis.png"), QPixmap("images\Menu\salatImageDis.png"),
                        QPixmap("images\Menu\cakeImageDis.png"),QPixmap("images\Menu\drinksImageEn.png"),
                        QPixmap("images\Menu\sushiImageDis.png")]

        list5 = [QPixmap("images\Menu\pizzaImageDis.png"), QPixmap("images\Menu\salatImageDis.png"),
                        QPixmap("images\Menu\cakeImageDis.png"),QPixmap("images\Menu\drinksImageDis.png"),
                        QPixmap("images\Menu\sushiImageEn.png")]
#------------ CREATE RIGHT MENU ----------------

        def create_clickable_right_menu(list, widget):
            y = 190
            for el_rb in range(5):
                self.button = QPushButton(widget)
                self.button.setIcon(QIcon(QPixmap(list[el_rb])))
                self.button.setIconSize(QSize(105,105))
                self.button.setGeometry(1175, y, 105, 105)

                y += 105
                if el_rb == 0:
                    self.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
                elif el_rb == 1:
                    self.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
                elif el_rb == 2:
                    self.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
                elif el_rb == 3:
                    self.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
                elif el_rb == 4:
                    self.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))



#-------------------------------------------------



#-----------------------Start Menu-------------------------------
        self.startMenu = QWidget()

        self.startMenu.setStyleSheet("background-color:F5F5F5")

        self.elip1 = QLabel(self.startMenu)
        self.elip1.setPixmap(QPixmap("images\\Start_Menu\\elip1.png"))
        self.elip1.setGeometry(293,-80,694,692)
        self.elip1.setStyleSheet("background: transparent;")

        self.elip2 = QLabel(self.startMenu)
        self.elip2.setPixmap(QPixmap("images\\Start_Menu\\elip2.png"))
        self.elip2.setGeometry(500,81,279,279)
        self.elip2.setStyleSheet("background: transparent;")

        self.elip3 = QLabel(self.startMenu)
        self.elip3.setPixmap(QPixmap("images\\Start_Menu\\elip3.png"))
        self.elip3.setGeometry(590, 485, 100, 100)
        self.elip3.setStyleSheet("background: transparent;")

        self.face1 = QLabel(self.startMenu)
        self.face1.setPixmap(QPixmap("images\\Start_Menu\\face1.png"))
        self.face1.setGeometry(535, 119, 211, 392)
        self.face1.setStyleSheet("background : transparent;")

        self.sushiText = QLabel(self.startMenu)
        self.sushiText.setPixmap(QPixmap("images\\Start_Menu\\sushi.png"))
        self.sushiText.setGeometry(176, 255.09, 329.33, 104.91)
        self.sushiText.setStyleSheet("background : transparent;")


        self.houseText = QLabel(self.startMenu)
        self.houseText.setPixmap(QPixmap("images\\Start_Menu\\house.png"))
        self.houseText.setGeometry(797.33, 258.54, 297, 98)
        self.houseText.setStyleSheet("background : transparent;")


        self.textStartbtn = QPushButton(self.startMenu, text="START")
        self.textStartbtn.setFont(self.textFont)
        self.textStartbtn.setStyleSheet("background : transparent; color : white;")
        self.textStartbtn.setGeometry(597, 496, 90, 80)

        self.textStartbtn.clicked.connect(lambda: start_btn())

        def start_btn():
            self.stackedWidget.setCurrentIndex(1)

        self.stackedWidget.addWidget(self.startMenu)

#-----------------------Main Menu--------------------------------
        def create_basket_menu_ui(parent):
            self.blackrec = QLabel(parent)
            self.blackrec.setPixmap(QPixmap("images\\Menu\\blackRec.png"))
            self.blackrec.setGeometry(0, 0, 1280, 146)
            self.blackrec.setStyleSheet("background : transparent;")

            self.sushi_image = QLabel(parent)
            self.sushi_image.setPixmap(QPixmap("images\\Menu\\imageSushi.png"))
            self.sushi_image.setGeometry(288, 0, 703, 146)
            self.sushi_image.setStyleSheet("background : transparent;")


            self.transRec = QLabel(parent)
            self.transRec.setPixmap(QPixmap("images\Menu\\transRec.png"))
            self.transRec.setGeometry(892.52, 101, 344.48, 30)
            self.transRec.setStyleSheet("background : transparent;")

            self.lineEdit = QLineEdit(parent)
            self.lineEdit.setGeometry(892, 101, 344, 30)
            self.lineEdit.setStyleSheet("background : transparent;")
            self.lineEdit.setFrame(False)


            self.lupaVec = QLabel(parent)
            self.lupaVec.setPixmap(QPixmap("images\\Menu\\Vector.png"))
            self.lupaVec.setGeometry(1207, 108.24, 15.52, 15.52)
            self.lupaVec.setStyleSheet("background : transparent;")


            self.recmenu = QLabel(parent)
            self.recmenu.setPixmap(QPixmap("images\\Menu\\menuRec.png"))
            self.recmenu.setGeometry(0, 150, 1280, 40)
            self.recmenu.setStyleSheet("background : transparent;")



            self.scrollArea = QScrollArea(parent)
            # self.scrollArea.setGeometry(471, 190, 400, 540)
            self.scrollArea.setGeometry(380, 190, 400, 540)
            self.scrollArea.setSizePolicy(self.fixedSizePolicy)
            self.scrollArea.setFrameShape(QFrame.NoFrame)
            self.scrollArea.setFrameShadow(QFrame.Plain)
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrollArea.setWidgetResizable(True)

            self.scrollArea.setStyleSheet("background:red")


            # self.scrollAreaWidgetContents = QWidget(self.scrollArea)
            # self.scrollAreaWidgetContents.setGeometry(400, 190, 600, 800)
            # self.scrollAreaWidgetContents.setStyleSheet("background:black")
            # self.scrollAreaWidgetContents.setSizePolicy(self.fixedSizePolicy)

            # # ЦЕ ВЖЕ БУЛО ЗАКОМЕНТОВАНО НЕ ТРОГАЙ
            # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            # self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)


            self.scrollAreaWidgetContents = QWidget(self.scrollArea)
            self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))

            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)


            # self.back_to_menu_label = QLabel(parent, text= "Меню")
            # self.back_to_menu_label.setGeometry(171, 255, 70, 22)
            # self.back_to_menu_label.setFont(self.textFont)
            # self.back_to_menu_label.setStyleSheet("color: #F58D13")

            self.end_price = 0

            self.end_price_field = QLabel(parent, text = f"Загальна сума: {self.end_price}")
            self.end_price_field.setGeometry(950, 415, 200, 30)
            font_price = QFont()
            font_price.setPointSize(12)
            self.end_price_field.setFont(font_price)

            self.contacts = QLineEdit(parent)
            self.contacts.setPlaceholderText("Вкажіть ваші контактні дані")
            self.contacts.setGeometry(950, 460, 200, 40)

            self.address = QLineEdit(parent)
            self.address.setPlaceholderText("Вкажіть вашу адресу")
            self.address.setGeometry(970, 520, 150, 40)

            self.test_refresh = QPushButton(parent, text = "ЗАМОВИТИ")
            self.test_refresh.setGeometry(970, 580, 150, 60)


            self.test_refresh.clicked.connect(lambda: send_order(self.scrollAreaWidgetContents.children(), self.end_price, self.contacts.text(), self.address.text()))

            create_clickable_right_menu(list0, parent)


        def create_menu_ui(parent, en_icon_list):
            self.blackrec = QLabel(parent)
            self.blackrec.setPixmap(QPixmap("images\\Menu\\blackRec.png"))
            self.blackrec.setGeometry(0, 0, 1280, 146)
            self.blackrec.setStyleSheet("background : transparent;")


            self.sushi_image = QLabel(parent)
            self.sushi_image.setPixmap(QPixmap("images\\Menu\imageSushi.png"))
            self.sushi_image.setGeometry(288, 0, 703, 146)
            self.sushi_image.setStyleSheet("background : transparent;")


            self.transRec = QLabel(parent)
            self.transRec.setPixmap(QPixmap("images\\Menu\\transRec.png"))
            self.transRec.setGeometry(892.52, 101, 344.48, 30)
            self.transRec.setStyleSheet("background : transparent;")

            self.lineEdit = QLineEdit(parent)
            self.lineEdit.setGeometry(892, 101, 344, 30)
            self.lineEdit.setStyleSheet("background : transparent;")
            self.lineEdit.setFrame(False)


            self.lupaVec = QLabel(parent)
            self.lupaVec.setPixmap(QPixmap("images\\Menu\\Vector.png"))
            self.lupaVec.setGeometry(1207, 108.24, 15.52, 15.52)
            self.lupaVec.setStyleSheet("background : transparent;")


            self.recmenu = QLabel(parent)
            self.recmenu.setPixmap(QPixmap("images\\Menu\\menuRec.png"))
            self.recmenu.setGeometry(0, 150, 1280, 40)
            self.recmenu.setStyleSheet("background : transparent;")


            self.scrollArea = QScrollArea(parent)
            self.scrollArea.setGeometry(0, 190, 1175, 550)
            self.scrollArea.setSizePolicy(self.fixedSizePolicy)
            self.scrollArea.setFrameShape(QFrame.NoFrame)
            self.scrollArea.setFrameShadow(QFrame.Plain)
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrollArea.setWidgetResizable(True)


            self.scrollAreaWidgetContents = QWidget(self.scrollArea)
            self.scrollAreaWidgetContents.setGeometry(0, 0, 1175, 550)
            # self.scrollAreaWidgetContents.setStyleSheet("background:red")
            self.scrollAreaWidgetContents.setSizePolicy(self.fixedSizePolicy)


            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)

            create_clickable_right_menu(en_icon_list, parent)




        self.pizzawidget = QWidget()
        create_menu_ui(self.pizzawidget, en_icon_list=list1)
        pizzaMenu = Pizza(self)

        self.snidankiwidget = QWidget()
        create_menu_ui(self.snidankiwidget, en_icon_list=list2)
        snidankiMenu = Snidanki(self)

        self.eurowidget = QWidget()
        create_menu_ui(self.eurowidget, en_icon_list=list3)
        euroMenu = Euro(self)

        self.barwidget = QWidget()
        create_menu_ui(self.barwidget, en_icon_list=list4)
        barMenu = Bar(self)

        self.sushiwidget = QWidget()
        create_menu_ui(self.sushiwidget, en_icon_list=list5)
        sushiMenu = Sushi(self)

        self.checkoutwidget = QWidget()
        create_basket_menu_ui(self.checkoutwidget)


        self.stackedWidget.addWidget(self.pizzawidget)
        self.stackedWidget.addWidget(self.snidankiwidget)
        self.stackedWidget.addWidget(self.eurowidget)
        self.stackedWidget.addWidget(self.barwidget)
        self.stackedWidget.addWidget(self.sushiwidget)
        self.stackedWidget.addWidget(self.checkoutwidget)

#------------------------------------------------------



        self.stackedWidget.setCurrentIndex(0)



def App():
    app = QApplication(sys.argv)
    window = MainWindow()


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    App()
