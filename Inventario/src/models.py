from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default='passenger')
    productos = db.relationship('Producto', backref='user', lazy=True)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    fecha_vencimiento = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

class Vuelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    hora_llegada = db.Column(db.Time, nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_reserva = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    motivo_viaje = db.Column(db.String(200), nullable=False)
    nombre_usuario = db.Column(db.String(80), nullable=False)
    cantidad_asientos = db.Column(db.Integer, nullable=False)
    clase = db.Column(db.String(20), nullable=False)
    maletas = db.Column(db.Integer, nullable=False)
    vuelo_id = db.Column(db.Integer, db.ForeignKey('vuelo.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_checkin = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    maletas_confirmadas = db.Column(db.Integer, nullable=False)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reserva.id'), nullable=False)
