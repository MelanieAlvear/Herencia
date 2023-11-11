from cuentaAhorro import CuentaAhorro
from cuentaCorriente import CuentaCorriente


class Test(CuentaAhorro, CuentaCorriente):
    def __init__(self, numero, nombre_propietario, saldo, interes, tieneChequera):
        CuentaAhorro.__init__(self, numero, nombre_propietario, saldo, interes)
        CuentaCorriente.__init__(self, numero, nombre_propietario, saldo, tieneChequera)


# Ejemplo
cuenta_pr = Test('4563897', 'Zach Hardway', 7432.94, 6.0, True)

# Acceder a propiedades y métodos de ambas clases base
print("Saldo de la cuenta de ahorros:")
print(cuenta_pr.saldo)
print("Tiene chequera en la cuenta corriente:")
print(cuenta_pr.tieneChequera)

# Realizar transacciones
cuenta_pr.credito(217.0)
cuenta_pr.debito(230.0)
cuenta_pr.pagar_cheque(150.0)

# Mostrar saldos después de las transacciones
print("Saldo después de las transacciones:")
print(cuenta_pr.saldo)

#Melanie Alvear Ortiz.