from flask import Blueprint, Flask, render_template, request
from config.db import app, bd, ma

from models.CommentsModel import Comment, CommentsSchema 

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

ruta_comment = Blueprint('ruta_post', __name__)

@ruta_comment.route('/comment')
def indercomment():
    return 'Hola mundo de controlador Comment'