# input
print("#######################################")
cant_minuto = input ("digite la cant_minuto: ")
print("#######################################")
cant_minuto = int (cant_minuto)
print("#######################################")

#processing
if  cant_minuto <= 3 :
     valor_llamada= 300

else:
    valor_llamada = 300+50* (cant_minuto -3)


    #output
    print("###############################################")
    print ("el valor de llamada es: " +str(valor_llamada))
    print("###############################################")    