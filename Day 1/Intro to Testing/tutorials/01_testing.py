
def calculate_discount(amount: float, percentage: float) -> float:
    """Calculate discount amount."""
    return amount * (percentage / 100)


print(calculate_discount(100, 10))
