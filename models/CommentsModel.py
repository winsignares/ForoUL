from config.db import bd, ma, app


class Comment(bd.Model):
    __tablename__ = "tblcomments"
   # idPost = bd.Column(bd.Integer, bd.ForeignKey('tblPostsW.idPost'))
    Comentario = bd.Column(bd.String(200))
    id_User = bd.Column(bd.Integer, bd.ForeignKey('tblUsers.id'))
    idComments = bd.Column(bd.Integer, primary_key = True)
   
    def __init__(self, Comentario,id_User,idPost):
        self.Comentario = Comentario
        self.id_User = id_User
        self.idPost = idPost
       

with app.app_context():
    bd.create_all()

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ('idPost', 'Comentario', 'id_User','idComments')
