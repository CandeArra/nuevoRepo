from mi_modelo_clientes import registrar_usuario, login_usuario, mostrar_usuarios, eliminar_usuario

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver usuarios registrados")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            registrar_usuario()  # registra un nuevo usuario
        elif opcion == "2":
            login_usuario()  # inicia sesión
        elif opcion == "3":
            mostrar_usuarios()  # muestra usuarios registrados
        elif opcion == "4":
            eliminar_usuario()  # elimina un usuario
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break  # sale del programa
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()