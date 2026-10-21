# 🏦 Online Banking Management System

A beginner-friendly **Python console application** that demonstrates the core features of a simple banking system. Users can create bank accounts, apply for loans, manage deposits and withdrawals, view customer details, and manage a locker with a PIN.

> **Project type:** Python CLI / Console Application  
> **Language:** Python 3.10+  
> **Storage:** In-memory lists and dictionaries

---

## ✨ Features

| Feature | Description |
|---|---|
| 👤 Account Creation | Create a Current or Saving account with basic customer details |
| 💳 Money Transactions | Deposit money, withdraw money, and check the current balance |
| 🏠 Loan Application | Apply for a Home, Car, Education, or Agricultural loan |
| 📋 Customer Details | Display account and customer information using an account number |
| 🔐 Locker Section | Create a locker, access it with a 4-digit PIN, and view locker details |
| 🧾 Loan Details | View loan application details for an account |
| 🚪 Exit | Exit the application from the main menu |

## 🧰 Requirements

- Python 3.10 or newer (the program uses `match` / `case`)
- Any Python editor or terminal, such as PyCharm, VS Code, or Command Prompt

No third-party Python packages are required.

## 🚀 Getting Started

1. Install Python 3.10 or newer.
2. Save the program as `OnlineBankingSystem.py`.
3. Open a terminal in the folder containing the file.
4. Run:

```bash
python OnlineBankingSystem.py
```

If your system uses the Python launcher, you can also try:

```bash
py OnlineBankingSystem.py
```

## 🧭 Main Menu

When the program starts, it displays the following menu:

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Section
6. Display Loan Details
7. Exit
Enter Your Choice:
```

## 🧪 How to Use

### 1. Create an Account
- Enter the customer's name, gender, age, date of birth, and mobile number.
- Choose Current Account or Saving Account.
- Enter the initial balance.
- The program applies a minimum initial balance of ₹5,000 for Current Accounts and ₹1,000 for Saving Accounts.
- An account number is generated and displayed.

### 2. Apply for a Loan
- Choose Home, Car, Education, or Agricultural Loan.
- Enter the account number and account holder's name.
- Enter the requested loan amount, annual income, and repayment period.
- The program performs a simple educational eligibility check.

### 3. Display Customer Details
- Enter an account number to view the customer's stored details and current balance.

### 4. Money Transactions
- Choose Deposit, Withdraw, or Check Balance.
- Enter a positive amount for deposits and withdrawals.
- Withdrawals cannot exceed the available balance.

### 5. Locker Section
- Create one locker per account.
- Set a 4-digit numeric PIN.
- Access the locker by entering the account number and PIN.
- View the locker number and locker status.

### 6. Display Loan Details
- Enter an account number to view loan applications stored for that account.

## 🗂️ Project Structure

```text
Online-Banking-System/
├── OnlineBankingSystem.py
├── README.md
└── OUTPUT.md
```

## 🧠 Python Concepts Used

- Functions
- Global variables
- Lists and dictionaries
- `if` / `elif` / `else` conditions
- `for` loops
- `match` / `case`
- User input with `input()`
- Random number generation with `random`
- Basic validation and menu-driven programming

## ⚠️ Limitations

This project is intended for learning and demonstration, not real banking.

- Account, loan, and locker information is stored in memory and is lost when the program exits.
- The loan eligibility check is simplified and is not a real bank approval process.
- The locker PIN is stored as plain text in memory and is not secure for real-world use.
- Account numbers and locker numbers are randomly generated.
- Input validation is basic; unexpected input may need additional handling.

## 🔮 Possible Improvements

- Save records in a database such as SQLite or MySQL.
- Add transaction history and receipts.
- Hash locker PINs and limit incorrect attempts.
- Add stronger validation for age, mobile number, amounts, and dates.
- Implement loan interest, EMI calculation, and more realistic eligibility rules.
- Add authentication and account recovery.

## 👩‍💻 Learning Project

Built as a practice project to learn Python functions, data structures, conditions, loops, and menu-driven application design.

---

**Disclaimer:** This is a demonstration project only. It is not connected to a real bank and must not be used to store real financial or personal information.
