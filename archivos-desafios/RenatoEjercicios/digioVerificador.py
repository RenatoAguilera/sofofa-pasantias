import math #para acceder a funciones matematicas
print("inserte los numeros de su rut en orden, sin el digito verificador")#texto para explicar
n1 = int(input(": ")) #los inputs asignan a las variables los numeros individuales del rut sin digito verificador
n2 = int(input(": ")) 
n3 = int(input(": "))  
n4 = int(input(": ")) 
n5 = int(input(": ")) 
n6 = int(input(": ")) 
n7 = int(input(": ")) 
n8 = int(input(": ")) 

N8 = n8 *2 #comiensa la formula 
N7 = n7 *3 #los numeros de la lista de inputs se invierte y se multiplica cada uno por la secuencia de numeros correspondiente a la formula para sacar el digito verificdor
N6 = n6 *4 #y esos resultados los asignamo a una variable para cada uno
N5 = n5 *5
N4 = n4 *6
N3 = n3 *7
N2 = n2 *2
N1 = n1 *3

sumaDeNumeros = N1 + N2 + N3 + N4 + N5 + N6 + N7 + N8 #se suman los resultados

diviEnOnce = sumaDeNumeros / 11 #sumadenumeros se divide en 11

multiOnce = math.trunc(diviEnOnce) * 11 #el resultado de divenonce es un float, asi que usando la funcion math.trunc se combierte en un int y se mulktiplica en 11

resultado = sumaDeNumeros - multiOnce #despues restamos la sum inicial, por multionce

final = 11 - resultado #como dicta la formula hay restarle la variable anterior a 11
if final == 11: #if para identificar el caso de que al final resulte en 11 o 10
    final = 0
    print(0)
elif final == 10:
    final = "K"
    print("K")
else:
    print(final) #imprime el digito verificador
rut = str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8) #consige los numeros originles del rut sin digito v
rutFinal = str(rut)+"-"+str(final) # agrega el digito v
print(rutFinal) #prin para comprobar

def creaeTxt(): #funcion que añade el rutFinal al achibo .txt
    Archibo.write(rutFinal)
    Archibo.close()
Archibo = open("text.txt","w") #abre un archibo .txt
creaeTxt()
