from collections import defaultdict


territory_data = [
    ('NA', 'USA', 'West', 'CA', 'San Francisco'),
    ('NA', 'USA', 'West', 'CA', 'Los Angeles'),
    ('NA', 'USA', 'East', 'NY', 'New York'),
    ('NA', 'USA', 'East', 'MA', 'Boston'),
    ('EMEA', 'UK', 'South', 'London', 'City'),
    ('EMEA', 'FR', 'North', 'Paris', 'Center'),
    ('APAC', 'JP', 'East', 'Tokyo', 'Shibuya'),
    ('APAC', 'AU', 'East', 'Sydney', 'CBD')
]

# Create a nested defaultdict structure
territories = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(set)
        )
    )
)

# Populate the hierarchy
for region, country, area, state, city in territory_data:
    territories[region][country][area][state].add(city)
    

for region, countries in territories.items():
    print(f"\nRegion: {region}")
    for country, areas in countries.items():
        print(f"  Country: {country}")
        for area, states in areas.items():
            print(f"    Area: {area}")
            for state, cities in states.items():
                print(f"      State: {state}")
                print(f"        Cities: {', '.join(sorted(cities))}")