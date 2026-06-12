listaperguntas = ["2+2" , "3+3" , "5+5"]
respostascertas = ["4" , "6" , "10"]
contador =0
for vez in range(3) :
    print (listaperguntas [vez])
    resposta = input("escreva a resposta da perguntas : ")
    if resposta == respostascertas[vez] :
        print ("acertou")
        contador +=1
    elif resposta == "" :
        print ("nada?")
    else : 
        print ("errou")
print (f"acertou {contador} vezes")
