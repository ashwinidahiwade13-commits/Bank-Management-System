
import random

acc_number = 0
customer_name = None
accountCreated = False
balance = 0
customer_details = list()
loan_details = list()
locker_details = list()


def findAccount(account_number):
    for customer in customer_details:
        if account_number in customer:
            return customer
    return None


def createAccount():
    global acc_number, customer_name, accountCreated, balance

    print('\n----------- ACCOUNT CREATION -----------')

    cust_name = input('Enter Your Name: ')
    cust_gender = input('Enter Your Gender: ')
    cust_age = int(input('Enter Your Age: '))

    if cust_age < 18:
        print('You Are Under Age To Open Account')
        return

    cust_dob = input('Enter Your Date of Birth (DD/MM/YYYY): ')
    cust_mobile = input('Enter Your Mobile Number: ')

    print('1. Current Account\n2. Saving Account')
    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        account_type = 'Current'
        minimum_balance = 5000
    elif choice == 2:
        account_type = 'Saving'
        minimum_balance = 1000
    else:
        print('Invalid Account Type')
        return

    initial_balance = int(input('Enter Initial Balance: '))

    if initial_balance < minimum_balance:
        print('Minimum Balance Required:', minimum_balance)
        return

    account_number = random.randint(100000000000, 999999999999)

    while findAccount(account_number) is not None:
        account_number = random.randint(100000000000, 999999999999)

    balance = initial_balance
    acc_number = account_number
    customer_name = cust_name
    accountCreated = True

    temp_cust_details = [
        customer_name, cust_age, balance, accountCreated,
        cust_dob, cust_mobile, account_type, cust_gender
    ]

    customer_details.append({acc_number: temp_cust_details})

    print('\n-------- CREATION SUCCESSFUL --------')
    print('Account Holder:', customer_name)
    print('Gender:', cust_gender)
    print('Account Type:', account_type)
    print('Balance:', balance)
    print('Account Number:', acc_number)
    print('--------------------------------------')

def applyLoan():
    print('\n------- LOAN SECTION -------')
    print('1. Home Loan')
    print('2. Car Loan')
    print('3. Education Loan')
    print('4. Agricultural Loan')

    loan_choice = int(input('Enter Your Choice: '))

    loan_types = {
        1: 'Home Loan',
        2: 'Car Loan',
        3: 'Education Loan',
        4: 'Agricultural Loan'
    }

    if loan_choice not in loan_types:
        print('Invalid Loan Type')
        return

    acc_confirm = int(input('Enter Account Number: '))
    customer = findAccount(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    cust = customer[acc_confirm]
    acc_name = input('Enter Your Name: ')

    if acc_name.lower() != cust[0].lower():
        print('Customer Name Does Not Match')
        return

    loan_amount = int(input('Enter Loan Amount: '))
    annual_income = int(input('Enter Annual Income: '))
    total_loan_year = int(input('In How Many Years Will You Repay The Loan: '))

    if loan_amount <= 0 or annual_income <= 0 or total_loan_year <= 0:
        print('Enter Valid Loan Details')
        return

    monthly_salary = annual_income / 12
    monthly_repayment = loan_amount / (total_loan_year * 12)

    if monthly_repayment <= monthly_salary / 2:
        loan_details.append({
            'account_number': acc_confirm,
            'loan_type': loan_types[loan_choice],
            'loan_amount': loan_amount,
            'years': total_loan_year,
            'monthly_repayment': round(monthly_repayment, 2)
        })

        print('\n-------- LOAN APPLICATION SUCCESSFUL --------')
        print('Loan Holder:', cust[0])
        print('Loan Type:', loan_types[loan_choice])
        print('Loan Amount:', loan_amount)
        print('Estimated Monthly Principal:', round(monthly_repayment, 2))
        print('Repayment Period:', total_loan_year, 'years')
        print('---------------------------------------------')
        print('Note: This is a basic project eligibility check.')
        print('Actual loans include interest and bank verification.')
    else:
        print('Sorry, You Are Not Eligible Based On This Basic Check')


def displayCustomerDetails():
    acc_confirm = int(input('Enter Your Account Number: '))
    customer = findAccount(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_confirm]

    print('\n============== CUSTOMER DETAILS ==============')
    print('Account Number:', acc_confirm)
    print('Account Holder Name:', details[0])
    print('Holder Age:', details[1])
    print('Current Balance:', details[2])
    print('Has Account in Bank:', details[3])
    print('Date of Birth:', details[4])
    print('Mobile Number:', details[5])
    print('Account Type:', details[6])
    print('Gender:', details[7])
    print('===============================================')


def moneyTransaction():
    print('\n------- MONEY TRANSACTION -------')

    acc_confirm = int(input('Enter Your Account Number: '))
    customer = findAccount(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_confirm]

    print('1. Deposit Money')
    print('2. Withdraw Money')
    print('3. Check Balance')

    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        amount = int(input('Enter Amount To Deposit: '))

        if amount > 0:
            details[2] += amount
            print('Money Deposited Successfully')
            print('Updated Balance:', details[2])
        else:
            print('Enter A Valid Amount')

    elif choice == 2:
        amount = int(input('Enter Amount To Withdraw: '))

        if amount <= 0:
            print('Enter A Valid Amount')
        elif amount > details[2]:
            print('Insufficient Balance')
        else:
            details[2] -= amount
            print('Money Withdrawn Successfully')
            print('Updated Balance:', details[2])

    elif choice == 3:
        print('Available Balance:', details[2])

    else:
        print('Invalid Transaction Choice')

def lockerSection():
    while True:
        print('\n========== LOCKER SECTION ==========')
        print('1. Create Locker')
        print('2. Access Locker')
        print('3. View Locker Details')
        print('4. Back To Main Menu')

        choice = int(input('Enter Your Choice: '))

        if choice == 1:
            acc_confirm = int(input('Enter Your Account Number: '))
            customer = findAccount(acc_confirm)

            if customer is None:
                print('Account Number Not Found')
                continue

            existing_locker = None

            for locker in locker_details:
                if acc_confirm in locker:
                    existing_locker = locker
                    break

            if existing_locker is not None:
                print('Locker Already Exists For This Account')
                continue

            pin = input('Create A 4-Digit Locker PIN: ')

            if len(pin) != 4 or not pin.isdigit():
                print('PIN Must Contain Exactly 4 Digits')
                continue

            locker_number = random.randint(10000, 99999)

            locker_details.append({
                acc_confirm: {
                    'locker_number': locker_number,
                    'pin': pin,
                    'status': 'Active'
                }
            })

            print('\nLocker Created Successfully')
            print('Locker Number:', locker_number)
            print('Keep Your PIN Secret')

        elif choice == 2:
            acc_confirm = int(input('Enter Your Account Number: '))
            customer = findAccount(acc_confirm)

            if customer is None:
                print('Account Number Not Found')
                continue

            locker = None

            for item in locker_details:
                if acc_confirm in item:
                    locker = item[acc_confirm]
                    break

            if locker is None:
                print('No Locker Found. Please Create A Locker First')
                continue

            pin = input('Enter Your Locker PIN: ')

            if pin == locker['pin']:
                print('\nLocker Access Successful')
                print('Locker Number:', locker['locker_number'])
                print('Locker Status:', locker['status'])
            else:
                print('Incorrect PIN')

        elif choice == 3:
            acc_confirm = int(input('Enter Your Account Number: '))
            customer = findAccount(acc_confirm)

            if customer is None:
                print('Account Number Not Found')
                continue

            found = False

            for item in locker_details:
                if acc_confirm in item:
                    locker = item[acc_confirm]
                    print('\n------- LOCKER DETAILS -------')
                    print('Account Holder:', customer[acc_confirm][0])
                    print('Locker Number:', locker['locker_number'])
                    print('Locker Status:', locker['status'])
                    print('------------------------------')
                    found = True
                    break

            if not found:
                print('No Locker Found For This Account')

        elif choice == 4:
            break

        else:
            print('Invalid Choice')

def displayLoanDetails():
    acc_confirm = int(input('Enter Your Account Number: '))
    customer = findAccount(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    found = False

    for loan in loan_details:
        if loan['account_number'] == acc_confirm:
            print('\n------- LOAN DETAILS -------')
            print('Loan Type:', loan['loan_type'])
            print('Loan Amount:', loan['loan_amount'])
            print('Repayment Period:', loan['years'], 'years')
            print('Estimated Monthly Principal:', loan['monthly_repayment'])
            print('----------------------------')
            found = True

    if not found:
        print('No Loan Application Found')

def welcome():
    while True:
        print('\n========== BANK SYSTEM ==========')
        print('1. Create Account')
        print('2. Apply For Loan')
        print('3. Display Customer Details')
        print('4. Money Transaction')
        print('5. Locker Section')
        print('6. Display Loan Details')
        print('7. Exit')

        try:
            customer_choice = int(input('Enter Your Choice: '))

            match customer_choice:
                case 1:
                    createAccount()
                case 2:
                    applyLoan()
                case 3:
                    displayCustomerDetails()
                case 4:
                    moneyTransaction()
                case 5:
                    lockerSection()
                case 6:
                    displayLoanDetails()
                case 7:
                    print('Thank You For Using Our Banking System!')
                    break
                case _:
                    print('Invalid Choice')

        except ValueError:
            print('Please Enter A Valid Number')


welcome()
