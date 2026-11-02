# Python Banking System

A console-based banking application built with Python and object-oriented design. It supports Savings and Current accounts with different business rules, and it separates data models from business logic.

## Features

- Create Savings and Current accounts
- Deposit, withdraw, and transfer money between accounts
- Check balance and view account details
- View transaction history
- Apply monthly interest and charges
- Manage customer information

## Demo

```text
[Paste real output from your app here: the main menu, a deposit, a transfer, and a transaction history]
```

## Tech Stack

- Python 3 (standard library only, no external dependencies)
- Object-oriented programming

## Design Decisions

- **Abstract `Account` base class:** defines the common interface (deposit, withdraw, balance) so each account type must implement its own rules.
- **Inheritance and polymorphism:** `SavingsAccount` and `CurrentAccount` override withdrawal and monthly-charge behavior instead of using `if/else` on account type.
- **Encapsulation:** balances are private and accessed through getters, so rules like minimum balance can't be bypassed.
- **Model / service separation:** `model/` holds the data classes and `service/` holds the banking logic, which keeps each part easy to test and replace (for example, swapping in a database later).
- [Add one or two decisions that are specific to your code, such as how transfers or transaction IDs work.]

## Project Structure

```text
banking-project/
├── banking_app.py          # Menu-driven entry point
├── model/
│   ├── account.py          # Abstract base class
│   ├── savings_account.py
│   ├── current_account.py
│   ├── customer.py
│   └── transaction.py
├── service/
│   └── banking_system.py   # Business logic
└── README.md
```

## How to Run

```bash
git clone https://github.com/Nikhil-raj33/banking-project.git
cd banking-project
python banking_app.py
```

Requires Python 3.[your version] or newer.

## Account Rules

| | Savings Account | Current Account |
|---|---|---|
| Minimum balance | ₹1,000 | ₹5,000 |
| Interest | 4.5% p.a. | None |
| Free withdrawals | 5 per month | Unlimited |
| Withdrawal limit | ₹50,000 | None |
| Overdraft | None | ₹50,000 |
| Monthly fee | None | ₹100 |

## Limitations

- Data is stored in memory and is lost when the app closes.
- No database, authentication, or real banking integration.

## Roadmap

- [ ] Add unit tests with pytest
- [ ] Persist data in PostgreSQL
- [ ] Expose a REST API with FastAPI and JWT authentication
- [ ] Add atomic transfers, idempotency keys, and an audit log
- [ ] Containerize with Docker
- [ ] Deploy on AWS (VPC, ALB, RDS) with Terraform and GitHub Actions CI/CD
