'''
@Author: Sailesh Chauhan
@Date: 24-06-2021
@Last Modified time: 24-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database.
'''

import logging
import LogConfig
from decouple import config
import mysql.connector

class CRUD_Methods:

    def __init__(self):
        self._host=config('host')
        self._userName=config('user')
        self._passWord=config('passwd')
        self._databaseName=config('database')
    
    def new_connection(self):
        try:
            db=mysql.connector.connect(
                host=self._host,
                user=self._userName,
                passwd=self._passWord,
                database=self._databaseName
                )
            if(db.is_connected):
                logging.info("Connection Succesful")
            self._db=db
        except Exception as ex:
            logging.critical(ex)
    


