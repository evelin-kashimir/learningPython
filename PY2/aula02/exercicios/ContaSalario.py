from Conta import Conta
class ContaSalario(Conta):
    def sacar(self, saque):
        return super().sacar(saque)

    def verSaldo(self):
        return super().verSaldo()