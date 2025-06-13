import pandas as pd
import datetime
import matplotlib.pyplot as plt

# The menu() function generates the UI that accepts and validates user choice
def menu():
    while True:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling (GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print('7. Would you like to convert graphs')
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-7): ")

        try:
            menu_choice = int(menu_choice)
            if 1 <= menu_choice <= 7:
                return menu_choice
            else:
                print("Sorry, you did not enter a valid choice.")
        except ValueError:
            print("Sorry, you did not enter a valid choice.")

# Function to get the currency pair based on menu choice
def get_currency(menu_choice):
    currencies = {
        1: 'GBP - EUR',
        2: 'EUR - GBP',
        3: 'GBP - AUD',
        4: 'AUD - GBP',
        5: 'GBP - JPY',
        6: 'JPY - GBP'}
    return currencies.get(menu_choice)

# Function to read CSV and plot the conversion graph
def display_conversion_graph(menu_choice_for_graph, df_filtered):
    # Assuming the df_filtered data frame is already filtered based on the selected date range
    X = df_filtered['Date']  # Dates in the selected range
    
    if menu_choice_for_graph == 1:  # GBP to EUR
        Y = df_filtered['GBP - EUR']
        plt.plot(X, Y)
        plt.title('GBP to EUR Conversion Rate')
        plt.ylabel('GBP to EUR Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 2:  # EUR to GBP
        Y = df_filtered['EUR - GBP']
        plt.plot(X, Y)
        plt.title('EUR to GBP Conversion Rate')
        plt.ylabel('EUR to GBP Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 3:  # GBP to AUD
        Y = df_filtered['GBP - AUD']
        plt.plot(X, Y)
        plt.title('GBP to AUD Conversion Rate')
        plt.ylabel('GBP to AUD Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 4:  # AUD to GBP
        Y = df_filtered['AUD - GBP']
        plt.plot(X, Y)
        plt.title('AUD to GBP Conversion Rate')
        plt.ylabel('AUD to GBP Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 5:  # GBP to JPY
        Y = df_filtered['GBP - JPY']
        plt.plot(X, Y)
        plt.title('GBP to JPY Conversion Rate')
        plt.ylabel('GBP to JPY Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 6:  # JPY to GBP
        Y = df_filtered['JPY - GBP']
        plt.plot(X, Y)
        plt.title('JPY to GBP Conversion Rate')
        plt.ylabel('JPY to GBP Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 7:  # GBP to USD
        Y = df_filtered['GBP - USD']
        plt.plot(X, Y)
        plt.title('GBP to USD Conversion Rate')
        plt.ylabel('GBP to USD Rate')
        plt.xlabel('Dates')
    elif menu_choice_for_graph == 8:  # USD to GBP
        Y = df_filtered['USD - GBP']
        plt.plot(X, Y)
        plt.title('USD to GBP Conversion Rate')
        plt.ylabel('USD to GBP Rate')
        plt.xlabel('Dates')

    plt.xticks(rotation=60)
    plt.show()


# Function to get the conversion rate for a given date
def get_conversion_rate(df):
    oldest, latest = df["Date"].iloc[0], df["Date"].iloc[-1]
    while True:
        try:
            date_input = input(f"Enter Date between {oldest} & {latest} (dd/mm/yyyy): ")
            valid_date = datetime.datetime.strptime(date_input, '%d/%m/%Y')
            oldest = datetime.datetime.strptime(oldest, '%d/%m/%Y')
            latest = datetime.datetime.strptime(latest, '%d/%m/%Y')
            if oldest <= valid_date <= latest:
                mask = (df["Date"] == valid_date.strftime('%d/%m/%Y'))
                df_filtered = df[mask]
                if not df_filtered.empty:
                    return df_filtered
                else:
                    print("Invalid Date. Try again.")
            else:
                print(f"Please enter a date between {oldest} and {latest}.")
        except ValueError:
            print("Invalid date format. Try Again.")

# Function to get the amount to convert
def get_amount_to_convert():
    while True:
        conversion_amount = input("Please enter the amount you wish to convert: ")
        try:
            conversion_amount = float(conversion_amount)
            if conversion_amount > 0:
                return conversion_amount
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Sorry, you must enter a numerical value.")

# Function to perform the conversion
def perform_conversion(currency, conversion_amount, conversion_rate):
    amount_received = round(conversion_amount * conversion_rate, 2)
    print(f"##################################")
    print(f"You are converting {conversion_amount} from {currency[0:3]}")
    print(f"You will receive {amount_received} in {currency[6:9]}")
def get_dates_for_graphs():
    df = pd.read_csv("Task4a_data.csv")  # Load the dataset
    oldest, latest = df['Date'].iloc[0], df['Date'].iloc[-1]  # Get the first and last available dates
    
    while True:
       try:
           df = 

   
    conversion_rate = round(df[currency].iloc[-1],2)
def menu_for_graphs():
    while True:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Would you like to see graph for GBP to EUR ")
        print("2. Would you like to see graph for EUR to GBP")
        print("3. Would you like to see graph for GBP to AUD")
        print("4. Would you like to see graph for AUD to GBP")
        print("5. Would you like to see graph for GBP to JPY")
        print("6. Would you like to see graph for JPY to GBP")
        print("7. Would you like to see graph for GBP to USD")
        print("8. Would you like to see graph for USD to GBP")
        print("######################################################")

        menu_choice_for_graphs = input("Please enter the number of your choice (1-8): ")

        try:
            menu_choice_for_graphs = int(menu_choice_for_graphs)
            if 1 <= menu_choice_for_graphs <= 8:
                return menu_choice_for_graphs
            else:
                print("Sorry, you did not enter a valid choice.")
        except ValueError:
            print("Sorry, you did not enter a valid choice.")

# --------------------- Main --------------------- 
# Function called and sets menu choice to the value returned by menu()

menu_choice = menu()

if menu_choice < 7:  # For all conversions except graphs
    # Load the data
    df = pd.read_csv('Task4a_data.csv')
    # Get the conversion rate for the date input
    df_filtered = get_conversion_rate(df)

    # Get the amount to convert
    conversion_amount = get_amount_to_convert()

    # Get the conversion rate
    if menu_choice == 1:  # GBP to EUR
        conversion_rate = df_filtered['GBP - EUR'].iloc[0]
    elif menu_choice == 2:  # EUR to GBP
        conversion_rate = df_filtered['EUR - GBP'].iloc[0]
    elif menu_choice == 3:  # GBP to AUD
        conversion_rate = df_filtered['GBP - AUD'].iloc[0]
    elif menu_choice == 4:  # AUD to GBP
        conversion_rate = df_filtered['AUD - GBP'].iloc[0]
    elif menu_choice == 5:  # GBP to JPY
        conversion_rate = df_filtered['GBP - JPY'].iloc[0]
    elif menu_choice == 6:  # JPY to GBP
        conversion_rate = df_filtered['JPY - GBP'].iloc[0]
    
    # Perform the conversion
    perform_conversion(currency, conversion_amount, conversion_rate)

elif menu_choice == 7:  # If user chooses to see graphs
    menu_choice_for_graph = menu_for_graphs()
    get_dates_for_graphs()# Get the graph menu choice
    display_conversion_graph(menu_choice_for_graph)  # Display the corresponding graph
