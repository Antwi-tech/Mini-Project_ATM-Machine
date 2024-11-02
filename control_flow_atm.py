
# Function to save user pin
def save_pin():
    global pin
    while True:
        pin = input('Add a 4-digit pin: ')

        if pin.isdigit() and len(pin) == 4:
            print('Pin saved successfully')
            break
        else:
            print('Please enter a 4-digit pin.')
            
save_pin()


# User authentication
user_pin = ''
def authenticate_user(user_pin):
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        user_pin = input('Enter your pin: ')

        if user_pin == pin:
            print('Authentication successful!')
            print('Main Menu function goes here!')

            break
        else:
            attempts += 1
            print('Incorrect pin. Try again')

        if attempts == max_attempts:
            print('Too many incorrect attempts. Access blocked.')
            exit()

authenticate_user(user_pin)


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
            print('Check balance function goes here!')
        elif user_choice == '2':
            print('Deposit Funds function goes here!')
        elif user_choice == '3':
            print('Withdraw Funds function goes here!')
        elif user_choice == '4':
            print('Change PIN function goes here!')
        elif user_choice == '5':
            print('Exiting main menu')
            break
        else:
            print('Invalid choice!')

main_menu()
