aluguel=int(input("Quantos dias alugado: "))
km = float(input("Quantos KM rodados: "))
dia = aluguel * 60
kmrodados = km * 0.15

a = dia + kmrodados

print("O Total a pagar pelos dias utilizados é de R${:.2f}".format(a))