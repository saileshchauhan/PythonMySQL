'''
@Author: Sailesh Chauhan
@Date: 24-06-2021
@Last Modified time: 24-06-2021
@Title : To Perform CRUD operation in MySQL database using Python.
'''

from MySQL_Functions import Functions


class Main:
    
    func=Functions()

    switcher={
    '1':func.read_table,
    '2':func.show_tables,
    '3':func.order_by_marks,
    '4':func.count
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3','4']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"
