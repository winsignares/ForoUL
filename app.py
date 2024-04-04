from flask import Flask, render_template, request, json, jsonify
from config.db import app

from models.UserModel import Users, UsersSchema
from models.PostModel import Post, PostsSchema
from models.CommentsModel import Comment, CommentsSchema 

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
