'''
@Author: Sailesh Chauhan
@Date: 24-06-2021
@Last Modified time: 24-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database.
'''
import sys

sys.path.append(r"D:\PythonMySQL\Python_CRUD")
import LogConfig
import logging,re

from decouple import config
import mysql.connector

class CRUD_Methods:

    def __init__(self):
        self._host=config('host')
        self._userName=config('user')
        self._passWord=config('passwd')
        self._databaseName=config('database')
        self._db=self.new_connection()

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
            return db
        except Exception as ex:
            logging.critical(ex)
    
    def validation(value):
        '''
        Description:
            Method validates values given as parameters.
        Parameters:
            Takes value as parameter.
        Return:
            value after validating.
        '''
        try:
            regexFloat="^[A-Z]{1,}[a-z]{2,}$"
            if(re.match(regexFloat,value)):
                return str(value)
            logging.info("Invalid FirstName")
            quit()
        except Exception as ex:
            logging.critical(ex)
    
    def new_entry(self):
        try:
            mycursor=self._db.cursor()
            name=CRUD_Methods.validation(input("Enter First Name"))
            address=CRUD_Methods.validation(input("Enter Address"))
            value=(name,address)
            query="INSERT INTO student (NAME,ADDRESS) VALUES (%s,%s)"
            mycursor.execute(query,value)
            self._db.commit()
            logging.info(mycursor.rowcount,'record inserted.')
        except Exception as ex:
            logging.critical(ex)
    
    def read_table(self):
        try:
            mycursor=self._db.cursor()
            mycursor.execute("SELECT * FROM STUDENT")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            logging.critical(ex)

    def delete_entry(self):
        try:
            mycursor=self._db.cursor()
            self.read_table()
            id=int(input("Enter Id entry to be delete\n"))
            query="DELETE FROM STUDENT WHERE ID={}".format(id)
            mycursor.execute(query)
            self._db.commit()
        except Exception as ex:
            logging.critical(ex)

