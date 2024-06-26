def menu_principal():
    print("1) Registrar pedido.")
    print("2) Listar todos los pedidos.")
    print("3) Imprimir hoja de ruta.")
    print("4) Salir dle programa.")

while True:
    menu_principal()
    op = input("Ingrese opcion: ")
    if op == "4":
        print("Saliendo del programa...")
        break
    elif op == "1":
        print("Ingresando a opcion 1")
    elif op == "2":
        print("Ingresando a opcion 2")
    elif op == "3":
        print("Ingresando a opcion 3")
    else: 
        print("Ingrese una opcion valida.")