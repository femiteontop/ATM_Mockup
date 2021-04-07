import random
import sys

database = {}


def init():
    print('Welcome to BankPHP \n')
    customerStatus = int(input('Do you have account with us? \n 1. Yes \n 2. No \n'))

    if customerStatus == 1:
        login()
    elif customerStatus == 2:
        register()
    else:
        print('Invalid selection, try again.')
        init()


def generateAccountNumber():

    return random.randrange(1111111111, 9999999999)


def login():
    print('**' * 10 + ' LOGIN PAGE ' + '**' * 10 + '\n')

    print('Kindly login with your account number and password: \n')

    accountNoFromUser = int(input('Enter your account number: \n'))
    passwordFromUser = input('Enter your password: \n')

    for accountNumber, userDetails in database.items():
        if accountNoFromUser == accountNumber:
            if passwordFromUser == userDetails[3]:
                bankOperation(userDetails)

            else:
                print('Invalid Password, try again. \n')
                login()

        else:
            print('Incorrect account number, try again. \n')
            login()


def register():
    print('**' * 10 + ' REGISTER FOR NEW ACCOUNT ' + '**' * 10 + '\n')

    firstName = input('Enter your first name: \n')
    lastName = input('Enter your Last name: \n')
    email = input('Enter your email address: \n')
    password = input('Enter your password: \n')

    accountNumber = generateAccountNumber()
    accountBalance = 0

    database[accountNumber] = [firstName, lastName, email, password]
    database['accountBalance'] = accountBalance

    print('====================================================')
    print(f'Hello {firstName} {lastName}')
    print(f'Your account number is {accountNumber} \nKindly keep it safe!')
    print('==================================================== \n')
    login()


def bankOperation(user):
    print(f"\n******* Welcome {user[0]} ******* \n")
    print('Find available options below: ')
    print('1. Deposit ')
    print('2. Withdraw ')
    print('3. Complaints ')
    print('4. Logout ')
    print('5. Exit \n')
    userInput = int(input('Select one option: \n'))

    if userInput == 1:
        deposit()
    elif userInput == 2:
        withdraw()
    elif userInput == 3:
        complaint()
    elif userInput == 4:
        login()
    elif userInput == 5:
        exit()
    else:
        print('Wrong option selected, try again: \n')
        bankOperation(user)


def deposit():
    print(('=' * 20) + ' DEPOSIT CHANNEL ' + ('=' * 20))
    userDeposit = int(input('\nHow much do you want to deposit? \n'))
    print(f'\n₦{userDeposit} deposited')

    database.update({'accountBalance': (userDeposit + database['accountBalance'])})
    print(f"Your account balance is ₦{database['accountBalance']} \n")
    moreTransaction()


def withdraw():
    print(('=' * 20) + ' WITHDRAWAL CHANNEL ' + ('=' * 20))
    userWithdraw = int(input('\nHow much do you want to Withdraw? \n'))
    print(f'\n₦{userWithdraw} debited from your account')

    database.update({'accountBalance': (database['accountBalance'] - userWithdraw)})
    print(f"Your account balance is {database['accountBalance']} \n")
    moreTransaction()


def complaint():
    print(('=' * 20) + ' COMPLAINT CHANNEL ' + ('=' * 20))
    userComplaint = (input('\nWhat is your complaint? \n'))
    print(f"\nYour complaint of '{userComplaint}' is noted, our team will contact you.")

    database.update({'customerComplaint': userComplaint})
    database.update({'complaintNo': random.randrange(1111, 9999)})
    print(f"Your complaint number is {database['complaintNo']}, kindly save it for future reference \n")
    moreTransaction()


def moreTransaction():
    print('Do you want to perform another transaction? ')
    print('1. Yes \n2. No')

    anotherTransaction = int(input('Select an option. \n'))
    if anotherTransaction == 1:
        login()
    elif anotherTransaction == 2:
        exit()
    else:
        print('Invalid option selected, try again. ')
        moreTransaction()


def exit():
    print('########## Thank You For Banking With Us ##########')
    sys.exit()


init()
