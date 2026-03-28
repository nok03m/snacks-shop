from tienda_snacks import *

print()
print("--- Bienvenido a la tienda de SNACKS ---")

while True:
    # Menu
    print()
    print("- Menu -")
    print("Opciones:")
    print("6. Ver productos disponibles")
    print("7. Agregar producto al carrito")
    print("8. Ver carrito de compras")
    print("9. Pagar y salir")
    print("0. Salir")
    
    try:
        opcion = int(input("Ingresa tu seleccion: "))
        
        match opcion:
            case 6:
                listar_productos()
            case 7:
                listar_productos()
                try:
                    seleccion = input("Ingresa tu producto: ").capitalize()
                    cantidad = int(input("Ingresa la cantidad: "))
                    agregar_al_carrito(seleccion, cantidad)
                except ValueError:
                    print("ERROR ---> Cantidad erronea")
            case 8:
                ver_carrito()
            case 9:
                salir = pagar()
                if salir:
                    break
            case 0:
                    break
            case _:
                print("ERROR ---> Numero invalido, REINTENTA")
                print()
    except ValueError:
        print("ERROR ---> Tipo de dato no valido, REINTENTA")
        continue