import random 
digite = 0
maximo=int(input("digite ate que numero que vc vai adivinhar: "))
chance=int(input("quantas chances? "))
secret = random.randint(1,maximo)
while  not (digite == secret) and chance > 0:
    digite = int(input("digite um numero entre 1 e o numero maximo : "))
    if digite == secret :
        print ("acertou")
    elif digite < secret :
        print ("aumente")
        chance-=1
    else : 
        print ("diminua")
        chance-=1
