from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Pista(SQLAlchemy().Model):
    __tablename__ = 'Pista'
    idPista = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, unique=True, nullable=False)
    Capacidad = SQLAlchemy().Column(SQLAlchemy().Integer, nullable=False, unique=True)
    Orientacion = SQLAlchemy().Column(SQLAlchemy().String(10), nullable=False)
    Aeropuerto_idAeropuerto = SQLAlchemy().Column(SQLAlchemy().String(10), primary_key=True, nullable=False)

    def __init__(self, id, capacidad, orientacion, idAeropuerto):
        self.idPista = id
        self.Capacidad = capacidad
        self.Orientacion = orientacion
        self.Aeropuerto_idAeropuerto = idAeropuerto

class PistaSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idPista', 'Capacidad', 'Orientacion', 'idAeropuerto')