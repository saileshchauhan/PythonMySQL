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