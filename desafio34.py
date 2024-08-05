salario = float(input("Digite o Salario atual do funcionario: "))

if salario >= 1250.00:
    por = salario + (salario * 10 / 100)
    
else:
    por = salario + (salario * 15/100)
print("O Salario de {:.2f} passa a ser {}".format(salario ,por))