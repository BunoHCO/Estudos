from datetime import date

ano = int(input("Qual ano analisar? Coloque 0 para verificar o ano atual!"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O Ano é Bisexto!")
else:
    print("O Ano não é Bisexto!")
