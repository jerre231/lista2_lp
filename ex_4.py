class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def mostrarInformacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura} cm"

pessoa = Pessoa("Maria", 18, 60, 160)
print(pessoa.mostrarInformacoes())
pessoa.envelhecer(3)
pessoa.engordar(5)
pessoa.emagrecer(2)
print(pessoa.mostrarInformacoes())
