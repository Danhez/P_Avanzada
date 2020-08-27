from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Ruta(SQLAlchemy().Model):
    __tablename__ = 'Ruta'
    idRuta = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)
    Ruta = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False, unique=True)

    def __init__(self, id, ruta):
        self.idRuta = id
        self.Ruta = ruta

class RutaSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idRuta', 'Ruta')