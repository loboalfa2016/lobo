from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256


db = SQLAlchemy()


class Rol(db.Model):
    __tablename__ = 'roles'
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), unique=True, nullable=False)


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable=False)

    rol = db.relationship('Rol', backref='usuarios', lazy=True)

    def get_id(self):
        return str(self.id_usuario)

    def set_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    def check_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)


class Actividad(db.Model):
    __tablename__ = 'actividades'
    id_actividad = db.Column(db.Integer, primary_key=True)
    nombre_actividad = db.Column(db.String(100), unique=True, nullable=False)


class Entrenamiento(db.Model):
    __tablename__ = 'entrenamientos'
    id_entrenamiento = db.Column(db.Integer, primary_key=True)
    id_entrenador = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    entrenador = db.relationship('Usuario', backref='entrenamientos', lazy=True)
    actividad = db.relationship('Actividad', backref='entrenamientos', lazy=True)
