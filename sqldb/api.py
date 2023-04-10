from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import sqlite3
import json

app = Flask(__name__)
api = Api(app)


class GetPizza(Resource):
    def get(self):
        conn = sqlite3.connect("C:\sushi_house\\api\sushi_house_database.db")
        cursor = conn.cursor()

        raw = cursor.execute("SELECT * FROM pizza").fetchall()

        object = {}
        for i in range(len(raw)):
            object.update({i : {
                "item_name" : f"{raw[i][1]}",
                "item_ingradients" : f"{raw[i][2]}",
                "item_size" : f"{raw[i][3]}",
                "item_price" : f"{raw[i][4]}",
            }})


        return object


class GetSnidanki(Resource):
    def get(self):
        conn = sqlite3.connect("C:\sushi_house\\api\sushi_house_database.db")
        cursor = conn.cursor()

        raw = cursor.execute("SELECT * FROM snidanki").fetchall()

        object = {}
        for i in range(len(raw)):
            object.update({i : {
                "item_name" : f"{raw[i][1]}",
                "item_ingradients" : f"{raw[i][2]}",
                "item_size" : f"{raw[i][3]}",
                "item_price" : f"{raw[i][4]}",
            }})


        return object



class GetEuro(Resource):
    def get(self):
        conn = sqlite3.connect("C:\sushi_house\\api\sushi_house_database.db")
        cursor = conn.cursor()

        raw = cursor.execute("SELECT * FROM euro").fetchall()

        object = {}
        for i in range(len(raw)):
            object.update({i : {
                "item_name" : f"{raw[i][1]}",
                "item_ingradients" : f"{raw[i][2]}",
                "item_size" : f"{raw[i][3]}",
                "item_price" : f"{raw[i][4]}",
            }})


        return object



class GetBar(Resource):
    def get(self):
        conn = sqlite3.connect("C:\sushi_house\\api\sushi_house_database.db")
        cursor = conn.cursor()

        raw = cursor.execute("SELECT * FROM bar").fetchall()

        object = {}
        for i in range(len(raw)):
            object.update({i : {
                "item_name" : f"{raw[i][1]}",
                "item_ingradients" : f"{raw[i][2]}",
                "item_size" : f"{raw[i][3]}",
                "item_price" : f"{raw[i][4]}",
            }})


        return object



class GetSushi(Resource):
    def get(self):
        conn = sqlite3.connect("C:\sushi_house\\api\sushi_house_database.db")
        cursor = conn.cursor()

        raw = cursor.execute("SELECT * FROM sushi").fetchall()

        object = {}
        for i in range(len(raw)):
            object.update({i : {
                "item_name" : f"{raw[i][1]}",
                "item_ingradients" : f"{raw[i][2]}",
                "item_size" : f"{raw[i][3]}",
                "item_price" : f"{raw[i][4]}",
            }})


        return object




api.add_resource(GetPizza, "/pizza")
api.add_resource(GetSnidanki, "/snidanki")
api.add_resource(GetEuro, "/euro")
api.add_resource(GetBar, "/bar")
api.add_resource(GetSushi, "/sushi")
api.init_app(app=app)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port = "4444")
