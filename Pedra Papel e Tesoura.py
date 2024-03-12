import random
import time

jogadas = ["Pedra", "Papel", "Tesoura"]
print("-="*20)
print("Pedra, Papel & Tesoura!!")
print("-="*20)
contPC = 0
contJog = 0
while True:
    pc = random.randint(0,2)
    print("[0] Pedra [1] Papel [2] Tesoura")

    usuario_jogada = int(input("Digite seu jogada: "))
    while usuario_jogada < 0 or usuario_jogada > 2:
        print("Erro! Digite entre 0 e 2!")
        usuario_jogada = int(input("Digite seu jogada: "))
    print("JO")
    time.sleep(0.8)
    print("KEN")
    time.sleep(0.8)
    print("PO!!!")

    print("-="* 20)
    print(f"O usuário jogou {jogadas[usuario_jogada]}.")
    print(f"O computador jogou {jogadas[pc]}.")
    print("-="*20)

    if usuario_jogada == 0:
        if pc == 1:
            print("O computador ganhou!")
            contPC += 1
        elif pc == 2:
            print("O usuário ganhou!")
            contJog+= 1
    elif usuario_jogada == 1:
        if pc == 0:
            print("O usuário ganhou!")
            contJog+= 1
        elif pc == 2:
            print("O computador ganhou!")
            contPC+=1
    elif usuario_jogada == 2:
        if pc == 0:
            print("O computador ganhou!")
            contPC+=1
        elif pc == 1:
            print("O usuário ganhou!")
            contJog+=1
    if usuario_jogada == pc:
        print("Empate!")

    resp = str(input("Mais uma vez?[S]/[N]")).upper().strip()
    if resp == "N":
        break

print("-="*20)
print("Placar Final!!")
print("O usuário ganhou {} veze(s).".format(contJog))
print("O computador ganhou {} veze(s).".format(contPC))