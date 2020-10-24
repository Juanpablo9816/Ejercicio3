class Camion:
    __idCamion = 0
    __Conductor = ""
    __Patente = ""
    __Marca = ""
    __Tara = ""

    def __init__(self, idCamion, name, patente, marca, tara):
        self.__idCamion = idCamion
        self.__Conductor = name
        self.__Patente = patente
        self.__Marca = marca
        self.__Tara = tara
    
    def getId(self):
        return self.__idCamion

    def getConductor(self):
        return self.__Conductor
    
    def getPatente(self):
        return self.__Patente
    
    def getMarca(self):
        return self.__Marca
    
    def getTara(self):
        return self.__Tara
