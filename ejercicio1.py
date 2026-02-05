#Tienda TechStore

class producto():
    def __init__(self,nombre,precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock
        
    def aplicar_descuento(self,porcentaje):
        self.precio_base *-(-porcentaje)
        print(f"el nuevo precio es {self.precio_base}")
        
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0 :
            print("no hay stock negativo")
        else:
            self.stock +=cantidad
            print(f"la nueva cantidad es{self.stock}")
            
class categoria():
    def __init__(self,nombre_categoria,lista_productos):
        self.nombre_categoria=nombre_categoria
        self.lista=[]
        
    def agregar_productos(self,producto):
        self.lista.append(producto)
        print(f"el producto {producto} se agrego a la lista")
        
    def valor_total_categoria(self):
        pass