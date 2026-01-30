class BankAccount:
    """Simple bank account with deposit, withdraw and transfer operations."""

    def __init__(self, account_id: str, owner: str, balance: float = 0.0):
        self.account_id = account_id
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self) -> float:
        """Return current balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw a positive amount from the account if sufficient funds."""
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def transfer_to(self, other: "BankAccount", amount: float) -> None:
        """Transfer amount from this account to another BankAccount."""
        if not isinstance(other, BankAccount):
            raise TypeError("other must be BankAccount")
        # withdraw will raise on insufficient funds
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self) -> str:
        return f"BankAccount({self.account_id}, owner={self.owner}, balance={self._balance:.2f})"


# Quick sanity checks when run directly
if __name__ == "__main__":
    a = BankAccount("A1", "Alice", 100.0)
    b = BankAccount("B1", "Bob", 50.0)
    print(a)
    print(b)

    a.deposit(25.0)
    print("After deposit:", a.balance)

    try:
        a.withdraw(200)
    except ValueError as e:
        print("Withdraw failed as expected:", e)

    a.transfer_to(b, 50.0)
    print("After transfer:", a, b)
    print("Quick checks done.")