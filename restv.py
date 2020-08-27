from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from Entities.Aeropuerto import *
from Entities.Ruta import *
from Entities.Pasajero import *
from Entities.Avion import *
from Entities.Pista import *
from Entities.Aeropuerto_has_Aerolinea import *
from Entities.Aerolinea import *

serv = Flask(__name__)
serv.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://prog_avanzada:pa2020-1@db-prog-avanzada-g81.cq73qyc2lysx.us-east-1.rds.amazonaws.com/DanielDB'
serv.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Sesion
serv.secret_key=os.urandom(16)

db = SQLAlchemy(serv)
ma = Marshmallow(serv)




@serv.route('/')
def index():

    return render_template('createU.html')

#Rutas de creacion de datos

@serv.route('/aeropuerto/crear', methods=['POST'])
def createAp():
    if request.method == 'POST':

        airport = Aeropuerto(request.json['idAeropuerto'], request.json['Nombre'], request.json['Ubicacion'])
        db.session.add(airport)
        db.session.commit()

    return 'completo'

@serv.route('/aerolinea/crear/<string:id>', methods=['POST'])
def createAl(id):
    if request.method == 'POST':

        airline = Aerolinea(request.json['idAerolinea'], request.json['Nombre'])
        db.session.add(airline)
        db.session.commit()

        enlace = Aeropuerto_has_Aerolinea(id, request.json['idAerolinea'])
        db.session.add(enlace)
        db.session.commit()

    return 'completo'

@serv.route('/avion/crear', methods=['POST'])
def createAv():
    if request.method == 'POST':

        airplane = Avion(request.json['idAvion'], request.json['Modelo'], request.json['Capacidad'], request.json['idAerolinea'], request.json['idRuta'])
        db.session.add(airplane)
        db.session.commit()

    return 'completo'


@serv.route('/pasajero/crear', methods=['POST'])
def createPa():
    if request.method == 'POST':

        pasajero = Avion(request.json['Nombre'], request.json['Clase'], request.json['idAvion'], request.json['idAerolinea'])
        db.session.add(pasajero)
        db.session.commit()

    return 'completo'
@serv.route('/pista/crear', methods=['POST'])
def createPi():
    if request.method == 'POST':

        pista = Pista(request.json['idPista'], request.json['Capacidad'], request.json['Orientacion'], request.json['idAeropuerto'])
        db.session.add(pista)
        db.session.commit()

    return 'completo'

@serv.route('/ruta/crear', methods=['POST'])
def createRu():
    if request.method == 'POST':

        ruta = Ruta(request.json['idRuta'], request.json['Ruta'])
        db.session.add(ruta)
        db.session.commit()

    return 'completo'

#Rutas de modificacion de datos

@serv.route('/aeropuerto/mod/<id>', methods=['PUT'])
def modAp(id):
    if request.method == 'PUT':
        aeropuerto = Aeropuerto.query.get(id)

        aeropuerto.idAeropuerto = request.json['idAeropuerto']
        aeropuerto.Nombre = request.json['Nombre']
        aeropuerto.Ubicacion = request.json['Ubicacion']

        db.session.commit()

    return 'completo'

@serv.route('/aerolinea/mod/<id>', methods=['PUT'])
def modAl(id):
    if request.method == 'PUT':
        aerolinea = Aerolinea.query.get(id)

        aerolinea.idAerolinea = request.json['idAerolinea']
        aerolinea.Nombre = request.json['Nombre']

        db.session.commit()

    return 'completo'

@serv.route('/avion/mod', methods=['PUT'])
def modAv():
    if request.method == 'PUT':
        avion = Avion.query.get(request.json['idAvion'], request.json['idAerolinea'], request.json['idRuta'])


        avion.idAvion = request.json['idAvionM']
        avion.Modelo = request.json['ModeloM']
        avion.Capacidad = request.json['CapacidadM']
        avion.Aerolinea_idAerolinea = request.json['idAerolineaM']
        avion.Ruta_idRuta = request.json['idRutaM']

        db.session.commit()

    return 'completo'

@serv.route('/pasajero/mod/<id>', methods=['PUT'])
def modPa(id):
    if request.method == 'PUT':
        pasajero = Pasajero.query.get(id)

        pasajero.Nombre = request.json['Nombre']
        pasajero.Clase = request.json['Clase']
        pasajero.Avion_idAvion = request.json['idAvion']
        pasajero.Avion_Aerolinea_idAerolinea = request.json['idAerolinea']

        db.session.commit()

    return 'completo'

@serv.route('/pista/mod/<id>', methods=['PUT'])
def modPi(id):
    if request.method == 'PUT':
        pista = Pista.query.get(id)

        pista.idPista = request.json['idPista']
        pista.Capacidad = request.json['Capacidad']
        pista.Orientacion = request.json['Orientacion']
        pista.Aeropuerto_idAeropuerto = request.json['idAeropuerto']

        db.session.commit()

    return 'completo'

@serv.route('/ruta/mod/<id>', methods=['PUT'])
def modRu(id):
    if request.method == 'PUT':
        ruta = Ruta.query.get(id)

        ruta.idRuta = request.json['idRuta']
        ruta.Ruta = request.json['Ruta']

        db.session.commit()

    return 'completo'

#Rutas de recuperacion de datos

@serv.route('/aeropuerto/rec/<id>', methods=['GET'])
def recAp(id):
    if request.method == 'GET':

        return jsonify(AeropuertoSch().dump(Aeropuerto.query.get(id)))

@serv.route('/aerolinea/rec/<id>', methods=['GET'])
def recAl(id):
    if request.method == 'GET':

        return jsonify(AerolineaSch().dump(Aerolinea.query.get(id)))

@serv.route('/avion/rec', methods=['GET'])
def recAv():
    if request.method == 'GET':

        return jsonify(AvionSch(many=True).dump(Avion.query.all()))

@serv.route('/enlace/rec', methods=['GET'])
def recAp_Al():
    if request.method == 'GET':

        return jsonify(Aeropuerto_has_AerolineaSch(many=True).dump(Aeropuerto_has_Aerolinea.query.all()))

@serv.route('/pasajero/rec', methods=['GET'])
def recPa():
    if request.method == 'GET':

        return jsonify(PasajeroSch(many=True).dump(Aeropuerto.query.all()))

@serv.route('/pista/rec', methods=['GET'])
def recPi():
    if request.method == 'GET':

        return jsonify(PistaSch(many=True).dump(Pista.query.all()))

@serv.route('/ruta/rec/<id>', methods=['GET'])
def recRu(id):
    if request.method == 'GET':

        return jsonify(RutaSch().dump(Ruta.query.get(id)))

#Rutas de eliminacion de datos

@serv.route('/aeropuerto/eliminar/<id>', methods=['DELETE'])
@serv.route('/aerolinea/eliminar/<id>', methods=['DELETE'])
@serv.route('/avion/eliminar/<id>', methods=['DELETE'])
@serv.route('/enlace/eliminar/<id>', methods=['DELETE'])
@serv.route('/pasajero/eliminar/<id>', methods=['DELETE'])
@serv.route('/pista/eliminar/<id>', methods=['DELETE'])
@serv.route('/ruta/eliminar/<id>', methods=['DELETE'])





@serv.route('/create/user', methods=['POST', 'GET'])
def createU():
    if request.method == 'POST':

        user = Usuario(request.form['nombre'], request.form['clave'], request.form['permiso'])
        db.session.add(user)
        db.session.commit()

    return render_template('createU.html')

@serv.route('/show/users', methods=['GET'])
def shUsers():
    if request.method == 'GET':
        return jsonify({"Usuarios":UsuarioSch(many=True).dump(db.session.query(Usuario).all())})

if __name__ == '__main__':
    serv.run(port=8080, debug=True)






