from mi_modelo_clientes.cliente import Cliente, ClientePremium 
import json

ARCHIVO_USUARIOS = "usuarios.json"  # archivo donde se guardan los datos de usuarios y clientes

def guardar_datos(usuarios, clientes):
    data = {}
    for usuario in usuarios:
        cliente = clientes[usuario]
        data[usuario] = {
            "password": usuarios[usuario], 
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "email": cliente.email,
            "saldo": cliente.saldo,
            "tipo": "premium" if isinstance(cliente, ClientePremium) else "normal"  # se guarda si es premium o normal
        }
    
    with open(ARCHIVO_USUARIOS, "w") as f:  
        json.dump(data, f)
    print("datos guardados correctamente.")

def cargar_datos():
    usuarios = {}
    clientes = {}
    try:
        with open(ARCHIVO_USUARIOS, "r") as f:  
            data = json.load(f)
            for usuario, info in data.items():
                usuarios[usuario] = info["password"]  # asignamos la contraseña
                if info.get("tipo") == "premium":  # si es premium, instanciamos ClientePremium
                    cliente = ClientePremium(info["nombre"], info["apellido"], info["email"], info["saldo"])
                else:
                    cliente = Cliente(info["nombre"], info["apellido"], info["email"], info["saldo"])  # si no, Cliente normal
                clientes[usuario] = cliente
    except FileNotFoundError:
        print("no hay datos guardados previamente. puedes registrar un usuario.")  # si no existe el archivo
    return usuarios, clientes

