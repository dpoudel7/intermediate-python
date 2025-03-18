import pytest
from classes import Employee


@pytest.mark.parametrize("name, age, salary, expected", [
    ("John", 30, 50000, "John"),
    ("Jane", 25, 50000, "Jane"),
])
def test_employee_creation(name, age, salary, expected):
    employee = Employee(name, age, salary)
    assert employee.name == expected




