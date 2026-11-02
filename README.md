# Python Banking System

A console-based banking application built using **Python and OOP concepts**.

## Features

- Create Savings and Current Accounts
- Deposit and withdraw money
- Check account balance
- Transfer money between accounts
- View account details
- View transaction history
- Apply monthly interest and charges
- Manage customer information

## Tech Stack

- Python 3
- Object-Oriented Programming
- Python standard libraries

## OOP Concepts

1. **Abstraction:** Uses an abstract `Account` class.
2. **Inheritance:** `SavingsAccount` and `CurrentAccount` inherit from `Account`.
3. **Encapsulation:** Uses private attributes and getter methods.
4. **Polymorphism:** Different account types implement withdrawal and monthly charges differently.

## Project Structure

```text
Banking-System/
│
├── banking_app.py
├── model/
│   ├── account.py
│   ├── savings_account.py
│   ├── current_account.py
│   ├── customer.py
│   └── transaction.py
│
├── service/
│   └── banking_system.py
│
└── README.md
```

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/Nikhil-raj33/banking-project.git
```

**2. Open the project folder**

```bash
cd Banking-System
```

**3. Run the application**

```bash
python banking_app.py
```

## Account Types

| Savings Account | Current Account |
|---|---|
| Minimum balance: ₹1,000 | Minimum balance: ₹5,000 |
| Interest: 4.5% p.a. | Overdraft: ₹50,000 |
| 5 free withdrawals/month | Monthly fee: ₹100 |
| Withdrawal limit: ₹50,000 | No withdrawal limit |

## Limitations

- Data is stored in memory.
- Data is lost when the application closes.
- No database or real banking integration.

## Learning Outcomes

- Understanding Python OOP
- Working with classes and objects
- Implementing inheritance and polymorphism
- Building a menu-driven application
- Managing transactions using Python

