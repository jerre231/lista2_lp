class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

# Programa de teste
funcionario1 = Funcionario("João", 3000.0)
funcionario2 = Funcionario("Maria", 3500.0)

print(f"Nome do funcionário 1: {funcionario1.obterNome()}")
print(f"Salário do funcionário 1: R$ {funcionario1.obterSalario():.2f}")

print(f"Nome do funcionário 2: {funcionario2.obterNome()}")
print(f"Salário do funcionário 2: R$ {funcionario2.obterSalario():.2f}")
