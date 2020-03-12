class Bank:

    def __init__(self):
        self.total = 10000

    def mainMenu(self):
        print("""
        1. Deposit
        2. Withdraw
        3. Check Loan Availibility
        4. Change PIN
        """)

        ch = input("Enter your choice : ")

        operations = {
            "1" : self.deposit,
            "2" : self.withdraw,
            "3" : self.checkLoanEligibility,
        }
        operations.get(ch)()

    def withdraw(self):
        pass

    def deposit(self):
        pass

    def checkLoanEligibility(self):
        pass