lista = ["alexandre" , "arthur" , "hiago" , "pedro"]
print (lista)
index = int(input("escolha o index do aluno que voce deseja saber(começa com 0 ) "))

if index < 0 or index > len(lista)-1:
    print("o index que voce escolheu nao esta presente na lista ")
else:
    print(lista[index])
