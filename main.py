print("Zodiaco")
dia = int(input("Dia: "))
mes = int(input("Mes: "))

if (dia>0 and dia<=31) and (mes>0 and mes<=12):
    if (dia>20 and dia<=31) and (mes==3) or (dia>0 and dia<=21) and (mes==4):
        print("aries") 
    elif (dia>21 and dia<=30) and (mes==4) or (dia>0 and dia<=21) and (mes==5):
        print("tauro")
    elif (dia>21 and dia<=31) and (mes==5) or (dia>0 and dia <=21) and (mes==6):
        print("geminis")
    elif (dia>21 and dia<=30) and (mes==6) or (dia>0 and dia<=21) and (mes==7):
        print("cancer")
    elif (dia>21 and dia<=31) and (mes==7) or (dia>0 and dia<=21) and (mes==8):
        print("leo")
    elif (dia>21 and dia<=30) and (mes==8) or (dia>0 and dia<=21) and (mes==9):
        print("virgo")
    elif (dia>21 and dia<=31) and (mes==9) or (dia>0 and dia<=21) and (mes==10):
        print("libra")
    elif (dia>21 and dia<=30) and (mes==10) or (dia>0 and dia<=21) and (mes==11):
        print("escorpio")
    elif (dia>21 and dia<=31) and (mes==11) or (dia>0 and dia<=21) and (mes==12):
        print("sagitario")
    elif (dia>21 and dia<=30) and (mes==12) or (dia>0 and dia<=21) and (mes==1):
        print("capricornio")
    elif (dia>21 and dia<=31) and (mes==1) or (dia>0 and dia<=21) and (mes==2):
        print("acuario")
    elif (dia>21 and dia<=29) and (mes==2) or (dia>0 and dia<=21) and (mes==3):
        print("piscis")
    else:
        print("Numero no valido...")