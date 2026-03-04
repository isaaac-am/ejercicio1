class Persona:
    total_personas = 0

    def __init__(self, idPersona, nombre, email, telefono):
        self._idPersona = idPersona
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        Persona.total_personas += 1

    def login(self):
        raise NotImplementedError

    def logout(self):
        return f"{self._nombre} cerró sesión"

    def actualizarDatos(self, nombre, email):
        self._nombre = nombre
        self._email = email

    def __eq__(self, other):
        return isinstance(other, Persona) and self._idPersona == other._idPersona

    def __str__(self):
        return self._nombre

    def __repr__(self):
        return f"Persona({self._idPersona}, {self._nombre})"


class Usuario(Persona):

    def __init__(self, idPersona, nombre, email, telefono):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = 0
        self.historialReservas = []

    def login(self):
        return f"Usuario {self._nombre} inició sesión"

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)

    def cancelarReserva(self, reserva):
        reserva.estado = "CANCELADA"

    def consultarPromociones(self):
        return "Promociones disponibles"


class Empleado(Persona):

    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol  # "TAQUILLERO", "ADMIN", "LIMPIEZA"
        self.horario = horario

    def login(self):
        return f"Empleado {self._nombre} inició sesión"

    def marcarEntrada(self):
        return "Entrada registrada"

    def gestionarFunciones(self):
        if self.rol == "ADMIN":
            return "Funciones gestionadas"
        return "No autorizado"


class Espacio:

    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificarDisponibilidad(self):
        return True

    def limpiarEspacio(self):
        return "Espacio limpio"


class Sala(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo  # "2D", "3D", "IMAX"
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip
        self.asientos_ocupados = []

    def ajustarAforo(self, nuevo):
        self.capacidadTotal = nuevo

    def obtenerTipoSala(self):
        return self.tipo


class ZonaComida(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def venderProducto(self, producto):
        if self.stockActual.get(producto, 0) > 0:
            self.stockActual[producto] -= 1

    def actualizarInventario(self, producto, cantidad):
        self.stockActual[producto] = cantidad
        
class Pelicula:

    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        return f"Sinopsis de {self.titulo}"

    def esAptaParaTodoPublico(self):
        return self.clasificacion == "AA"

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f"Pelicula({self.titulo})"


class Funcion:

    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio  # string
        self.precioBase = precioBase

    def calcularAsientosLibres(self):
        return self.sala.capacidadTotal - len(self.sala.asientos_ocupados)

    def obtenerDetallesFuncion(self):
        return f"{self.pelicula.titulo} - {self.horarioInicio}"


class Promocion:

    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion  # string

    def esValida(self, usuario):
        return True

    def aplicarDescuento(self, monto):
        return monto * (1 - self.porcentajeDescuento)


class Reserva:
    total_reservas = 0

    def __init__(self, usuario, funcion, asientos):
        Reserva.total_reservas += 1
        self.idReserva = Reserva.total_reservas
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = len(asientos) * funcion.precioBase
        self.estado = "PENDIENTE"

    def confirmarPago(self):
        self.estado = "PAGADA"

    def generarTicket(self):
        return f"Ticket {self.idReserva} - {self.usuario}"

    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)

    def __add__(self, other):
        nuevos_asientos = self.asientos + other.asientos
        return Reserva(self.usuario, self.funcion, nuevos_asientos)

    def __mul__(self, n):
        return Reserva(self.usuario, self.funcion, self.asientos * n)

    def __eq__(self, other):
        return self.idReserva == other.idReserva

    def __str__(self):
        return f"Reserva {self.idReserva} - Total: {self.montoTotal}"

    def __repr__(self):
        return f"Reserva({self.idReserva}"
