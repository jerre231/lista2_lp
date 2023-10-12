class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        if self.quantidade_combustivel == 0:
            print("A bomba está vazia. Não é possível abastecer.")
            return

        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecer_por_litro(self, litros):
        if self.quantidade_combustivel == 0:
            print("A bomba está vazia. Não é possível abastecer.")
            return

        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

    def mostrar_status(self):
        print(f"Tipo de Combustível: {self.tipo_combustivel}")
        print(f"Valor por Litro: R$ {self.valor_litro:.2f}")
        print(f"Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros")

bomba = BombaCombustivel("Gasolina", 5.0, 1000)

bomba.mostrar_status()

bomba.abastecer_por_valor(50)
bomba.abastecer_por_litro(20)

bomba.alterar_valor(5.5)
bomba.alterar_combustivel("Álcool")

bomba.mostrar_status()
