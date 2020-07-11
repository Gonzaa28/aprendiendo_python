from models import *

# Ubicacion
u = Ubicacion(latitud=75.50, longitud=45.78, pais="Argentina", provincia="Buenos Aires", direccion="9 de Julio")
u.save()
u2 = Ubicacion(latitud=45.52, longitud=49.11, pais="Argentina", provincia="Cordoba", direccion="Caguazu")
u2.save()

# Aeropuerto
aeropuerto1 = Aeropuerto(nombre="Ezeiza", saldo=150000, ubicacion=u)
aeropuerto1.save()
aeropuerto2 = Aeropuerto(nombre="El Palomar", saldo=170000, ubicacion=u2)
aeropuerto2.save()

# Marca
marca = Marca(nombre="Ford")
marca.save()

# Modelo
m1 = Modelo(nombre="Mustang", cantidad_asientos=80, coste=170000, marca=marca)
m1.save()
m2 = Modelo(nombre="Focus", cantidad_asientos=60, coste=110000, marca=marca)
m2.save()

# Avion
avion1 = Avion(modelo=m1, esta_en=aeropuerto1)
avion1.save()
avion2 = Avion(modelo=m2, esta_en=aeropuerto2)
avion2.save()

# Vuelo
v = Vuelo(asientos_libres=20, precio=20000, completado=False, origen=aeropuerto1, destino=aeropuerto2, avion=avion1)
v.save()
v = Vuelo(asientos_libres=15, precio=18000, completado=False, origen=aeropuerto2, destino=aeropuerto1, avion=avion1)
v.save()

# Piloto
p = Piloto(nombre="Gonzalo", apellido="Ajuria", dni="43199715", legajo="111", sueldo=15000, esta_en=aeropuerto1)
p.save()

# Usuario
u1 = Usuario(username="Juan Perez", password="abc123", type="Pasajero")
u1.save()
u2 = Usuario(username="Pedro Martinez", password="123abc", type="Pasajero")
u2.save()

# Pasajero
p = Pasajero(nombre="Nicolas", apellido="Aguero", dni="30123456", saldo=20000, es_viajero_frecuente=True, usuario=u1)
p.save()
