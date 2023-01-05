import pandas as pd

#https://diccionario.motorgiga.com/diccionario/consumo-combinado-definicion-significado/gmx-niv15-con88320.htm
#https://www.google.com/search?client=firefox-b-e&q=que+significa+hwy+en+ingl%C3%A9s
#https://www.google.com/search?client=firefox-b-e&q=que+es+mpg+en+carros
#https://interactivechaos.com/es/manual/tutorial-de-pandas/agrupaciones-en-dataframes
#https://es.wikihow.com/calcular-la-eficiencia-del-combustible-de-tu-auto-(MPG-o-KML)
#https://aprendeconalf.es/docencia/python/manual/pandas/
#https://www.delftstack.com/es/howto/python-pandas/how-to-rename-columns-in-pandas/
#https://www.codigopiton.com/seleccionar-filas-de-dataframe-segun-valor-de-columnas/

df = pd.read_csv('MY2022 Fuel Consumption Ratings.csv')

#print(df)

#print("\nOriginal DataFrame")
#print(pd.DataFrame(df))
df.columns = ['Año Modelo','Marca','Modelo','Clase Vehiculo','Tamaño Maquina(L)','Cilindros','Transmicion',
'Tipo Fuel','Consumo Fuel(ciudad(L/100km)','Consumo Fuel(carretera(L/100km)','Consumo Fuel(Consumo Combinado(L/100km)',
'Consumo Fuel(Consumo Combinado(mpg(millas por galon))','CO2 emiciones(g/km)','CO2 Rating','Smog Rating']

#print("\nModified DataFrame")
#print(pd.DataFrame(df))

#print(df.groupby(by = ["Marca"]).mean())

#promedio consumo por marca
#print("promedio consumo")
#print(df.groupby(by = ["Marca"]).mean())

#maximo consumo por marca
#print("maximo consumo")
#print(df.groupby(by = ["Marca"]).max())

#minimo Consumo por marca
#print("minimo consumo")
#print(df.groupby(by = ["Marca"]).min())

