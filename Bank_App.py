print("Welcome to ALX Microfinance Bank")
id_number = int(input("Please enter I.D Number: "))
while True:
    
    if id_number == 2003:
        print("Hello Mentor Blessing Malik, What would you like to do today?")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        balance = 2400
        option = int(input("Please Enter option number: "))
        if option == 1:
            print(f"Your current balance is {balance}")
        elif option == 2:
            withdrawal_amount = int(input("How much would you like to withdraw?: "))
            if withdrawal_amount > balance:
                print("Insufficient funds, please check your balance and try again")
            else:
                print(f"You have successfully withdrawn {withdrawal_amount}, your new balance is {balance - withdrawal_amount}")
        elif option == 3:
            deposit_amount = int(input("How much would you like to deposit?: "))
            print(f"You have successfully deposited {deposit_amount}, new balance is {deposit_amount + balance}")
        elif option == 4:
            print("Thank you for banking with ALX Microfinance Bank.")
            break
    elif id_number == 2005:
        print("Hello Mr. Nehemiah Kamolu, What would you like to do today?")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        balance = 1200
        option = int(input("Please Enter option number: "))
        if option == 1:
            print(f"Your current balance is {balance}")
        elif option == 2:
            withdrawal_amount = int(input("How much would you like to withdraw?: "))
            if withdrawal_amount > balance:
                print("Insufficient funds, please check your balance and try again")
            else:
                print(f"You have successfully withdrawn {withdrawal_amount}, your new balance is {balance - withdrawal_amount}")
        elif option == 3:
            deposit_amount = int(input("How much would you like to deposit?: "))
            print(f"You have successfully deposited {deposit_amount}, new balance is {deposit_amount + balance}")
        elif option == 4:
            print("Thank you for banking with ALX Microfinance Bank.")  
            break
    else:
        print("Unrecognised I.D number. The Program will close for security reasons. Please restart the program and enter your correct I.D number to continue")
        break

