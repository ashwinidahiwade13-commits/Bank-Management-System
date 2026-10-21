# 🖥️ Online Banking Management System — Sample Output

This file shows **illustrative sample console output** for the Python banking project.

> **Note:** The account number and locker number are generated randomly, so your output will differ. This is a sample walkthrough, not a transcript captured from an actual program run.

## 1. Main Menu

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Section
6. Display Loan Details
7. Exit
Enter Your Choice: 1
```

## 2. Create Account

```text
----------- ACCOUNT CREATION -----------
Enter Your Name: Ashwini
Enter Your Gender: Female
Enter Your Age: 21
Enter Your Date of Birth (DD/MM/YYYY): 15/08/2005
Enter Your Mobile Number: 9876543210
1. Current Account
2. Saving Account
Enter Your Choice: 2
Enter Initial Balance: 5000

-------- CREATION SUCCESSFUL --------
Account Holder: Ashwini
Gender: Female
Account Type: Saving
Balance: 5000
Account Number: 123456789012
--------------------------------------
```

*The account number above is an example only.*

## 3. Display Customer Details

```text
Enter Your Account Number: 123456789012

============== CUSTOMER DETAILS ==============
Account Number: 123456789012
Account Holder Name: Ashwini
Holder Age: 21
Current Balance: 5000
Has Account in Bank: True
Date of Birth: 15/08/2005
Mobile Number: 9876543210
Account Type: Saving
Gender: Female
===============================================
```

## 4. Deposit Money

```text
------- MONEY TRANSACTION -------
Enter Your Account Number: 123456789012
1. Deposit Money
2. Withdraw Money
3. Check Balance
Enter Your Choice: 1
Enter Amount To Deposit: 1500
Money Deposited Successfully
Updated Balance: 6500
```

## 5. Withdraw Money

```text
------- MONEY TRANSACTION -------
Enter Your Account Number: 123456789012
1. Deposit Money
2. Withdraw Money
3. Check Balance
Enter Your Choice: 2
Enter Amount To Withdraw: 500
Money Withdrawn Successfully
Updated Balance: 6000
```

## 6. Apply for a Loan

```text
------- LOAN SECTION -------
1. Home Loan
2. Car Loan
3. Education Loan
4. Agricultural Loan
Enter Your Choice: 3
Enter Account Number: 123456789012
Enter Your Name: Ashwini
Enter Loan Amount: 120000
Enter Annual Income: 600000
In How Many Years Will You Repay The Loan: 5

-------- LOAN APPLICATION SUCCESSFUL --------
Loan Holder: Ashwini
Loan Type: Education Loan
Loan Amount: 120000
Estimated Monthly Principal: 2000.0
Repayment Period: 5 years
---------------------------------------------
Note: This is a basic project eligibility check.
Actual loans include interest and bank verification.
```

## 7. Create a Locker

```text
========== LOCKER SECTION ==========
1. Create Locker
2. Access Locker
3. View Locker Details
4. Back To Main Menu
Enter Your Choice: 1
Enter Your Account Number: 123456789012
Create A 4-Digit Locker PIN: 2580

Locker Created Successfully
Locker Number: 54321
Keep Your PIN Secret
```

*The locker number above is an example only. Do not use a real PIN in sample files.*

## 8. Access Locker

```text
========== LOCKER SECTION ==========
1. Create Locker
2. Access Locker
3. View Locker Details
4. Back To Main Menu
Enter Your Choice: 2
Enter Your Account Number: 123456789012
Enter Your Locker PIN: 2580

Locker Access Successful
Locker Number: 54321
Locker Status: Active
```

## 9. View Locker Details

```text
========== LOCKER SECTION ==========
1. Create Locker
2. Access Locker
3. View Locker Details
4. Back To Main Menu
Enter Your Choice: 3
Enter Your Account Number: 123456789012

------- LOCKER DETAILS -------
Account Holder: Ashwini
Locker Number: 54321
Locker Status: Active
------------------------------
```

## 10. Display Loan Details

```text
Enter Your Account Number: 123456789012

------- LOAN DETAILS -------
Loan Type: Education Loan
Loan Amount: 120000
Repayment Period: 5 years
Estimated Monthly Principal: 2000.0
----------------------------
```

## 11. Exit

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Section
6. Display Loan Details
7. Exit
Enter Your Choice: 7
Thank You For Using Our Banking System!
```

---

## Important Notes

- This is a **sample output** with illustrative values. Random account and locker numbers will differ each run.
- The program stores data in memory, so information is lost when the program exits.
- The loan calculation shown is a simple principal-per-month estimate; it does not include interest.
- The locker PIN is only for demonstrating basic conditional logic. This is not a secure locker system.
