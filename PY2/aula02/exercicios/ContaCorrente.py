from Conta import Conta
class ContaCorrente(Conta):
    def sacar(self, saque):
        return super().sacar(saque)

    def verSaldo(self):
        return super().verSaldo()

    def depositar(self, deposito):
       
        self.saldo += deposito
        return 'Saldo atual: R$' + str(self.saldo)

    def tranferir(self, contas, contaDestino, valor):      
        for x in range(len(contas)):
            if contas[x] == contaDestino:                    
                if self.saldo > valor:
                    return 'Saldo insulficiente! Saldo: R$' + self.saldo
                self.saldo -= valor
                contaDestino.saldo += valor
                return 'Transferência realizada com sucesso! '

