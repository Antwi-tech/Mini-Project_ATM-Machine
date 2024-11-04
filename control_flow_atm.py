# Function to save user pin
#global pin
def save_pin():
    global pin
    while True:
        try:
            pin = int(input('Add a 4-digit pin: '))

            if len(str(pin)) == 4:
                print('Pin saved successfully.\n')
                break
            else:
                print('Please enter a 4-digit pin.\n')
        except ValueError as e:
            print(f'{e}\nEnter a numeric value instead')


# Function to change user pin
def change_pin():
    while True:
        user_pin = input('Enter your current pin: ')

        global pin

        if user_pin == pin:
            print('You are about to change your PIN')
        else:
            print('Wrong PIN')
        
        new_pin = input('Enter a new 4-digit pin: ')
        confirm_pin = input('Enter new PIN again: ')

        if confirm_pin == new_pin:

            if new_pin.isdigit() and len(new_pin) == 4:
                pin = new_pin
                print('Pin updated successfully!')
                break
            else:
                print('Please enter a 4-digit pin.')
        else:
            print('This does not match up with the PIN you just entered')



# User authentication function
user_pin = ''
def authenticate_user():
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        user_pin = input('Enter your pin: ')

        if user_pin == pin:
            print('Authentication successful!\n')
            return True
        else:
            attempts += 1
            print('Incorrect pin. Try again')

        if attempts == max_attempts:
            print('Too many incorrect attempts. Access blocked.')
            return False


            
#Set user balance to 0 at the begining
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
    amount = float(input('Enter an amount to deposit: '))
    
    if amount > 0:
        print('Enter your pin to proceed')
        authenticate_user()
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
        authenticate_user()
        depositors_balance -= withdraw
        print(f'An amount of ${withdraw:.2f} withdrawn successfullly\nCurrent balace is: ${depositors_balance:.2f}')  
        
        
        
# Main Menu Function
def main_menu():
    while True:

        print(
        'Main Menu Options:\n'
        '1. Check Balance\n'
        '2. Deposit Funds\n'
        '3. Withdraw Funds\n'
        '4. Change PIN\n'
        '5. Exit'
    )
        user_choice = input('Enter number associated with choice: ')

        if user_choice == '1':
            print('Enter your pin to proceed.')
            check_balance()
        elif user_choice == '2':
            deposit_funds()
        elif user_choice == '3':
            withdraw_funds()
        elif user_choice == '4':
            change_pin()
        elif user_choice == '5':
            print('Exiting main menu....\n'
                  'Thank you for visiting Rholant ATM Services.\n'
                  'We hope you come next time.'
            )
            break
        else:
            print('Invalid choice!')



# Main Application simulation
def main():
    print('Welcome to RholAnt Bank ATM Services.\nAdd a pin to proceed') 
    save_pin()
    print('Enter your new pin to proceed to the main menu.')
    authenticate_user()
    main_menu()
main()
