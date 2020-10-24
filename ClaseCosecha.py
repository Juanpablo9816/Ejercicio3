class Cosecha:
    __matriz = None
    __dia = 0
    __idCamion = 0
    __peso = 0
      
    @classmethod
    def cereoMatriz(cls):
        # **** CONSTANTES ****
        Dias = 30  # FILAS
        Camiones = 20  # COLUMNAS
        
        cls.__matriz = [0] * Dias #Numero de filas
        i=0
        for i in range(Dias):
            cls.__matriz[i] = [0] * Camiones #Numero de columnas
            i+=1

    def __init__(self, dia = 0, idCamion = 0 , peso = 0):
        self.__dia = dia
        self.__idCamion = idCamion
        self.__peso = peso
        
    def getDia(self):
        return self.__dia

    def getId(self):
        return self.__idCamion
    
    def getPeso(self):
        return self.__peso
    
    def setTabla(self, dia, camion, peso):
        dia = int(dia)-1
        camion = int(camion)-1
        try:
            self.__matriz[dia][camion] = self.__matriz[dia][camion] + float(peso)
        except IndexError:
            pass
                 
    def getKilos(self, idcamion):
        acum = 0
        for i in range(len(self.__matriz)):
            acum += float(self.__matriz[i][idcamion])
        return acum

    def verListado(self, dia, listaCamiones):
        print("PATENTE {0:10.0} CONDUCTOR {0:10.0} CANTIDAD DE KILOS" .format(""))

        for i in range(len(self.__matriz[(dia)])):
            if (float(self.__matriz[dia][i]) != 0):
                patente = listaCamiones[i].getPatente()
                conductor = listaCamiones[i].getConductor()
                print("{} {:10.0s} {} {:15.0s} {:.2f}" .format(patente,"",conductor,"",self.__matriz[dia][i]))

