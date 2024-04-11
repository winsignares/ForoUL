from flask import Blueprint, Flask, request, render_template, jsonify
from config.db import app, bd, ma

from models.PostModels import Postsm, PostsSchema

ruta_post = Blueprint("route_post", __name__)

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

@ruta_post.route("/Post")
def indexPost():
    return "Hola mundo desde el Post Controller"
