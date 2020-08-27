from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Aeropuerto(SQLAlchemy().Model):
    __tablename__ = 'Aeropuerto'
    idAeropuerto = SQLAlchemy().Column(SQLAlchemy().String(10), primary_key=True, unique=True, nullable=False)
    Nombre = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False, unique=True)
    Ubicacion = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False)

    def __init__(self, id, nombre, ubicacion):
        self.idAeropuerto = id
        self.Nombre = nombre
        self.Ubicacion = ubicacion

class AeropuertoSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idAeropuerto', 'Nombre', 'Ubicacion')