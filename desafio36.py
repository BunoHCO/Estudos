valor_casa = float(input("Qual Valor da Casa?: "))
salario = float(input("Qual Salario?: "))
qnt_anos = int(input("Quantos anos?: "))

prestacoes = valor_casa / (qnt_anos * 12)
valor_empre = salario * 30 / 100

print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}".format(valor_casa, qnt_anos,prestacoes))

if prestacoes <= valor_empre:
    print("Empresitmo Aprovador!!")
else:
    print("Empréstimo Negado!!!")