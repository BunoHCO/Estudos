num=int(input("Digite um Numero: "))
contador = 1

print("=======")

for i in range (10):
    soma = num * contador
    print("{} x {:2} = {}".format(num, contador, soma))
    contador = contador +1
print("=======")    