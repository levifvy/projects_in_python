'''Ejercicio 7

Enunciado: clase CuentaBancaria

Se requiere un programa que modele una cuenta bancaria que posee los siguientes atributos:

Nombres del titular.
Apellidos del titular.
Número de la cuenta bancaria.
Tipo de cuenta: puede ser una cuenta de ahorros o una cuenta corriente.
Saldo de la cuenta.
Se debe definir un constructor que inicialice los atributos de la clase. Cuando se crea una cuenta bancaria, su saldo inicial tiene un valor de cero.

En una determinada cuenta bancaria se puede:

Imprimir por pantalla los valores de los atributos de una cuenta bancaria.
Consultar el saldo de una cuenta bancaria.
Consignar un determinado valor en la cuenta bancaria, actualizando el saldo correspondiente.
Retirar un determinado valor de la cuenta bancaria, actualizando el saldo correspondiente. Es necesario tener en cuenta que no se puede realizar el retiro si el valor solicitado supera el saldo actual de la cuenta.'''

class CuentaBancaria:
    def __init__(self, nombre, apellido, numero_cuenta, tipo_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0

    def imprimir_datos(self):
        print(f"Titular: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nTipo de cuenta: {self.tipo_cuenta}\nSaldo: {self.saldo}")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad


cuenta = CuentaBancaria("Juan", "Perez", "123456", "Ahorros")
cuenta.consignar(500)
cuenta.imprimir_datos()
cuenta.retirar(200)
print("Saldo actual:", cuenta.consultar_saldo())
