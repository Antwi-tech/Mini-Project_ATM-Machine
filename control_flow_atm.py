from user import *
from transactions import *
        
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
        else:
            print('\nInvalid choice!')
            print('\nEnter a number 1-5!')



# Main Application simulation
def main():
    print('Welcome to RholAnt Bank ATM Services.\nAdd a pin to proceed') 
    save_pin()
    print('Enter your new pin to proceed to the main menu.')
    authenticate_user()
    main_menu()
    
main()

