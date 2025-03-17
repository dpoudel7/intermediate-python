from typing import List, Dict, Optional, Callable, Iterator
from datetime import datetime

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
    A flexible filtering system for sales data.
    
    TODO:
    1. Implement filter predicates
    2. Add filter combination methods
    3. Add result processing
    4. Implement filter reuse
    
    Use filter with custom predicates to create a powerful filtering system.
    """
    
    def __init__(self, data: List[Dict]):
        self.data = data
        # Your code here
    
    def by_region(self, regions: List[str]) -> 'SalesFilter':
        """Filter by regions."""
        # Your code here
        pass
    
    def by_amount(self, min_amount: float) -> 'SalesFilter':
        """Filter by minimum amount."""
        # Your code here
        pass
    
    def by_customer_size(self, sizes: List[str]) -> 'SalesFilter':
        """Filter by customer size."""
        # Your code here
        pass
    
    def by_product(self, products: List[str]) -> 'SalesFilter':
        """Filter by product."""
        # Your code here
        pass
    
    def renewals_only(self) -> 'SalesFilter':
        """Filter renewal deals only."""
        # Your code here
        pass
    
    def execute(self) -> List[Dict]:
        """Execute all filters and return results."""
        # Your code here
        pass


sales_filter = SalesFilter(sales_data)
filter_results = (
    sales_filter
    .by_region(['North America', 'Europe'])
    .by_amount(2000)
    .by_customer_size(['Enterprise', 'Mid-Market'])
    .execute()
)

print(filter_results)

