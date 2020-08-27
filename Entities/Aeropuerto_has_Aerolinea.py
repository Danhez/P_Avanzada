from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Aeropuerto_has_Aerolinea(SQLAlchemy().Model):
    __tablename__ = 'Aeropuerto_has_Aerolinea'
    Aeropuerto_idAeropuerto = SQLAlchemy().Column(SQLAlchemy().String(10), primary_key=True, nullable=False)
    Aerolinea_idAerolinea = SQLAlchemy().Column(SQLAlchemy().Integer, primary_key=True, nullable=False)

    def __init__(self, idAeropuerto, idAerolinea):
        self.Aerolinea_idAerolinea = idAerolinea
        self.Aeropuerto_idAeropuerto = idAeropuerto

class Aeropuerto_has_AerolineaSch(Marshmallow().Schema): #Esquema para convertir a json
    class Meta:
        fields = ('Aeropuerto_idAeropuerto', 'Aerolinea_idAerolinea')