from cine import *

usuario1 = Usuario(1, "Isaac", "isaac@mail.com", "222")
usuario2 = Usuario(2, "Ana", "ana@mail.com", "333")

empleado1 = Empleado(3, "Carlos", "carlos@mail.com", "111", "E01", "ADMIN", "Matutino")
empleado2 = Empleado(4, "Luis", "luis@mail.com", "444", "E02", "TAQUILLERO", "Vespertino")

print(usuario1.login())
print(empleado1.login())
print(empleado2.marcarEntrada())
print(empleado1.gestionarFunciones())
print(empleado2.gestionarFunciones())
print()

sala1 = Sala(1, "Sala IMAX", "Planta alta", "IMAX", 100, True)
sala2 = Sala(2, "Sala 3D", "Planta baja", "3D", 60, False)

zona_comida = ZonaComida(3, "Snack Zone", "Entrada")
zona_comida.actualizarInventario("Palomitas", 50)
zona_comida.actualizarInventario("Refresco", 40)

print("Inventario inicial:", zona_comida.stockActual)
zona_comida.venderProducto("Palomitas")
print("Inventario después de vender:", zona_comida.stockActual)
print()

pelicula1 = Pelicula("Batman", 120, "B", "Acción")
pelicula2 = Pelicula("Toy Story", 95, "AA", "Animación")

print(pelicula1.obtenerSinopsis())
print("¿Toy Story es para todo público?", pelicula2.esAptaParaTodoPublico())
print()

funcion1 = Funcion(1, pelicula1, sala1, "20:00", 80)
funcion2 = Funcion(2, pelicula2, sala2, "18:00", 60)

print("Asientos libres función 1:", funcion1.calcularAsientosLibres())
print(funcion1.obtenerDetallesFuncion())
print()

promo1 = Promocion("DESC10", "Descuento 10%", 0.10, "31-12-2026")
promo2 = Promocion("DESC20", "Descuento 20%", 0.20, "31-12-2026")

reserva1 = Reserva(usuario1, funcion1, ["A1", "A2", "A3"])
reserva2 = Reserva(usuario1, funcion1, ["A4"])
reserva3 = Reserva(usuario2, funcion2, ["B1", "B2"])

usuario1.crearReserva(reserva1)
usuario1.crearReserva(reserva2)
usuario2.crearReserva(reserva3)

print(reserva1)
print(reserva2)
print(reserva3)
print()

print("Total antes de promo:", reserva1.montoTotal)
reserva1.aplicarPromocion(promo1)
print("Total después de promo:", reserva1.montoTotal)
print()

reserva_combinada = reserva1 + reserva2
print("Reserva combinada:", reserva_combinada)

reserva_x2 = reserva2 * 2
print("Reserva multiplicada:", reserva_x2)
print()

print("¿reserva1 es igual a reserva2?", reserva1 == reserva2)
print("¿usuario1 es igual a usuario2?", usuario1 == usuario2)
print()

reserva1.confirmarPago()
print("Estado reserva1:", reserva1.estado)

usuario1.cancelarReserva(reserva2)
print("Estado reserva2:", reserva2.estado)
print()

print("Historial de Isaac:")
for r in usuario1.historialReservas:
    print(r)

print()
print("Total personas creadas:", Persona.total_personas)
print("Total reservas creadas:", Reserva.total_reservas)
