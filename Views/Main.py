'''
@Author: Sailesh Chauhan
@Date: 25-06-2021
@Last Modified time: 25-06-2021
@Title : To Perform CRUD operation in MySQL database using Python.
'''

from MySQL_Views import ViewFunction


class Main:

    func=ViewFunction()

    switcher={
    '1':func.read_view,
    '2':func.show_tables,
    '3':func.create_views,
    '4':func.drop_views
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3','4']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"

    choice=''
    while(choice.lower()!='q'):
        print("==================FUNCTIONS In MySQL====================")
        print('1.Read Views\n2.Show Table Schema\n3.Create Views.')
        print('4.Drop views')
        choice=input('Make your choice\n')
        
        print(switcher_to_call_Methods(choice,switcher))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')

        if(choice.lower()=='q'):
            print("Selected to exit Program")
