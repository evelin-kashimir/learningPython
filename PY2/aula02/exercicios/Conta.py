class Conta():
    def __init__(self, dono, numero):  
        self.dono = dono 
        self.numero = numero 
        self.saldo = 0
    
    def verSaldo(self):
        return 'Saldo atual: ' + str(self.saldo)

    def sacar(self, saque):
        if saque > self.saldo:
            return 'Saldo insulficiente.' 
        self.saldo -= saque
        return 'Saldo atual: R$' + str(self.saldo)
        
        