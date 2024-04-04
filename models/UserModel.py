from config.db import bd, ma, app

class Users (bd.Model):
    __tablename__ = "tblUsers"

    id = bd.Column(bd.Integer, primary_key = True)
    Fullname = bd.Column(bd.String(50))
    email = bd.Column(bd.String(50))

    def __init__(self, Fullname, email):
        self.Fullname = Fullname
        self.email = email

with app.app_context():
    bd.create_all()

class UsersSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'Fullname', 'email')