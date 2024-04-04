from config.db import bd, ma, app

class Post (bd.Model):
    __tablename__ = "tblPost"

    
    idForo = bd.Column(bd.Integer, primary_key = True)
    Comentario = bd.Column(bd.String(200))
    id_User = bd.Column(bd.Integer, foreing_key = True)

    def __init__(self, Comentario):
        self.Comentario = Comentario

with app.app_context():
    bd.create_all()

class UsersSchema(ma.Schema):
    class Meta: 
        fields = ('idForo', 'Comentario', 'id_User')