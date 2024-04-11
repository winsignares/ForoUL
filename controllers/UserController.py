<<<<<<< HEAD
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

from models.UserModel import Users, UsersSchema

ruta_user = Blueprint("clave", __name__)
=======
from flask import Blueprint, Flask, request, render_template, jsonify
from config.db import app, bd, ma

from models.UserModel import Users, UsersSchema

ruta_user = Blueprint("route_user", __name__)
>>>>>>> ddab5d4343f51c9b0aff6c9f07612558e3b8c897

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

<<<<<<< HEAD
@ruta_user.route('/User')
def indexuser():
    return 'Hola Mundo controlador User'
=======
@ruta_user.route("/User")
def indexUser():
    return "Hola mundo desde el User Controller"
>>>>>>> ddab5d4343f51c9b0aff6c9f07612558e3b8c897
