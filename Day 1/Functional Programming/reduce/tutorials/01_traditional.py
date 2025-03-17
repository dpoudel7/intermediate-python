

opportunities = [
    {'Amount': '1000.00', 'Probability': '90'},
    {'Amount': '5000.00', 'Probability': '60'},
    {'Amount': '2000.00', 'Probability': '75'}
]

# Traditional approach with loops
print("\nTraditional Loop Approach:")

# Calculate total pipeline
total = 0
for opp in opportunities:
    total += float(opp['Amount'])
print("Total Pipeline (Loop):", total)

# Calculate weighted pipeline
weighted_total = 0
for opp in opportunities:
    amount = float(opp['Amount'])
    probability = float(opp['Probability']) / 100
    weighted_total += amount * probability
print("Weighted Pipeline (Loop):", weighted_total)