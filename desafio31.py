km = int(input("Digite a distancia da viagem em KM: "))

if km <= 200:
    preço = km * 0.5
    print("O preço que dará por uma viagem de {}KM será RS${:.2f}!".format(km, preço))
else:
    preço = km * 0.45
    print("O preço que dara por uma viagem de {}KM será R${:.2f}".format(km ,preço))
