# Function to save user pin
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
            print(f'{e}\nEnter a numeric value instead\n')


# Function to change user pin
def change_pin():
    while True:
        try:
            user_pin = int(input('Enter your current pin: '))

            global pin
            while True:
                if user_pin == pin:
                    print('You are about to change your PIN')
                    break
                else:
                    print('Wrong PIN')
                    user_pin = int(input('Enter your current pin: '))
            
            while True:
                new_pin = int(input('Enter a new 4-digit pin: '))
                confirm_pin = int(input('Enter new PIN again: '))

                if confirm_pin == new_pin:

                    if len(str(new_pin)) == 4:
                        pin = new_pin
                        print('Pin updated successfully!\n')
                        break
                    else:
                        print('Please enter a 4-digit pin.')
                else:
                    print('This does not match up with the PIN you just entered')
            break
        except ValueError as e:
            print(f'{e}\nEnter a numeric value instead\n')




# User authentication function
user_pin = ''
def authenticate_user():
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            user_pin = int(input('Enter your pin: '))
            
            if user_pin == pin:
                print('Authentication successful!\n')
                return True
            else:
                attempts += 1
                print('Incorrect pin. Try again')
    
            if attempts == max_attempts:
                print('Too many incorrect attempts. Access blocked.')
                exit()
          
        except ValueError as e:
            print(f'{e}\nEnter a numeric value instead\n')
