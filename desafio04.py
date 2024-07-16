algo = input("Digite algo: ")

print("O tipo primitivo desse valor é" , type(algo))#type retorna o tipo de dado de uma variavél
print("Só tem espaço?", algo.isspace())#.isspace retorna se a variavél é composta de espaços
print("É um numero?", algo.isnumeric())#.isnumeric retorna se é um numero
print("É alfabético?", algo.isalpha())#.isalpha retorna se é alfabético (comsposto apenas por letras)
print("É alfanumérico?", algo.isalnum())#.isalnum retorna se é alfanumérico (composto por numeros e letras)
print("Esta em maiúsculo?", algo.isupper())#.isupper retorna se esta em maiúsculo
print("Esta em minúscula?", algo.islower())#islower retorna se é minúscila
print("Esta capitalizada(Com maiusculas e minusculas)?", algo.istitle())