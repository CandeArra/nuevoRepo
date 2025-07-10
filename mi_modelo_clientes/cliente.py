class Cliente:
    # clase que representa a un cliente con un saldo y métodos para agregar fondos y realizar compras.
    
    def __init__(self, nombre, apellido, email, saldo=0.0):
        self.nombre = nombre  # Nombre del cliente
        self.apellido = apellido  # Apellido del cliente
        self.email = email  # Email del cliente
        self.saldo = saldo  # Saldo inicial del cliente

    def __str__(self):
        # Devuelve el nombre completo del cliente
        return f"{self.nombre} {self.apellido}"

    def agregar_fondos(self, monto):
        # Agrega fondos al saldo del cliente si el monto es positivo
        if monto <= 0:
            print("Error: El monto debe ser mayor a cero.")
        else:
            self.saldo += monto
            print(f"Se agregaron ${monto:.2f} a la cuenta de {self.nombre}.")

    def realizar_compra(self, monto):
        # Realiza una compra si el saldo es suficiente y el monto es positivo
        if monto <= 0:
            print("Error: El monto de la compra debe ser mayor a cero.")
        elif monto > self.saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"Compra realizada por ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")


class ClientePremium(Cliente):
    # clase hija de Cliente que aplica un descuento en las compras y ofrece características exclusivas para clientes premium.
    
    def __init__(self, nombre, apellido, email, saldo=0.0, limite_credito=1000.0):
        super().__init__(nombre, apellido, email, saldo)  # Inicializa los atributos heredados de la clase Cliente
        self.limite_credito = limite_credito  # Atributo exclusivo de los clientes premium, define el crédito adicional disponible.

    def realizar_compra(self, monto):
        # Realiza una compra con un descuento del 10%.
        # Si el saldo no es suficiente, utiliza el crédito disponible.
        descuento = 0.10  # Descuento del 10% para clientes premium
        total = monto * (1 - descuento)  # Se calcula el total con el descuento aplicado
        
        if total <= self.saldo:
            # Si el saldo es suficiente, se realiza la compra y se actualiza el saldo
            self.saldo -= total
            print(f"Compra (con 10% de descuento): ${total:.2f}. Saldo actual: ${self.saldo:.2f}")
        elif total <= self.saldo + self.limite_credito:
            # Si el saldo no es suficiente, pero hay crédito disponible, se realiza la compra a crédito
            credito_restante = (self.saldo + self.limite_credito) - total
            print(f"Compra a crédito (con descuento): ${total:.2f}. Saldo actual: ${credito_restante:.2f}")
            self.saldo = credito_restante  # Se actualiza el saldo con el crédito utilizado
        else:
            # Si el saldo y el crédito juntos no cubren el monto, la compra no puede realizarse
            print("Fondos insuficientes (incluso con descuento y crédito).")

    def __str__(self):
        # Devuelve el nombre completo del cliente premium con la etiqueta "(Premium)"
        return f"{self.nombre} {self.apellido} (Premium)"