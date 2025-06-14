import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Get the highest interactions")
        print("### 3. display graph") 


        choice = input('Enter your number selction here: ')

        try:
            if int(choice) >= 1 and  int(choice) <= 3:
                return choice
            else:
                flag = True
                print('1')
            
        except:
            print("Sorry, you did not enter a valid option")
            flag = True


def average_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments")


        choice = input('Enter your number selction here: ')

        try:
            if int(choice) <= 3 and int(choice) >= 0:
                return choice
            else:
                raise
            
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice      

def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"  
    
    return avg_choice


def get_avg_data(avg_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    print("Here is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index
def highest(choice):
    df = pd.read_csv("Task4a_data.csv")
    extract =  df.groupby(['Post Type'], as_index=True)[choice].mean()
    #extract_no_index = extract.sort_values(by=[choice],ascending = False)
    #print(extract_no_index.head(5))
    
    extract.plot.pie(y= choice, autopct = '%1.1f%%')
    plt.title('Average for all posts')
    plt.show()

    #return extract_no_index
def plotting(dataframe):
    
    df = pd.read_csv("Task4a_data.csv")
    extract =  df.groupby(['Post Type'], as_index=True)[choice].mean()
    #extract_no_index = extract.sort_values(by=[choice],ascending = False)
    #print(extract_no_index.head(5))
def bar()
    df = pd.read_csv("Task4a_data.csv")
    extract =  df.groupby(['Post Type'], as_index=True)['Likes','Shares','Comments'].sum()
    plt.bar()

    
    


main_menu_choice = main_menu()
if main_menu_choice == "1":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))
if main_menu_choice == "2":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    highest(avg_choice)
if main_menu_choice == "3":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)

    
