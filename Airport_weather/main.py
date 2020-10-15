from aeroporturi_repository import *
from request_class import *
from aeroport_class import *
def main():
    internet = request()
    internet.completezTotul()
    obj = Aeroporturi_Repository()
    for i in range(0,obj.getLungimeVarAeroporturi()):
        aeroport = obj.getAeroport(i)
        print(aeroport.getICAO(), " ", aeroport.getTemperature(), " ", aeroport.getWindGust())
   
main()