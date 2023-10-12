class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar_desligar(self):
        self.ligada = not self.ligada

    def alterar_canal(self, novo_canal):
        if self.ligada and 1 <= novo_canal <= 100:
            self.canal = novo_canal

    def aumentar_volume(self):
        if self.ligada and self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 1

    def mostrar_status(self):
        status = "ligada" if self.ligada else "desligada"
        return f"TV está {status}, Canal: {self.canal}, Volume: {self.volume}"

minha_tv = TV()

while True:
    print(minha_tv.mostrar_status())
    opcao = input("Opções: Ligar/Desligar (L/D), Mudar Canal (C), Aumentar Volume (+), Diminuir Volume (-), Sair (S): ").upper()

    if opcao == "L":
        minha_tv.ligar_desligar()
    elif opcao == "D":
        minha_tv.ligar_desligar()
    elif opcao == "C":
        novo_canal = int(input("Informe o número do canal desejado: "))
        minha_tv.alterar_canal(novo_canal)
    elif opcao == "+":
        minha_tv.aumentar_volume()
    elif opcao == "-":
        minha_tv.diminuir_volume()
    elif opcao == "S":
        break
    else:
        print("Opção inválida. Tente novamente.")
