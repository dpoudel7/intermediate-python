from collections import defaultdict

# Example 1: Grouping Opportunities by Account
opportunities = [
    {'id': '001', 'account': 'Acme', 'amount': 5000},
    {'id': '002', 'account': 'Globex', 'amount': 7500},
    {'id': '003', 'account': 'Acme', 'amount': 3000},
    {'id': '004', 'account': 'Stark', 'amount': 10000},
    {'id': '005', 'account': 'Globex', 'amount': 4500}
]

# Group opportunities by account
account_opportunities = defaultdict(list)
for opp in opportunities:
    account_opportunities[opp['account']].append(opp)

print("Opportunities by Account:")
for account, opps in account_opportunities.items():
    print(f"{account}: {len(opps)} opportunities")

# Example 2: Aggregating Sales Data
sales_totals = defaultdict(lambda: {'count': 0, 'total': 0})
for opp in opportunities:
    sales_totals[opp['account']]['count'] += 1
    sales_totals[opp['account']]['total'] += opp['amount']

print("\nSales Totals by Account:")
for account, stats in sales_totals.items():
    print(f"{account}: {stats['count']} deals, ${stats['total']:,}")

# Example 3: Building Territory Hierarchy
territory_hierarchy = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

# Sample territory data
territories = [
    ('West', 'CA', 'SF', 'Acme'),
    ('West', 'CA', 'LA', 'Globex'),
    ('East', 'NY', 'NYC', 'Stark'),
    ('West', 'CA', 'SF', 'Wayne'),
    ('East', 'MA', 'BOS', 'Oscorp')
]

# Build hierarchy without any explicit dictionary creation
for region, state, city, account in territories:
    territory_hierarchy[region][state][city].append(account)

print("\nTerritory Hierarchy:")
for region, states in territory_hierarchy.items():
    print(f"\n{region}:")
    for state, cities in states.items():
        print(f"  {state}:")
        for city, accounts in cities.items():
            print(f"    {city}: {', '.join(accounts)}")

