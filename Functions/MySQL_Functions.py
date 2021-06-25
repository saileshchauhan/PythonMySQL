'''
@Author: Sailesh Chauhan
@Date: 24-06-2021
@Last Modified time: 24-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database.
'''
import sys

from mysql.connector import cursor

sys.path.append(r"D:\PythonMySQL\Functions")
import LogConfig
import logging,re

from decouple import config
import mysql.connector

class Functions:

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

    def read_table(self):
        try:
            mycursor=self.db.cursor()
            mycursor.execute("SELECT * FROM STUDENT")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            logging.critical(ex)        

    
    def show_tables(myobj):
        '''
        '''
        try:
            coursor=myobj.db.cursor()
            query="SHOW TABLES"
            coursor.execute(query)
            for table in coursor:
                print(table)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def order_by_marks(myobj):
        '''
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT * FROM STUDENT ORDER BY MATH_MARKS"
            coursor.execute(query)
            for row in coursor:
                print(row)
        except Exception as ex:
            logging.critical(ex)


############ NUMERIC FUNCTIONS ###########################

    def count(myobj):
        '''
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT COUNT(NAME) FROM STUDENT"
            coursor.execute(query)
            for row in coursor:
                print("Total number of students ",row)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)