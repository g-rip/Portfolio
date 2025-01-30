import datetime
import random
import string

def is_valid_name(name):
    return name.isalpha()

def password_gen():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation
    password = [random.choice(upper),
                random.choice(lower),
                random.choice(digit)]
    password += random.choices(lower + upper + special + digit, k=5)
    random.shuffle(password)
    return ''.join(password)

def making_ID(firstname, lastname, birth_date):
    if len(firstname) < 3:
        firstname = firstname + ('x' * (3 - len(firstname)))
    if len(lastname) < 3:
        lastname = lastname + ('x' * (3 - len(lastname)))
    userID = firstname[:3] + lastname[:3] + str(birth_date.year)
    return userID

print('Enter your date of birth')
current_date = datetime.date.today()

while True:
    try:
        date_of_birth = input("Enter your date of birth (format: DD-MM-YYYY): ")
        birth_date = datetime.datetime.strptime(date_of_birth, "%d-%m-%Y").date()
        age = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        if age < 18:
            print("You must be at least 18 years old!")
            continue
        if current_date < birth_date:
            print("The date cannot be in the future!")
            continue
        break
    except ValueError:
        print("Invalid format! Please try again!")
        pass

firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')
while not firstname.isalpha() or not lastname.isalpha() or firstname == "" or lastname == "":
    print("First name and last name should only contain alphabetic characters and cannot be empty.")
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')

print(f"Full name: {firstname} {lastname}")
print(f'and your birthday is {birth_date}')

userID = making_ID(firstname, lastname, birth_date)
password = password_gen()

print(f"Generated User ID: {userID}")
print(f'Temp password Generated: {password}')
