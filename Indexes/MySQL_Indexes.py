'''
@Author: Sailesh Chauhan
@Date: 25-06-2021
@Last Modified time: 25-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database.
'''
import sys

from mysql.connector import cursor

sys.path.append(r"D:\PythonMySQL\Functions")
import LogConfig
import logging,re

from decouple import config
import mysql.connector

class IndexFunction:

    def __init__(self):
        self.host=config('host')
        self.userName=config('user')
        self.passWord=config('passwd')
        self.databaseName=config('database')
        self.db=self.new_connection()

    def new_connection(self):
        '''
        Description:
            Method connects python with MySql databases.
        '''
        try:
            db=mysql.connector.connect(
                host=self.host,
                user=self.userName,
                passwd=self.passWord,
                database=self.databaseName
                )
            if(db.is_connected):
                logging.info("Connection Succesful")
            return db
        except Exception as ex:
            logging.critical(ex)
    
    
    def read_index(self):
        '''
        Description:
            Method Finds index.
        '''
        try:
            self.show_tables()
            mycursor=self.db.cursor()
            tableName=input("Enter Table name to find indexes\n")
            mycursor.execute("SHOW INDEX FROM practisedb.{}".format(tableName))
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            logging.critical(ex)
    
    