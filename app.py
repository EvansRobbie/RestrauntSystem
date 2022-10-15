import function
import pages
import re

start = ""

Username_List = function.username_list()


while start == "" :
    print('***** Restaurant System ******')
    print('Please Enter 1 for sign up')
    print('please enter 2 to Login')
    print('Please enter 3 to exit')
    choice = int(input('Enter response:'))
    if choice == 1:
        pages.signup()
    elif choice == 2:
        pages.login()
    elif choice == 3:
        break
    else:
        print('invalid response ')
        start = ""