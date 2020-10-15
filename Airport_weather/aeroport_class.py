class Aeroport:

    def setICAO(self, ICAO):
        self.__ICAO = ICAO
    
    def getICAO(self):
        return self.__ICAO

    def setTemperature(self,temp):
        self.__temp = temp

    def getTemperature(self):
        return self.__temp

    def setWindGusts(self, wind):
        self.__windGust = wind

    def getWindGust(self):
        return self.__windGust

    def setVisibility(self, viz):
        self.__visibility = viz

    def getVisibility(self):
        return self.__visibility