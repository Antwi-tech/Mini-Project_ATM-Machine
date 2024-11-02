# Function to save user pin
def save_pin():
    global pin
    pin = input('Add a pin: ')
    print('Pin saved successfully')
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
