salarioi=float(input("Qual o Valor atual do Salario do funcionaro: "))
aumento = int(input("Digite a porcentagem do aumento do salario: "))

salariof = salarioi + (salarioi * aumento / 100)

print("O Salario atual é de {}, com o aumento de {} é equivalente a {:.2f}".format(salarioi, aumento, salariof))