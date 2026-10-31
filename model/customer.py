
"""
Customer Class
Represents a bank customer with personal information
"""


class Customer:
    def __init__(self, customer_id: str, name: str, email: str,
                 phone_number: str, address: str):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = address

    # Getter methods (Encapsulation)
    def customer_id(self) -> str:
        """Get customer ID"""
        return self._customer_id

    def customer_name(self) -> str:
        """Get customer name"""
        return self._name

    def email(self) -> str:
        """Get customer email"""
        return self._email

    def phone_number(self) -> str:
        """Get customer phone number"""
        return self._phone_number

    def address(self) -> str:
        """Get customer address"""
        return self._address

    # Setter methods for updatable fields
    def update_email(self, email: str):
        """Update customer email"""
        self._email = email

    def update_phone_number(self, phone_number: str):
        """Update customer phone number"""
        self._phone_number = phone_number

    def update_address(self, address: str):
        """Update customer address"""
        self._address = address

    def show_customer_info(self):
        """Display customer information"""
        print("\n========== Customer Information ==========")
        print(f"Customer ID: {self._customer_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Phone: {self._phone_number}")
        print(f"Address: {self._address}")
        print("==========================================\n")

    def __str__(self) -> str:
        """String representation of customer"""
        return (f"Customer{{ID='{self._customer_id}', Name='{self._name}', "
                f"Email='{self._email}', Phone='{self._phone_number}'}}")
