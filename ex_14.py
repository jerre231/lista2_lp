class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, percentual_de_aumento):
        aumento = self.salario * (percentual_de_aumento / 100)
        self.salario += aumento

# Exemplo de uso:
harry = Funcionario("Harry", 25000)
print(f"Salário inicial de {harry.obterNome()}: R$ {harry.obterSalario():.2f}")

harry.aumentarSalario(10)  # Aumento de 10%
print(f"Novo salário de {harry.obterNome()}: R$ {harry.obterSalario():.2f}")
