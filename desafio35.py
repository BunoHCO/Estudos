print("Analisando Triangulos")

a = float(input("Primeiro Segmento: "))
b = float(input("Segundo Segmento: "))
c = float(input("Terceiro Segmento: "))

if a < b+c and b < a+c and c < a+b:
    print("Os Segmentos acima podem formar um triangulo!")
else:
    print("Esses segmentos não formam um triangulo")
