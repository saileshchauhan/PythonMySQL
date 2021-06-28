'''
@Author: Sailesh Chauhan
@Date: 28-06-2021
@Last Modified time: 28-06-2021
@Title : This Script have methods to implement inner join,left join
         right join,cross join in MySQL Database.
'''

from Joins import Joins_Methods


class Main:

    join=Joins_Methods()
    
    switcher={
    '1':join.inner_join,
    '2':join.left_join,
    '3':join.right_join,
    '4':join.cross_join
    }

    def switcher_to_call_Methods(choice,switcher):
        if(choice in ['1','2','3','4']):
            function=switcher.get(choice)
            return function()
        return "Invalid Input"

    choice=''
    while(choice.lower()!='q'):
        print("==================JOINS In MySQL====================")
        print('1.Inner join two tables STUDENT and PARENTS.\n2.Left join TABLE STUDENT and PARENTS')
        print('3.Right join Tables STUDENT and PARENTS\n4.Cross join Tables STUDENT and PARENTS')
        choice=input('Make your choice\n')
        
        print(switcher_to_call_Methods(choice,switcher))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')

        if(choice.lower()=='q'):
            print("Selected to exit Program")