digite = 0
secret = 7
while  not (digite == secret) :
    digite = int(input("digite um numero entre 1 a 10: "))
    if digite == secret :
        print ("acertou")
    elif digite < secret :
        print ("aumente")
    else : 
        print ("diminua")
