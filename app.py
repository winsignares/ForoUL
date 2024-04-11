from flask import Flask, render_template, request, json, jsonify
from config.db import app

from controllers.UserController import ruta_user
from controllers.CommentController import ruta_comment

app.register_blueprint(ruta_user, url_prefix="/controller")
app.register_blueprint(ruta_comment, url_prefix="/controller")

from models.PostModel import Post, PostsSchema

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)


@app.route('/', methods=['GET'])
def index():
    return "Hola Mundo index"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
