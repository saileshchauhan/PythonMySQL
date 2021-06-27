'''
@Author: Sailesh Chauhan
@Date: 27-06-2021
@Last Modified time: 27-06-2021
@Title : This Script provide method for CRUD operation in MySQL Database using
         procedure.
'''

import logging
from random import choice
from CRUD_Methods import CRUD_Methods


class Main:

    def main():
        try:
            operation=CRUD_Methods()
            choice=''
            while(choice.lower()!='q'):
                print("==================CRUD Operation In MySQL====================")
                print('1.New Entry to STUDENT table\n2.Read entry from STUDENT table')
                print('3.Delete entry from STUDENT table\n4.Update entry of STUDENT')
                choice=input('Make your Selection\n')
                pass