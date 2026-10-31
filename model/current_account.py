
"""
Current Account Class
Demonstrates INHERITANCE and POLYMORPHISM
"""

from .account import Account


class CurrentAccount(Account):
   
    MINIMUM_BALANCE = 5000.0
    OVERDRAFT_LIMIT = 50000.0
    OVERDRAFT_INTEREST_RATE = 12.0  # per annum
    MONTHLY_MAINTENANCE_FEE = 100.0
    
    def __init__(self, account_number: str, account_holder_name: str, 
                 initial_balance: float):
        if initial_balance < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Initial balance must be at least ₹{self.MINIMUM_BALANCE} "
                f"for Current Account"
            )
        
        super().__init__(account_number, account_holder_name, initial_balance)
        self._overdraft_used = 0.0
    
    def withdraw_money(self, amount: float) -> bool:
        
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        current_balance = self.balance()
        available_balance = current_balance + (self.OVERDRAFT_LIMIT - self._overdraft_used)
        
        if amount > available_balance:
            print(f"Insufficient funds! Available balance (including overdraft): "
                  f"₹{available_balance:.2f}")
            return False
        
        if amount <= current_balance:
            # Normal withdrawal
            self._update_balance(current_balance - amount)
            self._record_transaction("WITHDRAWAL", amount, "Cash Withdrawal")
            print(f"Withdrawal successful! Amount: ₹{amount:.2f}")
        else:
            overdraft_needed = amount - current_balance
            self._update_balance(0)
            self._overdraft_used += overdraft_needed
            self._record_transaction(
                "WITHDRAWAL", 
                amount, 
                f"Cash Withdrawal (Overdraft used: ₹{overdraft_needed:.2f})"
            )
            print(f"Withdrawal successful! Amount: ₹{amount:.2f}")
            print(f"Overdraft used: ₹{overdraft_needed:.2f}")
            print(f"Total overdraft: ₹{self._overdraft_used:.2f}")
        
        print(f"Remaining Balance: ₹{self.balance():.2f}")
        if self._overdraft_used > 0:
            print(f"Overdraft Outstanding: ₹{self._overdraft_used:.2f}")
        
        return True
    
    def deposit_money(self, amount: float):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        if self._overdraft_used > 0:
            if amount >= self._overdraft_used:
                # Repay full overdraft
                remaining_amount = amount - self._overdraft_used
                print(f"Overdraft of ₹{self._overdraft_used:.2f} repaid.")
                self._overdraft_used = 0
                
                current_balance = self.balance()
                self._update_balance(current_balance + remaining_amount)
                self._record_transaction("DEPOSIT", amount, "Cash Deposit (Overdraft Repaid)")
            else:
                # Partial overdraft repayment
                self._overdraft_used -= amount
                self._record_transaction(
                    "DEPOSIT", 
                    amount, 
                    "Cash Deposit (Partial Overdraft Repayment)"
                )
                print(f"Partial overdraft repayment. Remaining overdraft: "
                      f"₹{self._overdraft_used:.2f}")
        else:
            current_balance = self.balance()
            self._update_balance(current_balance + amount)
            self._record_transaction("DEPOSIT", amount, "Cash Deposit")
        
        print(f"Deposit successful! Amount: ₹{amount:.2f}")
        print(f"Current Balance: ₹{self.balance():.2f}")
    
    def monthly_charges(self):
        total_charges = self.MONTHLY_MAINTENANCE_FEE
        
        overdraft_interest = 0
        if self._overdraft_used > 0:
            overdraft_interest = (self._overdraft_used * self.OVERDRAFT_INTEREST_RATE) / (12 * 100)
            total_charges += overdraft_interest
        
        current_balance = self.balance()
        self._update_balance(current_balance - total_charges)
        
        description = f"Monthly Charges (Maintenance: ₹{self.MONTHLY_MAINTENANCE_FEE}"
        if overdraft_interest > 0:
            description += f", Overdraft Interest: ₹{overdraft_interest:.2f}"
        description += ")"
        
        self._record_transaction("CHARGES", total_charges, description)
        
        print(f"Monthly charges of ₹{total_charges:.2f} deducted from account!")
        if overdraft_interest > 0:
            print(f"(Includes overdraft interest: ₹{overdraft_interest:.2f})")
    
    def account_type(self) -> str:
        return "Current Account"
    
    def show_current_account_details(self):
        """Display detailed current account information"""
        self.show_account_info()
        print(f"Minimum Balance: ₹{self.MINIMUM_BALANCE}")
        print(f"Overdraft Limit: ₹{self.OVERDRAFT_LIMIT}")
        print(f"Overdraft Used: ₹{self._overdraft_used:.2f}")
        print(f"Available Overdraft: ₹{self.available_overdraft():.2f}")
        print(f"Monthly Maintenance Fee: ₹{self.MONTHLY_MAINTENANCE_FEE}")
        if self._overdraft_used > 0:
            print(f"Overdraft Interest Rate: {self.OVERDRAFT_INTEREST_RATE}% per annum")
    
    def overdraft_limit(self) -> float:
        """Get overdraft limit"""
        return self.OVERDRAFT_LIMIT
    
    def overdraft_used(self) -> float:
        """Get amount of overdraft currently used"""
        return self._overdraft_used
    
    def available_overdraft(self) -> float:
        """Get available overdraft amount"""
        return self.OVERDRAFT_LIMIT - self._overdraft_used
    
    def minimum_balance(self) -> float:
        """Get minimum balance requirement"""
        return self.MINIMUM_BALANCE
