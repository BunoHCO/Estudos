vel = int(input("Qual velocidade atual do carro? "))

if vel <= 80:
    print("Ok, dirija com segurança!!")
else:
    print("Voce ultrapassou o limite de velocidade!!")
    multa = (vel - 80) * 7
    print("Sua multa é de R${:.2f}".format(float(multa)))