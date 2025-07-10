def menu_cliente(cliente):
    # Muestra el menú principal del cliente donde puede realizar acciones sobre su cuenta.
    while True:
        print(f"\n--- Menú de {cliente.nombre} ---")
        print("1. Ver perfil")  # Opción para ver el perfil del cliente
        print("2. Agregar fondos")  # Opción para agregar fondos al saldo del cliente
        print("3. Realizar compra")  # Opción para realizar una compra
        print("4. Ver saldo")  # Opción para ver el saldo actual del cliente
        print("5. Cerrar sesión")  # Opción para cerrar sesión

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Muestra los datos del cliente
            print(f"Nombre: {cliente.nombre}")
            print(f"Apellido: {cliente.apellido}")
            print(f"Email: {cliente.email}")
            print(f"Saldo: ${cliente.saldo:.2f}")
        elif opcion == "2":
            # Permite al cliente agregar fondos a su saldo
            monto = float(input("Monto a agregar: "))
            cliente.agregar_fondos(monto)
        elif opcion == "3":
            # Permite al cliente realizar una compra
            monto = float(input("Monto de la compra: "))
            cliente.realizar_compra(monto)
        elif opcion == "4":
            # Muestra el saldo actual del cliente
            print(f"Saldo actual: ${cliente.saldo:.2f}")
        elif opcion == "5":
            # Cierra la sesión del cliente
            print("Sesión cerrada.")
            break
        else:
            # Si la opción es inválida
            print("Opción no válida.")