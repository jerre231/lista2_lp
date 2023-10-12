class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def main():
    ponto = Ponto(0, 0)
    retangulo = Retangulo(ponto, 5, 3)

    while True:
        print("\nMenu:")
        print("1. Alterar valores do retângulo")
        print("2. Encontrar o centro do retângulo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            novo_x = float(input("Digite o novo valor de x: "))
            novo_y = float(input("Digite o novo valor de y: "))
            nova_largura = float(input("Digite a nova largura: "))
            nova_altura = float(input("Digite a nova altura: "))
            ponto = Ponto(novo_x, novo_y)
            retangulo = Retangulo(ponto, nova_largura, nova_altura)
            print("Valores do retângulo atualizados.")

        elif escolha == "2":
            centro = retangulo.encontrar_centro()
            print("Centro do retângulo:")
            centro.imprimir()

        elif escolha == "3":
            break

if __name__ == "__main":
    main()
