import datetime

from DBObject import DBObject


class Usuario(DBObject):
    id_name = "idusuario"
    table_name = "usuario"

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
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
        self.usuario = kwargs.get("usuario", 0)


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
        self.esta_en = kwargs.get("esta_en", 0)


class Vuelo(DBObject):
    id_name = "idvuelo"
    table_name = "vuelo"

    def __init__(self, **kwargs):
        super(Vuelo, self).__init__(kwargs.get("id", 0))
        self.fecha = kwargs.get("fecha", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.asientos_libres = kwargs.get("asientos_libres", 0)
        self.precio = kwargs.get("precio", 0)
        self.completado = kwargs.get('completado', 0)
        self.avion = kwargs.get("avion", 0)
        self.origen = kwargs.get("origen", 0)
        self.destino = kwargs.get("destino", 0)


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
        self.ubicacion = kwargs.get("ubicacion", 0)


class Avion(DBObject):
    id_name = "idavion"
    table_name = "avion"

    def __init__(self, **kwargs):
        super(Avion, self).__init__(kwargs.get("id", 0))
        self.ultimo_mantenimiento = kwargs.get("ultimo_mantenimiento", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.modelo = kwargs.get("modelo", 0)
        self.esta_en = kwargs.get("esta_en", 0)


class Modelo(DBObject):
    id_name = "idmodelo"
    table_name = "modelo"

    def __init__(self, **kwargs):
        super(Modelo, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", '')
        self.cantidad_asientos = kwargs.get("cantidad_asientos", 0)
        self.coste = kwargs.get("coste", 0)
        self.fecha_fabricacion = kwargs.get("fecha_fabricacion", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.marca = kwargs.get('marca', None)

    def __str__(self):
        return f'{str(self.marca)} {str(self.nombre)} ({self.fecha_fabricacion}) - ${self.cantidad_asientos}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Modelo, cls).get(obj_id)
        retorno.marca = Marca.get(retorno.marca)
        return retorno


class Marca(DBObject):
    id_name = "idmarca"
    table_name = "marca"

    def __init__(self, **kwargs):
        super(Marca, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)

    def __str__(self):
        return self.nombre