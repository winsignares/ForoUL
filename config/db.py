from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localshost/foroul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.secret_key='sheylita123'

bd=SQLAlchemy(app)
ma= Marshmallow(app)
=======
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/foroul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.secret_key = "41E5653FC7AEB894026D6BB7B2DB7F65902B454945FA8FD65A6327047B5277FB"

bd = SQLAlchemy(app)
ma = Marshmallow(app)
>>>>>>> 19f2e174e8d077e6d13d9c5f1caec6dcd7843947
