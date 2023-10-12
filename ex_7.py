class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor

meu_bichinho = BichinhoVirtual("Tom", 5, 10, 2)
print(f"Nome: {meu_bichinho.retornarNome()}")
print(f"Fome: {meu_bichinho.retornarFome()}")
print(f"Saúde: {meu_bichinho.retornarSaude()}")
print(f"Idade: {meu_bichinho.retornarIdade()}")
print(f"Humor: {meu_bichinho.retornarHumor()}")
