from csv import *

ruta_almacen = "Almacen/inventario.csv"

campos = ["producto", "precio"]
datos = [
    {
        "producto": "Papas",
        "precio": 2500
    },
    {
        "producto": "Gaseosa",
        "precio": 3000
    },
    {
        "producto": "Galletas",
        "precio": 2200
    },
    {
        "producto": "Jugo",
        "precio": 2800
    }
]

carrito = []


# Inicializamos los datos base de la tienda
with open(ruta_almacen, "w") as almacen:
    escritor = DictWriter(almacen, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos) 

# Creamos funcion para listar los productos disponibles
def listar_productos():
    with open(ruta_almacen) as almacen:
        lector = list(DictReader(almacen))
        
        print()
        print("- - - Listado de productos - - -")
        for producto in lector:
            nombre = producto["producto"]
            precio = producto["precio"]
            
            print(f"Producto '{nombre}' tiene precio de ${precio}")

# Agregar nuevo producto al carrito si existe
def agregar_al_carrito(nombre_producto, cantidad):
    with open(ruta_almacen) as almacen:
        nombre_producto = str(nombre_producto).capitalize()
        existe_producto = False
        producto_viejo = False
        lector = list(DictReader(almacen))
        
        if cantidad <= 0:
            print("ERROR ---> Cantidad no valida")
            return
        
        for producto in lector:
            if nombre_producto == producto["producto"]:
                for index in range(len(carrito)):
                    if nombre_producto in carrito[index]:
                        carrito[index][1] = carrito[index][1] + cantidad
                        producto_viejo = True
                existe_producto = True 
            
        if not producto_viejo:
            carrito.append([nombre_producto, cantidad])
        if existe_producto:
            print()
            print("Se agrego al carrito!!!")
        else:
            print()
            print("ERROR ---> (El producto ingresado NO existe en el almacen)")
            
# Calcular total del carrito
def calcular_total_carrito():
    valor_a_pagar = 0
    
    if carrito == []:
        print("ERROR ---> El carrito esta vacio")
        return 0
    
    with open(ruta_almacen) as almacen:
        lector = list(DictReader(almacen))
        
        for producto_carrito in carrito:
            for producto in lector:
                
                if producto_carrito[0] == producto["producto"]:
                    valor_a_pagar += (int(producto["precio"]) * producto_carrito[1])
                    break
    return valor_a_pagar

# Ver carrito
def ver_carrito():
    print()
    print("- - - Productos en el carrito - - -")

    for producto_carrito in carrito:
        print(f"Producto:'{producto_carrito[0]} --> Cantidad: {producto_carrito[1]}'.")
    
    print(f"Total: ${calcular_total_carrito()}")

def pagar():
    
    print()
    print("- - - Factura - - -")
    ver_carrito()
    terminar_programa = False
    confirmacion = 0

    while True:
        try:
            confirmacion = int(input("Quieres completar la compra? 1. Si 2.No "))
        
        except ValueError:
            print("ERROR ---> Ingresaste un dato invalido")
        else:
            match confirmacion:
                case 1:
                    print()
                    print("Pago realizado!!! Muchas gracias")
                    terminar_programa = True
                    break
                case 2:
                    print()
                    print("Okey, decidiste volver a revisarlo")
                    break
                case _:
                    print("ERROR ---> Opcion no permitida, reintenta")
    return terminar_programa