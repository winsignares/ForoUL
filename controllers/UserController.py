
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

from models.UserModel import Users, UsersSchema

ruta_user = Blueprint("route_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@ruta_user.route('/User')
def indexuser():
    return render_template("user.html")

@ruta_user.route("/User")
def indexUser():
    return "Hola mundo desde el User Controller"


@ruta_user.route("/Saveuser", methods=["POST"])
def Saveuser():
    email = request.json['email']
    fullname = request.json['fullname']
    newuser = Users(fullname,email)
    bd.session.add(newuser)
    bd.session.commit()
    return "guardado"
