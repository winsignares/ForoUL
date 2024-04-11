from flask import Flask, render_template, request, json, jsonify
from config.db import app

<<<<<<< HEAD
from controllers.UserController import ruta_user
from controllers.CommentController import ruta_comment

app.register_blueprint(ruta_user, url_prefix="/controller")
app.register_blueprint(ruta_comment, url_prefix="/controller")
=======

from models.PostModel import Post, PostsSchema
from models.CommentsModel import Comment, CommentsSchema 

from controllers.UserController import ruta_user

app.register_blueprint(ruta_user, url_prefix="/controller")

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)
>>>>>>> ddab5d4343f51c9b0aff6c9f07612558e3b8c897

@app.route('/', methods=['GET'])
def index():
    return "Hola Mundo index"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
