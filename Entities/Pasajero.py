from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Pasajero(SQLAlchemy().Model):
    __tablename__ = 'Pasajero'
    idPasajero = SQLAlchemy().Column(SQLAlchemy().String(10), primary_key=True, unique=True, nullable=False, autoincrement=True)
    Nombre = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False)
    Clase = SQLAlchemy().Column(SQLAlchemy().String(45), nullable=False)
    Avion_idAvion = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)
    Avion_Aerolinea_idAerolinea = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)

    def __init__(self, nombre, clase, idAvion, idAerolinea):
        self.Nombre = nombre
        self.Clase = clase
        self.Avion_idAvion = idAvion
        self.Avion_Aerolinea_idAerolinea = idAerolinea

class PasajeroSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('idPasajero', 'Nombre', 'Clase', 'Avion_idAvion', 'Avion_Aerolinea_idAerolinea')