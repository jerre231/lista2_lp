class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira

    def humor(self):
        return (self.fome + self.tedio) / 2

# Programa principal
nome_bichinho = input("Dê um nome ao seu bichinho virtual: ")
bichinho = BichinhoVirtual(nome_bichinho)

while True:
    print(f"{bichinho.nome}: Fome: {bichinho.fome}, Tédio: {bichinho.tedio}, Humor: {bichinho.humor():.2f}")
    
    comida = int(input("Quantidade de comida a fornecer (0 para sair): "))
    if comida == 0:
        break
    bichinho.alimentar(comida)
    
    brincadeira = int(input("Tempo de brincadeira (0 para sair): "))
    if brincadeira == 0:
        break
    bichinho.brincar(brincadeira)
