class BankAccount:
    
    def __init__(self):
        self.balance = None
        
    def get_balance(self):
        if self.balance is None:
            raise ValueError('account not open')
        return self.balance
    
    def open(self):
        if self.balance is not None:
            raise ValueError('account already open')
        self.balance = 0
        
    def deposit(self, amount):
        if self.balance is None:
            raise ValueError('account not open')
        elif amount < 0:
            raise ValueError('amount must be greater than 0')
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance is None:
            raise ValueError('account not open')
        elif self.balance < amount:
            raise ValueError('amount must be less than balance')
        elif amount < 0:
            raise ValueError('amount must be greater than 0')
        self.balance -= amount
        
    def close(self):
        if self.balance is None:
            raise ValueError('account not open')
        self.balance = None

