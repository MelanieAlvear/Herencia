from cuenta import cuenta


class CuentaCorriente(cuenta):
    def __init__(self, numero, nombre_propietario, saldo, tieneChequera: bool = None):
        super().__init__(numero, nombre_propietario, saldo)
        self._tieneChequera = tieneChequera

    @property
    def tieneChequera(self):
        return self._tieneChequera

    @tieneChequera.setter
    def tieneChequera(self, tiene_chequera):
        self._tieneChequera = tiene_chequera

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta corriente {self.numero}: ${self.saldo}")

    def pagar_cheque(self, cantidad):
        if self.tieneChequera:
            self.debito(cantidad)
            print(f"Se pagó un cheque por ${cantidad}")
        else:
            print("Esta cuenta corriente no tiene chequera")


cuenta_pr = CuentaCorriente('278965', 'Raffaele Ferrara', 7869.00, True)
cuenta_pr.credito(649.00)
cuenta_pr.debito(564.00)
cuenta_pr.mostrar_saldo()
cuenta_pr.pagar_cheque(500.00)
cuenta_pr.mostrar_saldo()

#Melanie Alvear Ortiz.
