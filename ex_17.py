import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(1, 100)
        self.tedio = random.randint(1, 100)

    def alimentar(self):
        self.fome -= 10

    def brincar(self):
        self.tedio -= 20

    def humor(self):
        return (self.fome + self.tedio) / 2

    def __str__(self):
        return f"{self.nome}: Fome: {self.fome}, Tédio: {self.tedio}"

# Criar uma fazenda de bichinhos
fazenda = [BichinhoVirtual("Bichinho1"), BichinhoVirtual("Bichinho2"), BichinhoVirtual("Bichinho3")]

while True:
    print("Ações disponíveis:")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")

    escolha = input("Escolha uma ação: ")

    if escolha == "1":
        for bichinho in fazenda:
            bichinho.alimentar()
    elif escolha == "2":
        for bichinho in fazenda:
            bichinho.brincar()
    elif escolha == "3":
        for bichinho in fazenda:
            print(bichinho)
    elif escolha == "4":
        break
    else:
        print("Escolha inválida. Tente novamente.")
