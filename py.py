file = open('employees.txt', 'a+')

def get_valid_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Please enter a valid name.")

employee_check = get_valid_int('''Would you like to check an employee, add an employee, or edit sales?
Check employee = 1
Add employee = 2
Edit employee sales = 3
''', 1, 3)

if employee_check == 2:
    num_employees = get_valid_int('How many employees are working this week? ', 3, 6)
    
    for i in range(num_employees):
        employee_name_add = get_valid_string('What is the name of the employee you would like to add? ')
        employee_car_add = get_valid_int(f'How many cars has {employee_name_add} sold? ')
        file.write(f'Employee: {employee_name_add}, Cars Sold: {employee_car_add}\n')
    print('Data added successfully.')

elif employee_check == 1:
    employee_name_check = get_valid_string('Enter the employee name to check how many cars they have sold: ')
    file.seek(0) 
    content = file.readlines()
    found = False
    for line in content:
        if employee_name_check in line:
            name, cars_sold = line.split(', Cars Sold: ')
            print(f'{name} has sold {cars_sold.strip()} cars.')
            found = True
            break
    if not found:
        print(f'Employee {employee_name_check} not found in the database.')

elif employee_check == 3:
    employee_name_edit = get_valid_string('Enter the employee name whose sales you want to edit: ')
    new_sales = get_valid_int(f'Enter the new number of cars sold by {employee_name_edit}: ')
    
    file.seek(0)
    content = file.readlines()
    found = False
    for i, line in enumerate(content):
        if employee_name_edit in line:
            name, _ = line.split(', Cars Sold: ')
            content[i] = f'Employee: {name}, Cars Sold: {new_sales}\n'
            found = True
            break
    if found:
        file.seek(0)
        file.truncate()
        file.writelines(content)
        print(f'{employee_name_edit}\'s sales have been updated to {new_sales} cars.')
    else:
        print(f'Employee {employee_name_edit} not found in the database.')

file.close()
