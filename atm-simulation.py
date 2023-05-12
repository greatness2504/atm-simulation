import random
import string


def no_user_account():
    print("let's create your account: ")
    user_info = {}
    info = ["first name", "last name", "single/married", "gender", "phone number", "email address"]
    for key in info:
        value = input(f"what is your '{key}': ")
        user_info[key] = value
    user_account_number = "".join(random.choices(string.digits,k=10))
    user_account_pin = input("Enter a 4 digit pin for your account:\n")
    pin_length = len(user_account_pin)
    if pin_length != 4:
        print("sorry it has to be 4 digit only!")
    else:
        atm_menu()
        atm_options()
        

# define a function for the atm menu
def atm_menu():
    print("Welcome to ATM services, what would you like to do today")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    
def atm_options():
    balance = 0
    choice = int(input("Pick a number: "))
            
        # to check the account balance of the user
    if choice == 1:
        print(f"Your account balance is ${balance: .2f}")

        # to deposit some money
    elif choice == 2:
        amount = float(input("Enter deposit amount: $"))
        balance += amount
        print(f"Deposited: ${amount: .2f}")
        print(f"Current balance is: ${balance: .2f}")
            
        #  to withdraw somme money
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
        
        # if the amount you want to withdraw is more than your balance
        if withdraw_amount > balance:
            print("Insufficient Balance!!!")
            retry = input("Would you like another transaction? (yes or no)").lower().strip()
            if retry == "yes":
                atm_menu()
                atm_options()
            else:
                print("Thanks for using our atm services")
            
        # if the amount you want to withdraw is more than your balance
        else:
            balance -= withdraw_amount
            print(f"Withdrawn: ${withdraw_amount}")
            print(f"Current balance is: ${balance}")
                
        # if the user input another number
    else:
        print("Invalid choice!!!")
        
# if the user has an account call this function
def yes_user_account():
    while True:
        # Display menu
        atm_menu()
        atm_options()
        
        # ask the user if they would like to perform another transaction
        retry = input("Would you like another transaction? (yes or no)").lower().strip()
        if retry == "yes":
            atm_menu()
            atm_options()
        else:
            print("Thanks for using our atm services")
            break


# confirm if the user has an account or not
user_account = input("Do you have  an account with us(yes/no):\n").lower().strip()
      
# if the user does not have an account call the function to create a account for the user
if user_account == "no":
    no_user_account()
    
# if the user has an account proceed with the atm services function
elif user_account == "yes":
    yes_user_account()
            
# if the user enters anything apart from yes or no            
else:
    print("Invalid, pick only yes or no")