'''
@Author: Sailesh Chauhan
@Date: 25-06-2021
@Last Modified time: 25-06-2021
@Title : To Perform Indexes related operation to create,show and drop indexes.
'''

from MySQL_Indexes import IndexFunction

class Main:

    func=IndexFunction()

    switcher={
    '1':func.read_index,
    '2':func.show_tables,
    '3':func.create_indexes,
    '4':func.drop_indexes
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3','4']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"

    
    choice=''
    while(choice.lower()!='q'):
        print("==================FUNCTIONS In MySQL====================")
        print('1.Read Indexes\n2.Show Table Schema\n3.Create Indexes.')
        print('4.Drop Indexes')
        choice=input('Make your choice\n')
        
        print(switcher_to_call_Methods(choice,switcher))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')

        if(choice.lower()=='q'):
            print("Selected to exit Program")