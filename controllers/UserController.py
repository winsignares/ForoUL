from flask import Blueprint, Flask, request, render_template, jsonify
from config.db import app, bd, ma

from models.UserModel import Users, UsersSchema

ruta_user = Blueprint("route_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@ruta_user.route("/User")
def indexUser():
    return "Hola mundo desde el User Controller"
