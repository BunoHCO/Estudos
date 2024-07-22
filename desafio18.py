import math

num = int(input("Digite um angulo: "))

sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tang = math.tan(math.radians(num))  

print("O Angulo de {}° tem o SENO de {:.2f}".format(num, sen))
print("O Angulo de {}° tem o COSENO de {:.2f}".format(num, cos))
print("A Angulo de {}° tem a TANGENTE de {:.2f}".format(num, tang))