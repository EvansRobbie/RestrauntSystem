import time
import function
import datetime
import re
# create a menu list  and a price list
food = ['Noodles', 'Sandwich', 'Dumpling', 'Muffins', 'Pasta', 'Pizza']
prices = [2, 4, 6, 8, 10, 20]
myOrder = []
priceList = []
myOrders = []
pricesList = []

counter = 0
total = 0

def username_list():
    # create an empty list to append the details keyed in
    username_list=[]
    # create a csv or txt file where user  signup details will be stored
    with open('signup_info.csv','r') as f:
        for line in f :
            username_list.append(line.split(',')[0])
        return username_list

def user_input():
    user_input = str(input('Enter X to to start the signup process again:'))
    if user_input.lower() == 'x':
        signup()



def signup():
    start = ''
    while start == '':
        username = input("Enter a Username: ")
        if username == '':
            print('username can\'t be blank')
            user_input()
        for user in username_list():
            while user == username:
                username = input("Username Exists, Try Again: ")

        password = input("Please Enter you password: ")
        confirm_password = input("Please re-enter your password for confirmation: ")
        # password confirmation and authentication
        # TODO hash password
        if password == '':
            print('password can\'t be blank')
            user_input()
        elif password != confirm_password:
            print('Password do not match')
            user_input()

        elif not re.search('[A-Z]', password):
            print('password must have a capital letter')
            user_input()

        elif not re.search('[a-z]', password):
            print('password must have small letters')
            user_input()

        elif not re.search('[0-9]', password):
            print('password must have numeric numbers')
            user_input()

        elif not re.search('[_@$]', password):
            print('password must have special characters')
            user_input()
        address = input("Please enter you address ")
        if address == '':
            addres = input('Address maybe required for delivery purposes, Are you sure you want to leave it blank?y/n: ')
            if addres.lower() == 'y':
                pass
            elif addres.lower() == 'n':
                address = input("Please enter you address ")
            else:
                print('invalid response')
                signup()
        phone_number = input("Please enter your phone number ")

        if phone_number == '':
            print('phone number can\'t be blank')

        elif len(phone_number) != 10:
            print('phone number must be equal to 10 digits ')
            user_input()
        year = int(input("Please enter Year of birth "))
        # first get the current year - the year of birth, pass date of birth later
        x = datetime.datetime.now()
        age = x.year - year
        if age< 18:
            print('You are' + ' '+ str(age) + 'Years old')
            print('Too young.  User must be 18 years and above')
            break
        else:
            print('You are' + ' '+ str(age) + 'Years old')
            dob = input('Please Enter you date of birth i.e DD/MM/YYYY: ')


        function.sign_up(username,confirm_password,address,phone_number,dob)
        print('Account successfully registered. Please login!!')
        login()



def login():
    start = ''
    while start == '':
        login_username = input("Enter Your Username: ")
        while login_username not in username_list():
            print('Username Does not Exist.')
            user_input = input("Type R to retry and X to exit: ")
            if user_input.lower() == "r":
                login_username = input("Enter Your Username: ")
            if user_input.lower() == 'x':
                break
        if login_username not in username_list():
            print("Invalid Session \n\n")
            start = ""
        else:
            no = username_list().index(login_username)
            password = input("Enter a Password: ")
            function.extract_matrix(login_username, password, no)
            start = ""


def homepage():
    starthomepage = ''
    while starthomepage == "" :
        print('***** Home Page ******')
        print('Please Enter 2.1 to start ordering')
        print('please enter 2.2 to Print statistics')
        print('Please enter 2.3 to Logout')
        choice = float(input('Enter response:'))
        if choice == 2.1:
            orderingpage()
        elif choice == 2.2:
            statistics()
        elif choice == 2.3:
            logout()
        else:
            print('invalid response ')
            starthomepage = ""

def orderingpage():
    startorderingpage = ''
    while startorderingpage == "":
        print('***** Ordering Page ******')
        print('Please Enter 1 fo Dine in.')
        print('please enter 2 for order online')
        print('Please enter 3 to go to login page')
        choice = int(input('Enter response:'))
        if choice == 1:
            dinein()
        elif choice == 2:
            onlineorder()
        elif choice == 3:
            login()
        else:
            print('invalid response ')
            startorderingpage = ""
def statistics():
    global orderid, date, ordertype, totalPaid
    print('Please Enter the options to Print the statistics')
    print('1 - All Dine in orders')
    print('2 - All Pick up in orders')
    print('3 - All Deliveries')
    print('4 - Total  amount spent on all orders')
    print('5 - To go to previous Menu')

    order = input('Do you want to print or view the statistics?y/n:')
    if order.lower() == 'n':
        exit()
    else:
        print('Thank You')

    nextOrder = True
    while nextOrder == True:
        choice = int(input('Choose the receipt of transaction you want to  want to print'))

        if choice == 1:
            ordertype = "Dine in"
            orderid = 1
            date =  time.ctime()
            print('Here is your Dine in order Transaction history')
            # find the 10% service fee and add it to the initial total
            paidPercentage = 10 / 100 * total
            totalPaid = paidPercentage + total
            print('Order Id:{}\n Date:{}\nOrder Type:{}\n Order Amount:{}'.format(orderid, date, ordertype, str(totalPaid)))

        elif choice == 2:
            ordertype = "Pick up"
            orderid = 2
            date = time.ctime()
            print('Here is your Pick up order Transaction history')
            print('    ')
            print('Order Id:{}\n Date:{}\nOrder Type:{}\n Order Amount:{}'.format(orderid, date, ordertype, str(total)))
        elif choice == 3:
            ordertype = "Delivery"
            orderid = 3
            date = time.ctime()
            print('Here is your Delivery Order transaction History')
            print('  ')
            #The extra delivery cost is paid upon delivery and varies with distance
            print('Order Id:{}\n Date:{}\nOrder Type:{}\n Order Amount:{}'.format(orderid,date,ordertype,str(total)))
        elif choice == 4:
            totaltransaction = totalPaid+total+total
            print('Total amount spent on all order is:' + str(totaltransaction))
        elif choice == 5:
            homepage()
        else:
            print('Not on Menu')
        orderAgain = input('Do you want to print another transaction?y/n')
        if orderAgain == 'y':
            # the program only continue as long as the next order is true
            # when set to false, the programs terminates and records the orders and their prices
            nextOrder = True
        else:
            nextOrder = False

def logout():
    logouts = ''
    while logouts == '':
        logout = input('Are you sure you want to Logout?y/n')
        if logout.lower() == 'y':
            break
        elif logout.lower() == 'n':
            homepage()
        else:
            print('invalid response')
            logouts = ''
def onlineorder():
    onlineorder = ''
    while onlineorder == "":
        print('***** Ordering Page ******')
        print('Enter 1 for pickup.')
        print('Enter 2 for home delivery')
        print('Enter 3 to go to previous menu')
        choice = int(input('Enter response:'))
        if choice == 1:
            pickup()
        elif choice == 2:
            homedelivery()
        elif choice == 3:
            orderingpage()
        else:
            print('invalid response ')
            onlineorder = ""

def homedelivery():
    #counter = 0
    #total = 0
    global counter, total
    print('***** Food Menu *********')
    print('ID      Name     Price ')
    print('1      Noodles    AUD 2 ')
    print('2      Sandwich   AUD 4 ')
    print('3      Dumpling   AUD 6 ')
    print('4      Muffins    AUD 8 ')
    print('5      Pasta      AUD 10 ')
    print('6      Pizza      AUD 20 ')
    print('7      Checkout    ')

    print('***** Place you order *********')
    print('Enter 1 for Noodles')
    print('Enter 2 for sandwich')
    print('Enter 3 for Dumpling')
    print('Enter 4 for  muffins')
    print('Enter 5 for Pasta')
    print('Enter 6 for Pizza')
    print('Enter 7 for Checkout')
    print('Enter 8 to go back to main menu')

    order = input('Can I take your order?y/n')
    if order.lower() == 'n':
        exit()
    else:
        print('Thank you')

    nextOrder = True
    while nextOrder == True:
        choice = int(input('Please choose your item:'))
        if choice == 1:
            myOrders.append(food[0])
            pricesList.append(prices[0])
            counter = counter + 1
            total = total + (prices[0])

        elif choice == 2:
            myOrders.append(food[1])
            pricesList.append(prices[1])
            counter = counter + 1
            total = total + (prices[1])
        elif choice == 3:
            myOrders.append(food[2])
            pricesList.append(prices[2])
            counter = counter + 1
            total = total + (prices[2])
        elif choice == 4:
            myOrders.append(food[3])
            pricesList.append(prices[3])
            counter = counter + 1
            total = total + (prices[3])
        elif choice == 5:
            myOrders.append(food[4])
            pricesList.append(prices[4])
            counter = counter + 1
            total = total + (prices[4])
        elif choice == 6:
            myOrders.append(food[5])
            pricesList.append(prices[5])
            counter = counter + 1
            total = total + (prices[5])
        elif choice == 7:
            checkout = True
            while checkout == True:
                completeOrder = input('Please enter Y to proceed to checkout or Enter N to cancel order')
                if completeOrder.lower() == 'y':
                    checkout = False
                    print('Thank you for confirmation, Your order has been confirmed')

                else:
                    checkout = True
                    print('Your order has been Canceled')
                    onlineorder()
        elif choice == 8:
            onlineorder()
        else:
            print('Not in menu')
        orderAgain = input('Do you want to place another order?y/n')
        if orderAgain.lower() == 'y':
            nextOrder = True
        else:
            nextOrder = False

    y = 0
    print('Here is your order')
    print('    ')
    print('**********')
    print('   ')
    print('A fix charges for delivery based on the distance')
    print('More than 0 - 2 kms    AUD 5')
    print('More than 2 - 5 kms    AUD 10')
    print('More than 5 kms  No delivery')
    print('  ')
    while y < counter:
        print('Item:' + myOrders[y])
        print('cost: AUD' + ' ' + str(pricesList[y]))
        y = y + 1

    print('Total amount to be paid is: AUD' + ' ' + str(total) + ' '+'and there will be an additional charges for delivery')
    homepage()
def dinein():

    counter = 0
    total = 0

    print('***** Food Menu *********')
    print('ID      Name     Price ')
    print('1      Noodles    AUD 2 ')
    print('2      Sandwich   AUD 4 ')
    print('3      Dumpling   AUD 6 ')
    print('4      Muffins    AUD 8 ')
    print('5      Pasta      AUD 10 ')
    print('6      Pizza      AUD 20 ')
    print('7      Checkout    ')

    print('***** Place you order *********')
    print('Enter 1 for Noodles')
    print('Enter 2 for sandwich')
    print('Enter 3 for Dumpling')
    print('Enter 4 for  muffins')
    print('Enter 5 for Pasta')
    print('Enter 6 for Pizza')
    print('Enter 7 for Checkout')

    order = input('Can I take your Order?y/n:')
    if order.lower() == 'n':
        exit()
    else:
        print('Thank You')

    nextOrder = True
    while nextOrder == True:
        choice = int(input('Choose the meal you want to take:'))

        if choice == 1:
            myOrder.append(food[0])
            priceList.append(prices[0])
            counter = counter + 1
            total = total + (prices[0])
        elif choice == 2:
            myOrder.append(food[1])
            priceList.append(prices[1])
            counter = counter + 1
            total = total + (prices[1])
        elif choice == 3:
            myOrder.append(food[2])
            priceList.append(prices[2])
            counter = counter + 1
            total = total + (prices[2])
        elif choice == 4:
            myOrder.append(food[3])
            priceList.append(prices[3])
            counter = counter + 1
            total = total + (prices[3])
        elif choice == 5:
            myOrder.append(food[4])
            priceList.append(prices[4])
            counter = counter + 1
            total = total + (prices[4])
        elif choice == 6:
            myOrder.append(food[5])
            priceList.append(prices[5])
            counter = counter + 1
            total = total + (prices[5])
        elif choice == 7:
            drinksmenu()
        elif choice == 8:
            onlineorder()
        else:
            print('Not on Menu')
        orderAgain = input('Do you want to add another meal to your Order?y/n')
        if orderAgain == 'y':
            nextOrder = True
        else:
            nextOrder = False

    x = 0
    print('Here is your order')
    print('    ')
    print('**********')
    while x < counter:
        print('Item:' + myOrder[x])
        print('cost: AUD' + ' ' + str(priceList[x]))
        x = x + 1
    paidPercentage = 10 / 100 * (total)
    totalPaid = paidPercentage + total
    print('The total cost to be paid is: Aud' + ' '+ str(totalPaid) + 'including AUD:' + ' '+ str(paidPercentage) + 'for service Charges')


def drinksmenu():
    drinks= ['Coffee','coldDrink','Milkshake']
    prices = [2,4,6]
    myOrder = []
    priceList = []
    counter = 0
    total = 0

    print('***** Drinks Menu *********')
    print('ID      Name     Price ')
    print('1      Coffee      AUD 2 ')
    print('2      ColdDrink   AUD 4 ')
    print('3      Milkshake   AUD 6 ')
    print('4      Checkout    ')

    print('***** Place you order *********')
    print('Enter 1 for Coffee')
    print('Enter 2 for ColdDrink')
    print('Enter 3 for milkshake')
    print('Enter 4 for Checkout')

    order = input('Can I take your Order?y/n:')
    if order.lower() == 'n':
        exit()
    else:
        print('Thank You')

    nextOrder = True
    while nextOrder == True:
        choice = int(input('Choose the meal you want to take:'))

        if choice == 1:
            myOrder.append(drinks[0])
            priceList.append(prices[0])
            counter = counter + 1
            total = total + (prices[0])
        elif choice == 2:
            myOrder.append(drinks[1])
            priceList.append(prices[1])
            counter = counter + 1
            total = total + (prices[1])
        elif choice == 3:
            myOrder.append(drinks[2])
            priceList.append(prices[2])
            counter = counter + 1
            total = total + (prices[2])

        elif choice == 4:
            checkout = True
            while checkout == True:
                completeOrder = input('Please enter Y to proceed to checkout or Enter N to cancel order')
                if completeOrder.lower() == 'y':
                    checkout = False
                    print('Thank you for confirmation, Your order has been confirmed')

                else:
                    checkout = True
                    print('Your order has been Canceled')
                    onlineorder()
        elif choice == 8:
            onlineorder()
        else:
            print('Not on Menu')
        orderAgain = input('Do you want to add another meal to your Order?y/n')
        if orderAgain == 'y':
            nextOrder = True
        else:
            nextOrder = False

    x = 0
    print('Here is your order')
    print('    ')
    print('**********')
    while x < counter:
        print('Item:' + myOrder[x])
        print('cost: AUD' + ' ' + str(priceList[x]))
        x = x + 1
    print('The total cost to be paid is: Aud' + str(total))
def pickup():
    counter = 0
    total = 0

    print('***** Food Menu *********')
    print('ID      Name     Price ')
    print('1      Noodles    AUD 2 ')
    print('2      Sandwich   AUD 4 ')
    print('3      Dumpling   AUD 6 ')
    print('4      Muffins    AUD 8 ')
    print('5      Pasta      AUD 10 ')
    print('6      Pizza      AUD 20 ')
    print('7      Checkout    ')

    print('***** Place you order *********')
    print('Enter 1 for Noodles')
    print('Enter 2 for sandwich')
    print('Enter 3 for Dumpling')
    print('Enter 4 for  muffins')
    print('Enter 5 for Pasta')
    print('Enter 6 for Pizza')
    print('Enter 7 for Checkout')

    order = input('Can I take your Order?y/n:')
    if order.lower() == 'n':
        exit()
    else:
        print('Thank You')

    nextOrder = True
    while nextOrder == True:
        choice = int(input('Choose the meal you want to take:'))

        if choice == 1:
            myOrder.append(food[0])
            priceList.append(prices[0])
            counter = counter + 1
            total = total + (prices[0])
        elif choice == 2:
            myOrder.append(food[1])
            priceList.append(prices[1])
            counter = counter + 1
            total = total + (prices[1])
        elif choice == 3:
            myOrder.append(food[2])
            priceList.append(prices[2])
            counter = counter + 1
            total = total + (prices[2])
        elif choice == 4:
            myOrder.append(food[3])
            priceList.append(prices[3])
            counter = counter + 1
            total = total + (prices[3])
        elif choice == 5:
            myOrder.append(food[4])
            priceList.append(prices[4])
            counter = counter + 1
            total = total + (prices[4])
        elif choice == 6:
            myOrder.append(food[5])
            priceList.append(prices[5])
            counter = counter + 1
            total = total + (prices[5])
        elif choice == 7:
            drinksmenu()
        elif choice == 8:
            onlineorder()
        else:
            print('Not on Menu')
        orderAgain = input('Do you want to add another meal to your Order?y/n')
        if orderAgain == 'y':
            nextOrder = True
        else:
            nextOrder = False

    x = 0
    print('Here is your order')
    print('    ')
    print('**********')
    while x < counter:
        print('Item:' + myOrder[x])
        print('cost: AUD' + ' ' + str(priceList[x]))
        x = x + 1

    print('The total cost to be paid is: AUD' + ' ' + str(total))




