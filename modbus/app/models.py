from app import db
import time
from datetime import datetime


class moduloDC(db.Model):
    __tablename__ = 'moduloDC'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tensao = db.Column(db.Float, nullable=False)
    corrente = db.Column(db.Float, nullable=False)
    potencia = db.Column(db.Float, nullable=False)
    alerta = db.Column(db.String(50), nullable=False)
    registro = db.Column(db.DateTime, default=datetime.now)