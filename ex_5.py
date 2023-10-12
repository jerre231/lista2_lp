class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def mostrarSaldo(self):
        return f"Conta: {self.numero_conta}, Correntista: {self.nome_correntista}, Saldo: R$ {self.saldo:.2f}"

conta = ContaCorrente("12345-6", "João da Silva")
print(conta.mostrarSaldo())
conta.deposito(1000)
print(conta.mostrarSaldo())
conta.saque(500)
print(conta.mostrarSaldo())
conta.alterarNome("Maria da Silva")
print(conta.mostrarSaldo())
