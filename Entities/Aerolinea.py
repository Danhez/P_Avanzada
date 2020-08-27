from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Aerolinea(SQLAlchemy().Model):
    __tablename__ = 'Aerolinea'
    idAerolinea = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, unique=True, nullable=False)
    Nombre = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False, unique=True)

    def __init__(self, id, nombre):
        self.idAerolinea = id
        self.Nombre = nombre

class AerolineaSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idAerolinea', 'Nombre')