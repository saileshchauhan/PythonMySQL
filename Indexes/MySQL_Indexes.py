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

    