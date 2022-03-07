#Clase auxiliar para conectar DB
#Creado por josegomezJ
#2022-03-06
#Magneto quiere reclutar la mayor cantidad de mutantes para poder lucharcontra los X-Men.
from pymysql import connect

from pymysql.cursors import DictCursor
import json
import os

class ToConnectExec:

    ########### Conexion DB MYSQL ##############
    def connectDBMysql (self):
        self.conn = connect(host='127.0.0.1', port=xxxx, user='******', passwd='*******', db='integrac_lab-***', autocommit = True, cursorclass=DictCursor)
        
    ########### Conexion DB MYSQL ##############
    def connectionMy(self):
        self.connectDBMysql()
        cur = self.conn.cursor()
        cur.execute(self.reader_qy())
        result = cur.fetchall()
        self.conn.commit()
        cur.close()
        self.conn.close()
        return result


    ###########  Conexion DB pasando multiples parametros  ##############
    def connectionMyMultiParam(self, query, *param):
        self.connectDBMysql()
        cur = self.conn.cursor()
        result=""
        if not (param is None):
            #print( param)
            cur.execute(query,(param))
            result = cur.fetchall()
            self.conn.commit()
            cur.close()
            self.conn.close()
            return result
        elif not param:
            return "sin parametros para consultar"

    ###########  insertar registros en DB tabla  #######
    def insert_mysql(self,type,name,date,digest):
        self.connectDBMysql()
        sql = "INSERT INTO stat_adn (type_adn,name_adn,cur_date,digest) VALUES (%s,%s,%s,%s)"  
        cur = self.conn.cursor()
        try:
            with cur as cursor:
                #mantener la conexión activa    
                self.conn.ping(reconnect=True) 
                cursor.execute(sql,(type,name,date,digest))
                self.conn.commit()
                cursor.close()
                return print( "record inserted.")   
        finally:
            self.conn.close()
    

