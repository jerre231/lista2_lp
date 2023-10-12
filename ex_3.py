class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarLados(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def retornarLados(self):
        return self.comprimento, self.largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)


comprimento_local = float(input("Informe o comprimento do local em metros: "))
largura_local = float(input("Informe a largura do local em metros: "))

local = Retangulo(comprimento_local, largura_local)

area_local = local.calcularArea()
perimetro_local = local.calcularPerimetro()


quantidade_pisos = area_local
quantidade_rodapes = (2 * (comprimento_local + largura_local)) * 0.1

print(f"Para cobrir o local, você precisará de {quantidade_pisos:.2f} pisos e {quantidade_rodapes:.2f} rodapés.")
