from operator import add, mul, itemgetter, attrgetter
from functools import reduce
from typing import List, Dict, Any


# Sample Salesforce opportunity data
opportunities = [
    {'Amount': '1000.00', 'Probability': '90'},
    {'Amount': '5000.00', 'Probability': '60'},
    {'Amount': '2000.00', 'Probability': '75'}
]
