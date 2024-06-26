#### FUNCIONES
def menu_principal():
    print("1) Registrar pedido.")
    print("2) Listar todos los pedidos.")
    print("3) Imprimir hoja de ruta.")
    print("4) Salir del programa.")

def registrar_pedido():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    direccion = input("Ingrese direccion: ")
    comuna = input("Ingrese comuna: ")
    c5 = input("Ingrese cantidad de cilindros de 5 Kg: ")
    c15 = input("Ingrese cantidad de cilindros de 15 Kg: ")
    c45 = input("Ingrese cantidad de cilindros de 45 Kg: ")
    l = [nombre, apellido, direccion, comuna, c5, c15, c45]
    L_pedidos.append(l)

def listar_pedidos():
    for i in L_pedidos:
        print(i)

def imprimir_hoja(comuna):
    l = []  #### Es la lista que guardara los pedidos de la comuna solicitada
    for pedido in L_pedidos:  # pedido = [nombre, apellido, direccion, comuna, 5kg, 15kg, 45kg]
        if pedido[3] == comuna:
            l.append(pedido)
    #### Escribir archivo
    arch = open("Hoja de ruta_" + comuna + ".txt", "w")
    for pedido in l:
        s = "--".join(pedido)
        arch.write(s + "\n")
    arch.close()
    print("Archivo creado con exito.")

##### MAIN
L_pedidos = []  # [[], [], [], [] ...]
while True:
    menu_principal()
    op = input("Ingrese opcion: ")
    if op == "4":
        print("Saliendo del programa...")
        break
    elif op == "1":
        print("Ingresando a opcion 1")
        registrar_pedido()  ### llamamos  a la funcion
    elif op == "2":
        print("Ingresando a opcion 2")
        listar_pedidos()   ### llamamos  a la funcion
    elif op == "3":
        print("Ingresando a opcion 3")
        comuna = input("Ingrese comuna: ")
        imprimir_hoja(comuna)
    else: 
        print("Ingrese una opcion valida.")