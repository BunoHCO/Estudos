from random import randint
from time import sleep

print("Vou pensar em um numero entre 0 e 5. Tente adivinhar qual é...")

pc = randint(0,5)
buno = int(input("Tenta a sorte: "))
print("Processando...")
sleep(2)

if pc == buno:
    print("Carai voce acertou!!")
else:
    print("EROOOOU! O numero que eu escolhi foi {}".format(pc))