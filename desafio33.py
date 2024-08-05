a = int(input("Digite o Primeiro Numero: "))
b = int(input("Digite o Segundo Numero: "))
c = int(input("Digite o Terceiro Numero: "))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O menor valor digitado foi {}".format(menor))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O Maior valor digitado foi {}".format(maior))