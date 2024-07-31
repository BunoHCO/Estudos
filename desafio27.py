nome = str(input("Digite seu nome: ")).title().strip().split()
print("Muito prazer, seu primeiro nomo como vi é {}, e seu ultimo nome é {}".format(nome[0], nome[len(nome)-1]))