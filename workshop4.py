
""" Driver Code for Task 1 """


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your name has been changed to", self.name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


'''drvier code task 2
bob = User("Bob",1234,'password')
print(bob.name)
print(bob.pin)
print(bob.password)
bob.change_password('change_password')
bob.change_pin('new pin')
bob.change_name('new name')
print(bob.name)
print(bob.pin)
print(bob.password)
'''


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"Your current balance is ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(
            f"${amount} was taken from your account, your current balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(
            f"${amount} was added to your account, your current balance is ${self.balance}")

    def transfer(self, amount, pin, user):
        if pin == self.pin:
            self.withdraw(amount)
            user.deposit(amount)
            return True
        else:
            return False

    def request_money(self, amount, pin, password, user):

        if pin == user.pin:
            if password == self.password:
                user.withdraw(amount)
                self.deposit(amount)
                return True
            else:
                return False
        else:
            return False


''' driver task 3
user1 = BankUser('BOB',1234,'password')
print(user1.pin)
print(user1.password)
print(user1.name)
print(user1.balance)
'''

""" driver code task 4
user1 = BankUser("Aaron", "1234", "password")
user1.deposit(100)
user1.show_balance()
user1.withdraw(100)
user1.show_balance()
"""
""" driver code 5"""
user1 = BankUser('angus', '1234', '1')
user2 = BankUser('angus', '1234', '1')
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
user2.transfer(500, '1234', user1)
user2.show_balance()
user1.show_balance()
