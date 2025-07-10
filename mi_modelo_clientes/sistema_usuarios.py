from mi_modelo_clientes.cliente import Cliente, ClientePremium
from mi_modelo_clientes.menu_cliente import menu_cliente
from mi_modelo_clientes.persistencia import guardar_datos, cargar_datos

usuarios, clientes = cargar_datos()
def registrar_usuario():
    while True:
        nombre_usuario = input("Nombre de usuario: ")
        if not nombre_usuario.strip():
            print("El nombre de usuario no puede estar vacío. Intenta de nuevo.")
            continue
        if nombre_usuario in usuarios:
            print("El usuario ya existe. Intenta con otro nombre.")
            continue

        # Validación de la contraseña
        contraseña = input("Contraseña (mínimo 6 caracteres): ")
        if len(contraseña) < 6:
            print("Error: La contraseña debe tener al menos 6 caracteres.")
            continue

        # Validación del apellido
        apellido = input("Apellido: ")
        if not apellido.strip():
            print("Error: El apellido no puede estar vacío.")
            return  # Salir al menú principal

        # Validación del email
        email = input("Email: ")
        if "@" not in email:
            print("Error: El email no es válido. Asegúrate de incluir '@'.")
            return  # Salir al menú principal

        #  try - catch con saldo
        try:
            saldo = float(input("Saldo inicial: "))
        except ValueError:
            print("Error: El saldo debe ser un número válido.")
            return  # Salir al menú principal

        # Tipo de cliente
        tipo = input("¿Cliente premium? (si/no): ").strip().lower()
        if tipo == "si":
            cliente = ClientePremium(apellido, email, saldo)
        else:
            cliente = Cliente(apellido, email, saldo)

        # Registrar el usuario
        usuarios[nombre_usuario] = contraseña
        clientes[nombre_usuario] = cliente

        print(f"Usuario {nombre_usuario} registrado con éxito.")
        guardar_datos(usuarios, clientes)
        break  # Salir del ciclo de registro => el usuario fue registrado correctamente

def login_usuario():
    # Permite a un usuario iniciar sesión. Verifica el nombre de usuario y la contraseña.
    nombre_usuario = input("Nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("El usuario no existe.")
        return

    contraseña = input("Contraseña: ")
    if usuarios[nombre_usuario] == contraseña:
        print(f"Bienvenido {nombre_usuario}!")
        menu_cliente(clientes[nombre_usuario])  # Muestra el menú del cliente
    else:
        print("Contraseña incorrecta.")

def mostrar_usuarios():
    # Muestra todos los usuarios registrados en el sistema.
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for u in usuarios:
            print(f"- {u}")

def eliminar_usuario():
    # Elimina un usuario del sistema si existe.
    nombre_usuario = input("Nombre de usuario a eliminar: ")
    if nombre_usuario in usuarios:
        del usuarios[nombre_usuario]  # Elimina el usuario de la lista de usuarios
        del clientes[nombre_usuario]  # Elimina el cliente asociado
        guardar_datos(usuarios, clientes)  # Guarda los datos actualizados
        print(f"Usuario {nombre_usuario} eliminado.")
    else:
        print("Usuario no encontrado.")