#Programa detectar secuencia ADN Mutante
#Creado por josegomezJ
#2022-03-06
#Magneto quiere reclutar la mayor cantidad de mutantes para poder lucharcontra los X-Men.
import re
import sys
import logging
import pymysql
import datetime
import hashlib
import json
from connectdb import ToConnectExec

dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG","GGGGTT","AAAAGT"}
dnac ={'dna': ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG','AAAAGT']}
pathfileslogs='/home/goldenman/lab/'
#pathfileslogs='/Users/joseagomezjaramillo/home/betaws/mutantex/'
#validar fecha actual y formatearla
date_eval = datetime.datetime.now()
date_log= date_eval.strftime("%Y%m%d")
daterecord = date_eval.strftime("%Y-%m-%d %H:%M:%S")


########### Clase Mutante ##############
class Mutant():
    
    ####### valida si es una secuencia mutante dada por json #######
    def isMutant(self, dna):
        loggerm = self.setup_custom_logger('mutantes')
        loggerh = self.setup_custom_logger('humanos')
        mutante=[]
        count=0
 
        for key in dna["dna"]: #valida la llave json dna    
            mutant = re.search(r'([A-Z])\1{3}.+',key) #expresion valida secuencia de 4 letras
            if mutant:
                count +=1
                mutante.append("{'Mutante "+str(count)+"':'"+mutant.group()+"'}")
                loggerm.info(' Mutante Encontrado # '+ mutant.group())
                try:
                    digest=hashlib.sha256(str(mutant.group()).encode("utf-8")).hexdigest() #digest control huella unica registro mutante
                    ToConnectExec().insert_mysql('mutante',mutant.group(),date_eval,digest)
                except pymysql.err.ProgrammingError as except_detail:
                    loggerh.error(' Error mysql '+ except_detail) 
                    print("pymysql.err :"+ except_detail)                     
            else:
                count +=1
                mutante.append("{'Humano "+str(count)+"':'"+key+"'}")
                try:
                    digest=hashlib.sha256(str(key).encode("utf-8")).hexdigest() #digest control huella unica registro humano
                    ToConnectExec().insert_mysql('humano',key,date_eval,digest)
                except pymysql.err.ProgrammingError as except_detail:
                    loggerh.error(' Error mysql '+ except_detail)
                    print("pymysql.err :"+ except_detail)
                    
                loggerh.info(' Humano Encontrado # '+ key)
        return mutante

    ####### valida estadisticas #######
    def stats(self):
        query = """select  count(%s) as counter, type_adn,
                (CASE WHEN type_adn='mutante' THEN  (select count(*) from stat_adn where type_adn='mutante')/(select count(*) from stat_adn where type_adn='humano') ELSE 0 END) as ratio
                from stat_adn group by type_adn """
        stats = ToConnectExec().connectionMyMultiParam(query,'type_adn')
        colect=[]
        for x in stats:
            if "mutante" in x['type_adn']:
                colect.append('count_mutant_dna :'+str(x['counter']))
            else:
                colect.append('count_human_dna:'+str(x['counter']))
            colect.append('ratio:'+str(x['ratio']))
        
        return colect

    ####### configuracion log #######
    def setup_custom_logger(self,name):
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler(pathfileslogs+'log_mutante_'+name+'_'+date_log+'.txt', mode='a')
        handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHandler(screen_handler)
        return logger

if __name__ == '__main__':
    validateAdn = Mutant()
    print(validateAdn.isMutant(dnac))

    
