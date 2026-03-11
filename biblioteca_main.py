from biblioteca import *

print("===== BIBLIOTECA DIGITAL =====")
print()

libro1 = Libro(1,"1984",1949,"George Orwell","111","Distopía")
libro2 = Libro(2,"El Quijote",1605,"Cervantes","222","Novela")
libro3 = Libro(3,"Fahrenheit 451",1953,"Ray Bradbury","333","Distopía")
libro4 = Libro(4,"Dracula",1897,"Bram Stoker","444","Terror")
libro5 = Libro(5,"It",1986,"Stephen King","555","Terror")
libro6 = Libro(6,"Dune",1965,"Frank Herbert","666","Ciencia ficción")
libro7 = Libro(7,"Fundación",1951,"Isaac Asimov","777","Ciencia ficción")
libro8 = Libro(8,"El Hobbit",1937,"Tolkien","888","Fantasía")
libro9 = Libro(9,"Orgullo y Prejuicio",1813,"Jane Austen","999","Romance")
libro10 = Libro(10,"La Odisea",-700,"Homero","101","Épica")

print(libro1)
print(libro2)
print(libro3)
print(libro4)
print(libro5)
print(libro6)
print(libro7)
print(libro8)
print(libro9)
print(libro10)


suc1 = Sucursal(1, "Centro")
suc2 = Sucursal(2, "Norte")

print("Materiales cargados en sucursales")
print()

usuario1 = Usuario(1,"Isaac",3)
usuario2 = Usuario(2,"Ana",2)
usuario3 = Usuario(3,"Mario",3)
usuario4 = Usuario(4,"Lucia",2)
usuario5 = Usuario(5,"Pedro",3)
usuario6 = Usuario(6,"Sofia",2)
usuario7 = Usuario(7,"Diego",3)
usuario8 = Usuario(8,"Valeria",2)
usuario9 = Usuario(9,"Andres",3)
usuario10 = Usuario(10,"Fernanda",2)

biblio1 = Bibliotecario(3, "Carlos")

print("Usuarios creados:")
print(usuario1) 
print(usuario2)
print(usuario3)
print(usuario4)
print(usuario5)
print(usuario6)
print(usuario7)
print(usuario8)
print(usuario9)
print(usuario10)
print()

prestamo1 = Prestamo("01/02/2026", "10/02/2026", usuario1, libro1)
prestamo2 = Prestamo("02/06/2026", "10/02/2026", usuario2, libro2)
prestamo3 = Prestamo("03/07/2026", "10/02/2026", usuario3, libro5)
prestamo4 = Prestamo("04/02/2026", "10/02/2026", usuario4, libro6)
prestamo5 = Prestamo("05/04/2026", "10/02/2026", usuario5, libro8)
prestamo6 = Prestamo("06/09/2026", "10/02/2026", usuario6, libro2)
prestamo7 = Prestamo("07/03/2026", "10/02/2026", usuario7, libro4)
prestamo8 = Prestamo("08/01/2026", "10/02/2026", usuario8, libro6)
prestamo9 = Prestamo("09/06/2026", "10/02/2026", usuario9, libro7)
prestamo10 = Prestamo("10/09/2026", "10/02/2026", usuario10, libro1)

usuario1.solicitarPrestamo(prestamo1)
usuario2.solicitarPrestamo(prestamo2)
usuario3.solicitarPrestamo(prestamo3)
usuario4.solicitarPrestamo(prestamo4)
usuario5.solicitarPrestamo(prestamo5)
usuario6.solicitarPrestamo(prestamo6)
usuario7.solicitarPrestamo(prestamo7)
usuario8.solicitarPrestamo(prestamo8)
usuario9.solicitarPrestamo(prestamo9)
usuario10.solicitarPrestamo(prestamo10)

print(prestamo1)
print(prestamo2)
print(prestamo3)
print(prestamo4)
print(prestamo5)
print(prestamo6)
print(prestamo7)
print(prestamo8)
print(prestamo9)
print(prestamo10)
print()


biblio1.gestionarPrestamo(prestamo1)
biblio1.transferirMaterial(libro1, suc2)
print()


penal1 = Penalizacion(50, "Retraso en devolución")
penal1.calcularMulta()
penal1.bloquearUsuario(usuario1)
print()


catalogo = Catalogo([suc1, suc2])
catalogo.buscarPorAutor("George Orwell")
catalogo.buscarEnTodasSucursales("1984")
print()


prestamo_total = prestamo1 
prestamo_x2 = prestamo1 * 2

print(prestamo_total)
print(prestamo_x2)
print()

print("¿Prestamo1 == Prestamo2?", prestamo1)
print("Total personas:", Persona.total_personas)
print("Total prestamos:", Prestamo.total_prestamos)
