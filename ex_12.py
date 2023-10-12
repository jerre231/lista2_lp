class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxa_juros


poupanca = ContaInvestimento(1000.0, 10.0)

for _ in range(5):
    poupanca.adicioneJuros()

saldo_final = poupanca.saldo
print(f"Saldo após 5 vezes a aplicação de juros: R$ {saldo_final:.2f}")
