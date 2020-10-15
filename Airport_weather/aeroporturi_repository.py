import aeroport_class
#aceasta clasa se va instantia o sigura data 
class Aeroporturi_Repository:

    __aeroporturi = list()
    __listaAeroporturi = ["LRAR", "LRBC","LRBM","LRBS","LRCK","LRCL","LRCV","LRIA","LROD","LROP","LRSB","LRSM","LRSV","LRTC","LRTM","LRTR"]

    def getNumeAeroport(self, pozitie):
        return self.__listaAeroporturi[pozitie]

    def adaugaAeroportInLista(self, aeroport):
        self.__aeroporturi.append(aeroport)

    def getAeroport(self,pozitie):
        return self.__aeroporturi[pozitie]

    def getLungimeListaAeroporturi(self):
        return len(self.__listaAeroporturi)

    def getLungimeVarAeroporturi(self):
        return len(self. __aeroporturi)