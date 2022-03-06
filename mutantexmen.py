#Programa detectar secuencia ADN Mutante
#Creado por josegomezJ
#2022-03-06
#Magneto quiere reclutar la mayor cantidad de mutantes para poder lucharcontra los X-Men.
import re
import sys


dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG","GGGGTT","AAAAGT"}
dnac ={'dna': ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG','AAAAGT']}

########### Clase Mutante ##############
class Mutant():
    
    ####### valida si es una secuencia mutante dada por json #######
    def isMutant(self, dna):
        mutante=[]
        count=0
        for key in dna["dna"]: #valida la llave json dna    
            mutant = re.search(r'([A-Z])\1{3}.+',key) #expresion valida secuencia de 4 letras
            if mutant:
                count +=1
                mutante.append("{'Mutante "+str(count)+"':'"+mutant.group()+"'}")
                #print ("Secuencia Mutante Encontrada OK :"+ mutant.group())
        return mutante
if __name__ == '__main__':
    #args = str(sys.argv[1])
    validateAdn = Mutant()
    print(validateAdn.isMutant(dnac))

    
