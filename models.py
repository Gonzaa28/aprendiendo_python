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

    def __str__(self):
        return f'{str(self.username)} {str(self.password)} {str(self.type)}'


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

    def __str__(self):
        return  f'{str(self.usuario)} {str(self.nombre)} {str(self.apellido)} {str(self.dni)} ${self.saldo} {self.es_viajero_frecuente}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Pasajero, cls).get(obj_id)
        retorno.usuario = Usuario.get(retorno.usuario)
        return retorno


class Piloto(DBObject):
    id_name = "idpiloto"
    table_name = "piloto"
    foreign_key_fields = ['esta_en', ]

    def __init__(self, **kwargs):
        super(Piloto, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.apellido = kwargs.get("apellido", None)
        self.dni = kwargs.get("dni", None)
        self.legajo = kwargs.get("legajo", None)
        self.sueldo = kwargs.get("sueldo", 0)
        self.esta_en = kwargs.get("esta_en", 0)

    def __str__(self):
        return f'{str(self.esta_en)} {str(self.nombre)} {str(self.apellido)} {str(self.dni)} {str(self.legajo)} ${self.sueldo}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Piloto, cls).get(obj_id)
        retorno.esta_en = Aeropuerto.get(retorno.esta_en)
        return retorno


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

    '''
    def __str__(self):
        return  f'{str(self.avion)} {str(self.origen)} {str(self.destino)} {str(self.fecha)} {self.asientos_libres} ${self.precio} {self.completado}'
    
    @classmethod
    def get(cls, obj_id):
        retorno = super(Vuelo, cls).get(obj_id)
        retorno.avion = Avion.get(retorno.avion)
        retorno.origen = Aeropuerto.get(retorno.origen)
        retorno.destino = Aeropuerto.get(retorno.destino)
        return retorno
    '''


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

    def __str__(self):
        return f'{self.latitud} {self.longitud} {str(self.pais)} {str(self.provincia)} {str(self.direccion)}'


class Aeropuerto(DBObject):
    id_name = "idaeropuerto"
    table_name = "aeropuerto"

    def __init__(self, **kwargs):
        super(Aeropuerto, self).__init__(kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", "")
        self.saldo = kwargs.get("saldo", 0)
        self.ubicacion = kwargs.get("ubicacion", 0)

    def __str__(self):
        return  f'{str(self.ubicacion)} {str(self.nombre)} ${self.saldo}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Aeropuerto, cls).get(obj_id)
        retorno.ubicacion = Ubicacion.get(retorno.ubicacion)
        return retorno


#Problema al guardar un avion en la base de datos

class Avion(DBObject):
    id_name = "idavion"
    table_name = "avion"

    def __init__(self, **kwargs):
        super(Avion, self).__init__(kwargs.get("id", 0))
        self.ultimo_mantenimiento = kwargs.get("ultimo_mantenimiento", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.modelo = kwargs.get("modelo", 0)
        self.esta_en = kwargs.get("esta_en", 0)

    '''
    def __str__(self):
        return f'{str(self.esta_en)} {str(self.modelo)} {str(self.ultimo_mantenimiento)}'

    
    @classmethod
    def get(cls, obj_id):
        retorno = super(Avion, cls).get(obj_id)
        retorno.modelo = Modelo.get(retorno.modelo)
        retorno.esta_en = Aeropuerto.get(retorno.esta_en)
        return retorno
    '''


class Modelo(DBObject):
    id_name = "idmodelo"
    table_name = "modelo"
    foreign_key_fields = ['marca']

    def __init__(self, **kwargs):
        super(Modelo, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", '')
        self.cantidad_asientos = kwargs.get("cantidad_asientos", 0)
        self.coste = kwargs.get("coste", 0)
        self.fecha_fabricacion = kwargs.get("fecha_fabricacion", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.marca = kwargs.get('marca', None)

    def __str__(self):
        return f'{str(self.marca)} {str(self.nombre)} ({self.fecha_fabricacion}) ${self.coste} {self.cantidad_asientos}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Modelo, cls).get(obj_id)
        retorno.marca = Marca.get(retorno.marca)
        retorno.fecha_fabricacion = retorno.fecha_fabricacion.strftime('%Y-%m-%d')
        return retorno

    @classmethod
    def search(cls, **kwargs):
        return super(Modelo, cls).search(**kwargs)


class Marca(DBObject):
    id_name = "idmarca"
    table_name = "marca"
    exclude_fields = ['lst_modelos', ]

    def __init__(self, **kwargs):
        super(Marca, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.lst_modelos = kwargs.get('lst_modelos', [])

    def __str__(self):
        return self.nombre

    def inicializar_lst_modelos(self):
        self.lst_modelos = Modelo.search(marca=self.id)

    @classmethod
    def get(cls, obj_id):
        retorno = super(Marca, cls).get(obj_id)
        retorno.inicializar_lst_modelos()
        return retorno
