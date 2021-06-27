'''
@Author: Sailesh Chauhan
@Date: 27-06-2021
@Last Modified time: 27-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database using
         procedure.
'''
import sys

from mysql.connector.errors import get_mysql_exception

sys.path.append(r"D:\PythonMySQL\StoredProcedure")
import LogConfig
import logging,re

from decouple import config
import mysql.connector

class CRUD_Methods:

    def __init__(self):
        self.db=mysql.connector.connect(
                host=config('host'),
                user=config('user'),
                passwd=config('passwd'),
                database=config('database')
                )
                
    def new_entry(self,name,marks,address,gender):
        '''
        Description:
            Method uses standard procedure to insert values in 
            student table.
        Parameters:
            Takes self,name,marks,address,gender.
        Return:
            None.
        '''
        try:
            mycursor=self.db.cursor()
            arg=[name,marks,address,gender]
            mycursor.callproc('sp_insert',arg)
            self.db.commit()
        except Exception as ex:
            logging.critical(ex)
        finally:
            mycursor.close()