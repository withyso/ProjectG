from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username= db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    gold = db.Column(db.Integer)
    codigo_referido = db.Column(db.String(7), unique=True, nullable=False)
    nombre = db.Column(db.String(12), nullable=False)
    apellido = db.Column(db.String(12), nullable=False)
    permiso_de_mineria = db.Column(db.String(15), nullable=True)
    pico = db.Column(db.String(10), nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Referidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    codigo_referido = db.Column(db.String(7),nullable=False)  

    # Relación inversa con el modelo Usuario
    usuario = relationship('User', backref='referencias',  foreign_keys=[usuario_id])

    def __repr__(self):
        return f'usuario con id{self.id} referido con codigo {self.codigo_referido}'

class Administrador(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(12))

    def __repr__(self):
        return f'Administrador con el correo {self.email}'
    
    def serialize(self):
        return {
            'username' : self.username,
            'email': self.email
        }