import pandas as pd

def format_currency(amount, currency="PKR"):
    """Formats raw numerical values into standard currency strings."""
    try:
        return f"{currency} {float(amount):,.0f}"
    except (ValueError, TypeError):
        return f"{currency} 0"
