#Prompt for User to confirm if he/she has an account

print('Welcome to RholAnt Bank ATM Services.')
prompt=('Do you have an account with us?\n1. Yes\n2. No\nEnter number associated to your choice: ')


user_choice = int(input(prompt))

depositors_balance = 0 

def create_account():
    global depositors_balance
    customer_name = input('\nEnter Full Name: ') 
    customer_pin = int(input('Set a 4 digit Pin: '))
    customer_email = input('Your Email: ')
    credentials = {
        'name':customer_name,
        'pin': customer_pin,
        'email': customer_email
    }
    print('Account created successfully!!\n')
  
  


    
def new_user_deposit():
    global depositors_balance
    print(f'Your account is {depositors_balance}$ so deposit to continue')
    balance = (int(input('How much would you like to deposit?: ')))
    depositors_balance += balance
    print(f'Successfully deposited {balance}')
   
   
#Function to check Balance   
def check_balance():
     global depositors_balance
     #Call verify pin function
     print(f'Current Balance:{depositors_balance}') 
     main_menu()
     

#Withdraw funds
withdraw = 0     
def withdraw_funds():
    #Pin function before withdrawal
    global depositors_balance
    withdraw = int(input('Enter withdrawal amount: '))   
    if withdraw > depositors_balance:
        print('Insufficient Balance')
        withdraw_funds()
    elif withdraw <= 0:
        print('Invalid Amount') 
        withdraw_funds()  
    else:
        depositors_balance -= withdraw
        print('Money withdrawn successfullly')  
        main_menu()   
      


choice = 0   
           
#function to display main menu    

            

#Deposit Funds
def deposit_funds():
    #Call pin function
    global depositors_balance
    amount = int(input('Enter an amount to deposit: '))
    if amount > 0:
        depositors_balance += amount
        print(f'Account updated successfully!! Crrent Balance: {depositors_balance}')  
    else:
        print('Amount rejected')  
    main_menu()       
       


          
if user_choice == 1:
    print("Please Login with your pin")
    main_menu()
elif user_choice == 2:
       print('\nThen create an account Create Account?\n1. Yes\n2. No')  
       answer = int(input('Choose an option: '))
       if answer == 1:
          create_account()
          new_user_deposit()
          main_menu()
       else:   
          print('Thank you for visiting Rholant ATM Services.\nWe hope you come next time.')
else:
    print('Invalid input try again')      
      


    
  
   
        


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
