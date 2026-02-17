import mysql.connector as c

mycon = c.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

if mycon.is_connected():
    print("Server connected successfully")

cursor = mycon.cursor()


# ------------------ FUNCTIONS ------------------

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))

    query = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
    cursor.execute(query, (name, balance))
    mycon.commit()

    acc_no = cursor.lastrowid   

    print("\nAccount created successfully!")
    print("Your Account Number is:", acc_no)   


def account_details(ac):
    query = "SELECT * FROM accounts WHERE account_number = %s"
    cursor.execute(query, (ac,))
    record = cursor.fetchone()

    if record:
        print("Account Number:", record[0])
        print("Name:", record[1])
        print("Balance:", record[2])
    else:
        print("Account not found!")


def check_balance(ac):
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    cursor.execute(query, (ac,))
    record = cursor.fetchone()

    if record:
        print("Current Balance:", record[0])
    else:
        print("Account not found!")


def withdraw(ac):
    amount = float(input("Enter amount to withdraw: "))

    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (ac,))
    record = cursor.fetchone()

    if record and record[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, ac))
        mycon.commit()
        print("Withdrawal successful!")
    else:
        print("Insufficient balance or account not found!")


def deposit(ac):
    amount = float(input("Enter amount to deposit: "))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, ac))
    mycon.commit()
    print("Deposit successful!")





# ------------------ MENU ------------------
insider()
choice = int(input("""
1: Create new account
2: Show account details
3: Check balance
4: Withdraw
5: Deposit
6: except 1 to 5 choice any number to exit the process
Enter your choice: """))

while(choice>=1 and choice<=5):
    if choice == 1:
        create_account()
        
    elif choice == 2:
        ac = int(input("Enter account number: "))
        account_details(ac)
    elif choice == 3:
        check_balance(ac)
    elif choice == 4:
        withdraw(ac)
    elif choice == 5:
        deposit(ac)
        
    else:
        print("Invalid choice!")
        break
    choice = int(input("""
    1: Create new account
    2: Show account details
    3: Check balance
    4: Withdraw
    5: Deposit
    6: except 1 to 5 choice any number to exit the process
    Enter your choice: """))

mycon.close()

