from typing import List, Dict, Optional, Callable, Iterator


# Sample sales data
sales_data = [
    {
        'id': 'SALE001',
        'product': 'CRM Pro',
        'amount': 5000,
        'region': 'North America',
        'customer_size': 'Enterprise',
        'renewal': True,
        'quarter': 'Q1'
    },
    {
        'id': 'SALE002',
        'product': 'Analytics Basic',
        'amount': 1000,
        'region': 'Europe',
        'customer_size': 'SMB',
        'renewal': False,
        'quarter': 'Q1'
    },
    {
        'id': 'SALE003',
        'product': 'CRM Pro',
        'amount': 4500,
        'region': 'Asia Pacific',
        'customer_size': 'Enterprise',
        'renewal': True,
        'quarter': 'Q2'
    },
    {
        'id': 'SALE004',
        'product': 'Analytics Premium',
        'amount': 3000,
        'region': 'North America',
        'customer_size': 'Mid-Market',
        'renewal': False,
        'quarter': 'Q2'
    },
    {
        'id': 'SALE005',
        'product': 'Support Plus',
        'amount': 2000,
        'region': 'Europe',
        'customer_size': 'SMB',
        'renewal': True,
        'quarter': 'Q1'
    }
]


class SalesFilter:
    """
    A flexible filtering system for sales data that demonstrates advanced filter usage.
    """
    
    def __init__(self, data: List[Dict]):
        self.data = data
        self.filters: List[Callable] = []
    
    def by_region(self, regions: List[str]) -> 'SalesFilter':
        """Filter by regions."""
        self.filters.append(
            lambda x: x['region'] in regions
        )
        return self
    
    def by_amount(self, min_amount: float) -> 'SalesFilter':
        """Filter by minimum amount."""
        self.filters.append(
            lambda x: x['amount'] >= min_amount
        )
        return self
    
    def by_customer_size(self, sizes: List[str]) -> 'SalesFilter':
        """Filter by customer size."""
        self.filters.append(
            lambda x: x['customer_size'] in sizes
        )
        return self
    
    def by_product(self, products: List[str]) -> 'SalesFilter':
        """Filter by product."""
        self.filters.append(
            lambda x: x['product'] in products
        )
        return self
    
    def renewals_only(self) -> 'SalesFilter':
        """Filter renewal deals only."""
        self.filters.append(
            lambda x: x['renewal']
        )
        return self
    
    def execute(self) -> List[Dict]:
        """Execute all filters and return results."""
        # Apply all filters sequentially
        result = self.data
        for filter_fn in self.filters:
            result = list(filter(filter_fn, result))
        return result

sales_filter = SalesFilter(sales_data)
filter_results = (
    sales_filter
    .by_region(['North America', 'Europe'])
    .by_amount(2000)
    .by_customer_size(['Enterprise', 'Mid-Market'])
    .execute()
)

print(filter_results)