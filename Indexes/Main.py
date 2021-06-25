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