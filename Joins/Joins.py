'''
@Author: Sailesh Chauhan
@Date: 28-06-2021
@Last Modified time: 28-06-2021
@Title : This Script have methods to implement inner join,left join
         right join,cross join in MySQL Database.
'''

import sys
sys.path.append(r"D:\PythonMySQL\Joins")
import LogConfig
import logging

from decouple import config
import mysql.connector

class Joins_Methods:

    def __init__(self):
        self.db=mysql.connector.connect(
                host=config('host'),
                user=config('user'),
                passwd=config('passwd'),
                database=config('database')
                )
    
    def inner_join(self):
        '''
        Description:
            Method implement inner join between two tables on id column.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycoursor=self.db.cursor()
            query="SELECT student.name,parents.parent_name from student inner join parents on student.id=parents.id"
            mycoursor.execute(query)
            for rows in mycoursor:
                print(rows)
        except Exception as ex:
            logging.critical(ex)
    
    def left_join(self):
        '''
        Description:
            Method implement left join between two tables on column id.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycoursor=self.db.cursor()
            query="SELECT student.name,parents.parent_name from student left join parents on student.id=parents.id"
            mycoursor.execute(query)
            for rows in mycoursor:
                print(rows)
        except Exception as ex:
            logging.critical(ex) 
    
    def right_join(self):
        '''
        Description:
            Method implement right join between two tables on column id.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycoursor=self.db.cursor()
            query="SELECT student.name,parents.parent_name from student right join parents on student.id=parents.id"
            mycoursor.execute(query)
            for rows in mycoursor:
                print(rows)
        except Exception as ex:
            logging.critical(ex)

    def cross_join(self):
        '''
        Description:
            Method implements cross join between two tables student and parents.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycoursor=self.db.cursor()
            query="SELECT student.name,parents.parent_name from student cross join parents"
            mycoursor.execute(query)
            for rows in mycoursor:
                print(rows)
        except Exception as ex:
            logging.critical(ex)

op=Joins_Methods()
