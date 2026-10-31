
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from .transaction import Transaction


class Account(ABC):
    
    def __init__(self, account_number: str, account_holder_name: str, 
                 initial_balance: float):
        
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = initial_balance
        self._created_date = datetime.now()
        self._transaction_history: List[Transaction] = []
        
        # Record initial deposit
        if initial_balance > 0:
            self._transaction_history.append(
                Transaction("DEPOSIT", initial_balance, "Initial Deposit")
            )
    
    # Getter methods (Encapsulation - controlled access to private fields)
    def account_number(self) -> str:
        """Get account number"""
        return self._account_number
    
    def account_holder(self) -> str:
        """Get account holder name"""
        return self._account_holder_name
    
    def balance(self) -> float:
        """Get current balance"""
        return self._balance
    
    def created_date(self) -> datetime:
        """Get account creation date"""
        return self._created_date
    
    def transaction_history(self) -> List[Transaction]:
        """Get copy of transaction history"""
        return self._transaction_history.copy()
    
    # Protected setter - accessible to subclasses
    def _update_balance(self, balance: float):
        """Set balance (protected - for subclass use)"""
        self._balance = balance
    
    def deposit_money(self, amount: float):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transaction_history.append(
            Transaction("DEPOSIT", amount, "Cash Deposit")
        )
        print(f"Deposit successful! Amount: ₹{amount:.2f}")
    
    @abstractmethod
    def withdraw_money(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def monthly_charges(self):
        pass
    
    @abstractmethod
    def account_type(self) -> str:
        pass
    
    def show_account_info(self):
        """Display basic account information"""
        print("\n========== Account Information ==========")
        print(f"Account Type: {self.account_type()}")
        print(f"Account Number: {self._account_number}")
        print(f"Account Holder: {self._account_holder_name}")
        print(f"Current Balance: ₹{self._balance:.2f}")
        print(f"Account Created: {self._created_date.strftime('%Y-%m-%d')}")
        print("=========================================\n")
    
    def show_transaction_history(self):
        """Display complete transaction history"""
        print("\n========== Transaction History ==========")
        print(f"Account: {self._account_number} ({self._account_holder_name})")
        print("-----------------------------------------")
        
        if not self._transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self._transaction_history:
                print(transaction)
        
        print("=========================================\n")
    
    def _record_transaction(self, transaction_type: str, amount: float, 
                        description: str):
        self._transaction_history.append(
            Transaction(transaction_type, amount, description)
        )
