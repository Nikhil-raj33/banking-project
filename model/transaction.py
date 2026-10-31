
"""
Transaction Class
Records all banking transactions with timestamp
"""

from datetime import datetime


class Transaction:
    def __init__(self, transaction_type: str, amount: float, description: str):

        self.type = transaction_type
        self._amount = amount
        self._description = description
        self._timestamp = datetime.now()

    def transaction_type(self) -> str:
        return self.type

    def amount(self) -> float:
        return self._amount

    def description(self) -> str:
        return self._description

    def timestamp(self) -> datetime:
        return self._timestamp

    def __str__(self) -> str:
        """String representation of transaction"""
        formatted_time = self._timestamp.strftime("%d-%m-%Y %H:%M:%S")
        return f"[{formatted_time}] {self.type:<12} ₹{self._amount:<10.2f} - {self._description}"
