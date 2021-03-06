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
        self.host=config('host')
        self.userName=config('user')
        self.passWord=config('passwd')
        self.databaseName=config('database')
        self.db=self.new_connection()

    def new_connection(self):
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
            regexNames="^[A-Z]{1,}[a-z]{2,}$"
            if(re.match(regexNames,value)):
                return str(value)
            logging.info("Invalid FirstName")
            quit()
        except Exception as ex:
            logging.critical(ex)
    
    def new_entry(self):
        try:
            mycursor=self.db.cursor()
            name=CRUD_Methods.validation(input("Enter First Name"))
            address=CRUD_Methods.validation(input("Enter Address"))
            value=(name,address)
            query="INSERT INTO student (NAME,ADDRESS) VALUES (%s,%s)"
            mycursor.execute(query,value)
            self.db.commit()
            logging.info(mycursor.rowcount,'record inserted.')
        except Exception as ex:
            logging.critical(ex)
    
    def read_table(self):
        try:
            mycursor=self.db.cursor()
            mycursor.execute("SELECT * FROM STUDENT")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            logging.critical(ex)

    def delete_entry(self):
        try:
            mycursor=self.db.cursor()
            self.read_table()
            id=int(input("Enter Id entry to be delete\n"))
            query="DELETE FROM STUDENT WHERE ID={}".format(id)
            mycursor.execute(query)
            self.db.commit()
        except Exception as ex:
            logging.critical(ex)

