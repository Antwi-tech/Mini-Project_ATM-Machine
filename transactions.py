from user import *


#Set user balance to 0 at the beginning
depositors_balance = 0

#Function to check Balance  
def check_balance():
    global depositors_balance
    authenticate_user()
    print(f"Current Balance: ${depositors_balance:.2f}\n")

#Deposit funds function
def deposit_funds():
    global depositors_balance
    print(f'Your account is ${depositors_balance:.2f}\n')

    while True:
        try:
            amount = float(input('Enter an amount to deposit: '))
            
            if amount > 0:
                print('Enter your pin to proceed')

                if authenticate_user():

                    depositors_balance += amount
                    print(f'Successfully deposited ${amount:.2f}\nCrrent Balance: ${depositors_balance:.2f}\n')
                    break
                else:
                    print('User authentication failed. Deposit process aborted.\n')
                    break

            elif amount == 0:
                print('Enter an amount greater than zero(0).\n')
            else:
                print('Enter a non-negative amount to deposit\n')
        except ValueError as e:
            print(f'{e}\nEnter a numeric value instead.\n')



#Withdraw funds function
withdraw: float
def withdraw_funds():
    global depositors_balance
    
    if depositors_balance == 0:
        print(f'Your balance is ${depositors_balance:.2f}\nDeposit funds first.\n')
        deposit_funds()
        withdraw_funds()
        return
    
    while True:
        try:
            withdraw = float(input('Enter withdrawal amount: ')) 

            if withdraw < 0:
                print('Enter a non-negative amount to withdraw') 
                #withdraw_funds()
                continue
            elif withdraw == 0:
                print('Enter an amount greater than zero(0)')
                continue

            if withdraw > depositors_balance:
                print('Insufficient Balance.')
                #withdraw_funds()
                continue
             
            print('Enter your pin to proceed')
            if authenticate_user():
                depositors_balance -= withdraw
                print(f'An amount of ${withdraw:.2f} withdrawn successfully\n'
                      f'Current balance is: ${depositors_balance:.2f}\n')  
                break
            else:
                print('Authentication process failed. Withdrawal aborted.\n')
                break
        except ValueError as e:
            print(f'{e}\nEnter a numeric amount instead.\n')
        
        