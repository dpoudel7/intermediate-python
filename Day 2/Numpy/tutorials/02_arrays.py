import numpy as np

# Create NumPy array from the same data
monthly_revenue = np.array([
    100000, 120000, 115000, 130000, 140000, 135000,
    145000, 150000, 160000, 165000, 175000, 180000
])

# Calculate growth rates (vectorized operation)
growth_rates = np.diff(monthly_revenue) / monthly_revenue[:-1] * 100

print("Monthly Growth Rates (%) using NumPy:")
for month, rate in enumerate(growth_rates, 1):
    print(f"Month {month}: {rate:.1f}%")

# Basic statistics (built-in functions)
print(f"\nAverage Monthly Revenue: ${monthly_revenue.mean():,.2f}")
print(f"Minimum Revenue: ${monthly_revenue.min():,.2f}")
print(f"Maximum Revenue: ${monthly_revenue.max():,.2f}")
print(f"Revenue Standard Deviation: ${monthly_revenue.std():,.2f}")