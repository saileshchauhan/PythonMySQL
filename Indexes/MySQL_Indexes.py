'''
@Author: Sailesh Chauhan
@Date: 25-06-2021
@Last Modified time: 25-06-2021
@Title : In this program I have added methods to perform create,read,show
         drop indexes in MySQL with Python.
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
    
    def show_tables(myobj):
        '''
        Description:
            Method reads tables in database.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SHOW TABLES"
            coursor.execute(query)
            for table in coursor:
                print(table)
            tableName=input("Enter table name\n")
            print("SCHEMA OF TABLE {}".format(tableName))
            query="DESCRIBE practisedb.{}".format(tableName)
            coursor.execute(query)
            for row in coursor:
                print(row)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def create_indexes(myobj):
        '''
        Description:
            Methods create index for user selected table.
        '''
        try:
            myobj.show_tables()
            coursor=myobj.db.cursor()
            tableName=input("Enter table name\n")
            viewName=input("Enter name of index\n")
            column=input("Enter Column name\n")
            createQuery="CREATE INDEX {} ON {} ({})".format(viewName,tableName,column)
            logging.info(coursor.execute(createQuery))
        except Exception as ex:
            logging.critical(ex)

    def drop_indexes(myobj):
        '''
        Description:
            Drop indexes which are existing in the database.    
        '''
        try:
            myobj.read_index()
            coursor=myobj.db.cursor()
            tableName=input("Enter name of table")
            indexDelete=input("Enter name of index to be dropped")
            query="ALTER TABLE {} DROP INDEX {}".format(tableName,indexDelete)
            coursor.execute(query)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)