'''
@Author: Sailesh Chauhan
@Date: 25-06-2021
@Last Modified time: 25-06-2021
@Title : This script provides function for performing create,show,drop
         and establish connection with MySQL.
'''
import sys

from mysql.connector import cursor

sys.path.append(r"D:\PythonMySQL\Functions")
import LogConfig
import logging,re

from decouple import config
import mysql.connector

class ViewFunction:

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

    def read_view(self):
        '''
        Description:
            Method reads all row of table.
        '''
        try:
            self.show_tables()
            mycursor=self.db.cursor()
            viewName=input("Enter Table name or view name\n")
            mycursor.execute("SELECT * FROM {}".format(viewName))
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
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)
    
    def create_views(myobj):
        '''
        Description:
            Methods create views from existing tables.
        '''
        try:
            myobj.show_tables()
            coursor=myobj.db.cursor()
            tablename=input("Enter table name\n")
            query="DESCRIBE practisedb.{}".format(tablename)
            coursor.execute(query)
            print("SCHEMA OF TABLE {}".format(tablename))
            for row in coursor:
                print(row)
            viewName=input("Enter name of view\n")
            condition=input("Enter condition it will go after WHERE\n")
            createQuery="CREATE VIEW {} AS SELECT * FROM {} WHERE {}".format(viewName,tablename,condition)
            logging.info(coursor.execute(createQuery))
        except Exception as ex:
            logging.critical(ex)
    
    
    def drop_views(myobj):
        '''
        Description:
            Drop view which are existing in the database.    
        '''
        try:
            myobj.show_tables()
            coursor=myobj.db.cursor()
            viewDelete=input("Enter name of view to be dropped")
            query="DROP VIEW {}".format(viewDelete)
            coursor.execute(query)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)
