from flask import Blueprint, Flask, request, render_template, jsonify
from config.db import app, bd, ma

from models.PostModel import Post, PostsSchema

ruta_user = Blueprint("route_user", __name__)

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

@ruta_user.route("/Post")
def indexPost():
    return "Hola mundo desde el Post Controller"
