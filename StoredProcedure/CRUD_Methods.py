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

    def read_table(self):
        '''
        Description:
            Method reads student table using stored procedure.
        Parameters:
            Takes self for connection.
        Return:
            None.
        '''
        try:
            mycursor=self.db.cursor()
            mycursor.callproc('sp_getall')
            rows=mycursor.stored_results()
            for result in rows:
                for row in result.fetchall():
                    print(row)             
        except Exception as ex:
            logging.critical(ex)

    def update_entry(self,id):
        '''
        Description:
            Method updates entry of particular student in student table
            using stored procedure.
        Parameters:
            Takes self and id as parameters.
        Return:
            None.
        '''
        try:
            name=input("Enter First Name of Student")
            marks=input("Enter Marks of {} ".format(name))
            address=input("Enter address of {} ".format(name))
            gender=input("Enter gender of {} ".format(name))
            mycursor=self.db.cursor()
            mycursor.callproc('sp_update',[name,marks,address,gender,id])
            self.db.commit()
        except Exception as ex:
            logging.critical(ex)