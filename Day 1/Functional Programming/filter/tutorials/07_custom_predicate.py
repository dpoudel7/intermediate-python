from typing import List, Dict, Optional, Callable, Iterator
from datetime import datetime

# Sample record structure
Record = Dict[str, str | int | float | datetime]

# Sample Salesforce-like records
opportunity_records = [
    {
        'id': 'OPP001',
        'name': 'Enterprise Deal',
        'amount': 150000,
        'stage': 'Negotiation',
        'probability': 75,
        'close_date': '2024-06-30'
    },
    {
        'id': 'OPP002',
        'name': 'SMB Package',
        'amount': 25000,
        'stage': 'Prospecting',
        'probability': 25,
        'close_date': '2024-04-15'
    },
    {
        'id': 'OPP003',
        'name': 'Strategic Partnership',
        'amount': 500000,
        'stage': 'Closed Won',
        'probability': 100,
        'close_date': '2024-03-01'
    },
    {
        'id': 'OPP004',
        'name': 'Maintenance Contract',
        'amount': 75000,
        'stage': 'Negotiation',
        'probability': 60,
        'close_date': '2024-05-15'
    }
]

class OpportunityFilter:
    """A class demonstrating advanced filtering techniques."""
    
    def __init__(self, records: List[Record]):
        self.records = records
        self.predicates: List[Callable[[Record], bool]] = []
    
    def add_amount_threshold(self, threshold: float) -> 'OpportunityFilter':
        """Add amount threshold filter."""
        self.predicates.append(
            lambda x: x['amount'] > threshold
        )
        return self
    
    def add_probability_threshold(self, threshold: float) -> 'OpportunityFilter':
        """Add probability threshold filter."""
        self.predicates.append(
            lambda x: x['probability'] >= threshold
        )
        return self
    
    def add_stage_filter(self, stages: List[str]) -> 'OpportunityFilter':
        """Add stage filter."""
        self.predicates.append(
            lambda x: x['stage'] in stages
        )
        return self
    
    def add_custom_filter(self, predicate: Callable[[Record], bool]) -> 'OpportunityFilter':
        """Add custom filter predicate."""
        self.predicates.append(predicate)
        return self
    
    def filter(self) -> Iterator[Record]:
        """Apply all filters in sequence."""
        result = self.records
        for predicate in self.predicates:
            result = filter(predicate, result)
        return result

def demonstrate_advanced_filtering():
    """Demonstrate advanced filtering techniques."""
    # Create filter chain
    opportunity_filter = OpportunityFilter(opportunity_records)
    
    # Build complex filter
    filtered_opportunities = list(
        opportunity_filter
        .add_amount_threshold(50000)
        .add_probability_threshold(60)
        .add_stage_filter(['Negotiation', 'Closed Won'])
        .add_custom_filter(
            lambda x: 'Partnership' in x['name'] or 'Enterprise' in x['name']
        )
        .filter()
    )
    
    return filtered_opportunities