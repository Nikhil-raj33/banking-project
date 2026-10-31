
"""
Savings Account Class
Demonstrates INHERITANCE and POLYMORPHISM
"""

from .account import Account


class SavingsAccount(Account):

    MINIMUM_BALANCE = 1000.0
    INTEREST_RATE = 4.5  # per annum
    WITHDRAWAL_LIMIT = 50000.0
    FREE_WITHDRAWALS = 5
    WITHDRAWAL_CHARGE = 10.0

    def __init__(self, account_number: str, account_holder_name: str,
                 initial_balance: float):
        if initial_balance < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Initial balance must be at least ₹{self.MINIMUM_BALANCE} "
                f"for Savings Account"
            )

        super().__init__(account_number, account_holder_name, initial_balance)
        self._withdrawal_count = 0

    def withdraw_money(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False

        if amount > self.WITHDRAWAL_LIMIT:
            print(f"Withdrawal limit exceeded! Maximum allowed: ₹{self.WITHDRAWAL_LIMIT}")
            return False

        current_balance = self.balance()
        charge_amount = 0

        if self._withdrawal_count >= self.FREE_WITHDRAWALS:
            charge_amount = self.WITHDRAWAL_CHARGE
            print(f"Note: Withdrawal charge of ₹{self.WITHDRAWAL_CHARGE} will be applied.")

        total_deduction = amount + charge_amount

        if current_balance - total_deduction < self.MINIMUM_BALANCE:
            print(f"Insufficient balance! Minimum balance of ₹{self.MINIMUM_BALANCE} "
                  f"must be maintained.")
            return False

        # Process withdrawal
        self._update_balance(current_balance - total_deduction)
        self._record_transaction("WITHDRAWAL", amount, "Cash Withdrawal")

        if charge_amount > 0:
            self._record_transaction("CHARGES", charge_amount, "Withdrawal Charge")

        self._withdrawal_count += 1

        print(f"Withdrawal successful! Amount: ₹{amount:.2f}")
        if charge_amount > 0:
            print(f"Withdrawal charge: ₹{charge_amount:.2f}")
        print(f"Remaining Balance: ₹{self.balance():.2f}")

        return True

    def monthly_charges(self):

        current_balance = self.balance()
        monthly_interest = (current_balance * self.INTEREST_RATE) / (12 * 100)

        self._update_balance(current_balance + monthly_interest)
        self._record_transaction(
            "INTEREST",
            monthly_interest,
            f"Monthly Interest Credit @ {self.INTEREST_RATE}% p.a."
        )

        print(f"Monthly interest of ₹{monthly_interest:.2f} credited to account!")

        self._withdrawal_count = 0

    def account_type(self) -> str:
        return "Savings Account"

    def show_savings_account_details(self):
        self.show_account_info()
        print(f"Interest Rate: {self.INTEREST_RATE}% per annum")
        print(f"Minimum Balance: ₹{self.MINIMUM_BALANCE}")
        print(f"Withdrawal Limit: ₹{self.WITHDRAWAL_LIMIT}")
        print(f"Free Withdrawals: {self.FREE_WITHDRAWALS} per month")
        print(f"Withdrawals this month: {self._withdrawal_count}")

    def interest_rate(self) -> float:
        """Get interest rate"""
        return self.INTEREST_RATE

    def minimum_balance(self) -> float:
        """Get minimum balance requirement"""
        return self.MINIMUM_BALANCE

    def withdrawal_count(self) -> int:
        """Get number of withdrawals this month"""
        return self._withdrawal_count
