produto = float(input("Qual o preço do produto: "))

desc = produto - (produto * 5 / 100)

print("O Produto esta no valor de {}, com 5% de desconto vai custar {:.2f}".format(produto, desc))