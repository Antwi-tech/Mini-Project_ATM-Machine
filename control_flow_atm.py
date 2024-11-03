depositors_balance = 0

#Function to check Balance
   
def check_balance():
    global depositors_balance
    authenticate_user(user_pin)
    print(f"Current Balance: ${depositors_balance:.2f}\n")

#Deposit funds function
def deposit_funds():
    global depositors_balance

    print(f'Your account is ${depositors_balance:.2f}\n')
    amount = float(input('Enter an amount to deposit: '))
    
    if amount > 0:
        print('Enter your pin to proceed')
        authenticate_user(user_pin)
        depositors_balance += amount
        print(f'Successfully deposited ${amount:.2f}\nCrrent Balance: ${depositors_balance:.2f}\n')  
    else:
        print('Enter a non-negative amount to deposit') 


#Withdraw funds function
withdraw: float    
def withdraw_funds():
    global depositors_balance
    withdraw = float(input('Enter withdrawal amount: '))
    if withdraw > depositors_balance:
        print('Insufficient Balance')
        withdraw_funds()
    elif withdraw <= 0:
        print('Enter a non-negative amout to withdraw') 
        withdraw_funds()  
    else:
        print('Enter your pin to proceed')
        authenticate_user(user_pin)
        depositors_balance -= withdraw
        print(f'An amount of ${withdraw:.2f} withdrawn successfullly\nCurrent balace is: ${depositors_balance:.2f}')  

