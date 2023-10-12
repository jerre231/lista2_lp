class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado * self.lado

meu_quadrado = Quadrado(5)
print("Tamanho do lado do quadrado: ", meu_quadrado.retornarLado())
meu_quadrado.mudarLado(7)
print("Novo tamanho do lado do quadrado: ", meu_quadrado.retornarLado())
print("Área do quadrado: ", meu_quadrado.calcularArea())
