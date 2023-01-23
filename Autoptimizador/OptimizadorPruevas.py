import pandas as pd
import folium
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
app = Nominatim(user_agent="tycgis")
import time
import win32com.client
bocinas = win32com.client.Dispatch("SAPI.spVoice")

#df = pd.read_csv('MY2022 Fuel Consumption Ratings.csv')
dfe = pd.read_csv('csvveiculos.csv')
"""
df.columns = ['Año Modelo','Marca','Modelo','Clase Vehiculo','Tamaño Maquina(L)','Cilindros','Transmicion',
'Tipo Fuel','Consumo Fuel(ciudad(L/100km)','Consumo Fuel(carretera(L/100km)','Consumo Fuel(Consumo Combinado(L/100km)',
'Consumo Fuel(Consumo Combinado(mpg(millas por galon))','CO2 emiciones(g/km)','CO2 Rating','Smog Rating']
"""

#seleccionar veiculo
#Filtro por marca
while True:
    buscaCoche=str(input("Ingrese la marca de su vehículo: "))
    buscaCoche=buscaCoche.lower()
    if buscaCoche == "acura":
        filtro=dfe[(dfe["Marca"]=="Acura")]
        break
    if buscaCoche == "alfa romeo":
        filtro=dfe[(dfe["Marca"]=="Alfa Romeo")]
        break
    if buscaCoche == "audi":
        filtro=dfe[(dfe["Marca"]=="Audi")]
        break
    if buscaCoche == "bmw":
        filtro=dfe[(dfe["Marca"]=="BMW")]
        break
    if buscaCoche == "bentley":
        filtro=dfe[(dfe["Marca"]=="Bentley")]
        break
    if buscaCoche == "bugatti":
        filtro=dfe[(dfe["Marca"]=="Bugatti")]
        break
    if buscaCoche == "buick":
        filtro=dfe[(dfe["Marca"]=="Buick")]
        break
    if buscaCoche == "cadillac":
        filtro=dfe[(dfe["Marca"]=="Cadillac")]
        break
    if buscaCoche == "chevrolet":
        filtro=dfe[(dfe["Marca"]=="Chevrolet")]
        break
    if buscaCoche == "chrysler":
        filtro=dfe[(dfe["Marca"]=="Chrysler")]
        break
    if buscaCoche == "dodge":
        filtro=dfe[(dfe["Marca"]=="Dodge")]
        break
    if buscaCoche == "fiat":
        filtro=dfe[(dfe["Marca"]=="FIAT")]
        break
    if buscaCoche == "ford":
        filtro=dfe[(dfe["Marca"]=="Ford")]
        break
    if buscaCoche == "gmc":
        filtro=dfe[(dfe["Marca"]=="GMC")]
        break
    if buscaCoche == "genesis":
        filtro=dfe[(dfe["Marca"]=="Genesis")]
        break
    if buscaCoche == "honda":
        filtro=dfe[(dfe["Marca"]=="Honda")]
        break
    if buscaCoche == "hyundai":
        filtro=dfe[(dfe["Marca"]=="Hyundai")]
        break
    if buscaCoche == "infiniti":
        filtro=dfe[(dfe["Marca"]=="Infiniti")]
        break
    if buscaCoche == "jaguar":
        filtro=dfe[(dfe["Marca"]=="Jaguar")]
        break
    if buscaCoche == "jeep":
        filtro=dfe[(dfe["Marca"]=="Jeep")]
        break
    if buscaCoche == "kia":
        filtro=dfe[(dfe["Marca"]=="Kia")]
        break
    if buscaCoche == "lamborghini":
        filtro=dfe[(dfe["Marca"]=="Lamborghini")]
        break
    if buscaCoche == "land rover":
        filtro=dfe[(dfe["Marca"]=="Land Rover")]
        break
    if buscaCoche == "lexus":
        filtro=dfe[(dfe["Marca"]=="Lexus")]
        break
    if buscaCoche == "lincoln":
        filtro=dfe[(dfe["Marca"]=="Lincoln")]
        break
    if buscaCoche == "mini":
        filtro=dfe[(dfe["Marca"]=="MINI")]
        break
    if buscaCoche == "maserati":
        filtro=dfe[(dfe["Marca"]=="Maserati")]
        break
    if buscaCoche == "mazda":
        filtro=dfe[(dfe["Marca"]=="Mazda")]
        break
    if buscaCoche == "mercedes-benz":
        filtro=dfe[(dfe["Marca"]=="Mercedes-Benz")]
        break
    if buscaCoche == "mitsubishi":
        filtro=dfe[(dfe["Marca"]=="Mitsubishi")]
        break
    if buscaCoche == "nissan":
        filtro=dfe[(dfe["Marca"]=="Nissan")]
        break
    if buscaCoche == "porsche":
        filtro=dfe[(dfe["Marca"]=="Porsche")]
        break
    if buscaCoche == "ram":
        filtro=dfe[(dfe["Marca"]=="Ram")]
        break
    if buscaCoche == "rolls-royce":
        filtro=dfe[(dfe["Marca"]=="Rolls-Royce")]
        break
    if buscaCoche == "subaru":
        filtro=dfe[(dfe["Marca"]=="Subaru")]
        break
    if buscaCoche == "toyota":
        filtro=dfe[(dfe["Marca"]=="Toyota")]
        break
    if buscaCoche == "volkswagen":
        filtro=dfe[(dfe["Marca"]=="Volkswagen")]
        break
    if buscaCoche == "volvo":
        filtro=dfe[(dfe["Marca"]=="Volvo")]
        break

print("-------------------------------------------------------------------------")
while True:
    try:
        gasoVehiculo = int(input("Ingresa la gasolina de tu vehículo en Mililitros o en Litros: "))
        if gasoVehiculo != "":
            break
    except ValueError:
        print("Por favor, ingrese un valor valido. Ej: 69")

#cambio a litross
if gasoVehiculo > 120.0:
    gasoVehiculo = gasoVehiculo/1000.0   
else:
    gasoVehiculo = gasoVehiculo*1.0

while True:
    estado = "ciudad" #str(input("¿Estás en la ciudad o en la carretera?: "))
    estado = estado.lower()
    #calculo gasto conbustible por ciudad
    if estado == "ciudad":
        consumo = filtro['Consumo Fuel(ciudad(L/100km)']
        index_consumo = consumo.index.values[0]#saca el elemnto
        a = dfe.loc[index_consumo,'Consumo Fuel(ciudad(L/100km)']
        porKm = a/100
        break
            
print("-------------------------------------------------------------------------")

#conseguir distancia 
import urllib
import requests
api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "Pz3XNvlinhcIHMRgiNsjW0yJKPVyK6qA"

while True:
    origin = input("Ingresa tu ubicacion: ")
    if origin == 'q':
        break
    destination = input("Ingresa tu destino: ")
    if destination == 'q':
        break

    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})

    json_data = requests.get(url).json()

    status_code = json_data["info"]["statuscode"]
    if status_code==0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"]*1.61

        print("---------------------------------------------------------------------------")
        
        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duración del viaje: {trip_duration}")
        print("Distancia en kilometros: " + str("{:.2f}".format(distance)+"km"))
        #gasolina requerida con precio
        consumoNece = distance*porKm
        print("Nececitaras: "+str("{:.2f}".format(consumoNece)+"L de gasolina"))
        laFAfa = consumoNece*1349.40#precio medio convustible
        print("Necesitaras: $"+str("{:.2f}".format(laFAfa)+" aproximadamnte"))
        
        #recomendaciones

        print("---------------------------------------------------------------------------")
        print("Indicacioens del Viaje\n")
        
        print("¿Desea ver escuchar indicaciones generales antes de comenzar?\n")
        bocinas.speak("¿Desea escuchar unas indicaciones generales antes de comenzar?")
        while True:
            indicacionesIn = input(str("¿si o no?: ")) 

            indicacionesIn = indicacionesIn.lower()
            if indicacionesIn == "si":
                print("Antes que nada, arranca el motor sin pisar el acelerador y comienza en 1ª")
                print("Cambia a 2ª despues de avanzar unos 6 metros o unos 2 segundos aprox")
                print("Realiza los cambios entre 3ª, 4ª y 5ª cada 2000 rpm aprox")
                #print("Si te guias más por la velocidad cambia a 3ª a los 30 km/h, a 4ª a los 40 km/h, a 5ª a los 50 km/h")
                print("Recueda circular en 4ª y 5ª a bajas revoluciones")
                print("Manten en lo posible una velocidad uniforme durante el trayecto, evita frenazos, aceleraciones y cambios innecesarios.")
                print("Para desacelerar levantar el pie del acelerador y dejar andar el vehículo con el cambio puesto, sin reducirlo")
                print("Y para frenar haslo suave y progresivo con el pedal de freno y reduce el cambio lo más tarde posible")

                bocinas.speak("Antes que nada arranca el motor sin pisar el acelerador y comienza en primera")
                bocinas.speak("Cambia a segunda despues de avanzar unos 6 metros o unos 2 segundos aprox")
                bocinas.speak("Realiza los cambios entre tercera, cuarta y quinta cada 2000 revoluciones por minuto aprox")
                bocinas.speak("Si te guias más por la velocidad cambia a tercera a los 30 kilometros por hora, a cuarta a los 40 kilometros por hora, a quinta a los 50 kilometros por hora")
                bocinas.speak("Recueda circular en cuarta y quinta a bajas revoluciones")
                bocinas.speak("Manten en lo posible una velocidad uniforme durante el trayecto, evita frenazos, aceleraciones y cambios innecesarios")
                bocinas.speak("Para desacelerar levantar el pie del acelerador y dejar andar el vehículo con el cambio puesto, sin reducirlo")
                bocinas.speak("Y para frenar haslo suave y progresivo con el pedal de freno y reduce el cambio lo más tarde posible")

                break
            if indicacionesIn == "no":
                bocinas.speak("obteniedo ruta")
                break

        #print("---------------------------------------------------------------------------")
        
        localizacion1 = origin
        #print("Primer punto -> " , localizacion1)
        location1 = app.geocode(localizacion1).raw
        latitude1 = location1["lat"]
        longitude1 = location1["lon"]
        punto1 = (latitude1, longitude1)

        #print(punto1)
        localizacion2 = destination
        #print("Segundo punto -> " , localizacion2)

        location2 = app.geocode(localizacion2).raw
        latitude2 = location2["lat"]
        longitude2 = location2["lon"]

        punto2 = (latitude2, longitude2)
        #print(punto2)
        map = folium.Map(localizacion1=[latitude1, longitude1], zoom_start=1)

        # Punto 1
        map.add_child(folium.Marker(punto1, popup=localizacion1, icon=folium.Icon(color='green', icon="car-side", prefix="fa")))

        # Punto 2
        map.add_child(folium.Marker(punto2, popup=localizacion2, icon=folium.Icon(color='red', icon="flag-checkered", prefix="fa")))

        map.save("map.html")
        
        print("---------------------------------------------------------------------------")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_remaining = distance - each["distance"]*1.61
            distance_rec = distance - distance_remaining
            consumido = porKm * distance_rec
            gasoVehiculo = gasoVehiculo - consumido
            #tiempoRec = distance_rec * 60 #por tener una velocidad
            
            if gasoVehiculo < gasoVehiculo*15/100:
                recomendaciones = " (¡Su gasolina estará llegando a niveles criticos!, por favor recarge su tanque)"
            else:
                recomendaciones = ""
            #reduccion de velocidad al abansar muy rapido o a destiempo
            #if gasoVehiculo:
            #    recomendos = ""
            #else:
            #    recomendos = ""
                       
            each["narrative"] = each["narrative"].replace("Head toward", "Dirigete a")
            each["narrative"] = each["narrative"].replace("Continue on", "Continua por")
            each["narrative"] = each["narrative"].replace("Turn right onto", "Gira a la derecha hacía")
            each["narrative"] = each["narrative"].replace("Turn left onto", "Gira a la izquierda hacía")
            each["narrative"] = each["narrative"].replace("Take right ramp onto", "Toma la rampa derecha hacía")
            each["narrative"] = each["narrative"].replace("Take left ramp onto", "Toma la rampa izquierda hacía")
            each["narrative"] = each["narrative"].replace("Take the left exit toward", "Toma la salida izquierda camino a")
            each["narrative"] = each["narrative"].replace("Take the right exit toward", "Toma la salida derecha camino a")
            each["narrative"] = each["narrative"].replace("onto", "hacía")
            each["narrative"] = each["narrative"].replace("Take exit", "Toma la salida")
            each["narrative"] = each["narrative"].replace("Take the exit toward", "Toma la salida camino a")
            each["narrative"] = each["narrative"].replace("Arrive at", "Llega a")
            each["narrative"] = each["narrative"].replace("slightly", "ligeramente a la")
            each["narrative"] = each["narrative"].replace("Turn ", "Gira ")
            each["narrative"] = each["narrative"].replace(" left ", " izquierda ")
            each["narrative"] = each["narrative"].replace(" right ", " derecha ")
            each["narrative"] = each["narrative"].replace("Keep", "Continua por la")
            each["narrative"] = each["narrative"].replace("Turn right ", "Gira a la derecha ")
            each["narrative"] = each["narrative"].replace("Turn left ", "Gira a la izquierda ")
            each["narrative"] = each["narrative"].replace("roundabouts", "rotondas")
            each["narrative"] = each["narrative"].replace("roundabout", "rotonda")
            each["narrative"] = each["narrative"].replace(" and ", " y ")
            each["narrative"] = each["narrative"].replace(" continue ", " continua ")
            each["narrative"] = each["narrative"].replace(" on ", " por ")
            each["narrative"] = each["narrative"].replace("Pass", "Pasa")
            each["narrative"] = each["narrative"].replace("Take the ", "Toma la ")
            each["narrative"] = each["narrative"].replace("exit", "salida")
            each["narrative"] = each["narrative"].replace("from", "por")
            each["narrative"] = each["narrative"].replace("toward", "camino a")
            each["narrative"] = each["narrative"].replace(" right.", " a la dercha.")
            each["narrative"] = each["narrative"].replace(" left.", " a la izquierda.")
            each["narrative"] = each["narrative"].replace(" Go for", " Continua por")
            each["narrative"] = each["narrative"].replace("Take ramp", "Toma la rampa")
            each["narrative"] = each["narrative"].replace("Head northeast", "Dirigete al noreste")
            each["narrative"] = each["narrative"].replace("Head north", "Dirigete al norte")
            each["narrative"] = each["narrative"].replace("Head northwest", "Dirigete al noroeste")
            each["narrative"] = each["narrative"].replace("Head south", "Dirigete al sur")
            each["narrative"] = each["narrative"].replace("Head southeast", "Dirigete al sudeste")
            each["narrative"] = each["narrative"].replace("Head southwest", "Dirigete al sudoeste")
            each["narrative"] = each["narrative"].replace("Head west", "Dirigete al oeste")
            each["narrative"] = each["narrative"].replace("Head east", "Dirigete al este")
            each["narrative"] = each["narrative"].replace("Make a U", "Has una U")
            
            #ejemplo Toyota, Camry AWD SE, Mid-size, 4, AS8, X, 9.4, 6.8
        
            print(each["narrative"] + " (" +str("{:.2f}".format(distance_remaining)) + " km faltantes)"
            #+" ("+str("{:.2f}".format(distance_rec))+" km recorridos)"
            +" ("+str("{:.2f}".format(consumido))+" L de gasolina consumidos)"
            +" ("+str("{:.2f}".format(gasoVehiculo))+" L de gasolina restante)"
            +recomendaciones+"\n")

            bocinas.speak(each["narrative"] + " (" +str("{:.2f}".format(distance_remaining)) + " Kilometros faltantes)"
            #+" ("+str("{:.2f}".format(distance_rec))+" Kilometros recorridos)"
            +" ("+str("{:.2f}".format(consumido))+" Litros de gasolina consumidos)"
            +" ("+str("{:.2f}".format(gasoVehiculo))+" Litros de gasolina restante)"
            +recomendaciones)            
            distance = distance_remaining

            #time.sleep(tiempoRec) 
            if distance_remaining < 0:
                print("\nSi estará más de unos minutos estacionado recuerde apagar el motor.\n")
                bocinas.speak("Si estará más de unos minutos estacionado recuerde apagar el motor")
            if gasoVehiculo <= 0:
                print("\n¡Sin gasolina!, recarga tu tanque.")  
                bocinas.speak("¡Sin gasolina!, recarga tu tanque.")
                break