import os

SALIDA = "Q"
ARCHIVO_LISTA ="lista_compra.txt"


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]: ".format(SALIDA))
       

def crear_archivo(lista_compra):
    
    #pasar_texto= open(name+".txt", "w") # w es modo escritura (w = write)
    #pasar_texto.write("\n".join(lista_compra))
    #pasar_texto.close()

    with open(ARCHIVO_LISTA,"w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

    #NO ocupo poner .close() pues mi fichero al estar ententado 4 a dentro al salir de esto me dice que ya no estoy trabajando dentro del archivo avierto

    print("Se ha guardado el archivo {} con exito!!!".format(ARCHIVO_LISTA))


def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:# Esto es un for super comprmido y sirve para filtrar es decir:
                                                         # segunda_lista =[]
                                                         #  for a in lista_compra:
                                                         #      segunda_lista.append(a.lower())


        print("EL PRODUCTO YA EXISTE")
    else:
        os.system("cls")
        lista_compra.append(item_a_guardar)


def cargar_o_crear_lista():
    lista_compra = []
    if input("¿Quieres cargar la ultima lista de la compra? [S/N]") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n") #Rompe el contenido por enters y asi recuperamos el contenido de una lista vieja
        except FileNotFoundError:
            print("\n¡Archivo de la compra no encontrado!\n")
    return lista_compra


def mostrar_lista(lista_compra):
    print ("\n".join(lista_compra))


def main():
    lista_compra = cargar_o_crear_lista()
    input_usuario= preguntar_producto_usuario() 
    
    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra,input_usuario)
        input_usuario= preguntar_producto_usuario()

    mostrar_lista(lista_compra)
    crear_archivo(lista_compra)


if __name__ == "__main__":
    main()
