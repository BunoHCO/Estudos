from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)

print("A Hipotenusa vai medir {:.2f}".format(hi))