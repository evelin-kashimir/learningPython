from Conta import Conta
class ContaPoupanca(Conta):
    
    def sacar(self, saque):
        return super().sacar(saque)

    def verSaldo(self):
        return super().verSaldo()

    def depositar(self, deposito):
        deposito = int(input('Valor do depósito: R$'))
        self.saldo += deposito
        return 'Saldo atual: R$' + self.saldo