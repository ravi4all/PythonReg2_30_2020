def atm():
    total = 5000
    pin = input("Enter your PIN : ")

    assert (pin == "1234"), "Invalid PIN"
    print("Login Success")

    amount = int(input("Enter the amount you want to withdraw : "))
    assert (amount < total), "Insufficient Balance"
    total -= amount
    print("Remaining Balance",total)

try:
    atm()
except AssertionError as err:
    print(err)
    atm()