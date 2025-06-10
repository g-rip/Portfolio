#2d list to hold table orders
tables = [["TABLE 1 - ", 0],["TABLE 2 - ", 0],["TABLE 3 - ", 0],["TABLE 4 - ", 0],["TABLE 5 - ", 0],
["TABLE 6 - ", 0],["TABLE 7 - ", 0],["TABLE 8 - ", 0],["TABLE 9 - ", 0],["TABLE 10 - ", 0]]

#menu items stored as a dictionary
menu = {
    "Nachos": 5.50 , "Soup":4.95, 
    "Burger":10.50, "Brisket": 12.50, "Ribs":15.00,
    "Corn":2.50, "Fries":3.00, "Salad":3.25
}
#receives input from user to collect server name and checks that it only contains letters
def get_server_name():
    flag = True

    while flag:

        server_name = input('Please enter your name: ')

        if server_name.isnumeric() == True:
            print("Sorry you have not entered a recognised name.")
            flag = True

        else:
            server_name = "Server name: {}".format(server_name.capitalize())
            flag = False

    return server_name

#receives input from user for table number checks it is an integer and that it is within the correct range
def get_table_num():
    flag= True

    while flag:
            
        table_num = input('Enter table number:  ')

        try:
            int(table_num)
        except:
                
                    
            table_num = int(table_num)
            if table_num < 1 or table_num > 9:
                flag = False
            else:
                print("Table number must be between 1 and 10")

                flag = True

        return table_num

#gets input of required menu item from user and validates it
def get_menu_item():
    flag = True
    
    while flag:
        for key, value in menu.items():
            print(f"{key}: {value}")

        menu_item = input('Enter menu item. Type x if there are no more items to enter: ')
      
            
        

        if menu_item.isalpha() == False:
            print("Sorry you have not entered a valid menu item.")
            flag = True
        elif menu_item == "x" or menu_item == "X":
            flag = False
        elif menu_item.capitalize() not in menu:
            print("Sorry you have not entered a valid menu item.")
            flag = True
        else:
            menu_item = menu_item.capitalize()
            flag = False

    return menu_item

#gets quantity of item required and validates the input
def get_qty():
    flag= True

    while flag:
            
        qty = input('Enter quantity of item required:  ')

        try:
            int(qty)
        except:
            print("Sorry, quantity must be a whole number")
            flag = True
        else:
                qty = int(qty)
                if qty < 1: 
                    print("Quantity must be a positive number")
                    flag = True
                else:
                    flag = False

    return qty

#gets user input for discount to be applied
def get_discount_choice():
    flag = True

    while flag:

        
        print("")
        print("###############################################")
        print("######### Please choose a discount #########")
        print('## 1. Early Bird: Monday - Friday 5pm-7pm')
        print("## 2. Staff")
        print("## 3. No discount")
        print("")
        
        discount_choice = input("Select a discount to apply:")

        try:
            int(discount_choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            discount_choice = int(discount_choice)
            if discount_choice < 1 or discount_choice > 3:
                print("Discount option must be 1, 2 or 3 only")
                flag = True
            else:
                if discount_choice == 1:
                    discount = 15
                elif discount_choice == 2:
                    discount = 25
                else:
                    discount = 0
                
                flag = False

    return discount

enter_order = True

while enter_order:

    print("###############################################")
    print("#### Gurreb's BBQ order processing system  ####")
    print("###############################################")
    print("")
    print("############# Choose an option ################")
    print("")
    print("1. Enter customer order")
    print("2. Output bill")
    print("3. Exit")
    print("")
    
    main_choice = input('Enter option here:')
 #allows user to enter the customer's order   
    if main_choice == "1":
        server_name = get_server_name()
        table_num = get_table_num()
        tables[table_num].append(server_name)
        item_enter = True
        subtotal = 0
        tables[table_num-1].remove(0)

        while item_enter:
           
            item_choice = get_menu_item()

            if item_choice == "X" or item_choice == "x":
                tables[table_num -1 ].append(subtotal)
                item_enter = False
            else:
                quantity = get_qty()
                price = menu[item_choice]
                cost = price * quantity
                tables[table_num -1].append(item_choice)
                tables[table_num -1].append(quantity)
                tables[table_num -1].append(cost)
                subtotal = subtotal + cost

        flag = False
 
 #finds and outputs the required bill   
    elif main_choice == "2":
        table_num = get_server_num()
        discount = get_discount_choice()
        print(str(tables[table_num -1][0]))
        print(str(tables[table_num -1][1]))
        print("Summary of bill before discounts:")
        print(str(tables[table_num -1][2:-1]))
        print("Discount percentage applied to this bill = {} ".format(discount))
        subtotal = float(tables[table_num -1][-1])
        print("Subtotal before discount = £{}".format(subtotal))
        final_total = subtotal - (subtotal*discount)
        print("Final total after discount = £{}".format(final_total))
        flag = False
    
    elif main_choice == "3":
        exit()
    
    else:
        flag = True
