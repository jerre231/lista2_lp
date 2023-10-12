class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if len(self.bucho) > 0:
            alimento_digerido = self.bucho.pop(0)
            return f"{self.nome} digeriu {alimento_digerido}"
        else:
            return f"{self.nome} está com o estômago vazio."

macaco1 = Macaco("Mico")
macaco2 = Macaco("Gorila")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco2.comer("Insetos")

print(f"Estômago do {macaco1.nome}: {macaco1.verBucho()}")
print(f"Estômago do {macaco2.nome}: {macaco2.verBucho()}")

print(macaco1.digerir())
print(macaco2.digerir())

print(f"Estômago do {macaco1.nome}: {macaco1.verBucho()}")
print(f"Estômago do {macaco2.nome}: {macaco2.verBucho()}")
