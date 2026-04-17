idade = int(input("digites sua idade: "))
ingresso = input("tem ingresso? ")
autorização = input("tem permição? ")
listavip = input("tu e vip? ")
if idade <= 12:
    print ("sai")
elif idade >=  18 and (ingresso== "sim" or listavip == "sim"):
    print ("pode passar trouxa")
elif autorização == "sim" and idade >=  18 and (ingresso== "sim" or listavip == "sim" ):
   print ("pode entrar")
else :
    print ("nao pode entrar")
