from abc import ABCMeta, abstractmethod
from random import randint

# SIMULATING A BANK ACCOUNT OPENING SYSTEM
class Account(metaclass = ABCMeta):
    @abstractmethod
    def create_account():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def display_balance():
        return 0



class SavingsAccount(Account):
    def __init__(self):
        self.savings_account = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(0, 9999999999)
        self.savings_account[self.account_number] = [name, initial_deposit]
        print('Account creation was successful. Your account number is', self.account_number)


    def authenticate(self, name, account_number):
        if account_number in self.savings_account.keys():
            if self.savings_account[account_number][0] == name:
                print('Authenticad Successful')
                self.account_number = account_number
                return True
            else:
                print('Authentication Failed')
                return False
        else:
            print('Authentication Failed')
            return False

    def deposit(self, deposit_amount):
        self.savings_account[self.account_number][1] += deposit_amount
        print('Deposit Successful !')
        self.display_balance()

    def display_balance(self):
        print('Available Balance: ', self.savings_account[self.account_number][1])

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.savings_account[self.account_number][1]:
            print('Insufficient Balance')
        else:
            self.savings_account[self.account_number][1] -= withdrawal_amount
            print('Withdral Successful !')
            self.display_balance()



savings_account = SavingsAccount()


while True:
    """Menu for creating a new account, access existing account and exit"""
    print('Enter 1 to create a new account ')
    print('Enter 2 to access an existing account ')
    print('Enter 3 to exit ')

    users_choice = int(input('Enter a number between 1 and 3: '))
    if users_choice is 1:   #Call the creat_account method and create user accout with name and initial deposit
        name = input('Enter your name: ')
        deposit_amount = int(input('Enter Amount: '))
        savings_account.create_account(name, deposit_amount)
    elif users_choice is 2: # Authenticate the user and display menu for withdrawal, deposit and balance
        name = input('Enter your name: ')
        account_number = int(input('Enter account number: '))
        auth_status = savings_account.authenticate(name, account_number)
        if auth_status is True:
            while True:
                print('Enter 1 to withdraw: ')
                print('Enter 2 to deposit: ')
                print('Enter 3 to display available balance: ')
                print('Enter 4 to go back to previous menu: ')
                users_choice = int(input('Enter a number between 1 and 4: '))
                if users_choice is 1:
                    withdrawal_amount = int(input('Amount to withdraw: '))
                    savings_account.withdraw(withdrawal_amount)
                elif users_choice is 2:
                    deposit_amount = int(input('Enter amount to deposit: '))
                    savings_account.deposit(deposit_amount)
                elif users_choice is 3:
                    savings_account.display_balance()
                elif users_choice is 4:
                    break

    elif users_choice is 3:
        quit()

    print(savings_account.savings_account)
    print(savings_account.display_balance())
