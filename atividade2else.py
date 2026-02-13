danodaespada = 5
vidadomob = 20
quantidadedegolpes = 15
vidadoboss = 25
if vidadomob < quantidadedegolpes * danodaespada:
  print ("ganhou do mob")
  if vidadoboss < quantidadedegolpes * danodaespada:
    print ("ganhou do boss")
  else : 
    print ("perdeu pelo boss")
else :
  print ("perdeu pelo mob")
 
