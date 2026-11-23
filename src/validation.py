def validate_limit_bal(value: int | float) -> bool:
    """
    Valida se o limite de crédito é aceitável.
    
    Args:
        value: Valor do limite de crédito.
        
    Returns:
        True se válido, False caso contrário.
        
    Examples:
        >>> validate_limit_bal(50000)
        True
        >>> validate_limit_bal(-1000)
        False
        >>> validate_limit_bal(2_000_000)
        False
    """
    MIN_LIMIT = 1
    MAX_LIMIT = 1_000_000
    
    return MIN_LIMIT <= value <= MAX_LIMIT