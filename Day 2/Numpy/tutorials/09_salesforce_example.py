# -----------------------------------------------------------------------------
# NUMPY IN SALESFORCE CONTEXT
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~30 minutes

This tutorial demonstrates practical NumPy applications in Salesforce scenarios:
1. Sales data analysis
2. Lead scoring
3. Customer segmentation
4. Performance metrics
5. Time series analysis
"""

import numpy as np

# 1. Sales Data Analysis
print("1. SALES DATA ANALYSIS")
print("-" * 50)

# Sample monthly sales data for different products
sales_data = np.array([
    # Product A, B, C, D
    [1000, 1500, 800, 1200],    # Jan
    [1200, 1400, 900, 1100],    # Feb
    [1100, 1600, 850, 1300],    # Mar
    [1300, 1450, 950, 1250]     # Apr
])

print("Monthly sales data:\n", sales_data)

# Calculate total sales per product
product_totals = sales_data.sum(axis=0)
print("\nTotal sales per product:", product_totals)

# Calculate monthly totals
monthly_totals = sales_data.sum(axis=1)
print("Monthly totals:", monthly_totals)

# Find best and worst performing products
best_product = np.argmax(product_totals)
worst_product = np.argmin(product_totals)
print(f"\nBest performing product index: {best_product}")
print(f"Worst performing product index: {worst_product}")

# 2. Lead Scoring
print("\n2. LEAD SCORING")
print("-" * 50)

# Sample lead data: [engagement_score, company_size, past_purchases, email_opens]
leads = np.array([
    [0.8, 500, 5, 10],
    [0.6, 100, 2, 5],
    [0.9, 1000, 8, 15],
    [0.3, 50, 1, 2],
    [0.7, 300, 4, 8]
])

# Weights for different factors
weights = np.array([0.4, 0.2, 0.25, 0.15])

# Normalize company size and email opens
leads[:, 1] = leads[:, 1] / leads[:, 1].max()
leads[:, 3] = leads[:, 3] / leads[:, 3].max()

# Calculate lead scores
lead_scores = np.dot(leads, weights)
print("Lead scores:", lead_scores)

# Get top 3 leads
top_leads = np.argsort(lead_scores)[-3:][::-1]
print("Top 3 lead indices:", top_leads)

# 3. Customer Segmentation
print("\n3. CUSTOMER SEGMENTATION")
print("-" * 50)

# Sample customer data: [annual_revenue, num_employees, years_as_customer]
customers = np.array([
    [100000, 50, 2],
    [500000, 200, 5],
    [1000000, 500, 8],
    [200000, 75, 3],
    [750000, 300, 6]
])

# Normalize data
normalized_customers = (customers - customers.mean(axis=0)) / customers.std(axis=0)
print("Normalized customer data:\n", normalized_customers)

# Simple segmentation based on revenue
segments = np.digitize(customers[:, 0], bins=[200000, 500000, 800000])
print("Customer segments:", segments)

# 4. Performance Metrics
print("\n4. PERFORMANCE METRICS")
print("-" * 50)

# Sample performance data: [calls_made, emails_sent, meetings_scheduled, deals_closed]
performance = np.array([
    [100, 200, 10, 3],
    [150, 180, 15, 5],
    [120, 220, 12, 4],
    [90, 160, 8, 2]
])

# Calculate success rates
success_rates = performance[:, -1] / performance[:, 0] * 100
print("Success rates (%):", success_rates)

# Calculate correlation matrix
correlation = np.corrcoef(performance.T)
print("\nCorrelation matrix:\n", correlation)

# 5. Time Series Analysis
print("\n5. TIME SERIES ANALYSIS")
print("-" * 50)

# Monthly revenue data
revenue = np.array([
    100000, 120000, 115000, 125000, 
    130000, 128000, 135000, 140000,
    142000, 145000, 150000, 155000
])

# Calculate moving average
window_size = 3
weights = np.ones(window_size) / window_size
moving_avg = np.convolve(revenue, weights, mode='valid')
print("3-month moving average:", moving_avg)

# Calculate growth rates
growth_rates = np.diff(revenue) / revenue[:-1] * 100
print("\nMonth-over-month growth rates (%):", growth_rates)

# Predict next month (simple linear extrapolation)
last_slope = revenue[-1] - revenue[-2]
prediction = revenue[-1] + last_slope
print(f"\nPredicted next month revenue: {prediction:.2f}")

"""
Key Takeaways:
1. NumPy is powerful for sales analytics
2. Efficient for processing large datasets
3. Useful for scoring and segmentation
4. Great for statistical analysis
5. Handles time series calculations well
""" 