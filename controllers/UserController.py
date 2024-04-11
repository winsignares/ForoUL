
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

