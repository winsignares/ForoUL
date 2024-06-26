
from flask import Blueprint, Flask, render_template, request, jsonify
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


@ruta_user.route("/Cuser", methods=["GET"])
def Cuser():
    result = bd.session.query(Users).all()
    data = {}
    i= 0
    for user in result:
        i+=1
        data[i]={
            'fullname' : user.fullname,
            'email': user.email
        }
    return jsonify(data)

@ruta_user.route("/Euser", methods=["Delete"])
def Euser():
    id = request.json['id']
    Usuario = Users.query.get(id)
    bd.session.delete(Usuario)
    bd.session.commit()
    return jsonify(user_schema.dump(Usuario))

@ruta_user.route("/Uuser", methods=["Delete"])
def Uuser():
    id = request.json['id']
    Usuario = Users.query.get(id)
    email = request.json['email']
    fullname = request.json['fullname']
    Usuario.fullname = fullname
    Usuario.email = email    
    bd.session.commit()
    return "Datos Actualizado"