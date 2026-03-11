class Material:
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible=True):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible

    def __str__(self):
        return f"{self.titulo} ({self.añoPublicacion})"

    def __repr__(self):
        return f"Material({self.titulo})"


class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero


class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad


class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB


class Persona:
    total_personas = 0

    def __init__(self, idPersona, nombre):
        self._idPersona = idPersona
        self._nombre = nombre
        Persona.total_personas += 1

    def __eq__(self, other):
        return isinstance(other, Persona) and self._idPersona == other._idPersona

    def __str__(self):
        return self._nombre

    def __repr__(self):
        return f"Persona({self._nombre})"


class Usuario(Persona):
    def __init__(self, idPersona, nombre, limitePrestamos):
        super().__init__(idPersona, nombre)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []

    def solicitarPrestamo(self, prestamo):
        if len(self.listaActiva) < self.limitePrestamos:
            self.listaActiva.append(prestamo)
            print("Préstamo registrado")
        else:
            print("Límite de préstamos alcanzado")


class Bibliotecario(Persona):
    def gestionarPrestamo(self, prestamo):
        print(f"Gestionando préstamo {prestamo.idPrestamo}")

    def transferirMaterial(self, material, sucursalDestino):
        sucursalDestino.catalogoLocal.append(material)
        print(f"Material transferido a {sucursalDestino.nombre}")


class Sucursal:
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

    def __str__(self):
        return self.nombre

class Prestamo:
    total_prestamos = 0

    def __init__(self, fechaInicio, fechaDevolucion, usuario, material):
        Prestamo.total_prestamos += 1
        self.idPrestamo = Prestamo.total_prestamos
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

    def __add__(self, other):
        print("Unificando préstamos")
        return Prestamo(self.fechaInicio, self.fechaDevolucion, self.usuario, self.material)

    def __mul__(self, n):
        print("Repitiendo préstamo")
        return Prestamo(self.fechaInicio, self.fechaDevolucion, self.usuario, self.material)

    def __eq__(self, other):
        return self.idPrestamo == other.idPrestamo

    def __str__(self):
        return f"Préstamo {self.idPrestamo} - {self.material.titulo}"

    def __repr__(self):
        return f"Prestamo({self.idPrestamo})"


class Penalizacion:
    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def calcularMulta(self):
        print(f"Multa: ${self.monto}")

    def bloquearUsuario(self, usuario):
        print(f"Usuario {usuario} bloqueado por: {self.motivo}")


class Catalogo:
    def __init__(self, sucursales):
        self.sucursales = sucursales

    def buscarPorAutor(self, autor):
        print(f"Buscando libros de {autor}")
        for suc in self.sucursales:
            for mat in suc.catalogoLocal:
                if isinstance(mat, Libro) and mat.autor == autor:
                    print(mat.titulo, "en", suc.nombre)

    def buscarEnTodasSucursales(self, titulo):
        print(f"Buscando {titulo}")
        for suc in self.sucursales:
            for mat in suc.catalogoLocal:
                if mat.titulo == titulo:
                    print("Encontrado en", suc.nombre)
