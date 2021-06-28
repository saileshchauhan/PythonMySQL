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
    '4':func.count,
    '5':func.max_functin,
    '6':func.min_marks,
    '7':func.avg_marks,
    '8':func.sum_marks,
    '9':func.current_date,
    '10':func.current_time,
    '11':func.current_timestamp,
    '12':func.date_diff,
    '13':func.upper_name,
    '14':func.reverse_name,
    '15':func.length_name
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3','4','5','6']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"

    choice=''
    while(choice.lower()!='q'):
        print("==================FUNCTIONS In MySQL====================")
        print('1.Read Tables\n2.Show Tables\n3.Order Table by Math Marks')
        print('4.Count name of student\n5.Max marks in Maths\n6.Min marks in Maths')
        choice=input('Make your choice\n')
        
        print(switcher_to_call_Methods(choice,switcher))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')

        if(choice.lower()=='q'):
            print("Selected to exit Program")