from config.db import bd,ma,app

class users (bd.Model):
    __tablename__ = "tblusers"
    id =bd.Cloum(bd.Integer,primary_key=True)
    fullname=bd.Cloum(bd.String(50))
    email=bd.colum(bd.String(50))

    def __init__ (self,fullname,email):
        self.fullname=fullname
        self.email=email

with app.app_context():
    bd.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fiels =('id','fullname','emai')
