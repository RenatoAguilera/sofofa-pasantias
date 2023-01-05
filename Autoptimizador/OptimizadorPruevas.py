import pandas as pd
import math

df = pd.read_csv('MY2022 Fuel Consumption Ratings.csv')

df.columns = ['Año Modelo','Marca','Modelo','Clase Vehiculo','Tamaño Maquina(L)','Cilindros','Transmicion',
'Tipo Fuel','Consumo Fuel(ciudad(L/100km)','Consumo Fuel(carretera(L/100km)','Consumo Fuel(Consumo Combinado(L/100km)',
'Consumo Fuel(Consumo Combinado(mpg(millas por galon))','CO2 emiciones(g/km)','CO2 Rating','Smog Rating']

#seleccionar veiculo
buscaMarca = str(input("Ingrese la marca de su vehiculo: "))
buscaModelo = str(input("Ingrese el modelo de su vehiculo: "))
buscaClase = str(input("Ingrese la clase de su vehiculo: "))
buscaCilindros = str(input("Ingrese la cantida de cilindros de su vehiculo: "))
buscaTransmicion = str(input("Ingrese la transmicion de su vehiculo: "))
buscaCombustible = str(input("Ingrese el tipo de convustible de su vehiculo: "))

#formuas 


#ciudad


#carretera

