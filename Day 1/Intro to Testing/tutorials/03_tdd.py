def test_password_validator():
    # Test minimum length
    assert not is_valid_password('short')
    
    # Test number requirement
    assert not is_valid_password('NoNumbers')
    
    # Test case requirements
    assert not is_valid_password('lowercase123')
    assert not is_valid_password('UPPERCASE123')
    
    # Test valid password
    assert is_valid_password('Valid1Password')


def is_valid_password(password: str) -> bool:
    """
    Validate password according to requirements.
    
    Args:
        password: The password to validate
        
    Returns:
        bool: True if password meets all requirements, False otherwise
    """
    if len(password) < 8:
        return False
    
    has_number = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    
    return has_number and has_upper and has_lower

test_password_validator()