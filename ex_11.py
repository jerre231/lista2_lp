class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def adicionarGasolina(self, litros):
        self.combustivel += litros

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario

    def obterGasolina(self):
        return self.combustivel

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print(f"Combustível restante: {meuFusca.obterGasolina()} litros.")
