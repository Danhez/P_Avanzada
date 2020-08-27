from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Avion(SQLAlchemy().Model):
    __tablename__ = 'Avion'
    idAvion = SQLAlchemy().Column(SQLAlchemy().String(10), primary_key=True, unique=True, nullable=False)
    Modelo = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False)
    Capacidad = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False)
    Aerolinea_idAerolinea = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)
    Ruta_idRuta = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)

    def __init__(self, id, modelo, capacidad, idAerolinea, idRuta):
        self.idAvion = id
        self.Modelo = modelo
        self.Capacidad = capacidad
        self.Aerolinea_idAerolinea = idAerolinea
        self.Ruta_idRuta = idRuta

class AvionSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idAvion', 'Modelo', 'Capacidad', 'Aerolinea_idAerolinea', 'Ruta_idRuta')