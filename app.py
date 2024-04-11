from flask import Flask, render_template, request, json, jsonify
from config.db import app

from controllers.UserController import ruta_user
from controllers.CommentController import ruta_comment
from controllers.PostController import ruta_post

app.register_blueprint(ruta_user, url_prefix="/controller")
app.register_blueprint(ruta_comment, url_prefix="/controller")
app.register_blueprint(ruta_post, url_prefix="/controller")

@app.route('/', methods=['GET'])
def index():
    return render_template("layaout.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
