#from models import  *

#Ubicacion
u = Ubicacion(latitud = 75.50, longitud = 45.78, pais = "Argentina", provincia = "Buenos Aires", direccion = "9 de Julio")
u.save()
u = Ubicacion(latitud = 45.52, longitud = 49.11, pais = "Argentina", provincia = "Cordoba", direccion = "Caguazu")
u.save()

#Aeropuerto
a = Aeropuerto(nombre = "Ezeiza", saldo = 150000, ubicacion = 1)
a.save()
a = Aeropuerto(nombre = "El Palomar", saldo = 170000, ubicacion = 2)
a.save()

#Marca
m = Marca(nombre = "Ford")
m.save()

#Modelo
m = Modelo(nombre = "Mustang", cantidad_asientos = 80, coste = 170000, marca = 1)
m.save()
m = Modelo(nombre = "Focus", cantidad_asientos = 60, coste = 110000, marca = 1)
m.save()

#Avion
a = Avion(modelo = 1, esta_en = 1)
a.save()
a = Avion(modelo = 2, esta_en = 1)
a.save()

#Vuelo
v = Vuelo(asientos_libres = 20, precio = 20000, completado = False, origen = 1, destino = 2, avion = 1)
v.save()
v = Vuelo(asientos_libres = 15, precio = 18000, completado = False, origen = 1, destino = 2, avion = 1)
v.save()

#Piloto
'''
p = Piloto(nombre = "Gonzalo", apellido = "Ajuria", dni = "43199715", legajo = "111", sueldo = 15000, esta_en = 1)
p.save()
'''

#Usuario
u = Usuario(username = "Juan Perez", password = "abc123", type = "Pasajero")
u.save()
u = Usuario(username = "Pedro Martinez", password = "123abc", type = "Pasajero")
u.save()

#Pasajero
p = Pasajero(nombre = "Nicolas", apellido = "Aguero", dni = "30123456", saldo = 20000, es_viajero_frecuente = True, usuario = 1)
p.save()