import mysql.connector as conn


class DBObject:
    id_name = "id"
    table_name = ""
    db = conn.connect(host="localhost", user="root", password="root", database="aprendiendo_python")
    exclude_fields = []  # una lista de string con los nombres de los atributos que no se persisten
    foreign_key_fields = []

    def __init__(self, obj_id=0):
        self.id = obj_id

    def __str__(self):
        return self.id

    @classmethod
    def search(cls, **kwargs):
        cursor = cls.db.cursor(dictionary=True)
        cursor.execute(f"select * from {cls.table_name} {cls.armar_campos(is_where=True, no_id=True, **kwargs)}")
        resultado = cursor.fetchall()
        return [cls(**r) for r in resultado]

    @classmethod
    def get(cls, obj_id):
        cursor = cls.db.cursor(dictionary=True)
        cursor.execute(f'select * from {cls.table_name} where {cls.id_name} = {obj_id}')
        return cls(**cursor.fetchone())

    def save(self):  # FIXME agregar exclusion de claves foraneas del diccinoario e incluir parametros por kwargs
        cursor = self.db.cursor()
        if self.id == 0:
            cursor.execute(
                f'''INSERT INTO {self.table_name} ({self.armar_campos(no_values=True, no_id=True, **self.__dict__)}) 
                VALUES ({self.armar_campos(no_names=True, no_id=True, **self.__dict__)})'''
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                f'''UPDATE {self.table_name} SET {self.armar_campos(no_id=False, **self.__dict__)} 
                WHERE {self.id_name}={self.id}'''
            )
        self.db.commit()

    def delete(self):
        cursor = self.db.cursor(dictionary=True)
        if self.id > 0:
            cursor.execute(f'''DELETE FROM {self.table_name} where {self.id_name} = {self.id}''')
            self.db.commit()
            self.id = 0

    @classmethod
    def armar_campos(cls, no_names=False, no_values=False, is_where=False, no_id=False, **kwargs):
        cadena = "where " if is_where and len(kwargs) > 0 else ""
        vals = kwargs.copy()
        for field in cls.exclude_fields:
            vals.pop(field, None)
        if no_id:
            vals.pop('id', None) or vals.pop(cls.id_name, None)
        else:
            vals[cls.id_name] = vals.pop('id', None) or vals.pop(cls.id_name, 0)

        cantidad_operadores = len(vals)

        if cantidad_operadores <= 0:
            return ''

        if not no_names and not no_values:  # Si lo pido con nombres y con valores
            for a in vals:
                cadena += str(a) + f'''={vals[a] if type(vals[a]) is not str else "'" + vals[a] + "'"}''' # FIXME agregar las fechassss y para NoneType
                cantidad_operadores -= 1
                if cantidad_operadores > 0:
                    cadena += ' and ' if is_where else ', '

        if no_values and not is_where:  # Si lo pido din valores
            for a in vals:
                cadena += str(a)
                cantidad_operadores -= 1
                if cantidad_operadores > 0:
                    cadena += ', '

        if no_names and not is_where:  # Si lo pido sin nombres
            for a in vals:
                cadena += f'''{vals[a] if type(vals[a]) is not str else "'" + vals[a] + "'"}'''
                cantidad_operadores -= 1
                if cantidad_operadores > 0:
                    cadena += ', '

        if no_names and no_values and is_where:
            raise Exception('No se que le llego al armar campos')

        return cadena

    @classmethod
    def execute_custom_select(cls, where_clause):  # Si se usan id aca tienen que poner el nombre que tiene en la BD
        q = f'SELECT * FROM {cls.table_name} ' + where_clause
        cursor = cls.db.cursor(dictionary=True)
        cursor.execute(q)
        return [cls(**x) for x in cursor.fetchall()]
