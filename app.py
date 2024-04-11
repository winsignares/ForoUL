from flask import Flask, render_template, request, json, jsonify
from config.db import app


from models.PostModel import Post, PostsSchema
from models.CommentsModel import Comment, CommentsSchema 

from controllers.UserController import ruta_user

app.register_blueprint(ruta_user, url_prefix="/controller")

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
