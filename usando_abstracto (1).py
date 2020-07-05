from abstract_conector import DBObject

'''
class Persona(DBObject):
    id_name = 'idPersona'  # este es el nombre del campo id
    table_name = 'persona'  # este es el nombre de la tabla

    def __init__(self, **kwargs):  # el id se manda solo como id, no como sea que lo llamaron uds en la bd
        super(Persona, self).__init__(kwargs.get('id', 0))  # Empezar los constructores siempre asi
        self.nombre = kwargs.get('nombre', None)  # El segundo parametro es el valor por defecto si no mandaron nombre
        self.dni = kwargs.get('dni', None)
        self.apellido = kwargs.get('apellido')

    def __str__(self):
        return f'''{self.nombre}, {self.apellido} - {self.dni}'''

    # Tambien pueden  sobreescribir los metodos que hice yo por si quieren cambiar alguna funcionalidad, por ejemplo traer otros objetos


class Vuelo(DBObject):
    id_name = 'idVuelo'
    table_name = 'vuelo'

    def __init__(self, **kwargs):
        super(Vuelo, self).__init__(kwargs.get('id', 0))
        self.piloto = kwargs.get('piloto', None)
        self.fecha = kwargs.get('fecha', None)

    @classmethod
    def get(cls, id):
        retorno = super(Vuelo, cls).get(id)
        retorno.piloto = Persona.get(retorno.piloto)  # asi me traigo el objeto asociado
        return retorno


class Pasajero(DBObject):
    id_name = "dni"
    table_name = "pasajero"

    def __init__(self, **kwargs):
        super(Pasajero, self).__init__(kwargs.get('id', 0))
        self.dni = kwargs.get('dni', 0)
        self.apellido = kwargs.get('apellido', "")
        self.nombre = kwargs.get('nombre', "")
        self.es_viajero_frecuente = kwargs.get('es_viajero_frecuente', 0)
'''

class Usuario(DBObject):
    id_name = "idusuario"
    table_name = "usuario"

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(kwargs.get("id", 0))
        self.username = kwargs.get("username", None)
        self.password = kwargs.get("password", None)
        self.type = kwargs.get("type", None)


class Pasajero(DBObject):
    id_name = "idpasajero"
    table_name = "pasajero"

    def __init__(self, **kwargs):
        super(Pasajero, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.apellido = kwargs.get("apellido", None)
        self.dni = kwargs.get("dni", None)
        self.saldo = kwargs.get("saldo", 0)
        self.es_viajero_frecuente = kwargs.get("es_viajero_frecuente", 0)


class Piloto(DBObject):
    id_name = "idpiloto"
    table_name = "piloto"

    def __init__(self, **kwargs):
        super(Piloto, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.apellido = kwargs.get("apellido", None)
        self.dni = kwargs.get("dni", None)
        self.legajo = kwargs.get("legajo", None)
        self.sueldo = kwargs.get("saldo", 0)


class Vuelo(DBObject):
    id_name = "idVuelo"
    table_name = "vuelo"

    def __init__(self, **kwargs):
        super(Vuelo, self).__init__(kwargs.get("id", 0))
        self.fecha = kwargs.get("fecha", None)
        self.asientos_libres = kwargs.get("asientos_libres", 0)
        self.precio = kwargs.get("precio", 0)


class Ubicacion(DBObject):
    id_name = "idUbicacion"
    table_name = "ubicacion"

    def __init__(self, **kwargs):
        super(Ubicacion, self).__init__(kwargs.get("id", 0))
        self.latitud = kwargs.get("latitud", 0)
        self.longitud = kwargs.get("longitud", 0)
        self.pais = kwargs.get("pais", None)
        self.provincia = kwargs.get("provincia", None)
        self.direccion = kwargs.get("direccion", None)


class Aeropuerto(DBObject):
    id_name = "idaeropuerto"
    table_name = "aeropuerto"

    def __init__(self, **kwargs):
        super(Aeropuerto, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.saldo = kwargs.get("saldo", 0)


class Avion(DBObject):
    id_name = "idavion"
    table_name = "avion"

    def __init__(self, **kwargs):
        super(Avion, self).__init__(kwargs.get("id", 0))
        self.ultimo_mantenimiento = kwargs.get("ultimo_mantenimiento", None)


class Modelo(DBObject):
    id_name = "idmodelo"
    table_name = "modelo"

    def __init__(self, **kwargs):
        super(Modelo, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.cantidad_asientos = kwargs.get("cantidad_asientos", 0)
        self.coste = kwargs.get("coste", 0)
        self.fecha_fabricacion = kwargs.get("fecha_fabricacion", None)


class Marca(DBObject):
    id_name = "idmarca"
    table_name = "marca"

    def __init__(self, **kwargs):
        super(Marca, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)


