larg=float(input("Qual a largura da parede: "))
alt=float(input("Qual altura da parede: "))

a = larg * alt
b= a / 2

print("Sua parede tem uma dimensão de {}x{} e sua area é {}m²".format(larg, alt, a))
print("Para pintar sua parede sera necessário {}L de tinta".format(b))