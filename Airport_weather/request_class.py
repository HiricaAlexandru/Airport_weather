import requests
from aeroport_class import Aeroport
from aeroporturi_repository import Aeroporturi_Repository
import sys
class request:
    __URL = "https://avwx.rest/api/metar/"


    def __setData(self,ICAO):
        
        aeroport = Aeroport()
        a = requests.get(self.__URL + ICAO)
        dictionar = a.json()
        aeroport.setICAO(ICAO)
        if a.status_code == 200:
           
            if "temperature" in dictionar:
                aeroport.setTemperature(dictionar["temperature"]["value"])
            
            if "wind_gust" in dictionar:
                aeroport.setWindGusts(dictionar["wind_gust"])
                
            if "visibility" in dictionar:
                aeroport.setVisibility(dictionar["visibility"]["value"])
        else:
            print("nu pot realiza conexiunea")

        self.__bazaDate.adaugaAeroportInLista(aeroport)

    def __init__(self):
        self.__bazaDate = Aeroporturi_Repository()

        
    def completezTotul(self):
        for i in range(0,self.__bazaDate.getLungimeListaAeroporturi()):
            self.__setData(self.__bazaDate.getNumeAeroport(i))

      
   