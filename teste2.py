frase = "Manipulando textos"
print(frase[3])#pega o terceiro caracter da frase
print(frase[3:13])#pega do terceiro até o décimo segundo caracter da frase
print(frase[1:13:2])#pega do caracter de indice 1 até o décimo segundo pulano 2 letras
print(frase[::2])#pula e mostra a cada 2 letras do começo até o fim da frase
print(frase.capitalize())#faz com que a primeira letra da frase fique em maíusculo
print(frase.title())#faz com que após um espaço todas a primeiras letras das palavras fiquem em maiúsculo
print(frase.upper())#deixa tudo em maíusculo
print(frase.lower())#deixa tudo em minúsculo
print(frase.count("a"))#conta quantas letras "a" tem na frase
print(frase.find("oi"))#procura uma palavra na frase e mostra em qual indicie começa e se esta na frase
print(frase.strip())#elimina espaços inuteis na frase
print(len(frase))#mostra o comprimento da frase
print(frase.replace("Manipulando", "Mexendo"))#Renomeia a palavra que voce quer por outro (sem salvar)
print("texto" in frase)#mostra se a palvra esta escrita no texto
print("oi" in frase)#mostra se a palvra esta escrita no texto
print(frase.split())#divide a frase pelos espaços tornando-as em listas com indicies
divido=frase.split()
print(divido[0])#vai mostrar o indicie que eu escolhi da lista que foi criada pelo split
print(divido[0][4])#vai mostrar o indicie que eu escolhi da lista que foi criada pelo split e mostrar o indicie dentro da palavra 