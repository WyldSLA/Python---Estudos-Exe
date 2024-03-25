import random
import time
import operator
jogadores = {}
ranking = {}
jogadores["jogador1"] = random.randint(1, 6)
jogadores["jogador2"] = random.randint(1, 6)
jogadores["jogador3"] = random.randint(1, 6)
jogadores["jogador4"] = random.randint(1, 6)
print("Valores Sorteados:")
for k, v in jogadores.items():
    time.sleep(0.8)
    print(f"    O {k} tirou {v}.")
print("Ranking dos jogadores:")

ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

for i, j in enumerate(ranking):
    print(f"    {i + 1}ª lugar: {j[0]} que tirou {j[1]}.")