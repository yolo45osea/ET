


def valOpcion():
    while(True):
        try:
            op=int(input("ingrese una opcion"))
            if(op<1 or op>5):
                print("ingrese una opcion valida")
            else:
                break
        except ValueError:
            print("error, dato no valido")
    return op

edificio=[]
def crearEdificio():
    for piso in range(10, 0, -1):
        pasillo = []
        for fila in range(4):
            suelo = ''
            pasillo.append(suelo)
        edificio.append(pasillo)
    print(edificio)


def mostrar():
    pisos=10
    for i in range(10):
        for j in range(4):
            print(edificio)


def menu():
    print("""
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir
    """)


def main():
    crearEdificio()


    while True:
        menu()
        op=valOpcion()


        if op ==2:
            mostrar()

        if op==5:
            print("gracias por comprar en ""casa feliz"" Benjamín Romero, 11/7/2023",)
            break

main()