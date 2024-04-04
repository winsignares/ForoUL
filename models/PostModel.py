from config.db import bd, ma, app

class Post (bd.Model):
    __tablename__ = "tblPost"

    
    idForo = bd.Column(bd.Integer, primary_key = True)
    Comentario = bd.Column(bd.String(200))
    id_User = bd.Column(bd.Integer, bd.ForeignKey('tblUsers.id'))

    def __init__(self, Comentario,id_User):
        self.Comentario = Comentario
        self.id_User = id_User

with app.app_context():
    bd.create_all()

class PostsSchema(ma.Schema):
    class Meta: 
        fields = ('idForo', 'Comentario', 'id_User')