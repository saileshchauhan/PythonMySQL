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
                if choice=='1':
                    name=input("Enter First Name of Student\n")
                    marks=input("Enter Marks of {} \n".format(name))
                    address=input("Enter address of {} \n".format(name))
                    gender=input("Enter gender of {} \n".format(name))
                    operation.new_entry(name,marks,address,gender)
                elif choice=='2':
                    operation.read_table()
                elif choice=='3':
                    operation.read_table()
                    id=input("Enter ID of the student to be deleted\n")
                    operation.delete_entry(id)
                elif choice=='4':
                    operation.read_table()
                    id=input("Enter ID of the student to be updated\n")
                    operation.update_entry(id)
                elif choice.lower()=='q':
                    print("Selected to exit Program")
                else:
                    print("Invalid input {} ".format(choice))
                print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
                choice=input('Enter your choice\n')
        except Exception as ex:
            logging.critical(ex)