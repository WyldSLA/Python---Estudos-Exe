import random
import time
#Número sorteado que vai de 0 até 100
numero_sorteado = random.randint(0, 100)

print("="*20)
print("Joguinho de Sorteio!")
print("="*20)

print("Tente adivinhar o número que está entre 0 e 100! :D")

cont = 0
while True:
    jogada = int(input("Digite um número entre 0 e 100: "))
    cont += 1
    while jogada < 0 or jogada > 100:
        print("Erro! digite um número entre 0 e 100! >:(")
        jogada = int(input("Tente novamente: "))
    if jogada == numero_sorteado:
        time.sleep(0.5)
        print("Parabéns! Você acertou em {} tentativas!".format(cont))
        break
    else:
        if(jogada > numero_sorteado):
            time.sleep(0.5)
            print("Tenta chutar mais baixo...")
        elif(jogada < numero_sorteado):
            time.sleep(0.5)
            print("Tenta um chute mais alto...")