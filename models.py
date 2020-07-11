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
        return f'Usuario: {str(self.username)}, {str(self.password)}, {str(self.type)}'


class Pasajero(DBObject):
    id_name = "idpasajero"
    table_name = "pasajero"
    foreign_key_fields = ['usuario']

    def __init__(self, **kwargs):
        super(Pasajero, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.apellido = kwargs.get("apellido", None)
        self.dni = kwargs.get("dni", None)
        self.saldo = kwargs.get("saldo", 0)
        self.es_viajero_frecuente = kwargs.get("es_viajero_frecuente", 0)
        self.usuario = kwargs.get("usuario", None)

    def __str__(self):
        return  f'Pasajero: {str(self.nombre)}, {str(self.apellido)}, {str(self.dni)}, ${self.saldo}, {self.es_viajero_frecuente} \n{str(self.usuario)}'

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
        super(Piloto, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.apellido = kwargs.get("apellido", None)
        self.dni = kwargs.get("dni", None)
        self.legajo = kwargs.get("legajo", None)
        self.sueldo = kwargs.get("sueldo", 0)
        self.esta_en = kwargs.get("esta_en", None)

    def __str__(self):
        return f'Piloto: {str(self.nombre)}, {str(self.apellido)}, {str(self.dni)}, {str(self.legajo)}, ${self.sueldo} \n{str(self.esta_en)}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Piloto, cls).get(obj_id)
        retorno.esta_en = Aeropuerto.get(retorno.esta_en)
        return retorno


class Vuelo(DBObject):
    id_name = "idvuelo"
    table_name = "vuelo"
    foreign_key_fields = ['avion', 'origen', 'destino']

    def __init__(self, **kwargs):
        super(Vuelo, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.fecha = kwargs.get("fecha", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.asientos_libres = kwargs.get("asientos_libres", 0)
        self.precio = kwargs.get("precio", 0)
        self.completado = kwargs.get('completado', 0)
        self.avion = kwargs.get("avion", None)
        self.origen = kwargs.get("origen", None)
        self.destino = kwargs.get("destino", None)

    def __str__(self):
        return  f'Vuelo: {str(self.fecha)}, {self.asientos_libres}, ${self.precio}, {self.completado} \n{str(self.avion)} \n{str(self.destino)}'
    
    @classmethod
    def get(cls, obj_id):
        retorno = super(Vuelo, cls).get(obj_id)
        retorno.avion = Avion.get(retorno.avion)
        retorno.origen = Aeropuerto.get(retorno.origen)
        retorno.destino = Aeropuerto.get(retorno.destino)
        retorno.fecha = retorno.fecha.strftime('%Y-%m-%d')
        return retorno

    @classmethod
    def search(cls, **kwargs):
        return super(Vuelo, cls).search(**kwargs)


class Ubicacion(DBObject):
    id_name = "idUbicacion"
    table_name = "ubicacion"

    def __init__(self, **kwargs):
        super(Ubicacion, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.latitud = kwargs.get("latitud", 0)
        self.longitud = kwargs.get("longitud", 0)
        self.pais = kwargs.get("pais", None)
        self.provincia = kwargs.get("provincia", None)
        self.direccion = kwargs.get("direccion", None)

    def __str__(self):
        return f'Ubicacion: {self.latitud}, {self.longitud}, {str(self.pais)}, {str(self.provincia)}, {str(self.direccion)}'


class Aeropuerto(DBObject):
    id_name = "idaeropuerto"
    table_name = "aeropuerto"
    exclude_fields = ["lst_aviones", 'lst_origenes', 'lst_destinos']
    foreign_key_fields = ['ubicacion', ]

    def __init__(self, **kwargs):
        super(Aeropuerto, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", "")
        self.saldo = kwargs.get("saldo", 0)
        self.ubicacion = kwargs.get("ubicacion", None)
        self.lst_aviones = kwargs.get('lst_aviones', [])
        self.lst_origenes = kwargs.get('lst_origenes', [])
        self.lst_destinos = kwargs.get('lst_destinos', [])

    def __str__(self):
        return  f'Aeropuerto: {str(self.nombre)}, ${self.saldo} \n{str(self.ubicacion)}'

    def inicializar_lst_aviones(self):
        self.lst_aviones = Avion.search(esta_en=self.id)

    def inicializar_lst_origenes(self):
        self.lst_origenes = Vuelo.search(origen=self.id)

    def inicializar_lst_destinos(self):
        self.lst_destinos = Vuelo.search(destino=self.id)

    @classmethod
    def get(cls, obj_id):
        retorno = super(Aeropuerto, cls).get(obj_id)
        retorno.ubicacion = Ubicacion.get(retorno.ubicacion)
        retorno.inicializar_lst_aviones()
        retorno.inicializar_lst_origenes()
        retorno.inicializar_lst_destinos()
        return retorno


class Avion(DBObject):
    id_name = "idavion"
    table_name = "avion"
    foreign_key_fields = ['modelo', 'esta_en']

    def __init__(self, **kwargs):
        super(Avion, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.ultimo_mantenimiento = kwargs.get("ultimo_mantenimiento", datetime.datetime.today().date().strftime('%Y-%m-%d'))
        self.modelo = kwargs.get("modelo", None)
        self.esta_en = kwargs.get("esta_en", None)

    def __str__(self):
        return f'Avion: {str(self.ultimo_mantenimiento)} \n{str(self.modelo)} \n{str(self.esta_en)}'
    
    @classmethod
    def get(cls, obj_id):
        retorno = super(Avion, cls).get(obj_id)
        retorno.modelo = Modelo.get(retorno.modelo)
        retorno.esta_en = Aeropuerto.get(retorno.esta_en)
        retorno.ultimo_mantenimiento = retorno.ultimo_mantenimiento.strftime('%Y-%m-%d')
        return retorno

    @classmethod
    def search(cls, **kwargs):
        return super(Avion, cls).search(**kwargs)


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
        return f'Modelo: {str(self.nombre)}, ({self.fecha_fabricacion}), ${self.coste}, {self.cantidad_asientos} \n{str(self.marca)}'

    @classmethod
    def get(cls, obj_id):
        retorno = super(Modelo, cls).get(obj_id)
        retorno.marca = Marca.get(retorno.marca)
        retorno.fecha_fabricacion = retorno.fecha_fabricacion.strftime('%Y-%m-%d')
        return retorno

    @classmethod
    def search(cls, **kwargs):
        return super(Modelo, cls).search(**kwargs)

    @classmethod
    def traer_modelos_por_nombre(cls, nombre):
        modelos = cls.execute_custom_select(f'''where nombre like ('%{nombre}%')''')
        for m in modelos:
            m.marca = Marca.get(m.marca)
        return modelos

    @classmethod
    def traer_modelos_por_cantidad_asientos(cls, minimo, maximo=None):
        pass


class Marca(DBObject):
    id_name = "idmarca"
    table_name = "marca"
    exclude_fields = ['lst_modelos', ]

    def __init__(self, **kwargs):
        super(Marca, self).__init__(kwargs.get(self.id_name, None) or kwargs.get("id", 0))
        self.nombre = kwargs.get("nombre", None)
        self.lst_modelos = kwargs.get('lst_modelos', [])

    def __str__(self):
        return f'Marca: {self.nombre}'

    def inicializar_lst_modelos(self):
        self.lst_modelos = Modelo.search(marca=self.id)

    @classmethod
    def get(cls, obj_id):
        retorno = super(Marca, cls).get(obj_id)
        retorno.inicializar_lst_modelos()
        return retorno


# TODO
# Traer vuelos entre fechas (puede o no recibir fechas de inicio y fin)
# Treaer vuelos por origen (solo uno)
# Traer aviones por ultimo_mantenimiento (recibe fecha inicio y puede o no recibir fecha fin)
# traer aeropuertos por nombre (usando la forma contiene, con %nombre%)
# Traer vuelos por asientos libres (Recibe una canitidad de asientos y debe retornar los que tengan al menos esa cantidad de asientos libres) y por origen y destino (puede o no recibirlos)
# Traer vuelos por si esta completado o no
# Traer aeropuertos por pais y provincia (la provincia es opcional). Para esto tienen que hacer select anidado
