
menu = str("""
    1. Balance Inquiry
    2. Deposit
    3. Withdraw 
    4. Exit
""")
balance = 5000
pin  = int(input("Enter the pin: "))

if pin == 1234:
    #proceed
    
    print(menu)
    choose = int(input('Choose In the menu: '))
    #nested if
    if choose == 1:
        print(balance)
    elif choose == 2:
        deposit = int(input('How much amount: '))
        print ('New Balance: ',balance + deposit)
    elif choose == 3:
        withdraw = int(input('How much amount you want to withdraw: '))
        #nested nested if
        if balance > withdraw:
            print('New Balance Amount: ',balance - withdraw)
        else:
            print("Insufficient funds!")
    elif choose == 4:
        print("Thank you goodbye!")
    else:
        print("Invalid Choice!")
else:
    #terminate
    print("Invalid PIN. Access denied.")