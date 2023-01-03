palabraInicial = str(input("inserete una palabra: "))
palabraInicial = palabraInicial.lower() #cambia todo a minuscula
palabraInicial = palabraInicial.replace(" ","") #quita espaciosy los 
palabraInicial = palabraInicial.replace("á", "")
palabraInicial = palabraInicial.replace("é", "")
palabraInicial = palabraInicial.replace("í", "")
palabraInicial = palabraInicial.replace("ó", "")
palabraInicial = palabraInicial.replace("ú", "")
if(palabraInicial) == (palabraInicial)[::-1]:#::recorre toda la cadena de caracteres, y -1 imbierte la lectura de caracteres del input
    print("es polindroma") #en el caso de ser polindroma
else:
    print("no es polindroma")

