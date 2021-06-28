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
        '''
        Description:
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

    def read_table(self):
        '''
        Description:
            Method reads all row of table.
        '''
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
        Description:
            Method implement query to get all tables in Database.
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
        Description:
            Method performs function to order students by maths marks.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT * FROM STUDENT ORDER BY MATH_MARKS"
            coursor.execute(query)
            for row in coursor:
                print(row)
        except Exception as ex:
            logging.critical(ex)

#-----------------------------NUMERIC FUNCTIONS -------------------------#

    def count(myobj):
        '''
        Description:
            Method performs function to get count marks in maths column.
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
    
    def max_functin(myobj):
        '''
        Description:
            Method performs function to get maximum marks in maths column.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT MAX(MATH_MARKS) FROM STUDENT"
            coursor.execute(query)
            for row in coursor:
                print("Maximum marks obtained by Students in Math ",row)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def min_marks(myobj):
        '''
        Description:
            Method performs function to get minimum marks in maths column.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT MIN(MATH_MARKS) FROM STUDENT"
            coursor.execute(query)
            for row in coursor:
                print("Minimum marks obtained by Students in Math ",row)
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex) 

    
    def avg_marks(myobj):
        '''
        Description:
            Method use average function AVG() to get average marks in maths
            group by gender.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT GENDER,AVG(MATH_MARKS) FROM STUDENT GROUP BY GENDER"
            coursor.execute(query)
            for row in coursor:
                print("Gender {}  Average of maths marks {} ".format(row[0],row[1]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def sum_marks(myobj):
        '''
        Description:
            Method use sum function SUM() to get sum of marks in maths
            group by gender.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT GENDER,SUM(MATH_MARKS) FROM STUDENT GROUP BY GENDER"
            coursor.execute(query)
            for row in coursor:
                print("Gender {}  Sum of Maths marks {} ".format(row[0],row[1]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

#------------------------------Date_Time_Function-----------------------------------#
    def current_date(myobj):
        '''
        Description:
            Method use CURRENT_DATE() function to get current date.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT CURRENT_DATE()"
            coursor.execute(query)
            for row in coursor:
                print("Current Date in YYYY-MM-DD {} ".format(row[0]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def current_time(myobj):
        '''
        Description:
            Method use CURRENT_TIME() function to get current time.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT CURRENT_TIME()"
            coursor.execute(query)
            for row in coursor:
                print("Current Time {} ".format(row[0]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)
    
    def current_timestamp(myobj):
        '''
        Description:
            Method use CURRENT_TIMESTAMP() function to get current time stamp.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT CURRENT_TIMESTAMP()"
            coursor.execute(query)
            for row in coursor:
                print("Current Time Stamp {} ".format(row[0]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)
    
      
    def date_diff(myobj):
        '''
        Description:
            Method use DATEDIFF() function to get difference between two date columns.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT `name`,datediff(`DateOfTransfer`,`DateOfAddmission`) from student"
            coursor.execute(query)
            for row in coursor:
                print("Student {} Stayed for {} days in School".format(row[0],row[1]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

#-----------------------------String_Function----------------------------------------------#

    def upper_name(myobj):
        '''
        Description:
            Method use UPPER() function to get Name of students in upper Case.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT upper(name) from student"
            coursor.execute(query)
            print("Student Name in Upper Case")
            for row in coursor:
                print(" {} ".format(row[0]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)

    def reverse_name(myobj):
        '''
        Description:
            Method use REVERSE() to reverse name of student.
        '''
        try:
            coursor=myobj.db.cursor()
            query="SELECT reverse(name),reverse(Address) from student"
            coursor.execute(query)
            print("Student name and address in reverse order")
            for row in coursor:
                print(" {}  {} ".format(row[0],row[1]))
            logging.info(coursor.close())
        except Exception as ex:
            logging.critical(ex)   