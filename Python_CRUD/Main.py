'''
@Author: Sailesh Chauhan
@Date: 24-06-2021
@Last Modified time: 24-06-2021
@Title : To Perform CRUD operation in MySQL database using Python.
'''

from CRUD_Methods import CRUD_Methods


class main:

    operation=CRUD_Methods()

    switcher={
    '1':operation.new_entry,
    '2':operation.read_table,
    '3':operation.delete_entry
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"

    choice=''
    while(choice.lower()!='q'):
        print("==================CRUD Operation In MySQL====================")
        print('1.New Entry to STUDENT table\n2.Read entry from STUDENT table')
        print('3.Delete entry from STUDENT table')
        choice=input('Make your choice\n')
        
        print(switcher_to_call_Methods(choice,switcher))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')

        if(choice.lower()=='q'):
            print("Selected to exit Program")